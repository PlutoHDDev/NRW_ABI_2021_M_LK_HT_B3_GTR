# Python
# Secret Sharing procedure
# Secret code is split into 3 partial secret codes
# Codes have 3 digits
# Three three-digit codes (x,y,z) are put into the function calculating the secret code
# The three codes (I, J, K) are the coordinates of an isosceles triangle
# The base of the isosceles triangle is IJ
# The height of the isosceles triangle is h
# The first three decimal places of the height are the secret code
from math import sqrt


def calculate_secret(ix, iy, iz, jx, jy, jz, kx, ky, kz):
    # Calculate the length of the base of the isosceles triangle
    base_length = sqrt((ix - jx) ** 2 + (iy - jy) ** 2 + (iz - jz) ** 2)
    # Calculate the length of one of the sides of the isosceles triangle
    side_length = sqrt((ix - kx) ** 2 + (iy - ky) ** 2 + (iz - kz) ** 2)
    # Calculate the height of the isosceles triangle
    # Formula: h = 1/2 * sqrt(4*(side_length**2) - (base_length**2))
    height = 1 / 2 * sqrt(4 * (side_length ** 2) - (base_length ** 2))
    # Calculate the secret code
    # x = first decimal place of height
    # y = second decimal place of height
    # z = third decimal place of height
    x = int(height * 10) % 10
    y = int(height * 100) % 10
    z = int(height * 1000) % 10
    return x, y, z


if __name__ == '__main__':
    # Ask for Code a
    ax = int(input("Enter the first digit of the first code: "))
    ay = int(input("Enter the second digit of the first code: "))
    az = int(input("Enter the third digit of the first code: "))
    # Ask for Code b
    bx = int(input("Enter the first digit of the second code: "))
    by = int(input("Enter the second digit of the second code: "))
    bz = int(input("Enter the third digit of the second code: "))
    # Ask for Code c
    cx = int(input("Enter the first digit of the third code: "))
    cy = int(input("Enter the second digit of the third code: "))
    cz = int(input("Enter the third digit of the third code: "))
    # Calculate the secret code
    x, y, z = calculate_secret(ax, ay, az, bx, by, bz, cx, cy, cz)
    # Print the secret code
    print('Secret code is:', str(x) + '' + str(y) + '' + str(z))
