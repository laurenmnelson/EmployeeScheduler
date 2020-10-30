import json
from Employee import Employee
import datetime
from datetime import timedelta
import pprint


class Schedule:
    def __init__(self):
        self.schedule = Schedule

    @staticmethod
    def read_file():
        file = '/Users/laurennelson/PersonalProjects/EmployeeScheduler/employee.json'
        array = []
        with open(file) as employee_schedule:
            schedule = json.load(employee_schedule)

        for employee in schedule:
            name = employee
            start_hr = schedule[employee]['start_hr']
            start_min = schedule[employee]['start_min']
            end_hr = schedule[employee]['end_hr']
            end_min = schedule[employee]['end_min']

            start_time = datetime.time(hour=start_hr, minute=start_min, second=0, microsecond=0)
            end_time = datetime.time(hour=end_hr, minute=end_min, second=0, microsecond=0)
            new_employee = Employee(name, start_time, end_time)
            array.append(new_employee)

        array.sort()

        # for employee in array:
        #     print(employee)

        return array

    def calculate_breaks(self, array):
        for x in array:
            start = x.start_time
            end = x.end_time
            time_start = datetime.datetime.combine(datetime.date.today(), start)
            time_end = datetime.datetime.combine(datetime.date.today(), end)
            # Get the difference between datetimes (as timedelta)
            date_time_difference = time_end - time_start
            # Divide difference in seconds by number of seconds in hour (3600)
            date_time_difference_in_hours = date_time_difference.total_seconds() / 3600

            if date_time_difference_in_hours >= 6:
                first_break = time_start
                print(first_break)

        return

    # Prints out the people in order
    def print_in_order(self, unsorted_array):
        for x in range(len(unsorted_array)):
            print(unsorted_array[x].start_time.strftime("%I:%M%p").lstrip("0").lower(),
                  unsorted_array[x].end_time.strftime("%I:%M%p").lstrip("0").lower())


def main():
    my_schedule = Schedule()
    sorted_array = my_schedule.read_file()
    calculated_breaks = my_schedule.calculate_breaks(sorted_array)


if __name__ == "__main__":
    main()
