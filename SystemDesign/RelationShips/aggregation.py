# An object is stored in the class but the class does not ows it

class Player:
    def __init__ (self,name):
        self.name = name
    def get_name(self):
        return self.name

class Team:
    def __init__ (self,name):
        self.name = name
        self.players = []
    def add_players(self,player):
        self.players.append(player)
    def team(self):
        for i in range(len(self.players)):
            player = self.players[i]
            print(player.get_name())

p1 = Player("Virat")
p2 = Player("Rohit")

team = Team("RCB")
team.add_players(p1)
team.add_players(p2)

team.team()