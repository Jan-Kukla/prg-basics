###
# Calculation of circle area and circumference 
#
import math
# determine radius and PI values
promien = int(input('Jaki promień? '))
PI = math.pi
# calculate area 
pole = round(promien ** 2 * PI,2)
# calculate circumference 
obwod = round(2 * PI * promien,2)
# print results
print(f'Pole: {pole}, Obwód: {obwod}')