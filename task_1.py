time_str = '1h 45m,360s,25m,30m 120s,2h 60s'

time_list = time_str.replace(' ', ',').split(',')

sum_min = 0

for i in time_list:
    if 'h' in i:
        m = int(i.replace('h','')) * 60
        sum_min += m
    elif 'm' in i:
        m = int(i.replace('m',''))
        sum_min += m
    else:
        m = int(i.replace('s',''))//60
        sum_min += m
print(sum_min)



