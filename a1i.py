# Python
# Use numpy
# Secret Sharing procedure
# Secret code is split into 3 partial secret codes
# Codes have 3 digits
# The line g:x=(1|3|4)+t*(4|-2|-1) is given
# Three three-digit codes (x,y,z) are put into the function calculating the secret code
# The three codes make up a plane
# The point of intersection of the line and the plane is the secret code (x,y,z)
import numpy as np


def calculate_parameters(ax, ay, az, bx, by, bz, cx, cy, cz):
    A = np.array([[(bx - ax), (cx - ax), -4], [(by - ay), (cy - ay), 2], [(bz - az), (cz - az), 1]])
    B = np.array([1 + (-ax), 3 + (-ay), 4 + (-az)])
    X = np.linalg.solve(A, B)
    # Round the result
    m = int(round(X[0]))
    n = int(round(X[1]))
    t = int(round(X[2]))
    return m, n, t


def g(t):
    return 1 + 4 * t, 3 + (-2) * t, 4 + (-1) * t


def calculate_secret(ax, ay, az, bx, by, bz, cx, cy, cz):
    # Calculate the parameters
    m, n, t = calculate_parameters(ax, ay, az, bx, by, bz, cx, cy, cz)
    # Calculate the secret code
    x, y, z = g(t)
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
