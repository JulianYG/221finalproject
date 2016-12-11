'''
Created on Dec 11, 2016

@author: JulianYGao
'''
from utils import *

class TaxiMDP(object):
    '''
    classdocs
    '''
    def __init__(self, start_time, available_time, start_grid, grid_factor, rdd, 
    	discount=1.0, boundaries=(-74.021611, -73.742833, 40.616669, 40.886116)):
        '''
        Constructor
        '''
        self.t_avail = available_time
        self.t_start = start_time
        self.g_start = start_grid
        self.gamma = discount
        self.grid_factor = grid_factor
        self.traffic_info = rdd
        self.boundaries = boundaries
        
    def isEnd(self, state):
        return get_state_time(state[1]) > get_state_time_stamp(self.t_start, self.t_avail)[0]
        
    def startState(self):
        return (self.t_start, self.g_start)

    def actions(self, state):

    	result = [self._stay]
    	# Stay in the old grid, driving around
    	grid_scale = 0.0111 * self.grid_factor
    	lon, lat = (float(state[0][0][0]), float(state[0][0][1])), \
        	(float(state[0][1][0]), float(state[0][1][1]))

        # Nine actions in all possible directions or stay
    	if (lon[0] - grid_scale) > self.boundaries[0]:
    		result.append(self._move_left)
    		if (lat[1] + grid_scale) < self.boundaries[3]:
    			result.append(self._move_up_left)

		if (lat[0] - grid_scale) > self.boundaries[2]:
			result.append(self._move_down)
			if (lon[0] - grid_scale) > self.boundaries[0]:
				result.append(self._move_down_left)

		if (lat[1] + grid_scale) < self.boundaries[3]:
			result.append(self._move_up)
			if (lon[1] + grid_scale) < self.boundaries[1]:
				result.append(self._move_up_right)

		if (lon[1] + grid_scale) < self.boundaries[1]:
    		result.append(self._move_right)
    		if (lat[0] - grid_scale) > self.boundaries[2]:
    			result.append(self._move_down_right)

    	return result

    def prob_succ_reward(self, state, action):

    	result = []
    	new_target_location = action(state[0])
    	current_hr = get_state_time_hr(state[1])
    	data = self.traffic_info.lookup((new_target_location, current_hr))
    	if data:
    		distance_dist, time_dist, pay_dist, cruise_time, loc_trans_prob = data
    	else:
    		# Just use some approximation

    	_, new_time_hr, new_time_str = get_state_time_stamp(state[1], cruise_time)
    	new_state = (new_location, new_time_str)

    	



        return result

    def discount(self):
        return self.gamma
        
    def _stay(self, loc):
    	return ((str(loc[0][0]), str(loc[0][1])), (str(loc[1][0]), str(loc[1][1])))

    def _move_left(self, loc):
        return ((str(loc[0][0] - grid_scale), str(loc[0][1] - grid_scale)), 
        	(str(loc[1][0]), str(loc[1][1])))

    def _move_right(self, loc):
 		return ((str(loc[0][0] + grid_scale), str(loc[0][1] + grid_scale)), 
 			(str(loc[1][0]), str(loc[1][1])))

 	def _move_up(self, loc):
 		return ((str(loc[0][0]), str(loc[0][1])), (str(loc[1][0] + grid_scale), 
 			str(loc[1][1] + grid_scale)))

    def _move_down(self, loc):
    	return ((str(loc[0][0]), str(loc[0][1])), (str(loc[1][0] - grid_scale), 
    		str(loc[1][1] - grid_scale)))

    def _move_up_left(self, loc):
    	return ((str(loc[0][0] - grid_scale), str(loc[0][1] - grid_scale)), \
        	(str(loc[1][0] + grid_scale), str(loc[1][1] + grid_scale)))

    def _move_up_right(self, loc):
    	return ((str(loc[0][0] + grid_scale), str(loc[0][1] + grid_scale)), \
        	(str(loc[1][0] + grid_scale), str(loc[1][1] + grid_scale)))

    def _move_down_left(self, loc):
    	return ((str(loc[0][0] - grid_scale), str(loc[0][1] - grid_scale)), \
        	(str(loc[1][0] - grid_scale), str(loc[1][1] - grid_scale)))

    def _move_down_right(self, loc):
    	return ((str(loc[0][0] + grid_scale), str(loc[0][1] + grid_scale)), \
        	(str(lloc[1][0]at0 - grid_scale), str(loc[1][1] - grid_scale)))

        