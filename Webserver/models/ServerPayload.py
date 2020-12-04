class ServerPayload(object):
    def __init__(self, game_state, question, time_out, winner):
        self.game_state = game_state
        self.question = question
        self.time_out = time_out
        self.winner = winner