# importing of modules
# import random
import random
from time import sleep
from colorama import Style, Fore, Back


# -------------------------------------------------------------------------------------------------------------------------------


def introduction():
    sleep(2)

    print("\n\n")
    print(
        Fore.BLUE + "\t\t\t\t*******************************************************************************************************")
    print(
        "\t\t\t\t*******************************************************************************************************")

    sleep(0.5)
    print("\t\t\t\t***\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t***")
    sleep(0.5)
    print("\t\t\t\t***\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t***")
    sleep(0.5)
    print("\t\t\t\t***\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t***")
    sleep(1)
    print("\t\t\t\t***\t\t\t" + Style.BRIGHT + Fore.MAGENTA + "WELCOME ", end="")
    sleep(1.5)
    print("TO THE GAME OF ", end="")
    sleep(1.5)
    print("HAND CRICKET", end="")
    sleep(1.5)
    print(": SINGLE PLAYER MODE" + Style.RESET_ALL + Fore.BLUE + "\t\t\t\t\t\t\t\t\t***")
    sleep(0.5)
    print("\t\t\t\t***\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t***")
    sleep(0.5)
    print("\t\t\t\t***" + Style.RESET_ALL + '\033[1m' + "\t\t\t\t\t\t\t\t\t\t\t\t\t - designed and proposed by", end="")
    sleep(1.5)
    print(Style.BRIGHT + Fore.LIGHTRED_EX + " Swastik Nayak" + Style.RESET_ALL + Fore.BLUE + "\t\t***")
    sleep(0.5)
    print("\t\t\t\t***\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t***")
    sleep(0.5)
    print("\t\t\t\t***\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t***")
    sleep(0.5)
    print("\t\t\t\t***\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t***")
    sleep(0.5)
    print(
        "\t\t\t\t*******************************************************************************************************")
    print(
        "\t\t\t\t*******************************************************************************************************\n\n" + Style.RESET_ALL)
    minput()


# ----------------------------------------------------------------------------------------------------------------------


def welcomeName(name):
    sleep(1)
    print("\t\t\t\t\t\t\t\t\t" + Back.LIGHTCYAN_EX, end="WELCOME TO THE GAME")
    sleep(1.5)
    print(f", {name}" + Style.RESET_ALL)
    pFormat(2)


# ----------------------------------------------------------------------------------------------------------------------


def check(strings):
    strings = strings.lower()
    if 'yes' in strings or 'no' in strings:
        return True
    else:
        return False


# ----------------------------------------------------------------------------------------------------------------------


def enterChoice(prefer="choice"):
    sleep(0.5)
    print(f"\n\t---->enter your {prefer} here: ", end="")
    i = input()
    pFormat(1)
    return i


# ----------------------------------------------------------------------------------------------------------------------


def pFormat(n=1.0):
    print(Fore.GREEN, end="")
    for i in range(7676):
        print(end="-")
    print(Style.RESET_ALL)
    sleep(n)


# ----------------------------------------------------------------------------------------------------------------------


def minput():
    print("\npress enter to continue or 0 to exit")
    ch = input()
    if ch == '0':
        print("\t\t" + Fore.RED + "please give feedback to the developer :):) VISIT AGAIN" + Style.RESET_ALL)
        exit(0)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------


def rules():
    print("we are going to show you the rules")
    pFormat()
    print("enter yes to look at rules and no to skip")
    ch = enterChoice()
    if 'yes' in ch.lower():
        print(Fore.RED + "\t1. You can only choose 0, 1, 2, 3, 4, 5 and 6")
        print(
            "\t2. Extra 1 run will be added if the bowler bowls 0 for 3 times consecutively as it will be declared as no ball (both while batting and bowling)")
        print(
            "\t3. There are always two batsmen at the crease and they both switch places when the run becomes 1, 3 and 5")
        print("\t4. Irresponsible choice picking and picking choices less than 0 or more than 6 will be declared NULL")
        print(
            "\t5. 2 times consecutive irresponsible input leads to run-out if you are batting, and no-ball if you are bowling")
        print(
            "\t6. Once the game has begun there is no option for quiting unless after the end of an innings; your high score might not get updated ")
        pFormat()
        input()


# ------------------------------------------------------------------------------------------------------------------------------------------------------


def toss():
    ch = " "

    print(Style.BRIGHT + "\tIT'S TIME FOR THE TOSS!!" + Style.RESET_ALL)
    chx = int()

    # 1--> bat and 0-->bowl

    while "head" != ch.lower() and "tail" != ch.lower():
        print("enter 'head' for head and 'tail' for tail")
        ch = enterChoice()
    rand = random.randint(0, 1)
    if rand == 0 and ch == 'head':
        print("It's head: you have won :)")
        res = 1
    elif rand == 1 and ch == 'tail':
        print("It's tail: you have won :)")
        res = 1
    elif rand == 0 and ch == "tail":
        print("It's head: you have lost :(")
        res = 0
    else:
        print("It's tail: you have lost :(")
        res = 0
    sleep(0.5)
    if res == 1:
        print("choose:\n\t1. bowl\t\t\t2. bat")
        pFormat()
        while chx != 1 and chx != 2:
            print("enter 1 to bowl or 2 to bat")
            cc = enterChoice()
            if cc == '1' or cc == '2':
                chx = int(cc)
            else:
                chx = 0
        if chx == 1:
            print("you have chosen to bowl")
            pFormat(0.5)
            return 0
        else:
            print("you have chosen to bat")
            pFormat(0.5)
            return 1
    else:
        randx = random.randint(0, 1)
        if randx == 0:
            print("your opponent has chosen to bowl")
            pFormat(0.5)
            return 1
        else:
            print("your opponent has chosen to bat")
            pFormat(0.5)
            return 0


# -------------------------------------------------------------------------------------------------------------------------------------------------------


def comBat(cname, pos):
    list1 = ["Here comes the {}, putting his pads on", "the stadium has gone crazy because it's {} on the ground",
             "{} on the crease, looks dangerous for the opponent", "{} has come up to the crease"]
    list2 = ["here come's the batsman, least hoped for", "another wicket another man standing, might not be the last",
             "the team might be in trouble if another wicket falls again"]
    print(Fore.RED, end="")
    if pos <= 6:
        rand = random.randint(0, 3)
        print("\t" + list1[rand].format(cname) + "\n" + Style.RESET_ALL)
        sleep(0.75)
    else:
        rand = random.randint(0, 2)
        print("\t" + list2[rand] + "\n" + Style.RESET_ALL)
        sleep(0.75)


# -------------------------------------------------------------------------------------------------------------------------------------------------------


def comBowl(cname):
    list = ["{} into attack", f"end of the over and there comes another bowler to bowl",
            "{} seems lethal for the batsman", "{} bowling from Swastik end"]
    rand = random.randint(0, 3)
    print(Fore.RED + "\t" + list[rand].format(cname) + "\n" + Style.RESET_ALL)
    sleep(0.75)


# -------------------------------------------------------------------------------------------------------------------------------------------------------


def out(cname):
    list = ["{} has been caught behind", "BOWLED!!", "stunning bowl got {} stunned, got him bowled",
            "catch is the call, and that's out", "BOWLED!!", "caught in the mid off", "caught behind",
            "caught in the long on",
            "square cut, and its an out", "an easy catch by the fielder in the deep",
            "stumped!!! lightning hands of the wicket keeper"]
    rand = random.randint(0, len(list) - 1)
    print(Fore.RED + "\t" + list[rand].format(cname) + "\n" + Style.RESET_ALL)
    sleep(0.75)


# -------------------------------------------------------------------------------------------------------------------------------------------------------


