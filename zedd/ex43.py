# 此练习中以编写迷你文字冒险游戏为例继续接受OOP更猛烈的洗礼

from sys import exit
# https://docs.python.org/3/library/sys.html?highlight=sys%20exit#sys.exit

from random import randint

from textwrap import dedent 
# Remove any common leading whitespace from every line in text. See more: https://docs.python.org/3/library/textwrap.html?highlight=dedent#textwrap.dedent
# 见CentralCorridor的前两个print，对于第一个print的字符串，如果没有dedent，打印时会把缩进也打印出来

# 请记住：set an instance 时丢进去的参数实际上丢给了这个类的 __init__ 函数

class Scene(object):
    
    # class Scene has-a enter that takes self param
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)
        # If it is an integer, zero is considered “successful termination” and any nonzero value is considered “abnormal termination” by shells and the like. Most systems require it to be in the range 0–127, and produce undefined results otherwise.
        # 为什么ex35里是0而这里是1？
        
    # 🚧这个enter到底干什么用的？？


class Engine(object):
    
    # class Engine has-a __init__ that takes self and scene_map params
    def __init__(self, scene_map):
        
        # __init__ has-a scene_map of some kind
        self.scene_map = scene_map
    
    def play(self):
        # 调用了后面Map类型的opening_scene和next_scene函数
        # 那么current_scene这里发生了什么？
            # 既然self.scene_map已经成为了类Map的实例（见此文档最后几行代码的注释），它就具有类Map的函数opening_scene()
            # 运行了opening_scene()函数，将得到的结果val（类CentralCorridor的一个实例）赋给current_scene（具体发生了什么？细节去见Map.opening_scene()的代码注释）
            # 也就是说，current_scene被设置为类CentralCorridor的一个实例，好的没了
        current_scene = self.scene_map.opening_scene()
        # 那么last_scene这里发生了什么？
            # （此处就没有current_scene那么详细了，类比就好）
            # 将last_scene设置为类Finished的一个实例
        last_scene = self.scene_map.next_scene('finished')
    
        # 只要条件符合【current_scene与last_scene不是同一个Scene】时：
        while current_scene != last_scene:
            # 🚧？？
            next_scene_name = current_scene.enter()
            # ？？
            current_scene = self.scene_map.next_scene(next_scene_name)
        
        # be sure to print out the last scene
        current_scene.enter()


