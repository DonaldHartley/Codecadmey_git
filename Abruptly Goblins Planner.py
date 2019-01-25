def add_gamer(gamer, lst):
    if type(gamer) == type({}):
        if 'name' in gamer.keys() and 'availability' in gamer.keys():
            lst.append({'name':gamer['name'], 'availability':gamer['availability']})
    else:
        print('fail')

def build_daily_frequency_table():
    return {'Sunday':0,'Monday':0,'Tuesday':0,'Wednesday':0,'Thursday':0,'Friday':0,'Saturday':0}

def calculate_availability(possible_players, available_frequency):
    for gamer in possible_players:
        for day in gamer['availability']:
            available_frequency[day] += 1 

def find_best_night(availability_lst):
    best_count = max(list(availability_lst.values()))
    if list(availability_lst.values()).count(best_count) > 1:
        days=[]
        for day, count in availability_lst.items():
            if count == best_count:
                days.append(day)
        return days, best_count
    elif list(availability_lst.values()).count(best_count) == 1:
        for day, count in availability_lst.items():
            if count == best_count:
                return [day], best_count

def available_on_night(gamers, days):
    player_lst = {}
    for day in days[0]:
        player_lst[day] = []
    for day in days[0]:
        for gamer in gamers:
            if day in gamer['availability']:
                player_lst[day].append(gamer['name'])
    return player_lst

def send_email(available_on_nights, game):
    for day in available_on_nights.keys():
        for name in available_on_nights[day]:
            print (f"Hello {name}, a game of {game} has openingings for players on {day}")

gamers = []
add_gamer({'name':'Kimberly Stall', 'availability':['Monday', 'Tuesday', 'Friday']}, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)
print(gamers)
count_availability = build_daily_frequency_table()
calculate_availability(gamers, count_availability)
print(count_availability)
game_night = find_best_night(count_availability)
print (game_night)
possible_attendees = available_on_night(gamers, game_night)
print (possible_attendees)
send_email(possible_attendees, "Abruptly Goblins!")

unable_to_attend_best_night = []

for person in gamers:
    if person['name'] not in possible_attendees['Thursday']:
        unable_to_attend_best_night.append(person)

second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
print(second_night_availability)
second_night = find_best_night(second_night_availability)
print (second_night)
possible_attendees_second_night = available_on_night(gamers, second_night)
print (possible_attendees_second_night)
send_email(possible_attendees_second_night, "Abruptly Goblins!")
