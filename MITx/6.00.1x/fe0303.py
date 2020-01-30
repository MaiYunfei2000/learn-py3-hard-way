# 让机器使用二分法猜一个[0,100)内的整数

x = 27

high = 100
low = 0
print("Please think of a number between 0 and 100!")

while True:
    ans = int((high + low)/2)
    while True:
        print("Is your secret number " + str(ans) + "?")
        print("Enter 'h' to indicate the guess is too high. ", end='')
        print("Enter 'l' to indicate the guess is too low. ", end='')
        print("Enter 'c' to indicate I guessed correctly. ", end='')
        indication = input()
        if indication not in ['h', 'l', 'c']:
            print("Sorry, I did not understand your input.")
        else: break
    if indication == 'h':
        high = ans
    if indication == 'l':
        low = ans
    if indication == 'c':
        break

print("Game over. Your secret number was:", ans)