# 什么意思？？？
from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
    
    choice = (isInt(input("> ")))
    # 如果 判断choice是否为整数的结果 为真
    if str.isdigit(choice) == True:
    # 这种做法输入小数点和负数仍然会出错，怎么解决？
    if not choice
        how_much = int(choice)
    else:
        dead("Man, learn to type a number. You are dead.")
    
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    
    while True: # 这是什么意思？？？到底是什么为真？但是这也许是为了不加任何其它条件进入while循环。
        choice = input("> ")
        
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        # 或者，如果 (choice为字符串“taunt bear” 且 非bear_moved) 的结果为真 
        elif "taunt bear" in choice and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        # 或者，如果(choice为字符串“taunt bear” 且 bear_moved) 的结果为真 
        elif ("open door" in choice or "leave" in choice) and "bear_moved":
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    
    choice = input("> ")
    
    if "flee" in choice:
        start()
    # 或者，如果choice的字符串中含有“head”
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        ethulu_room()


def dead(why):
    print(why, "Good job!")
    # ⚠️这是什么意思，结束程序吗？但是程序不是会自行停止吗？在网上查了一下之后：所以有这条代码和没有这条代码会有什么区别？
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    
    choice = input("> ")
    
    if choice == "left":
        # 运行函数bear_room()（进入熊的房间）
        bear_room()
    elif choice == "right":
        # 运行函数cthulhu_room()（进入克苏鲁的房间）
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
        

start() # 运行函数start()