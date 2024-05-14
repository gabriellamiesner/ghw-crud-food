import sqlite3

class plan_preload: 
  def __init__(self, date, time, description, location) -> None:
    self.date = date
    self.time = time
    self.description = description
    self.location = location

schedule = []
locations = ['at home', 'not at home']
times = ['breakfast', 'lunch', 'dinner']

schedule.append(plan_preload('2024-05-13', times[0], 'global hack week stream', locations[0]))
schedule.append(plan_preload('2024-05-13', times[1], 'global hack week stream', locations[0]))
schedule.append(plan_preload('2024-05-13', times[2], "group study session" , locations[1]))

schedule.append(plan_preload('2024-05-14', times[0], 'global hack week stream', locations[0]))
schedule.append(plan_preload('2024-05-14', times[1], "hike w/ roommate", locations[0]))
schedule.append(plan_preload('2024-05-14', times[2], "global hack week stream" , locations[0]))

schedule.append(plan_preload('2024-05-15', times[0], "apartment tour" , locations[0]))
schedule.append(plan_preload('2024-05-15', times[1], "work meeting" , locations[1]))
schedule.append(plan_preload('2024-05-15', times[2], "friend's going away party", locations[1]))

schedule.append(plan_preload('2024-05-16', times[0], "gym", locations[0]))
schedule.append(plan_preload('2024-05-16', times[1], 'career center call', locations[0]))
schedule.append(plan_preload('2024-05-16', times[2], "movie night w/ friends"  , locations[0]))

schedule.append(plan_preload('2024-05-17', times[0], "reading outside" , locations[0]))
schedule.append(plan_preload('2024-05-17', times[1], 'study group', locations[0]))
schedule.append(plan_preload('2024-05-17', times[2], "concert downtown"  , locations[1]))

schedule.append(plan_preload('2024-05-18', times[0], "knitting club" , locations[1]))
schedule.append(plan_preload('2024-05-18', times[1], '3 hour long walk', locations[1]))
schedule.append(plan_preload('2024-05-18', times[2], "making chicken salad w/ roommate" , locations[0]))




connection = sqlite3.connect("schedule_plan.db")
cursor = connection.cursor()

cursor.execute("drop table if exists plans")
cursor.execute("create table plans (date DATE, time TEXT, plan_description TEXT, eating_location TEXT)")
for i in schedule:
  cursor.execute("insert into plans (date, time, plan_description, eating_location) values (?, ?, ?, ?)", (i.date, i.time, i.description, i.location))
  print("added ", i.description)

connection.commit()
connection.close()
