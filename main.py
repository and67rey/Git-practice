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

n = int(input('Введи число кратное 2 в диапазоне от 8 до 64: '))
sierpinski_triangle(n)