from calendar import week


week_days = {1:'Пн', 2:'Вт', 3: 'Ср', 4:'Чт', 5:'Пт', 6:'Сб', 7:'Вс'}
print(week_days.keys())
print(week_days.values())
print(week_days.items())
print(week_days[3])
week_days['olga'] = 89650456534
print(week_days)