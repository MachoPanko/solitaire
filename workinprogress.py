import random
S = '\u2660'
H = '\u2665'
D = '\u2666'
C = '\u2663'
suits = S+H+D+C
class Cards:
    def __init__(self, rank, suit):
        picturevalues_dict = {"A": 1, "K": 13, "Q": 12, "J": 11}
        self.value = rank
        self.suit = suit
        self.face = 'down'
        if type(rank) == int:
            self.rank = rank
        else:
            self.rank = picturevalues_dict[rank]
    def get_rank(self):
        return self.rank
    def get_suit(self):
        return self.suit
    def get_value(self):
        return self.value
    def __str__(self):
        if self.face == 'up':
            return (str(self.value) + self.suit)
        else:
            return ('XX')

    def __repr__(self):
        return self.__str__()
class Deck:
    def __init__(self):
        self.storage = []
        for rank in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:
            for suit in suits:
                self.storage.append(Cards(rank, suit))
    def __str__(self):
        return self.storage[-1].__str__()
    def deal(self):
        carddealt = self.storage[-1]
        self.storage.pop()
        return carddealt
    def shuffle(self):
        random.shuffle(self.storage)
    def checktopcardface(self):
        if len(self.storage) == 0:
            pass
        else:
            self.storage[-1].face = 'up'
    def scroll(self):
        card = self.deal()
        self.storage.insert(0,card)
    def __repr__(self):
        return self.__str__()

class Gamescreen:
    def __init__(self, Columns_list, Foundations_list,Deck):
        self.Columns_list = Columns_list
        self.Foundations_list = Foundations_list
        self.Deck = Deck
    def __str__(self):
        maxlen = 0
        vertivalcol_list =[]
        screen_str = '%40s%s\n'%('Deck:', self.Deck)
        for column in self.Columns_list:
            if len(column.storage) > maxlen:
                maxlen = len(column.storage)
        for i in range(maxlen):
            vertivalcol_list.append([])
            for column in self.Columns_list:
                if i >= len(column.storage):
                    vertivalcol_list[i].append('  ')
                else:
                    vertivalcol_list[i].append(column.storage[i])

        for i in range(7):
            screen_str += '   %s  '%(i+1)
        screen_str += '\n'+'-'*45+'\n'
        for column in vertivalcol_list:
            for element in column:
                if type(element) == Cards and element.face == 'up' and element.get_rank() == 10:
                    screen_str += ' ' + element.__str__() + '  '
                else:
                    screen_str += '  '+element.__str__() +'  '
            screen_str += '\n'
        screen_str += '-'*45+'\n' + ' '*10
        for element in self.Foundations_list:
            screen_str += element.__str__() + '  |  '

        return screen_str



## NOTE: Column , deck and foundation are storages of cards.
## could be inherited from same baseclass leaving inheriting for later tho
class Column:
    def __init__(self):
        self.storage = []
        self.faceupcards = 1
    def __str__(self):
        returnstr = ''
        for card in self.storage:
            returnstr += card.__str__()
        return returnstr
    def deal(self):
        carddealt = self.storage[-1]
        self.storage.pop()
        self.faceupcards -= 1
        return carddealt
    def addcard(self, card):
        self.storage.append(card)
        self.faceupcards += 1
    def checktopcardface(self):
        if len(self.storage) == 0:
            pass
        elif self.storage[-1].face == 'down':
            self.storage[-1].face = 'up'
    def __repr__(self):
        return self.__str__()
class Foundation:
    def __init__(self, suit):
        self.storage = []
        self.suit = suit
    def __str__(self):
        if len(self.storage) == 0:
            return str(self.suit)
        else:
            return self.storage[-1].__str__()
    def addcard(self, card):
        self.storage.append(card)

################## END OF CLASSE ,  START OF FUNCTIONS ######################

def checkwin(foundations_list):
    wincondition = 0
    for foundation in foundations_list:
        if len(foundation.storage) == 13:
            wincondition += 1
    if wincondition == 4 :
        return True
    else: return False
