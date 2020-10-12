import json
from Person import Person
import datetime
from datetime import timedelta


# Using Person class to create people
# Each Person has name, start time, end time
# Doesn't matter if these are in order because they will be sorted later


class Schedule:
    def __init__(self, file):
        # Sorts people based on start time
        self.array = self.read_file(file)
        self.sorted_person_time = sorted(self.array, key=self.person_start)

    def read_file(self, file):
        with open(file) as employee_schedule:
            schedule = json.load(employee_schedule)

        obj_employee = None
        for employee in
        return []

    # Getter for the person start time
    def person_start(self, person):
        return person.start_time

    def calculate_breaks(self):
        for x in range(len(self.sorted_person_time)):
            start = self.sorted_person_time[x].start_time
            end = self.sorted_person_time[x].end_time
            # duration = datetime.combine(datetime.min, end) - datetime.combine(datetime.min, start)

    # Prints out the people in order
    def print_in_order(self):
        for x in range(len(self.sorted_person_time)):
            print(self.sorted_person_time[x].name,
                  self.sorted_person_time[x].start_time.strftime("%I:%M%p").lstrip("0").lower(),
                  self.sorted_person_time[x].end_time.strftime("%I:%M%p").lstrip("0").lower())


def main():
    p3 = Person('lauren', datetime.time(10, 0, 0), datetime.time(16, 30, 0))
    p5 = Person('steven', datetime.time(11, 0, 0), datetime.time(19, 30, 0))
    p2 = Person('robby', datetime.time(9, 30, 0), datetime.time(18, 0, 0))
    p1 = Person('tomas', datetime.time(9, 0, 0), datetime.time(17, 30, 0))
    p4 = Person('reuella', datetime.time(10, 30, 0), datetime.time(18, 30, 0))

    array = [p3, p2, p1, p4, p5]  # Puts people into array
    schedule = '/Users/laurennelson/PersonalProjects/EmployeeScheduler/employee.json'
    Schedule.read_file(schedule)
    schedule.print_in_order()


if __name__ == "__main__":
    main()
