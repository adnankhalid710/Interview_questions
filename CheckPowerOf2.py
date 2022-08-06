def check_power(num1, num2):
    counter = 0
    ncounter = 0
    num3 = pow(2, 10)
    for i in range(num2):
        c = pow(2, i)
        if c == num2:
            counter +=1
            break;
        else:
            ncounter +=1
    if counter == 1:
            return print("Yes")
    else:
            return print("No")

n1 = 2
n2 = 16
check_power(n1, n2)

