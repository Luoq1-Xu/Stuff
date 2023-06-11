class ForceUser:
    def __init__(self, name):
        self.name = name
        self.powers = [] # creates empty list of powers
    def do(self, action):
        if action in self.powers:
            print(self.name + " performs Force " + action)
        else:
            print(self.name + " does not know Force " + action)


class Jedi(ForceUser):
    def __init__(self, name):
        super().__init__(name)
        self.powers = ['jump', 'heal', 'mind trick', 'push']
    def do(self, action):
        if action in self.powers:
            print(self.name + " performs Force " + action)
        else:
            print(self.name + " does not know Force " + action)


class Sith(ForceUser):
    def __init__(self, *args):
        super().__init__(args[0])
        self.name = "Darth " + args[0]
        if len(args) == 2:
            self.alias = args[1]
        self.powers = ['jump', 'lightning', 'choke', 'push']
    def do(self, action):
        if action in self.powers:
            print(self.name + " performs Force " + action)
        else:
            print(self.name + " does not know Force " + action)

class JediTurnSith(Sith, Jedi):
    def __init__(self, name):
        super().__init__(name)


def main():
    vader = JediTurnSith("Vader")
    vader.do("choke")
    vader.do("heal")
    vader.do("jump")


if __name__ == "__main__":
    main()