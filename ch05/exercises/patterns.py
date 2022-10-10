def star_pyramid():
    rows = int(input("How many rows?"))
    for i in range(0, rows):
        for j in range(0, i + 1):
            print('*', end='')
        print("\n")


def rstar_pyramid():
    rows = int(input("How many rows?"))
    while rows > 0:
        print('*'*rows, end='')
        rows = rows - 1
        print("\n")


star_pyramid()
rstar_pyramid()
