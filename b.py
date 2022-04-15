# Python
# Secret Sharing procedure
# Secret code is split into 4 partial secret codes
# Codes have 3 parts
# The secret code is the first three digits of the volume of a square pyramid
# One code S(sx,sy,sz) is the top of the pyramid
# The codes A(ax,ay,az), B(bx,by,bz), C(cx,cy,cz) are three of the 4 corners of the base of the pyramid
from math import sqrt
from sympy import *


def calculate_secret(ax, ay, az, bx, by, bz, cx, cy, cz, sx, sy, sz):
    # Calculate the size of the base of the pyramid
    # Formula: G = a*b
    ab = sqrt((ax - bx) ** 2 + (ay - by) ** 2 + (az - bz) ** 2)
    ac = sqrt((ax - cx) ** 2 + (ay - cy) ** 2 + (az - cz) ** 2)
    bc = sqrt((bx - cx) ** 2 + (by - cy) ** 2 + (bz - cz) ** 2)
    # Initialize G
    G = 0
    if ab == ac:
        G = ab * ac
    elif ab == bc:
        G = ab * bc
    elif ac == bc:
        G = ac * bc
    # Calculate the height of the pyramid
    # h is the height of the pyramid
    # h is the distance of S(sx,sy,sz) from the base of the pyramid
    # The normal vector of the plane the base of the pyramid is in is given by the vector n(-3,0,4)
    # The plane the base of the pyramid is in is given by the equation Q:x=-3*x+4*z=9
    # Calculate the intersection of the plane and the line h
    # The line from S(sx,sy,sz) to the intersection of the plane and the line h is given by h:x=s+k*n
    # Get the x,y,z coordinates of h and put them into Q
    # -3*(sx+k*nx) + 4*(sz+k*nz) = 9
    # Solve the equation using sympy.solvers.solve
    # The solution is k
    n = Matrix([-3, 0, 4])
    k = Symbol('k')
    Qh = -3 * (sx + k * n[0]) + 4 * (sz + k * n[2]) - 9
    k = solve(Qh, k)[0]

    # Define a function for the line h:x=s+k*n
    def h(k):
        return sx + k * n[0], sy + k * n[1], sz + k * n[2]

    # Calculate the height of the pyramid using the function h
    h = sqrt((h(k)[0] - sx) ** 2 + (h(k)[1] - sy) ** 2 + (h(k)[2] - sz) ** 2)
    # Calculate the volume of the pyramid
    # Formula: V = 1/3*G*h
    V = 1 / 3 * G * h
    # Convert the volume to a string
    V = str(V)
    # Remove the decimal point
    V = V.replace('.', '')
    # Get the first three digits of the volume
    V = V[:3]
    # Convert the volume to an integer
    V = int(V)
    return V


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
    # Ask for Code s
    sx = int(input("Enter the first digit of the fourth code: "))
    sy = int(input("Enter the second digit of the fourth code: "))
    sz = int(input("Enter the third digit of the fourth code: "))
    # Calculate the secret code
    code = calculate_secret(ax, ay, az, bx, by, bz, cx, cy, cz, sx, sy, sz)
    # Print the secret code
    print('Secret code is:', code)
