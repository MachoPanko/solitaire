import random


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
class Deck:
    def __init__(self):
        self.storage = []
        for rank in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:
            for suit in "SHDC":
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
        reference_card = Cards(0,'SDHC')
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
        if reference_card.get_suit() in 'SC':
            if checking_card.get_suit() in 'HD':
                if reference_card.get_rank() - checking_card.get_rank() == 1:
                    return True
                else:
                    return False
            else:
                return False
        else:
            if checking_card.get_suit() in 'SC':
                if reference_card.get_rank() - checking_card.get_rank() == 1:
                    return True
                else:
                    return False
            else:
                return False

def move(gamedeck, column_list, foundations_list):
    choice = input('Move from what, to where?').split(',')
    for i in range(len(choice)):
        choice[i] = choice[i].strip()
    start = choice[0].lower()
    end = choice[1].lower()
    cardqty = 1
    if start == 'c':
        startindex = int(input("which column to take from?")) ## unfinished . if wrong input or want to go to other move should add stuffs
        if end == 'c':
            cardqty = int(input("How many cards?"))
    if end == 'c' or end == 'f':
        endindex = int(input("which to put to?"))
    if start == 'd':
        start_obj = gamedeck
    else:
        start_obj = column_list[startindex]
    if end == 'c':
        end_obj = column_list[endindex]
    else:
        end_obj = foundations_list[endindex]
    if validity(start_obj,end_obj,cardqty):
        for times in range(cardqty):
            moving_obj = start_obj.deal()
            end_obj.addcard(moving_obj)
    else:
        print("You have inputted an invalid move. pls try again :D")


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
    for suit in 'SHDC':
        foundations_list.append(Foundation(suit))
    command_dict = {'move': move, 'scroll': scroll}  ###unfinished
    if input("Welcome Marcus!! Start Game? (Y/N)").lower() == 'y':
        print('%20s%s' % ('Deck:',gamedeck))
        for column in columns_list:
            print('%8s' % (column))  ##unfinished print column like actual solitaire format
        for foundation in foundations_list:
            print(foundation, end=' ')
        print()
        command = input('What art thou bidding be?\nType -1 to exit ')
        while command != 'quit':  ## entire game loop, revolves around action on deck or columns
            if command not in command_dict:
                command = input('That was a wrong command, sorry not a flexible program, pls try again.')
                continue

            command_dict[command](gamedeck, columns_list,
                                  foundations_list)  ## note do i have to call all variables? like for scroll i only need gamedeck
            # if command == 'start':
            #     gamedeck = Deck()
            #     gamedeck.shuffle()
            #     for i in range(1,8):
            #         columni = Column()
            #         for i in range(3):
            #             columni.column.append(gamedeck.deal())
            gamedeck.checktopcardface()
            print('%20s' % (gamedeck))
            for column in columns_list:
                column.checktopcardface()
                print('%8s' % (column))  ##unfinished print column like actual solitaire format
            for foundation in foundations_list:
                print(foundation, end=' ')
            print()
            if checkwin(foundations_list):
                break
            command = input('What art thou bidding be?\nType -1 to exit')
        # except:
        #     print("i really dont know what to do if a wrong command is given. helppppp") ###this is really bad... should revert to last command.
        #     main()
    else:
        print("Bye bye see you again")
    print("game ended")


main()

