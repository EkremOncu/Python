# Solution 
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
            while result > 86399:   # 86399 -> 23:59:59'un saniyeye donusturulmus hali
                result = result - 86399
        elif isinstance(t, Time):
            result = self._tseconds + t._tseconds
            while result > 86399:
                result = result - 86399
        else:
            raise TypeError('invalid type')

        return self._seconds_to_time(result)
    __radd__ = __add__

    def __sub__(self, t):
        if isinstance(t, (int,float)):
            result= self._tseconds - t
            while result < 0:
                result= 86399+result

        elif isinstance(t, Time):
            result= self._tseconds - t._tseconds
            while result < 0:
                result = 86399 + result
        else:
            raise TypeError('invalid type')

        return self._seconds_to_time(result)
    __rsub__ = __sub__

    def __int__(self,t):
        return t._tseconds

    def __bool__(self):
        return bool(self._tseconds)

    def __getitem__(self, index):
        match index:
            case 0:
                return self.hour
            case 1:
                return self.minute
            case 2:
                return self.second
            case _:
                raise ValueError('Invalid index')

    def __setitem__(self, index, value):
        match index:
            case 0:
                self.hour = value
            case 1:
                self.minute = value
            case 2:
                self.second = value
            case _:
                raise ValueError('Invalid index')
        self._tseconds =self.hour * 3600 + self.minute * 60 + self.second

dc = Time(21,2,3)
ac = Time(10,2,3)


print(dc<ac)
print(dc>ac)
print(dc==ac)
print(dc!=ac)

print('------------')
print (dc._seconds_to_time(dc._tseconds))
print('------------')

dc._total_seconds()
ac._total_seconds()
print('------------')

print(dc+ac, type(dc+ac))
print(dc-ac, type(dc-ac))
print(ac-dc, type(ac-dc))
print('------------')

print(dc.__bool__())
print(dc.__int__(dc))
print('------------')
dc[1] = 23
print(dc[1])
print(dc._tseconds)