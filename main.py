weather = [
    ["Monday", 51, 8, True],
    ["Tuesday", 72, 2, True],
    ["Wednesday", 71, 5, True],
    ["Thursday", 39, 4, True],
    ["Friday", 12, 20, False],
    ["Saturday", 35, 15, True],
    ["Sunday", 48, 12, True],
]

activities = [
    ["Climbing", 0, 100, False],
    ["Hiking", 40, 5, True],
    ["Run", 45, 5, False],
    ["Walk", 35, 8, True],
    ["Biking", 50, 3, False],
]

def good_weather_for_activity(weather, activity):
    if weather[1] < activity[1]:
        return False
    if weather[2] > activity[2]:
        return False
    if weather[3] == activity[3]:
        return False
    return True

def activity_processor(days, activities):
    result = []
    for day in days:
        print day
        day_result = []
        for activity in activities:
            if good_weather_for_activity(day, activity):
                #result.append ([d,[0],])
                print "  {}".format(activity)


activity_processor(weather, activities)