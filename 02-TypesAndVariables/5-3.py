###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
b = input('b=')
c = input('c=')
integer_a = int(a)
integer_b = int(b)
integer_c = int(c)
objętość = integer_a * integer_b * integer_c
pole = 2 * (integer_c * integer_b + integer_b * integer_a + integer_a * integer_c)
print(f'Pole wynosi {pole}.')
print(f'Objętość wynosi {objętość}.')