def validity (start_obj, end_obj, cardqty):

    if len(end_obj.storage) == 0 :
        reference_card = Cards(0,suits)
    else:
        reference_card = end_obj.storage[-1]
    if len(start_obj.storage) == 0:
        return False
    else:
        checking_card = start_obj.storage[-cardqty]
    if type(start_obj) == Column and start_obj.faceupcards < cardqty:
        return False
    if type(end_obj) == Deck:
        return False
    if type(end_obj) == Foundation:
        if checking_card.get_suit() in reference_card.get_suit():
            if reference_card.get_rank() - checking_card.get_rank() == -1:
                return True
            else: return False
        else: return False
    if type(end_obj) == Column:
        if reference_card.get_suit() in S+C:
            if checking_card.get_suit() in H+D:
                if reference_card.get_rank() - checking_card.get_rank() == 1:
                    return True
                else:
                    return False
            else:
                return False
        else:
            if checking_card.get_suit() in S+C:
                if reference_card.get_rank() - checking_card.get_rank() == 1:
                    return True
                else:
                    return False
            else:
                return False

def move(gamedeck, column_list, foundations_list):
    choice = input('Move from which pile, to where?  Input format : Origin pile , Destination Pile ').split(',')
    for i in range(len(choice)):
        choice[i] = choice[i].strip().lower()
    if len(choice) != 2 :
        return move(gamedeck, column_list, foundations_list)
    start = choice[0]
    end = choice[1]
    cardqty = 1
    if start[0] == 'c':
        startindex = int(start[1])-1## unfinished . if wrong input or want to go to other move should add stuffs
        if end[0] == 'c':
            cardqty = int(input("How many cards?"))
    if end[0] == 'c' or end[0] == 'f':
        endindex = int(end[1])-1
    if start[0] == 'd':
        start_obj = gamedeck
    else:
        start_obj = column_list[startindex]
    if end[0] == 'c':
        end_obj = column_list[endindex]
    else:
        end_obj = foundations_list[endindex]
    if validity(start_obj,end_obj,cardqty):
        movinglist=[]
        for times in range(cardqty):
            moving_obj = start_obj.deal()
            movinglist.insert(0,moving_obj)
        for element in movinglist:
            end_obj.addcard(element)
    else:
        print("You have inputted an invalid move. pls try again :D")


def help (gamedeck, columns_list,foundations_list):
    print('''There are 3 piles (c,d,f) c stands for column, d for deck, f for foundation.
    <Command input format>
    move : For Column and Foundation, type 'C' / 'F' respectively followed by the pile number. For Deck , just type 'D'
    E.G. To move from column1 to foundation3, type : c1,f1
    scroll: no input
    quit: no input ''')
def scroll(gamedeck, columns_list, foundations_list):
    gamedeck.scroll()
def main():
    ##initializing variables . Does this have to be done manually or can i encapsualte it in a function?
    gamedeck = Deck()
    gamedeck.shuffle()
    columns_list = []
    ##storage for column instances, any other way? hmmm
    for i in range(7):
        acolumn = Column()
        for j in range(3):
            acolumn.addcard(gamedeck.deal())
        acolumn.checktopcardface()
        columns_list.append(acolumn)
    gamedeck.checktopcardface()
    foundations_list = []
    for suit in suits:
        foundations_list.append(Foundation(suit))
    command_dict = {'move': move, 'scroll': scroll, 'help': help}  ###unfinished
    if input("Welcome Marcus!! Start Game? (Y/N)").lower() == 'y':
        print(Gamescreen(columns_list,foundations_list,gamedeck))
        command = input('What art thou bidding be?(move/scroll/quit/help)\nType -1 to exit ')
        while command != 'quit':  ## entire game loop, revolves around action on deck or columns
            if command not in command_dict:
                command = input('That was a wrong command, sorry not a flexible program, pls try again.')
                continue

            command_dict[command](gamedeck, columns_list,foundations_list)  ## note do i have to call all variables? like for scroll i only need gamedeck
            gamedeck.checktopcardface()
            for column in columns_list:
                column.checktopcardface()
            print(Gamescreen(columns_list,foundations_list,gamedeck))
            if checkwin(foundations_list):
                break
            command = input('What art thou bidding be?(move/scroll/quit/help)\nType -1 to exit')
        # except:
        #     print("i really dont know what to do if a wrong command is given. helppppp") ###this is really bad... should revert to last command.
        #     main()
    else:
        print("Bye bye see you again")
    print("game ended")


main()
