
while True:
    try:
        n = int(input())
    except EOFError:
        break
    number = 1
    while number%n != 0:
        number*=10
        number+=1
    print(len(str(number)))