class Employee:
    def __init__(self, name, start_time, end_time, first_break, second_break, lunch):
        self.name = name
        self.start_time = start_time
        self.first_break = first_break
        self.second_break = second_break
        self.lunch = lunch
        self.end_time = end_time

    def __eq__(self, other):
        return self.start_time == other.start_time

    def __lt__(self, other):
        return self.start_time < other.start_time

    def __str__(self):
        return f'{self.name} {self.start_time.strftime("%I:%M %p").lstrip("0").lower()} {self.end_time.strftime("%I:%M %p").lstrip("0").lower()}'
