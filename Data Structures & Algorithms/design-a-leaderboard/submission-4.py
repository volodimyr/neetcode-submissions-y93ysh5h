class Player:
    def __init__(self, sc):
        self.score = sc
    
    def update(self, sc):
        self.score = sc

class Leaderboard:
    def __init__(self):
        self.players = []
        self.m = {}
        self.sorted = True

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.m:
            self.m[playerId].score += score
        else:
            player = Player(score)
            self.m[playerId] = player
            self.players.append(player)
        self.sorted = False


    def top(self, K: int) -> int:
        if not self.sorted:
            self.players.sort(key=lambda x: x.score)
        i = len(self.players)-1
        sm = 0
        while K > 0:
            K-=1
            sm += self.players[i].score
            i-=1
        self.sorted = True
        return sm

    def reset(self, playerId: int) -> None:
        self.m[playerId].update(0)
        self.sorted = False


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