def six():
    list = ["the ball goes flying", "now ask the crowd to fetch the ball", "MAXIMUM!!",
            "stay uprooted, coz the ball has gone out of the field", "the bowler scratches his head",
            "Pull!! and it goes for a six", "MAXIMUM!!", "Loft cover drive and crowd goes crazy",
            "helicopter shot; ball goes out of the stadium", "a flat six!!", "MAXIMUM!!",
            "chance for the fielder but no, the ball has been carried away into the crowd!!",
            "unorthodox yet satisfactory, gives his team a total six run", "MAXIMUM!!", "MAXIMUM!!"]
    rand = random.randint(0, len(list) - 1)
    print(Fore.RED + "\t" + list[rand] + "\n" + Style.RESET_ALL)
    sleep(0.5)


# -------------------------------------------------------------------------------------------------------------------------------------------------------


def four():
    list = ["beautiful, the batsman has found the gap", "FOUR!!",
            "the ball goes up, lands in the no man land; goes for four", "FOUR!!",
            "fielder made a good effort but the ball went for four",
            "catch is the call, but it lands way farther than the fielder and goes for four",
            "1 drop 2 drop and goes for four", "classy!! the batsman sure knows where the fielders are",
            "1 bounce and a four", "hits hard; and the ball goes for four"]
    rand = random.randint(0, len(list) - 1)
    print(Fore.RED + "\t" + list[rand] + "\n" + Style.RESET_ALL)
    sleep(0.5)


# -------------------------------------------------------------------------------------------------------------------------------------------------------


def fifty(striker):
    list = ["oh a magnificent knock from {}, he got his 50!!", "half century for {}",
            "at first he stumbled but the missed catch gave him another life",
            "in this format half century for a batsman is a big deal!!"]
    print("\t\t_______________   ______________     __\n"
          "\t\t_______________   ______________     ||\n"
          "\t\t||                || \\\\       ||     ||\n"
          "\t\t||                ||  \\\\      ||   ------\n"
          "\t\t_______________   ||   \\\\     ||   ||  ||\n"
          "\t\t_______________   ||    \\\\    ||   ||  ||\n"
          "\t\t             ||   ||     \\\\   ||   ||  ||\n"
          "\t\t             ||   ||      \\\\  ||   ||  ||\n"
          "\t\t_______________   ______________   ||  ||\n"
          "\t\t_______________   ______________   ------")
    rand = random.randint(0, len(list) - 1)
    print(Fore.RED + "\t" + list[rand].format(striker) + "\n" + Style.RESET_ALL)
    sleep(0.75)


# -------------------------------------------------------------------------------------------------------------------------------------------------------


def hundred(name):
    list = ["look how excited he is ", "a magnificent knock from {}", "and he is celebrating in his own style",
            "one hundred for  {}", "he is now the glory for his team"]
    print("\t\t   ______         ______________   ______________     __\n"
          "\t\t  _______         ______________   ______________     ||\n"
          "\t\t //   |||         || \\\\       ||   || \\\\       ||     ||\n"
          "\t\t//    |||         ||  \\\\      ||   ||  \\\\      ||   ------\n"
          "\t\t-     |||         ||   \\\\     ||   ||   \\\\     ||   ||  ||\n"
          "\t\t      |||         ||    \\\\    ||   ||    \\\\    ||   ||  ||\n"
          "\t\t      |||         ||     \\\\   ||   ||     \\\\   ||   ||  ||\n"
          "\t\t      |||         ||      \\\\  ||   ||      \\\\  ||   ||  ||\n"
          "\t\t_______________   ______________   ______________   ||  ||\n"
          "\t\t_______________   ______________   ______________   ------")
    rand = random.randint(0, len(list) - 1)
    print(Fore.RED + "\t" + list[rand].format(name) + "\n" + Style.RESET_ALL)
    sleep(0.75)

# -------------------------------------------------------------------------------------------------------------------------------------------------------


def onefifty(name):
    list = ["humongous batting by {}", "he has single-handedly geared up the score for his team",
            "one hundred and fifty runs for {}", "he is now the glory for his team"]
    print("\t\t   ______         _______________   ______________     __\n"
          "\t\t  _______         _______________   ______________     ||\n"
          "\t\t //   |||         ||                || \\\\       ||     ||\n"
          "\t\t//    |||         ||                ||  \\\\      ||   ------\n"
          "\t\t-     |||         _______________   ||   \\\\     ||   ||  ||\n"
          "\t\t      |||         _______________   ||    \\\\    ||   ||  ||\n"
          "\t\t      |||                      ||   ||     \\\\   ||   ||  ||\n"
          "\t\t      |||                      ||   ||      \\\\  ||   ||  ||\n"
          "\t\t_______________   _______________   ______________   ||  ||\n"
          "\t\t_______________   _______________   ______________   ------")
    rand = random.randint(0, len(list) - 1)
    print(Fore.RED + "\t" + list[rand].format(name) + "\n" + Style.RESET_ALL)
    sleep(0.75)


# ----------------------------------------------------------------------------------------------------------------------


def checkrun(ch):
    if ch >= 0 and ch <= 6:
        return True
    else:
        return False


# ----------------------------------------------------------------------------------------------------------------------


