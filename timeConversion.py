tot_seconds = int(input())
hour = 0
minutes= 0
seconds = 0
remaining = tot_seconds

if tot_seconds >= 3600:
    hour = tot_seconds // 3600
    remaining = tot_seconds % 3600

if tot_seconds % 60 < 60:
    minutes =  remaining // 60
    remaining = remaining % 60
    seconds = remaining

print(f"{hour}:{minutes}:{seconds}")