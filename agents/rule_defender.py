import numpy as np


class RuleDefender():

    def __init__(self, action_up, action_down, action_stop):
        self.actions = (action_up, action_down, action_stop)
        self.action_up = action_up
        self.action_down = action_down
        self.action_stop = action_stop
        self._area_size = 80
        self._interval = 30
        self._plan = []
    
    def act(self, observation):
        if len(self._plan) == 0:
            self._plan += [self.action_up] * self._interval  # up
            self._plan += [self.action_down] * (self._interval * 2)  # back to center & down
            self._plan += [self.action_up] * self._interval  # back to center
        
        return self._plan.pop(0)
    
    def observation_to_state(self, observation):
        """
        detect player, enemy and ball position
        """
        player_color = [92, 186, 92]
        enemy_color = [213, 130, 74]
        ball_color = [236, 236, 236]

        area = observation[35:194]  # cut game area

        player = self.search_position(area, player_color)
        enemy = self.search_position(area, enemy_color)
        ball = self.search_position(area, ball_color)

        #print("player:{} enemy:{} ball:{}".format(player, enemy, ball))

        return player, enemy, ball

    def search_position(self, area, color):
        position = []
        index = np.where(area == color)
        if len(index[0]) > 0:
            position = [index[0][0], index[1][0]]
        return position
