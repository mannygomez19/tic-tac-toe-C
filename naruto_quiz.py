print("\nHere is a quiz to determine which Naruto character you are")

sakura_points = 0
sakura_points = int(sakura_points)

naruto_points = 0
naruto_points = int(naruto_points)

kakashi_points = 0
kakashi_points = int(kakashi_points)

shikamaru_points = 0
shikamaru_points = int(shikamaru_points)

sasuke_points = 0
sasuke_points = int(sasuke_points)

print("\nHere is a quiz to determine which Naruto character you are")

def qstn1():
    
    print \
        """1) How do you manage your anger?
              1) Physically exert your rage
              2) Talk it out/vent
              3) Bottle it up inside
              4) Confront who/what is angering you
              5) Analyze it and think it out """

    q1 = input("\n Answer: ")

    if q1 == 1:
        sakura_points += 1
    elif q1 == 2:
        naruto_points += 1
    elif q1 == 3:
        sasuke_points += 1
    elif q1 == 4:
        shikamaru_points += 1
    elif q1 == 5:
        kakashi_points += 1
    else:
        print("\n Please choose answer choices 1-5")
        qstn1()

    qstn2()
"----------------------------------------------------------------------------"
def qstn2():

    print \
        """2) How would you approach an opponent in a fight?
              1)Observe and study their movements, strike once you see their weakness
              2)Come at them like an uncontrollable barrage of force
              3)Move quickly, like a blur
              4)Allow them to exhaust themselves
              5)Work with a partner to defeat the adversary """
        
    q2 = input("\n Answer: ")

    if q2 == 1:
        shikamaru_points += 1
    elif q2 == 2:
        naruto_points += 1
    elif q2 == 3:
        sasuke_points += 1
    elif q2 == 4:
        kakashi_points += 1
    elif q2 == 5:
        sakura_points += 1
    else:
        print("\n Please choose answer choices 1-5")
        qstn2()

    qstn3()
"---------------------------------------------------------------------------"
def qstn3():

    print \
        """3) What animal do you identify with most?
              1)Rabbit
              2)Crow
              3)Tiger
              4)Hawk
              5)Snake """
    q3 = input("\n Answer: ")

    if q2 == 1:
        sakura_points += 1
    elif q2 == 2:
        shikamaru_points += 1
    elif q2 == 3:
        naruto_points += 1
    elif q2 == 4:
        kakashi_points += 1
    elif q2 == 5:
        sasuke_points += 1
    else:
        print("\n Please choose answer choices 1-5")
        qstn3()

    qstn4()
"---------------------------------------------------------------------------"
def qstn4():
    print \
        """4) What element describes you best?
              1)Earth
              2)Wind
              3)Fire
              4)Water
              5)Lightening"""
    q4 = input("\n Answer: ")

    if q2 == 1:
        naruto_points += 1
    elif q2 == 2:
        shikamaru_points += 1
    elif q2 == 3:
        sasuke_points += 1
    elif q2 == 4:
        sakura_points += 1
    elif q2 == 5:
        kakashi_points += 1
    else:
        print("\n Please choose answer choices 1-5")
        qstn4()

    qstn5()
    

"-----------------------------------------------------------------"

def qstn5():
    print \
        """5) Which pair of words describes you best?
              1)Serious and hardworking
              2)Introverted and kind
              3)Independent and blunt
              4)Outgoing and energetic
              5)Smart and lazy"""
    q5 = input("\n Answer: ")

    
    if q2 == 1:
        sasuke_points += 1
    elif q2 == 2:
        sakura_points += 1
    elif q2 == 3:
        kakashi_points += 1
    elif q2 == 4:
        naruto_points += 1
    elif q2 == 5:
        shikamaru_points += 1
    else:
        print("\n Please choose answer choices 1-5")
        qstn5()

"-------------------------------------------------------------------"
if sakura_points >= 3:
    print("You are Sakura!")
    
if sasuke_points >= 3:
    print("You are Sasuke!")
    
if kakashi_points >= 3:
    print("You are Kakashi!")
    
if naruto_points >= 3:
    print("You are Naruto!")
    
if shikamaru_points >= 3:
    print("You are Shikamaru!")
    
















