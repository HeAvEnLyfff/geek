one_minute = 60
one_hour = 60 * one_minute
one_day = 24 * one_hour
duration = int (input('Введите количество времени в секундах'))

#Вывод времени до минуты
if duration < one_minute:
    print(duration,'Секунд')

#Вывод времени до часа
if duration >= one_minute and duration <= one_hour:
    print(duration // one_minute,'Минут', duration % one_minute,'Секунд')

#Вывод времени до дня
if duration >= one_hour and duration <= one_day:
    hour = duration // one_hour
    minute = duration // one_minute -(hour*one_minute)
    seconds = duration - (hour*one_hour+minute*one_minute)
    print(hour,'Часа',minute,'Минут',seconds,'Секунд')

#Вывод времени после суток
if duration >= one_day:
    day = duration // one_day
    hour = duration // one_hour - (day*24)
    minute = duration // one_minute - ((day*24+hour)*60)
    seconds = duration -((day*one_day)+(hour*one_hour)+(minute*one_minute))
    print(day,'Дней',hour, 'Часа', minute, 'Минут',seconds, 'Секунд')

