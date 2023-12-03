# Solution 1
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self._tseconds = hour*3600 + minute*60 + second

    def __repr__(self):
        print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d} - 0'dan geçen saniye sayısı= {self._tseconds}")

    def __str__(self):
        print(f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}')

    def _total_seconds(self):
        _tseconds = self.hour * 3600 + self.minute * 60 + self.second
        return print (_tseconds)

    def _seconds_to_time(self, seconds):
        if seconds >= 3600:
            hour = seconds // 3600
            minute = (seconds % 3600) // 60
            second = (seconds % 3600) % 60
        else:
            if seconds >= 60:
                hour = 0
                minute = seconds // 60
                second = seconds % 60
            else:
                hour = 0
                minute = 0
                second = seconds
        self.hour = hour
        self.minute = minute
        self.second = second
        return print(self.hour, self.minute, self.second)

dc = Time(5,8,4)
dc.__repr__()
dc.__str__()
dc._total_seconds()
dc._seconds_to_time(dc._tseconds)