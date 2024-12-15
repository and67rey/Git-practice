import sys

def sierpinski_triangle(n) :
    y = n - 1
    while (y >= 0) :
        # printing space till
        # the value of y
        i = 0
        while (i < y ):
            print(" " ,end="")
            i = i + 1
        # printing '*'
        x = 0
        while (x + y < n ):
            # printing '*' at the appropriate
            # position is done by the and
            # value of x and y wherever value
            # is 0 we have printed '*'
            if ((x & y) != 0) :
                print(" ", end = " ")
            else :
                print("* ", end = "")
            x =x + 1
        print()
        y = y - 1

def setTowers(total_disks):
    global TOWERS
    global TOTAL_DISKS
    TOTAL_DISKS = total_disks
    # Populate Tower A:
    TOWERS = {'A': list(reversed(range(1, TOTAL_DISKS + 1))),
             'B': [],
             'C': []}

def printDisk(diskNum):
    # Print a single disk of width diskNum.
    global TOTAL_DISKS
    emptySpace = ' ' * (TOTAL_DISKS - diskNum)
    if diskNum == 0:
        # Just draw the pole.
        sys.stdout.write(emptySpace + '||' + emptySpace)
    else:
        # Draw the disk.
        diskSpace = '@' * diskNum
        diskNumLabel = str(diskNum).rjust(2, '_')
        sys.stdout.write(emptySpace + diskSpace + diskNumLabel + diskSpace + emptySpace)

def printTowers():
    global TOWERS
    global TOTAL_DISKS
    # Print all three towers.
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (TOWERS['A'], TOWERS['B'], TOWERS['C']):
            if level >= len(tower):
                printDisk(0)
            else:
                printDisk(tower[level])
        sys.stdout.write('\n')
    # Print the tower labels A, B, and C.
    emptySpace = ' ' * (TOTAL_DISKS)
    print('%s A%s%s B%s%s C\n' % (emptySpace, emptySpace, emptySpace, emptySpace, emptySpace))

def moveOneDisk(startTower, endTower):
    # Move the top disk from startTower to endTower.
    global TOWERS
    disk = TOWERS[startTower].pop()
    TOWERS[endTower].append(disk)

def solve(numberOfDisks, startTower, endTower, tempTower):
    # Move the top numberOfDisks disks from startTower to endTower.
    if numberOfDisks == 1:
        # BASE CASE
        moveOneDisk(startTower, endTower)
        printTowers()
        return
    else:
        # RECURSIVE CASE
        solve(numberOfDisks - 1, startTower, tempTower, endTower)
        moveOneDisk(startTower, endTower)
        printTowers()
        solve(numberOfDisks - 1, tempTower, endTower, startTower)
        return


option = input('Выберите опцию - T для ханойской башни или S для треугольника Серпинского: ')
if option == 'T':
    TOTAL_DISKS = int(input('Выберите число дисков: '))
    setTowers(TOTAL_DISKS)
    printTowers()
    solve(TOTAL_DISKS, 'A', 'B', 'C')
elif option == 'S':
    n = int(input('Введите число кратное 2 в диапазоне от 8 до 64: '))
    sierpinski_triangle(n)
else:
    print('Программа завершена')