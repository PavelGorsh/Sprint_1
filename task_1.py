string_origin = '1h 45m,360s,25m,30m 120s,2h 60s'

string_list = string_origin.replace(' ', ',').split(',')

summ_minutes = 0

for i in string_list:
    if('h' in i):
        summ_minutes += 60 * int(i[:len(i) - 1])
    elif('m' in i):
        summ_minutes += int(i[:len(i) - 1])
    else:
        summ_minutes += (1 / 60) * int(i[:len(i) - 1])

print('Общее количество минут:', summ_minutes)
    