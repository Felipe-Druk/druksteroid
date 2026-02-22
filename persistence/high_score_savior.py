from persistence.savior import Savior


class HighScore():
    
    def __init__(self, score, player_name):
        self.score = score
        self.player_name = player_name

class HighScoreSavior(Savior):

    def __init__(self, file_name, score : HighScore):
        super().__init__(file_name)
        self._datos = score
    
    def deserialize(self):
        loded_data : HighScore = super().deserialize()
        return loded_data