class Death(Scene):
    
    
    quips = [
        "You died. You kinda suck at this.",
        "Your mun would be proud...if she were smarter.",
        "Such a loser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips))-1])
        exit(1)

class CentralCorridor(Scene):
    
    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew. You are the last surviving
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge, and 
            blow the ship up after getting into the escape pod.
            
            You're running down the central corridor to the Weapons
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            teeth, and evil clown costume flowing around his hate
            filled body. He's blocking the door to the Armory and
            about to pull a weapon to blast you.
            """))
            
        action = input("> ")
        
        if action == "shoot!":
            # 为什么开头是四个双引号？四个不对，会影响dedent的效果。试试就知道了。
            print(dedent("""
            Quick on the draw you yank out your blaster and fire
            it at the Gothon. His clown costume is flowing and 
            moving around his body, which throws off your aim.
            Your laser hits his costume but misses him entirely.
            This completely ruins his brand new costume his mother
            bought him, which makes him fly into an insane rage
            and blast you repeatedly in the face until you are
            dead. Then he eats you.
            """))
            return 'death'
        
        elif action == "dodge!":
            print(dedent("""
            Like a world class boxer you dodge, weave, slip and
            slide right as the Gothon's blaster cranks a laser
            past your head. In the middle of your artful dodge
            your foot slips and you bang your head on the metal
            wall and pass out. You wake up shortly after only to
            die as the Gothon stomps your head and eats you.
            """))
            return 'death'
        
        elif action == "tell a joke":
            print(dedent("""
                Lucky for you they made you learn Gothon insults in
                the academy. You tell the one Gothon joke you know:
                Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
                not to laugh, then bursts out laughing and can't move.
                While he's laughing you run up and shoot him square in
                the head putting him down, then jump through the
                Weapon Armory door.
            """))
            return 'laser_weapon_armory'
        
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    
    def enter(self):
        print(dedent("""
            You do a dive roll into the Weapon Armory, crouch and scan
            the room for more Gothons that might be hiding. It's dead
            quiet, too quiet. You stand up and run to the far side of 
            the room and find the neutron bomb in its container.
            There's a keypad lock on the box and you need the code to
            get the bomb out. If you get the code wrong 10 times then
            the lock closes forever and you can't get the bomb. The
            code is 3 digits.
            """))
        
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        print('this is code: ', code) # 调试用
        guess = input("[keypad]> ")
        guesses = 0
        
        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")
        
        if guess == code:
            print(dedent("""
                The container clicks open and the seal breaks, letting
                gas out. You grab the neutron bomb and run as fast as
                you can to the bridge where you must place it in the
                right spot.
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a 
                sickening melting sound as the mechanism is fused
                together. You decide to sit there, and finally the 
                Gothons blow up the ship from their ship and you die.
                """))
            return 'death'


class TheBridge(Scene):
    
    def enter(self):
        print(dedent("""
            You burst onto the Bridge with the netron destruct bomb
            under your arm and surprise 5 Gothon who are trying to 
            take control of the ship. Each of them has an even uglier
            clown costume that the last. They haven't pulled their
            weapons out yet, as they see the active bomb under your
            arms and don't want to set it off.
            """))
        
        action = input("> ")
        
        if action == "throw the bomb":
            print(dedent("""
                In a panic you throw the bomb at the group of Gothons
                and make a leap for the door. Right as you drop it a
                Gothon shoots you right in the back killing you. As
                you die you see another Gothon frantically try to 
                disarm the bomb. You die knowing they will probably
                blow up when it goes off.
                """))
            return 'death'
            
        elif action == "slowly place the bomb":
            print(dedent("""
                You point your blaster at the bomb under your arm and
                the Gothons put their hands up and start to sweat.
                You inch backward to the door, open it, and then
                carefully place the bomb on the floor, pointing your
                blaster at it. You then jump back through the door,
                punch the close button and blast the lock so the
                Gothons can't get out. Now that the bomb is placed
                you run to the escape pod to get off this tin can.
                """))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"


class EscapePod(Scene):
    
    def enter(self):
        print(dedent("""
            You rush through the ship desperately trying to make it to
            the escape pod before the whole ship explodes. It seems
            like hardly any Gothons are on the ship, so your run is
            clear of interference. You get to the chamber with the
            escape pods, and now need to pick one to take. Some of
            them could be damaged but you don't have time to lock.
            There's 5 pods, which one do you take?
            """))
        
        good_pod = randint(1,5)
        print('good pod: ', good_pod) # 调试用
        guess = input("[pod #]> ")
        
        if int(guess) != good_pod:
            print(dedent("""
                You jump into pod {guess} and hit the eject button.
                The pod escapes out into void of space, then
                implodes as the hull ruptures, crushing your body
                into jam jelly.
                """))
            return 'death'
        else:
            print(dedent("""
                You jump into pod {guess} and hit the eject button.
                The pod easily slides out into space heading to
                the planet below. As it flies to the planet, you look
                back and see your ship implode then explode like a
                bright star, taking our the Gothon ship at the same
                time. You win!
                """))
            return 'finished'


class Finished(Scene):
    
    def enter(self):
        print("You won! Good job.")
        return 'finished'
        

class Map(object):
    
    # class Map has-a scenes dictionary
    # create a dictionary named scenes which has 'central_corridor', ... , etc..
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }
    
    # class Map has-a __init__ that takes self and start_scene params
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    # class Map has-a next_scene that takes self and scene_name params
    def next_scene(self, scene_name):
        
        # get scene_name from the scenes dictionary and give it to val
        val = Map.scenes.get(scene_name)
        # if exclude "Map.", you will get NameError: name 'scenes' is not defined
        # 必须从Map类里获取这个字典
        return val
        
        # 以next_scene('central_corridor')为例，此时发生了什么呢？
            # 'central_corridor'赋给了变量scene_name
            # 此时相当于运行 val = Map.scenes.get('central_corridor')
            # 也就是从字典Map.scene里获取键'central_corridor'的值，也就是CentralCorridor()，赋给val
            # 这样，这段代码就相当于设置val为类CentralCorridor（类Scene的一个实例）的一个实例，并将这个val丢出去
    
    # class Map has-a opening_scene that takes self param
    def opening_scene(self):
        
        # 发生了什么呢？以程序起始状态为例，这个程序中Map获得的第一个参数（也就是start_scene也就是丢给self.start_scene的值）是'central_corridor'
            # 那么self.next_scene('central_corridor')发生了什么呢？见上面self.next_scene()的注释
        return self.next_scene(self.start_scene)


# set a_map as an instance of class Map and takes 'central_corridor' as start_scene
a_map = Map('central_corridor')
# set a_game as an instance of class Engine and takes a_map(an instance of class Map) as scene_map (so scene_map is an instance of class Map)
a_game = Engine(a_map)
    # 接下来发生了什么？
    # self.scene_map成为了class Map的（以central_corridor为start_scene的）实例
# 既然a_game是类Engine的对象了，那么a_game就具有函数play()了，运行！
a_game.play()