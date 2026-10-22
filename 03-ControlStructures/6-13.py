car_speed = int(input("Enter car speed: "))
speed_limit_min = 40
speed_limit_max = 140
if car_speed <= 140 and car_speed >= 40:
    print("OK")
else:
    print("Warning: invalid car speed!!")