def comment(ch, name):
    if ch == -1:
        out(name)
    elif ch == 6:
        six()
    elif ch == 5:
        print(Fore.RED + "\tThe Batsmen have reached the opposite creases before the fielder threw the ball")
        print("\tAnd the ball Went for a FOUR!!!!" + Style.RESET_ALL)
    elif ch == 4:
        four()
    elif ch == 0:
        print(Fore.RED + "\tDEFENSE!!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "\t Good Running between the wickets!!\n" + Style.RESET_ALL)


# ----------------------------------------------------------------------------------------------------------------------


def win(name):
    print(f"{name}, you have :)")
    sleep(0.75)
    print("\t\t:-)                                    :-)   ____________________   ______         :-)\n"
          "\t\t :-)                                  :-)    ____________________   ___ :-)        :-)\n"
          "\t\t  :-)                                :-)     :-)              :-)   :-)  :-)       :-)\n"
          "\t\t   :-)            :-):-)            :-)      :-)              :-)   :-)   :-)      :-)\n"
          "\t\t    :-)          :-)  :-)          :-)       :-)              :-)   :-)    :-)     :-)\n"
          "\t\t     :-)        :-)    :-)        :-)        :-)              :-)   :-)     :-)    :-)\n"
          "\t\t      :-)      :-)      :-)      :-)         :-)              :-)   :-)      :-)   :-)\n"
          "\t\t       :-)    :-)        :-)    :-)          :-)              :-)   :-)       :-)  :-)\n"
          "\t\t        :-)  :-)          :-)  :-)           ____________________   :-)        :-) :-)\n"
          "\t\t         :-):-)            :-):-)            ____________________   :-)         ------ ")


# ----------------------------------------------------------------------------------------------------------------------


def lose(name):
    print(f"{name}, you have :(")
    sleep(0.75)
    print("\t\t:-(                  --------------------       ---------       ---------------------\n"
          "\t\t:-(                  --------------------   -----------------   ---------------------\n"
          "\t\t:-(                  :-(              :-(   :-(                          :-(\n"
          "\t\t:-(                  :-(              :-(   :-(                          :-(\n"
          "\t\t:-(                  :-(              :-(   -------------                :-(\n"
          "\t\t:-(                  :-(              :-(       -------------            :-(\n"
          "\t\t:-(                  :-(              :-(                 :-(            :-(\n"
          "\t\t:-(                  :-(              :-(                 :-(            :-(\n"
          "\t\t------------------   --------------------   -----------------            :-(\n"
          "\t\t------------------   --------------------       ---------                :-(")


# ----------------------------------------------------------------------------------------------------------------------


def draw(name):
    print(f"{name}, it's a :-|")
    sleep(0.75)
    print(
        "\t\t:-|---------              :-|---------                :-|:-|      :-|                                    :-|\n"
        "\t\t:-|-------------          :-|-------------           :-|  :-|      :-|                                  :-|\n"
        "\t\t:-|          ------       :-|            :-|        :-|    :-|      :-|                                :-|\n"
        "\t\t:-|          --------     :-|            :-|       :-|       :-|     :-|            :-|:-|            :-|\n"
        "\t\t:-|                 :-|   :-|-------------        :-|         :-|     :-|          :-|  :-|          :-|\n"
        "\t\t:-|                 :-|   :-|---------           :-|-----------:-|     :-|        :-|    :-|        :-|\n"
        "\t\t:-|          --------     :-|   :-|             :-|-------------:-|     :-|      :-|      :-|      :-|\n"
        "\t\t:-|          ------       :-|      :-|         :-|               :-|     :-|    :-|        :-|    :-|\n"
        "\t\t:-|-------------          :-|         :-|      :-|               :-|      :-|  :-|          :-|  :-|\n"
        "\t\t:-|---------              :-|            :-|   :-|               :-|       :-|:-|            :-|:-|")


# ---------------------------------------------------------------------------------------------------------------------

class ForePlay:
    name = ""
    country = ""

    # functions

    def nameInput(self):

        self.ch2 = 1
        self.ch = self.cc = self.chx = self.word = ""
        self.c = 0
        self.i = " "
        self.name = ""
        self.nameList = self.cnameList = list()

        print(Style.BRIGHT + "\t\t\tPLAYER LOGIN:" + Style.RESET_ALL)
        with open("name.hc") as self.f:
            if self.f.read() == "":
                print("no registered players available")
                pFormat(1)
            else:
                with open("name.hc") as self.f:
                    while True:
                        self.i = self.f.readline()
                        if self.i == "":
                            break
                        self.i = self.i.rstrip(("\n")).replace("(!@#$%^)", " ")
                        self.nameList.append(self.i)
                        self.c += 1
                        print(f"\t{self.c}. {self.i}")
                        sleep(0.5)
                pFormat(1)
        while not check(self.ch) and self.c != 0:
            print("do you want to choose among those registered players?")
            pFormat(1)
            print("if yes then enter yes or if no then enter no: ")
            self.ch = enterChoice()

        if 'yes' in self.ch.lower():
            while True:
                self.chx = ""
                print("Enter your preferred number from the above list")
                self.cc = enterChoice("number")
                if self.cc.isnumeric():
                    self.ch2 = int(self.cc)
                else:
                    self.ch2 = ord(self.cc[0])

                if self.ch2 > 0 and self.ch2 <= self.c:
                    self.name = self.nameList[self.ch2 - 1]
                    print(f"your preferred name is {self.name}")
                    pFormat(0.5)
                    print("do you want to keep this name?")
                    pFormat(1)
                    while not check(self.chx):
                        print("enter 'yes' to continue or 'no' to modify")
                        self.chx = enterChoice()
                    if 'yes' in self.chx.lower():
                        welcomeName(self.name)
                        break
                else:
                    print("enter the correct number:(")
        else:
            while True:
                self.chx = ""
                while True:
                    print("enter the user name: ")
                    self.name = enterChoice("name")
                    print(f"you have entered {self.name}")
                    print("do you want keep this name?")
                    while not check(self.chx):
                        print("enter 'yes' to continue or 'no' to modify")
                        self.chx = enterChoice()
                    if self.name not in self.nameList:
                        break
                    else:
                        print("the name you have entered has already been registered\nenter again ")
                with open("country.hc") as self.f:
                    if self.name.replace(" ","(!@#$%^)") in self.f.read():
                        print("country name can not be the user name")
                        pFormat()
                        print("enter again")
                        continue
                if 'yes' in self.chx.lower():
                    break
            with open("name.hc") as self.f:
                if self.f.read() == "":
                    with open("name.hc", 'w') as self.f:
                        self.f.write(self.name.replace(" ", "(!@#$%^)"))
                else:
                    with open("name.hc", 'a') as self.f:
                        self.f.write("\n" + self.name.replace(" ", "(!@#$%^)"))
            welcomeName(self.name)
        minput()
        return

    def createPlayers(self, name, country="INDIA"):
        self.c = 0
        self.i = self.cc = self.word = ""
        self.ch1 = str()
        self.ch2 = 1
        self.chx = ""
        self.flag = 0
        self.cplayers = self.players = list()
        self.country = ""
        self.ccountrylist = self.countrylist = list()
        self.line = []
        self.lines = self.ele = ""

        # function body
        with open("highscore.hc") as self.f:
            if self.f.read() == "":
                with open("highscore.hc", 'a') as self.f:
                    self.f.write(self.name.replace(" ", "(!@#$%^)") + " " + country.replace(" ", "(!@#$%^)")+" 0")
            else:
                with open("highscore.hc") as self.f:
                    if self.name.replace(" ", "(!@#$%^)") not in self.f.read():
                        with open("highscore.hc", 'a') as self.f:
                            self.f.write(
                                "\n" + self.name.replace(" ", "(!@#$%^)") + " " + country.replace(" ", "(!@#$%^)")+" "+str(0))
        print(Style.BRIGHT + "\t\tTEAM AND PLAYER SELECTION:" + Style.RESET_ALL)
        print(f"your default country is {country}")
        pFormat(2)
        while not check(self.ch1):
            print("do you want to modify the country name?")
            pFormat(1)
            print("enter 'yes' to modify or enter 'no' to go with the country name")
            self.ch1 = enterChoice()

        if 'yes' in self.ch1.lower():
            with open("country.hc") as self.f:
                self.ccountrylist = self.f.readlines()
            for self.i in self.ccountrylist:
                self.word = self.i.rstrip("\n").replace("(!@#$%^)", " ")
                if self.word != "":
                    self.countrylist.append(self.word)

            print("The country list is: ")
            while self.flag == 0:
                self.c = 0
                for self.i in self.countrylist:
                    self.c += 1
                    if self.c % 4 == 0:
                        print()
                    print(str(self.c) + ".", self.i, end="\t\t")
                    sleep(0.2)
                print()
                pFormat()
                print("enter your preferred number from the above list: ")
                self.cc = enterChoice()
                if self.cc=="":
                    self.ch2=0
                elif self.cc.isnumeric():
                    self.ch2 = int(self.cc)
                else:
                    self.ch2 = ord(self.cc[0])
                if self.ch2 < 1 or self.ch2 > 11:
                    print("enter again :)")
                    pFormat(0.5)
                else:
                    self.country = self.countrylist[self.ch2 - 1]
                    print(f"you have chosen {self.country}")
                    pFormat(0.75)
                    self.chx = ""
                    while not check(self.chx):
                        print(f"do you want to go with {self.country}")
                        print("enter 'yes' to continue or 'no' to modify")
                        self.chx = enterChoice()
                    if 'yes' in self.chx.lower():
                        self.flag = 1
                        with open("highscore.hc") as self.f:
                            while True:
                                self.i = self.f.readline()
                                if self.i == "":
                                    break
                                self.i = self.i.strip("\n")
                                self.line = self.i.split()
                                self.i = ""
                                if self.name.replace(" ", "(!@#$%^)") in self.line:
                                    self.line[1] = self.line[1].replace(country.replace(" ", "(!@#$%^)"),
                                                                        self.country.replace(" ", "(!@#$%^)"))
                                for self.ele in self.line:
                                    self.i = self.i + self.ele + " "
                                self.lines = self.lines + self.i + "\n"
                        self.lines = self.lines.strip("\n")
                        with open("highscore.hc", 'w') as self.f:
                            self.f.write("")
                            self.f.write(self.lines)
        else:
            self.country = country
        with open(f"{self.country}.hc") as self.f:
            self.cplayers = self.f.readlines()
        for self.i in self.cplayers:
            self.word = self.i.rstrip("\n").replace("(!@#$%^)", " ")
            if self.word != "":
                self.players.append(self.word)
        print(f"{name}, your allotted players are: \n")
        for self.i in self.players:
            print(f"\t{self.i}")
            sleep(0.5)
        pFormat(0.5)
        minput()
        return

    def checkName(self, name):
        name = name.replace(" ", "(!@#$%^)")
        with open("highscore.hc") as f:
            while True:
                i = f.readline().rstrip("\n")
                if i == "":
                    break
                line = i.split()
                if name in line:
                    return line[1].replace("(!@#$%^)", " ")
        return ""

    def createOpponent(self):
        self.rnd = int()
        self.line = ""
        self.i = ""
        self.flag = 0
        self.ocountrylist = {}
        self.oppCountry = ""
        self.coppPlayer = self.oppPlayer = []
        c = 0

        with open("country.hc") as self.f:
            while True:
                self.line = self.f.readline()
                if self.line == "":
                    break
                self.line = self.line.rstrip("\n").replace("(!@#$%^)", " ")
                c = c+1
                self.ocountrylist.update({c: self.line})
        while self.flag == 0:
            self.rnd = random.randint(1, 11)
            if self.ocountrylist[self.rnd] != self.country:
                self.oppCountry = self.ocountrylist[self.rnd]
                self.flag = 1
        with open(f"{self.oppCountry}.hc") as self.f:
            self.coppPlayer = self.f.readlines()
        for self.i in self.coppPlayer:
            self.i = self.i.rstrip("\n")
            self.oppPlayer.append(self.i)
        print(f"Your opponent has chosen {self.oppCountry}")
        pFormat()
        print("opponent players are:")
        for self.i in self.oppPlayer:
            print(f"\t{self.i}")
            sleep(0.5)
        pFormat()
        minput()

# ----------------------------------------------------------------------------------------------------------------------

class GameThrough:

    def getBiodata(self, country, players, oppCountry, oppplayers):
        self.biodata = []
        self.copyp = []
        self.biodata.append(" ")
        self.biodata.append(country)

        self.j = ""
        for self.i in players:
            self.short = ""
            self.i = self.i.replace("(c)", "").replace("(wk)", "").strip()
            self.ci = self.i.split()
            for self.j in self.ci:
                self.short += self.j[0]
            self.short = self.short[0:len(self.short) - 1] + " " + self.j
            self.copyp.append(self.short)
        self.biodata.append(self.copyp)
        self.copyp = []
        self.biodata.append(oppCountry)
        for self.i in oppplayers:
            self.short = ""
            self.i = self.i.replace("(c)", "").replace("(wk)", "").strip()
            self.ci = self.i.split()
            for self.j in self.ci:
                self.short += self.j[0]
            self.short = self.short[0:len(self.short) - 1] + " " + self.j
            self.copyp.append(self.short)
        self.biodata.append(self.copyp)

    def bat(self,target=9999):
        global rand

        self.batord=[]
        self.bowlord=[]
        for i in self.biodata[2]:
            self.batord.append(i)
        self.bowlord = self.biodata[4]
        self.bowlord = self.bowlord[6:]
        self.scoBat = {}
        self.scoBowl = {}
        for self.i in self.bowlord:
            self.scoBowl[self.i] = [0, 0, 0.0]
        for self.i in self.batord:
            self.scoBat[self.i] = [0, 0]
        # print(self.scoBat)
        s50 = []
        s100 = []
        s150 = []
        for i in range(11):
            s50.append(0)
            s100.append(0)
            s150.append(0)
        striker = self.batord[0]
        runner = self.batord[1]
        bowler = self.bowlord[4]
        wicket = run = nb = 0
        temp = ""
        pw = 0
        pr = 0
        over = 0.0
        ball = 0.0

        ch = 0
        rout = 0

        while wicket != 10 and over < 10.0 and run<target:
            if over == 0.0:
                comBat(striker, wicket)
                comBat(runner, wicket)
            pFormat(0.8)
            print(Style.BRIGHT + Fore.RED + "\t\t\tScore: " + Fore.BLUE + str(run) + "-" + str(
                wicket) + Fore.RED + "\t\t\tOver: " + Fore.BLUE + str(
                over) + Fore.RED + "\t\t\tBowler: " + Fore.BLUE + bowler)
            print(
                Fore.RED + "\tOn Strike: " + Fore.BLUE + striker + Fore.LIGHTBLUE_EX + f" {self.scoBat[striker][0]}({self.scoBat[striker][1]})",end="")
            for i in range(50-len(striker+f" {self.scoBat[striker][0]}({self.scoBat[striker][1]})")):
                print(end=" ")
            print( Fore.RED + "Runner: " + Fore.BLUE + runner + Fore.LIGHTBLUE_EX + f" {self.scoBat[runner][0]}({self.scoBat[runner][1]})" + Style.RESET_ALL)
            c = 0
            while c != 2:
                chp = enterChoice()
                if chp.isnumeric():
                    ch = int(chp)
                else:
                    ch = -1
                if checkrun(ch):
                    break
                c += 1

            if c == 2:
                print(Fore.RED + "\tRUN OUT!! Misunderstanding between brain and hand" + Style.RESET_ALL)
                rout += 1
                sleep(0.5)
                wicket += 1
                self.scoBat[striker][1] += 1
                over += 0.1
                ball = over - int(over)
                ball = float("{:.1f}".format(ball))
                if wicket!=10:
                    self.batord.remove(striker)
                    for i in self.batord:
                        if i != runner:
                            striker = i
                            break
                    comBat(striker, wicket)
                if wicket==10 and ball!=0.6:
                    self.scoBowl[bowler][0] += run - pr
                    self.scoBowl[bowler][1] += wicket - pw - rout
                    self.scoBowl[bowler][2] += ball
                    rout = 0
                    pr = run
                    pw = wicket
                if ball == 0.6:
                    over -= 0.6
                    over += 1.0
                    self.scoBowl[bowler][0] += run - pr
                    self.scoBowl[bowler][1] += wicket - pw-rout
                    self.scoBowl[bowler][2] += 1
                    rout=0
                    pr = run
                    pw = wicket
                    while over!=10.0:
                        rb = random.randint(0, 4)
                        temp = self.bowlord[rb]
                        if temp != bowler and self.scoBowl[temp][2] != 2:
                            break
                    bowler = temp
                    comBowl(bowler)
                over = float("{:.1f}".format(over))
                continue
            if self.biodata[2].index(striker) <= 2:
                if self.scoBat[striker][0] <= 12:
                    rand = random.randint(0, 6)
                elif run / over > 15.0 and ch > 4:
                    rand = random.randint(5, 6)
                elif over >= 8.0 and run / over < 8.0:
                    rand = random.randint(0, 3)
                elif run / over <= 7.0 and ch <= 3:
                    rand = random.randint(0, 3)
                else:
                    rand = random.randint(2, 6)
            elif 2 < self.biodata[2].index(striker) <= 6:
                if self.scoBat[striker][0] <= 8 and (self.scoBat[striker][0] == 6 or self.scoBat[striker][0] == 5):
                    rand = ch
                elif self.scoBat[striker][0] <= 15:
                    rand = random.randint(0, 6)
                elif run / over > 15.0 and ch > 4:
                    rand = random.randint(5, 6)
                elif over >= 8.0 and run / over < 8.0:
                    rand = random.randint(0, 4)
                elif run / over < 7.0 and ch <= 3:
                    rand = random.randint(0, 3)
                else:
                    rand = random.randint(3, 6)
            else:
                if self.scoBat[striker][0] <= 12 and (
                        self.scoBat[striker][0] == 6 or self.scoBat[striker][0] == 5 or self.scoBat[striker][0] == 4):
                    rand = ch
                elif run / over >= 4.0:
                    rand = random.randint(5, 6)
                elif over >= 8.0 and run / over < 8.0:
                    rand = random.randint(0, 4)
                elif run / over < 7.0 and ch <= 3:
                    rand = random.randint(0, 3)
                else:
                    rand = random.randint(4, 6)

            print("\tOpponent has chosen:", rand)

            if rand == 0:
                if nb >= 3:
                    print(Fore.RED + "\tNO BALL!! A PLUNDER FROM THE BOWLER" + Style.RESET_ALL)
                    comment(ch, striker)
                    run += ch + 1
                    self.scoBat[striker][0] += ch
                    self.scoBat[striker][1] += 1
                    if run >= target:
                        self.scoBowl[bowler][0] += run - pr
                        self.scoBowl[bowler][1] += wicket - pw - rout
                        self.scoBowl[bowler][2] += ball
                        rout = 0
                        pr = run
                        pw = wicket
                else:
                    nb += 1
                    if ch != rand:
                        comment(ch, striker)
                        run += ch
                        self.scoBat[striker][0] += ch
                        self.scoBat[striker][1] += 1
                        if self.scoBat[striker][0] >= 50 and s50[self.biodata[2].index(striker)] != 1:
                            s50[self.biodata[2].index(striker)] = 1
                            fifty(striker)
                        elif self.scoBat[striker][0] >= 100 and s100[self.biodata[2].index(striker)] != 1:
                            s100[self.biodata[2].index(striker)] = 1
                            hundred(striker)
                        elif self.scoBat[striker][0] >= 150 and s150[self.biodata[2].index(striker)] != 1:
                            s150[self.biodata[2].index(striker)] = 1
                            onefifty(striker)
                        over += 0.1
                        ball = over - int(over)
                        ball = float("{:.1f}".format(ball))
                        if run>=target and ball != 0.6:
                            self.scoBowl[bowler][0] += run - pr
                            self.scoBowl[bowler][1] += wicket - pw - rout
                            self.scoBowl[bowler][2] += ball
                            rout = 0
                            pr = run
                            pw = wicket
                        if ball == 0.6:
                            over -= 0.6
                            over += 1.0
                            temp = striker
                            striker = runner
                            runner = temp
                            self.scoBowl[bowler][0] += run - pr
                            self.scoBowl[bowler][1] += wicket - pw-rout
                            self.scoBowl[bowler][2] += 1
                            rout=0
                            pr = run
                            pw = wicket
                            while over!=10.0:
                                rb = random.randint(0, 4)
                                temp = self.bowlord[rb]
                                if temp != bowler and self.scoBowl[temp][2] != 2:
                                    break
                            bowler = temp
                            comBowl(bowler)
                        over = float("{:.1f}".format(over))
                    else:
                        comment(-1, striker)
                        wicket += 1
                        self.scoBat[striker][1] += 1
                        over += 0.1
                        ball = over - int(over)
                        ball = float("{:.1f}".format(ball))
                        if wicket != 10:
                            self.batord.remove(striker)
                            for i in self.batord:
                                if i != runner:
                                    striker = i
                                    break
                            comBat(striker, wicket)
                        if wicket == 10 and ball != 0.6:
                            self.scoBowl[bowler][0] += run - pr
                            self.scoBowl[bowler][1] += wicket - pw - rout
                            self.scoBowl[bowler][2] += ball
                            rout = 0
                            pr = run
                            pw = wicket
                        if ball == 0.6:
                            over -= 0.6
                            over += 1.0
                            temp = striker
                            striker = runner
                            runner = temp
                            self.scoBowl[bowler][0] += run - pr
                            self.scoBowl[bowler][1] += wicket - pw-rout
                            self.scoBowl[bowler][2] += 1
                            rout=0
                            pr = run
                            pw = wicket
                            while over!=10.0:
                                rb = random.randint(0, 4)
                                temp = self.bowlord[rb]
                                if temp != bowler and self.scoBowl[temp][2] != 2:
                                    break
                            bowler = temp
                            comBowl(bowler)
                        over = float("{:.1f}".format(over))
            else:
                nb = 0

                if rand == ch:
                    comment(-1, striker)
                    wicket += 1
                    self.scoBat[striker][1] += 1
                    over += 0.1
                    ball = over - int(over)
                    ball = float("{:.1f}".format(ball))
                    if wicket != 10:
                        self.batord.remove(striker)
                        for i in self.batord:
                            if i != runner:
                                striker = i
                                break
                        comBat(striker, wicket)
                    if wicket == 10 and ball != 0.6:
                        self.scoBowl[bowler][0] += run - pr
                        self.scoBowl[bowler][1] += wicket - pw - rout
                        self.scoBowl[bowler][2] += ball
                        rout = 0
                        pr = run
                        pw = wicket
                    if ball == 0.6:
                        over -= 0.6
                        over += 1.0
                        temp = striker
                        striker = runner
                        runner = temp
                        self.scoBowl[bowler][0] += run - pr
                        self.scoBowl[bowler][1] += wicket - pw-rout
                        self.scoBowl[bowler][2] += 1
                        rout=0
                        pr = run
                        pw = wicket
                        while over!=10.0:
                            rb = random.randint(0, 4)
                            temp = self.bowlord[rb]
                            if temp != bowler and self.scoBowl[temp][2] != 2:
                                break
                        bowler = temp
                        comBowl(bowler)
                    over = float("{:.1f}".format(over))
                else:
                    if ch % 2 == 0:
                        comment(ch, striker)
                        run += ch
                        self.scoBat[striker][0] += ch
                        self.scoBat[striker][1] += 1
                        if self.scoBat[striker][0] >= 50 and s50[self.biodata[2].index(striker)] != 1:
                            s50[self.biodata[2].index(striker)] = 1
                            fifty(striker)
                        elif self.scoBat[striker][0] >= 100 and s100[self.biodata[2].index(striker)] != 1:
                            s100[self.biodata[2].index(striker)] = 1
                            hundred(striker)
                        elif self.scoBat[striker][0] >= 150 and s150[self.biodata[2].index(striker)] != 1:
                            s150[self.biodata[2].index(striker)] = 1
                            onefifty(striker)
                        over += 0.1
                        ball = over - int(over)
                        ball = float("{:.1f}".format(ball))
                        if run>=target and ball != 0.6:
                            self.scoBowl[bowler][0] += run - pr
                            self.scoBowl[bowler][1] += wicket - pw - rout
                            self.scoBowl[bowler][2] += ball
                            rout = 0
                            pr = run
                            pw = wicket
                        if ball == 0.6:
                            over -= 0.6
                            over += 1.0
                            temp = striker
                            striker = runner
                            runner = temp
                            self.scoBowl[bowler][0] += run - pr
                            self.scoBowl[bowler][1] += wicket - pw-rout
                            self.scoBowl[bowler][2] += 1
                            rout=0
                            pr = run
                            pw = wicket
                            while over!=10.0:
                                rb = random.randint(0, 4)
                                temp = self.bowlord[rb]
                                if temp != bowler and self.scoBowl[temp][2] != 2:
                                    break
                            bowler = temp
                            comBowl(bowler)
                        over = float("{:.1f}".format(over))
                    else:
                        comment(ch, striker)
                        run += ch
                        self.scoBat[striker][0] += ch
                        self.scoBat[striker][1] += 1
                        if self.scoBat[striker][0] >= 50 and s50[self.biodata[2].index(striker)] != 1:
                            s50[self.biodata[2].index(striker)] = 1
                            fifty(striker)
                        elif self.scoBat[striker][0] >= 100 and s100[self.biodata[2].index(striker)] != 1:
                            s100[self.biodata[2].index(striker)] = 1
                            hundred(striker)
                        elif self.scoBat[striker][0] >= 150 and s150[self.biodata[2].index(striker)] != 1:
                            s150[self.biodata[2].index(striker)] = 1
                            onefifty(striker)
                        temp = striker
                        striker = runner
                        runner = temp
                        over += 0.1
                        ball = over - int(over)
                        ball = float("{:.1f}".format(ball))
                        if run>=target and ball != 0.6:
                            self.scoBowl[bowler][0] += run - pr
                            self.scoBowl[bowler][1] += wicket - pw - rout
                            self.scoBowl[bowler][2] += ball
                            rout = 0
                            pr = run
                            pw = wicket
                        if ball == 0.6:
                            over -= 0.6
                            over += 1.0
                            temp = striker
                            striker = runner
                            runner = temp
                            self.scoBowl[bowler][0] += run - pr
                            self.scoBowl[bowler][1] += wicket - pw -rout
                            self.scoBowl[bowler][2] += 1
                            rout=0
                            pr = run
                            pw = wicket
                            while over!=10.0:
                                rb = random.randint(0, 4)
                                temp = self.bowlord[rb]
                                if temp != bowler and self.scoBowl[temp][2] != 2:
                                    break
                            bowler = temp
                            comBowl(bowler)
                        over = float("{:.1f}".format(over))

        if over!=10.0:
            pFormat(0.8)
            print(Style.BRIGHT + Fore.RED + "\t\t\tScore: " + Fore.BLUE + str(run) + "-" + str(
                wicket) + Fore.RED + "\t\t\tOver: " + Fore.BLUE + str(
                over) + Fore.RED + "\t\t\tBowler: " + Fore.BLUE + bowler)
        else:
            pFormat(0.8)
            print(Style.BRIGHT + Fore.RED + "\t\t\tScore: " + Fore.BLUE + str(run) + "-" + str(
                wicket) + Fore.RED + "\t\t\tOver: " + Fore.BLUE + str(
                over) + Fore.RED + "\t\t\tBowler: "+Fore.BLUE+"None")
        if wicket !=10:
            print(
                Fore.RED + "\tOn Strike: " + Fore.BLUE + striker + Fore.LIGHTBLUE_EX + f" {self.scoBat[striker][0]}({self.scoBat[striker][1]})",
                end="")
            for i in range(50 - len(striker + f" {self.scoBat[striker][0]}({self.scoBat[striker][1]})")):
                print(end=" ")
            print(
                Fore.RED + "Runner: " + Fore.BLUE + runner + Fore.LIGHTBLUE_EX + f" {self.scoBat[runner][0]}({self.scoBat[runner][1]})" + Style.RESET_ALL)
        else:
            print(
                Fore.RED + "\tOn Strike: " + Fore.BLUE +"None",end="")
            for i in range(50 - len(striker + f" {self.scoBat[striker][0]}({self.scoBat[striker][1]})")):
                print(end=" ")
            print(
                Fore.RED + "Runner: " + Fore.BLUE + runner + Fore.LIGHTBLUE_EX + f" {self.scoBat[runner][0]}({self.scoBat[runner][1]})" + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.MAGENTA + f"\t\tYou have scored {run}\n")
        pFormat(0.75)
        print(Style.RESET_ALL+Style.BRIGHT+f"\t\t{self.biodata[1]} BATTING SCORE CARD!!"+Style.RESET_ALL)
        print(Fore.RED+"\tName\t\t\tRun\t\tBalls Faced")
        print(Fore.BLUE,end="")
        for i in self.biodata[2]:
            print("\t"+i,end="")
            for j in range(16-len(i)):
                print(end=" ")
            print(str(self.scoBat[i][0])+"\t\t\t"+str(self.scoBat[i][1]))
        print(Style.RESET_ALL + Style.BRIGHT + f"\t\t{self.biodata[3]} BOWLING SCORE CARD!!" + Style.RESET_ALL)
        print(Fore.RED + "\tName\t\t\tRun\t\tWickets\t\tOvers")
        print(Fore.BLUE, end="")
        for i in self.scoBowl:
            print("\t" + i, end="")
            for j in range(16-len(i)):
                print(end=" ")
            print( str(self.scoBowl[i][0]) + "\t\t" + str(self.scoBowl[i][1])+"\t\t\t" + str(self.scoBowl[i][2]))
        if run>=target:
            return [run,1]
        elif run<target-1:
            return [run,0]
        else:
            return [run,2]

    def bowl(self,target=9999):
        global rand

        self.batord = []
        self.bowlord = []
        for i in self.biodata[4]:
            self.batord.append(i)
        self.bowlord = self.biodata[2]
        self.bowlord = self.bowlord[6:]
        self.scoBat = {}
        self.scoBowl = {}
        for self.i in self.bowlord:
            self.scoBowl[self.i] = [0, 0, 0.0]
        for self.i in self.batord:
            self.scoBat[self.i] = [0, 0]

        s50 = []
        s100 = []
        s150 = []
        for i in range(11):
            s50.append(0)
            s100.append(0)
            s150.append(0)
        striker = self.batord[0]
        runner = self.batord[1]
        bowler = self.bowlord[0]
        wicket = run = nb = 0
        temp = ""
        pw = 0
        pr = 0
        over = 0.0
        ball = 0.0

        ch = 0
        rout = 0

        while wicket != 10 and over < 10.0 and run<target:
            c = 0
            if over == 0.0 and c!=2:
                comBat(striker, wicket)
                comBat(runner, wicket)
            pFormat(0.8)
            print(Style.BRIGHT + Fore.RED + "\t\t\tScore: " + Fore.BLUE + str(run) + "-" + str(
                wicket) + Fore.RED + "\t\t\tOver: " + Fore.BLUE + str(
                over) + Fore.RED + "\t\t\tBowler: " + Fore.BLUE + bowler)
            print(
                Fore.RED + "\tOn Strike: " + Fore.BLUE + striker + Fore.LIGHTBLUE_EX + f" {self.scoBat[striker][0]}({self.scoBat[striker][1]})",
                end="")
            for i in range(50 - len(striker + f" {self.scoBat[striker][0]}({self.scoBat[striker][1]})")):
                print(end=" ")
            print(
                Fore.RED + "Runner: " + Fore.BLUE + runner + Fore.LIGHTBLUE_EX + f" {self.scoBat[runner][0]}({self.scoBat[runner][1]})" + Style.RESET_ALL)

            while c != 2:
                chp = enterChoice()
                if chp.isnumeric():
                    rand = int(chp)
                else:
                    rand = -1
                if checkrun(rand):
                    break
                c += 1

            if self.biodata[4].index(striker) <= 2:
                if self.scoBat[striker][0] <= 8:
                    ch=random.randint(0,6)
                elif run / over > 15.0 and rand >= 4:
                    ch = random.randint(0,3)
                elif run / over<8.0 and rand <= 4:
                    ch= random.randint(4,6)
                elif over >= 8.0 and run / over < 8.0:
                    ch = random.randint(4,6)
                else:
                    ch = random.randint(2, 6)
            elif 2 < self.biodata[4].index(striker) <= 6:
                if self.scoBat[striker][0] <= 3:
                    ch=random.randint(0,6)
                elif self.scoBat[striker][0] <= 8:
                    ch = random.randint(0,4)
                elif run / over > 15.0 and rand >= 4:
                    ch = random.randint(0,3)
                elif run / over < 7.0 and rand >= 4:
                    ch = random.randint(4,6)
                elif over >= 8.0 and run / over < 8.0:
                    ch = random.randint(5,6)
                else:
                    ch = random.randint(3, 6)
            else:
                if self.scoBat[striker][0] <=12:
                    ch = random.randint(0,4)
                elif run / over >= 4.0:
                    ch = random.randint(0, 6)
                elif run / over < 7.0:
                    ch = random.randint(3, 6)
                elif over >= 8.0 and run / over < 8.0:
                    ch = random.randint(4,6)
                else:
                    ch = random.randint(4, 6)

            if c == 2:
                ch = random.randint(4, 6)
                print(Fore.RED + "\tNO BALL!! Misunderstanding between brain and hand" + Style.RESET_ALL)
                print("\tOpponent has chosen:", ch)
                comment(ch, striker)
                run += ch + 1
                self.scoBat[striker][0] += ch
                self.scoBat[striker][1] += 1
                if run >= target:
                    self.scoBowl[bowler][0] += run - pr
                    self.scoBowl[bowler][1] += wicket - pw - rout
                    self.scoBowl[bowler][2] += ball
                    rout = 0
                    pr = run
                    pw = wicket
                continue

            print("\tOpponent has chosen:", ch)

            if rand == 0:
                if nb >= 3:
                    print(Fore.RED + "\tNO BALL!! A PLUNDER FROM THE BOWLER" + Style.RESET_ALL)
                    comment(ch, striker)
                    run += ch + 1
                    self.scoBat[striker][0] += ch
                    self.scoBat[striker][1] += 1
                    if run >= target:
                        self.scoBowl[bowler][0] += run - pr
                        self.scoBowl[bowler][1] += wicket - pw - rout
                        self.scoBowl[bowler][2] += ball
                        rout = 0
                        pr = run
                        pw = wicket
                else:
                    nb += 1
                    if ch != rand:
                        comment(ch, striker)
                        run += ch
                        self.scoBat[striker][0] += ch
                        self.scoBat[striker][1] += 1
                        if self.scoBat[striker][0] >= 50 and s50[self.biodata[4].index(striker)] != 1:
                            s50[self.biodata[4].index(striker)] = 1
                            fifty(striker)
                        elif self.scoBat[striker][0] >= 100 and s100[self.biodata[4].index(striker)] != 1:
                            s100[self.biodata[4].index(striker)] = 1
                            hundred(striker)
                        elif self.scoBat[striker][0] >= 150 and s150[self.biodata[4].index(striker)] != 1:
                            s150[self.biodata[4].index(striker)] = 1
                            onefifty(striker)
                        over += 0.1
                        ball = over - int(over)
                        ball = float("{:.1f}".format(ball))
                        if run>=target and ball != 0.6:
                            self.scoBowl[bowler][0] += run - pr
                            self.scoBowl[bowler][1] += wicket - pw - rout
                            self.scoBowl[bowler][2] += ball
                            rout = 0
                            pr = run
                            pw = wicket
                        if ball == 0.6:
                            over -= 0.6
                            over += 1.0
                            temp = striker
                            striker = runner
                            runner = temp
                            self.scoBowl[bowler][0] += run - pr
                            self.scoBowl[bowler][1] += wicket - pw - rout
                            self.scoBowl[bowler][2] += 1
                            rout = 0
                            pr = run
                            pw = wicket
                            while over != 10.0:
                                rb = random.randint(0, 4)
                                temp = self.bowlord[rb]
                                if temp != bowler and self.scoBowl[temp][2] != 2:
                                    break
                            bowler = temp
                            comBowl(bowler)
                        over = float("{:.1f}".format(over))
                    else:
                        comment(-1, striker)
                        wicket += 1
                        self.scoBat[striker][1] += 1
                        over += 0.1
                        ball = over - int(over)
                        ball = float("{:.1f}".format(ball))
                        if wicket != 10:
                            self.batord.remove(striker)
                            for i in self.batord:
                                if i != runner:
                                    striker = i
                                    break
                            comBat(striker, wicket)
                        if wicket == 10 and ball != 0.6:
                            self.scoBowl[bowler][0] += run - pr
                            self.scoBowl[bowler][1] += wicket - pw - rout
                            self.scoBowl[bowler][2] += ball
                            rout = 0
                            pr = run
                            pw = wicket
                        if ball == 0.6:
                            over -= 0.6
                            over += 1.0
                            temp = striker
                            striker = runner
                            runner = temp
                            self.scoBowl[bowler][0] += run - pr
                            self.scoBowl[bowler][1] += wicket - pw - rout
                            self.scoBowl[bowler][2] += 1
                            rout = 0
                            pr = run
                            pw = wicket
                            while over != 10.0:
                                rb = random.randint(0, 4)
                                temp = self.bowlord[rb]
                                if temp != bowler and self.scoBowl[temp][2] != 2:
                                    break
                            bowler = temp
                            comBowl(bowler)
                        over = float("{:.1f}".format(over))
            else:
                nb = 0

                if rand == ch:
                    comment(-1, striker)
                    wicket += 1
                    self.scoBat[striker][1] += 1
                    over += 0.1
                    ball = over - int(over)
                    ball = float("{:.1f}".format(ball))
                    if wicket != 10:
                        self.batord.remove(striker)
                        for i in self.batord:
                            if i != runner:
                                striker = i
                                break
                        comBat(striker, wicket)
                    if wicket == 10 and ball != 0.6:
                        self.scoBowl[bowler][0] += run - pr
                        self.scoBowl[bowler][1] += wicket - pw - rout
                        self.scoBowl[bowler][2] += ball
                        rout = 0
                        pr = run
                        pw = wicket
                    if ball == 0.6:
                        over -= 0.6
                        over += 1.0
                        temp = striker
                        striker = runner
                        runner = temp
                        self.scoBowl[bowler][0] += run - pr
                        self.scoBowl[bowler][1] += wicket - pw - rout
                        self.scoBowl[bowler][2] += 1
                        rout = 0
                        pr = run
                        pw = wicket
                        while over != 10.0:
                            rb = random.randint(0, 4)
                            temp = self.bowlord[rb]
                            if temp != bowler and self.scoBowl[temp][2] != 2:
                                break
                        bowler = temp
                        comBowl(bowler)
                    over = float("{:.1f}".format(over))
                else:
                    if ch % 2 == 0:
                        comment(ch, striker)
                        run += ch
                        self.scoBat[striker][0] += ch
                        self.scoBat[striker][1] += 1
                        if self.scoBat[striker][0] >= 50 and s50[self.biodata[4].index(striker)] != 1:
                            s50[self.biodata[4].index(striker)] = 1
                            fifty(striker)
                        elif self.scoBat[striker][0] >= 100 and s100[self.biodata[4].index(striker)] != 1:
                            s100[self.biodata[4].index(striker)] = 1
                            hundred(striker)
                        elif self.scoBat[striker][0] >= 150 and s150[self.biodata[4].index(striker)] != 1:
                            s150[self.biodata[4].index(striker)] = 1
                            onefifty(striker)
                        over += 0.1
                        ball = over - int(over)
                        ball = float("{:.1f}".format(ball))
                        if run>=target and ball != 0.6:
                            self.scoBowl[bowler][0] += run - pr
                            self.scoBowl[bowler][1] += wicket - pw - rout
                            self.scoBowl[bowler][2] += ball
                            rout = 0
                            pr = run
                            pw = wicket
                        if ball == 0.6:
                            over -= 0.6
                            over += 1.0
                            temp = striker
                            striker = runner
                            runner = temp
                            self.scoBowl[bowler][0] += run - pr
                            self.scoBowl[bowler][1] += wicket - pw - rout
                            self.scoBowl[bowler][2] += 1
                            rout = 0
                            pr = run
                            pw = wicket
                            while over != 10.0:
                                rb = random.randint(0, 4)
                                temp = self.bowlord[rb]
                                if temp != bowler and self.scoBowl[temp][2] != 2:
                                    break
                            bowler = temp
                            comBowl(bowler)
                        over = float("{:.1f}".format(over))
                    else:
                        comment(ch, striker)
                        run += ch
                        self.scoBat[striker][0] += ch
                        self.scoBat[striker][1] += 1
                        if self.scoBat[striker][0] >= 50 and s50[self.biodata[4].index(striker)] != 1:
                            s50[self.biodata[4].index(striker)] = 1
                            fifty(striker)
                        elif self.scoBat[striker][0] >= 100 and s100[self.biodata[4].index(striker)] != 1:
                            s100[self.biodata[4].index(striker)] = 1
                            hundred(striker)
                        elif self.scoBat[striker][0] >= 150 and s150[self.biodata[4].index(striker)] != 1:
                            s150[self.biodata[4].index(striker)] = 1
                            onefifty(striker)
                        temp = striker
                        striker = runner
                        runner = temp
                        over += 0.1
                        ball = over - int(over)
                        ball = float("{:.1f}".format(ball))
                        if run>=target and ball != 0.6:
                            self.scoBowl[bowler][0] += run - pr
                            self.scoBowl[bowler][1] += wicket - pw - rout
                            self.scoBowl[bowler][2] += ball
                            rout = 0
                            pr = run
                            pw = wicket
                        if ball == 0.6:
                            over -= 0.6
                            over += 1.0
                            temp = striker
                            striker = runner
                            runner = temp
                            self.scoBowl[bowler][0] += run - pr
                            self.scoBowl[bowler][1] += wicket - pw - rout
                            self.scoBowl[bowler][2] += 1
                            rout = 0
                            pr = run
                            pw = wicket
                            while over != 10.0:
                                rb = random.randint(0, 4)
                                temp = self.bowlord[rb]
                                if temp != bowler and self.scoBowl[temp][2] != 2:
                                    break
                            bowler = temp
                            comBowl(bowler)
                        over = float("{:.1f}".format(over))

        if over != 10.0:
            pFormat(0.8)
            print(Style.BRIGHT + Fore.RED + "\t\t\tScore: " + Fore.BLUE + str(run) + "-" + str(
                wicket) + Fore.RED + "\t\t\tOver: " + Fore.BLUE + str(
                over) + Fore.RED + "\t\t\tBowler: " + Fore.BLUE + bowler)
        else:
            pFormat(0.8)
            print(Style.BRIGHT + Fore.RED + "\t\t\tScore: " + Fore.BLUE + str(run) + "-" + str(
                wicket) + Fore.RED + "\t\t\tOver: " + Fore.BLUE + str(
                over) + Fore.RED + "\t\t\tBowler: "+Fore.BLUE+"None")
        if wicket != 10:
            print(
                Fore.RED + "\tOn Strike: " + Fore.BLUE + striker + Fore.LIGHTBLUE_EX + f" {self.scoBat[striker][0]}({self.scoBat[striker][1]})",
                end="")
            for i in range(50 - len(striker + f" {self.scoBat[striker][0]}({self.scoBat[striker][1]})")):
                print(end=" ")
            print(
                Fore.RED + "Runner: " + Fore.BLUE + runner + Fore.LIGHTBLUE_EX + f" {self.scoBat[runner][0]}({self.scoBat[runner][1]})" + Style.RESET_ALL)
        else:
            print(
                Fore.RED + "\tOn Strike: " + Fore.BLUE +"None",end="")
            for i in range(50 - len(striker + f" {self.scoBat[striker][0]}({self.scoBat[striker][1]})")):
                print(end=" ")
            print(
                Fore.RED + "Runner: " + Fore.BLUE + runner + Fore.LIGHTBLUE_EX + f" {self.scoBat[runner][0]}({self.scoBat[runner][1]})" + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.MAGENTA + f"\t\tOpponent has scored {run}\n")
        pFormat(0.75)
        print(Style.RESET_ALL + Style.BRIGHT + f"\t\t{self.biodata[3]} BATTING SCORE CARD!!" + Style.RESET_ALL)
        print(Fore.RED + "\tName\t\t\tRun\t\tBalls Faced")
        print(Fore.BLUE, end="")
        for i in self.biodata[4]:
            print("\t" + i, end="")
            for j in range(16-len(i)):
                print(end=" ")
            print(str(self.scoBat[i][0]) + "\t\t\t" + str(self.scoBat[i][1]))
        print(Style.RESET_ALL + Style.BRIGHT + f"\t\t{self.biodata[1]} BOWLING SCORE CARD!!" + Style.RESET_ALL)
        print(Fore.RED + "\tName\t\t\tRun\t\tWickets\t\tOvers")
        print(Fore.BLUE, end="")
        for i in self.scoBowl:
            print("\t" + i, end="")
            for j in range(16-len(i)):
                print(end=" ")
            print(str(self.scoBowl[i][0]) + "\t\t" + str(self.scoBowl[i][1]) + "\t\t\t" + str(self.scoBowl[i][2]))
        if run<target-1:
            return [run,1]
        elif run>=target:
            return [run,0]
        else:
            return [run,2]

# --------------------------------------------------------------------------------------------------------------------------------
# assume the below written statements are in main function


introduction()
user1 = ForePlay()
user1.nameInput()
while True:
    count = user1.checkName(user1.name)
    if count == "":
        user1.createPlayers(user1.name)
    else:
        user1.createPlayers(user1.name, count)
    user1.createOpponent()

    rules()
    ch=toss()
    sleep(2)
    user2 = GameThrough()
    user2.getBiodata(user1.country, user1.players, user1.oppCountry, user1.oppPlayer)


    if ch==1:
        print(Style.BRIGHT+Fore.MAGENTA + "\t1st inning of the Game is about to start!!\n\t\tCOUNTDOWN: ",
              end="" + Fore.YELLOW)
        for i in range(9, 2, -1):
            print(i + 1, end="... ")
            sleep(1)
        print(end="Let... ")
        sleep(1)
        print(end="The Game... ")
        sleep(1)
        print("BEGIN!!!" + Style.RESET_ALL)
        pFormat(0.75)
        temp1=user2.bat()
        run=temp1[0]
        pFormat(0.5)
        minput()
        print(Fore.RED+"\t\t\tTarget: "+str(temp1[0]+1)+Style.RESET_ALL)
        print(Style.BRIGHT + Fore.MAGENTA + "\t2nd inning of the Game is about to start!!\n\t\tCOUNTDOWN: ",
              end="" + Fore.YELLOW)
        for i in range(9, 2, -1):
            print(i + 1, end="... ")




            sleep(1)
        print(end="Let... ")
        sleep(1)
        print(end="The Game... ")
        sleep(1)
        print("BEGIN!!!" + Style.RESET_ALL)
        pFormat(0.75)
        temp2=user2.bowl(temp1[0]+1)
        pFormat(0.5)
        if temp2[1]==1:
            win(user1.name)
        elif temp2[1]==0:
            lose(user1.name)
        else:
            draw(user1.name)
    else:
        print(Style.BRIGHT + Fore.MAGENTA + "\t1st inning of the Game is about to start!!\n\t\tCOUNTDOWN: ",
              end="" + Fore.YELLOW)
        for i in range(9, 2, -1):
            print(i + 1, end="... ")
            sleep(1)
        print(end="Let... ")
        sleep(1)
        print(end="The Game... ")
        sleep(1)
        print("BEGIN!!!" + Style.RESET_ALL)
        pFormat(0.75)
        temp1 = user2.bowl()
        pFormat(0.5)
        minput()
        print(Fore.RED + "\t\t\tTarget: " + str(temp1[0]+1) + Style.RESET_ALL)
        pFormat(0.5)
        print(Fore.MAGENTA + "\t2nd inning of the Game is about to start!!\n\t\tCOUNTDOWN: ",
              end="" + Style.BRIGHT + Fore.YELLOW)
        for i in range(9, 2, -1):
            print(i + 1, end="... ")
            sleep(1)
        print(end="Let... ")
        sleep(1)
        print(end="The Game... ")
        sleep(1)
        print("BEGIN!!!" + Style.RESET_ALL)
        pFormat(0.75)
        temp2 = user2.bat(temp1[0]+1)
        run=temp2[0]
        pFormat(0.5)
        if temp2[1] == 1:
            win(user1.name)
        elif temp2[1]==0:
            lose(user1.name)
        else:
            draw(user1.name)
    total=""
    with open("highscore.hc") as f:
        while True:
            i=f.readline()
            if i=="":
                break

            line=i.split()
            if user1.name.replace(" ","(!@#$%^)") in line:
                print("your previous highscore was: "+line[2],end="")
            if run>int(line[2]):
                print(Fore.MAGENTA+"\nNow, your highscore becomes: "+str(run)+Style.RESET_ALL)
                i=i.replace(line[2],str(run))
            else:
                print(" and it stil remains the same!!")
            total=total+i

    with open("highscore.hc",'w') as f:
        f.write(total)

    print("do you want play again?")
    pFormat(0.2)
    ch0=""
    while not check(ch0):
        print("enter 'yes' to continue playing or 'no' to exit")
        ch0=enterChoice()
    if 'no' in ch0.lower():
        print("\t\t\t",end="")
        msg="THANQ!! VISIT AGAIN!!"
        for i in range(len(msg)):
            if i%6==0:
                print(Fore.CYAN,end="")
            elif i%6==1:
                print(Fore.MAGENTA,end="")
            elif i%6==2:
                print(Fore.RED,end="")
            elif i%6==3:
                print(Fore.YELLOW,end="")
            elif i%6==4:
                print(Fore.BLUE,end="")
            elif i%6==5:
                print(Fore.GREEN,end="")
            print(msg[i],end="")
        break