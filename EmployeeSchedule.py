import json
from Employee import Employee
import datetime
from datetime import timedelta
from xlwt import Workbook


class Schedule:
    def __init__(self):
        self.schedule = Schedule

    # Get employees from json file
    # Sort by start time
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
            new_employee = Employee(name, start_time, end_time, 0, 0, 0)
            array.append(new_employee)

        array.sort()

        return array

    # Figure out how many breaks an employee should have
    # Calculate what time the break should be at
    def calculate_breaks(self, array):
        count = 0

        for x in array:
            count += 1
            start = x.start_time
            end = x.end_time
            time_start = datetime.datetime.combine(datetime.date.today(), start)
            time_end = datetime.datetime.combine(datetime.date.today(), end)
            # Get the difference between datetimes (as timedelta)
            date_time_difference = time_end - time_start
            # Divide difference in seconds by number of seconds in hour (3600)
            date_time_difference_in_hours = date_time_difference.total_seconds() / 3600

            if date_time_difference_in_hours >= 6:
                # Make sure no breaks or lunches overlap
                if count != 1:  # not on first employee
                    if x.start_time == prev_start:  # overlap
                        x.first_break = time_start + timedelta(hours=2, minutes=15)
                        x.lunch = x.first_break + timedelta(hours=2, minutes=15)
                        x.second_break = x.lunch + timedelta(hours=2)
                    else:
                        self.reg_breaks(x, time_start)
                else:
                    self.reg_breaks(x, time_start)
            else:
                if count != 1:  # not on first employee
                    if x.start_time == prev_start:  # overlap
                        x.first_break = time_start + timedelta(hours=2, minutes=15)
                        x.lunch = datetime.time(hour=0, minute=0, second=0, microsecond=0)
                        x.second_break = datetime.time(hour=0, minute=0, second=0, microsecond=0)
                    else:
                        self.short_breaks(x, time_start)

                else:
                    self.short_breaks(x, time_start)

            prev_start = x.start_time

        return

    # calculates the breaks for a full day and no overlap
    @staticmethod
    def reg_breaks(x, time_start):
        x.first_break = time_start + timedelta(hours=2)
        x.lunch = x.first_break + timedelta(hours=2)
        x.second_break = x.lunch + timedelta(hours=2)
        return

    # calculates the breaks for a partial day and no overlap
    @staticmethod
    def short_breaks(x, time_start):
        x.first_break = time_start + timedelta(hours=2)
        x.lunch = datetime.time(hour=0, minute=0, second=0, microsecond=0)
        x.second_break = datetime.time(hour=0, minute=0, second=0, microsecond=0)
        return


    # Creqte an excel spreadsheet with the schedule
    @staticmethod
    def make_excel_sheet(array_sorted):
        # Heading
        wb = Workbook()
        sheet1 = wb.add_sheet('Sheet 1')
        row = 0
        sheet1.write(row, 1, 'Start')
        sheet1.write(row, 2, 'Break 1')
        sheet1.write(row, 3, 'Lunch')
        sheet1.write(row, 4, 'Break 2')
        sheet1.write(row, 5, 'End')
        row += 1

        # Actual Info
        for x in range(len(array_sorted)):
            if array_sorted[x].lunch == datetime.time(hour=0, minute=0, second=0, microsecond=0):  # no lunch
                sheet1.write(row, 0, array_sorted[x].name)
                sheet1.write(row, 1, array_sorted[x].start_time.strftime("%I:%M%p").lstrip("0").lower())
                sheet1.write(row, 2, array_sorted[x].first_break.strftime("%I:%M%p").lstrip("0").lower())
                sheet1.write(row, 5, array_sorted[x].end_time.strftime("%I:%M%p").lstrip("0").lower())
                row += 1
            else:
                sheet1.write(row, 0, array_sorted[x].name)
                sheet1.write(row, 1, array_sorted[x].start_time.strftime("%I:%M%p").lstrip("0").lower())
                sheet1.write(row, 2, array_sorted[x].first_break.strftime("%I:%M%p").lstrip("0").lower())
                sheet1.write(row, 3, array_sorted[x].lunch.strftime("%I:%M%p").lstrip("0").lower())
                sheet1.write(row, 4, array_sorted[x].second_break.strftime("%I:%M%p").lstrip("0").lower())
                sheet1.write(row, 5, array_sorted[x].end_time.strftime("%I:%M%p").lstrip("0").lower())
                row += 1

        wb.save("schedule.xls")


def main():
    my_schedule = Schedule()
    sorted_array = my_schedule.read_file()
    my_schedule.calculate_breaks(sorted_array)
    my_schedule.make_excel_sheet(sorted_array)


if __name__ == "__main__":
    main()
