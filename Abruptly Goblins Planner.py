def add_gamer(gamer, lst):
    if type(gamer) == type({}):
        if 'name' in gamer.keys() and 'availability' in gamer.keys():
            lst.append({gamer['name']: gamer['availability']})
    else:
        print('fail')

def build_daily_frequency_table():
    return {'Sunday':0,'Monday':0,'Tuesday':0,'Wednesday':0,'Thursday':0,'Friday':0,'Saturday':0}

def calculate_availability(possible_players, available_frequency):
    for i in range(0,len(possible_players)-1):
        for name, days in possible_players[i].items():
            for day in days:
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

gamers = []
add_gamer({'name':'Kimberly Stall', 'availability':['Monday', 'Tuesday', 'Friday']}, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)
print(gamers)
count_availability = build_daily_frequency_table()
calculate_availability(gamers, count_availability)
print(count_availability)
game_night = find_best_night(count_availability)
print (game_night)
