class ForceUser:
    def __init__(self, name):
        self.name = name
        self.powers = [] # creates empty list of powers
    def do(self, action):
        if action in self.powers:
            print(self.name + " performs Force " + action)
        else:
            print(self.name + " does not know Force " + action)


class Jedi:
    def __init__(self, name):
        self.name = name
        self.powers = ['jump', 'heal', 'mind trick', 'push']
    def do(self, action):
        if action in self.powers:
            print(self.name + " performs Force " + action)
        else:
            print(self.name + " does not know Force " + action)


class Sith:
    def __init__(self, *args):
        self.name = "Darth " + args[0]
        if len(args) == 2:
            self.alias = args[1]
        self.powers = ['jump', 'lightning', 'choke', 'push']
    def do(self, action):
        if action in self.powers:
            print(self.name + " performs Force " + action)
        else:
            print(self.name + " does not know Force " + action)




def main():
    emperor = Sith("Sidious", "Palpatine")
    print(emperor.name)
    print(emperor.alias)


if __name__ == "__main__":
    main()