# Solution 1
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self._tseconds = hour*3600 + minute*60 + second

    def __repr__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d} - 0'dan geçen saniye sayısı= {self._tseconds}"

    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'


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

        return Time(hour,minute,second)

    def __lt__(self, t):
        if isinstance(t, int | float):
            result = self._tseconds < t
        elif isinstance(t, Time):
            result = self._tseconds < t._tseconds
        else:
            raise TypeError('invalid type')
        return result

    def __le__(self, t):
        if isinstance(t, int | float):
            result = self._tseconds <= t
        elif isinstance(t, Time):
            result = self._tseconds <= t._tseconds
        else:
            raise TypeError('invalid type')
        return result

    def __gt__(self, t):
        if isinstance(t, int|float):
            result= self._tseconds > t
        elif isinstance(t, Time):
            result= self._tseconds > t._tseconds
        else:
            raise TypeError('invalid type')
        return result

    def __ge__(self, t):
        if isinstance(t, int | float):
            result = self._tseconds >= t
        elif isinstance(t, Time):
            result = self._tseconds >= t._tseconds
        else:
            raise TypeError('invalid type')
        return result

    def __eq__(self, t):
        if isinstance(t, int | float):
            result = self._tseconds == t
        elif isinstance(t, Time):
            result = self._tseconds == t._tseconds
        else:
            raise TypeError('invalid type')
        return result

    def __ne__(self, t):
        if isinstance(t, int | float):
            result = self._tseconds != t
        elif isinstance(t, Time):
            result = self._tseconds != t._tseconds
        else:
            raise TypeError('invalid type')
        return result

    def __add__(self,t):
        if isinstance(t, int | float):
            result= self._tseconds + t
        elif isinstance(t, Time):
            result = self._tseconds + t._tseconds
        else:
            raise TypeError('invalid type')

        return self._seconds_to_time(result)

    __radd__ = __add__

dc = Time(5,8,4)
ac = Time(4,2,3)
"""
dc.__repr__()
dc.__str__()
"""
print (dc._seconds_to_time(dc._tseconds))

dc._total_seconds()
ac._total_seconds()

print(dc+ac, type(dc+ac))