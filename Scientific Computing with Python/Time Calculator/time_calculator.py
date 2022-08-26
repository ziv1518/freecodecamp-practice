class time:
    def __init__(self,hour,min,PM=False, day=None):
        self.hour = int(hour)
        self.min = int(min)
        self.day = day
        if PM:
            self.hour += 12
    def display(self):
        display_hour = self.hour%12
        if display_hour == 0:
            display_hour += 12
        display_time = ':'.join([str(display_hour),str(self.min).rjust(2,'0')])
        if self.hour >= 12:
            display_time = ' '.join([display_time,'PM'])
        else:
            display_time = ' '.join([display_time,'AM'])
        if self.day:
            WEEK = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
            day_index = WEEK.index(self.day.lower())
            new_day = WEEK[(day_index + self.days)%7].capitalize()
            display_time = ', '.join([display_time,new_day])
        if self.days == 1:
            display_time = ' '.join([display_time,'(next day)'])
        elif self.days > 1:
            display_time = ' '.join([display_time,'({} days later)'.format(str(self.days))])
        return display_time


    def add(self,other):
        sum_min = self.min + other.min
        self.min = sum_min%60
        extra_hour = sum_min//60
        sum_hour = self.hour + other.hour + extra_hour
        self.hour = sum_hour%24
        self.days = sum_hour//24
        return self


def add_time(start, duration, day=None):
    current_time, AMPM = start.split(' ')
    current_hour, current_min = current_time.split(':')
    add_hour, add_min = duration.split(':')
    time1 = time(current_hour,current_min,AMPM=='PM',day)
    time2 = time(add_hour,add_min)
    time1.add(time2)
    print(time1.display())

if __name__ == '__main__':
    add_time("3:00 PM", "3:10")
    # Returns: 6:10 PM

    add_time("11:30 AM", "2:32", "Monday")
    # Returns: 2:02 PM, Monday

    add_time("11:43 AM", "00:20")
    # Returns: 12:03 PM

    add_time("10:10 PM", "3:30")
    # Returns: 1:40 AM (next day)

    add_time("11:43 PM", "24:20", "tueSday")
    # Returns: 12:03 AM, Thursday (2 days later)

    add_time("6:30 PM", "205:12")
    # Returns: 7:42 AM (9 days later)