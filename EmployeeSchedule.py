from Person import Person
import datetime
from datetime import timedelta

# Using Person class to create people
# Each Person has name, start time, end time
# Doesn't matter if these are in order because they will be sorted later

p3 = Person('lauren', datetime.time(10, 0, 0), datetime.time(16, 30, 0))
p5 = Person('steven', datetime.time(11, 0, 0), datetime.time(19, 30, 0))
p2 = Person('robby', datetime.time(9, 30, 0), datetime.time(18, 0, 0))
p1 = Person('tomas', datetime.time(9, 0, 0), datetime.time(17, 30, 0))
p4 = Person('reuella', datetime.time(10, 30, 0), datetime.time(18, 30, 0))

array = [p3, p2, p1, p4, p5]  # Puts people into array


# Getter for the person start time
def person_start(person):
    return person.start_time


# Sorts people based on start time
sorted_person_time = sorted(array, key=person_start)


def calculate_breaks(sorted_without_breaks):
    for x in range(len(sorted_without_breaks)):
        start = sorted_without_breaks[x].start_time
        end = sorted_without_breaks[x].end_time
        # duration = datetime.combine(datetime.min, end) - datetime.combine(datetime.min, start)


# Prints out the people in order
def print_in_order(sorted_people):
    for x in range(len(sorted_people)):
        print(sorted_people[x].name, sorted_people[x].start_time, sorted_people[x].end_time)


calculate_breaks(sorted_person_time)
print_in_order(sorted_person_time)
