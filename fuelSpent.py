
time = int(input())
avg_speed = int(input())

total_fuel_need = 0
car_milage = 12

total_distance = avg_speed*time
total_fuel_need = total_distance / car_milage

print(f"{total_fuel_need:.3f}")
