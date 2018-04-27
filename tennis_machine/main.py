# import tests
# import json
# import requests as req

# url = 'https://matchstat.com/tennis/match-stats/w/4247743'

# class JsonHelper(object):
#     def __init__(self, request_response):
#         self._request_response = request_response
    
#     def _get_json_elements(self):
#         json_elements = self._request_response.json()

#         file_name = json_elements['stats'][0]['match_stats_id']
#         with open(file_name + '.json', 'r') as f:
#             json.dump(json_elements, '')   


# def _request():
#     try:
#         response = req.get(url)
#     except req.HTTPError as error:
#         print('' % error.args)
#         raise
#     else:
#         if response.status_code >= 200 and response.status_code <= 300:
#             # Response Helper
#             JsonHelper(response)._get_json_elements()
#         else:
#             raise ConnectionAbortedError('')

# _request()
import collections as c
a = {'stats': [{'match_stats_id': 98845, 'serve_1st_attempts': 62, 'player_fullname': 'Eugenie Bouchard', 'team': 1, 'total_points': 124, 'points_won': 57, 'serve_games_total': None, 'serve_games_won': None, 'aces': 2, 'double_faults': 3, 'serve_1st_total': 41, 'serve_1st_won': 24, 'serve_2nd_total': 21, 'serve_2nd_won': 12, 'return_points_total': 62, 'return_points_won': 21, 'return_break_points_total': 5, 'return_break_points_won': 1, 'winners': None, 'unforced_errors': None, 'serve_speed_fastest': None, 'serve_speed_1st_avg': None, 'serve_speed_2nd_avg': None, 'net_approaches': None, 'odds': None, 'match': 4247743}, {'match_stats_id': 98846, 'serve_1st_attempts': 62, 'player_fullname': 'Abigail Spears', 'team': 2, 'total_points': 124, 'points_won': 67, 'serve_games_total': None, 'serve_games_won': None, 'aces': 2, 'double_faults': 5, 'serve_1st_total': 33, 'serve_1st_won': 22, 'serve_2nd_total': 29, 'serve_2nd_won': 19, 'return_points_total': 62, 'return_points_won': 26, 'return_break_points_total': 7, 'return_break_points_won': 3, 'winners': None, 'unforced_errors': None, 'serve_speed_fastest': None, 'serve_speed_1st_avg': None, 'serve_speed_2nd_avg': None, 'net_approaches': None, 'odds': None, 'match': 4247743}]}
p_1 = a['stats'][0]
p_2 = a['stats'][1]
features = ['player_fullname', 'points_won', 'aces', 'double_faults', 'winners', 'unforced_errors']
n = []
w = list([[p_1[x] for x in features], [p_2[x] for x in features]])
# n.append(w)
h = c.namedtuple('Players', ['match'])
print(h(w))
# print(w)
# print(h)  