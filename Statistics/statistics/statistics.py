from exporter.exporter import Exporter
from statistics.backend_interface import *

class StatisticsExporter(Exporter):

    necessary_information = []

    def __init__(self):
        pass


def search(player_name):
    # Belonging to a team?
    #player_name = args[0
    player_candidates = search_by_name_like(player_name)

    if len(player_candidates) > 1:
        text = "Too many players have that name... Please be more precise\n"
        for p in player_candidates:
            text+= "- " + p.name + "\n"
        return text
        # More Precise
    elif len(player_candidates) == 0:
        return None
    else:
        player = player_candidates[0]
        out_str = "Player: " + player.name + "\n"
        #    print([a for a in dir(player)])
        for attr, value in player.__dict__.items():
            if attr.startswith('_') or attr == "name" or attr == "position" or attr == "id":
                continue
            out_str += attr + " : " + str(value) + " \n"
#        team_id = Rosters.get_team(player.id)
#         if not team_id:
#             state = "Roster: Free Agent\n"
#             cost = ""
#         else:
#             state = "Roster: " + Teams.search_by_id(team_id).name + "\n"
#             cost = "Price: " + str(Rosters.get_cost(player.id)) + "\n"
        out_str += state + cost
        #        print(out_str)
        return out_str
