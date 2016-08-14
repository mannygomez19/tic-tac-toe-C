from fractions import Fraction

print("\nHere is a quiz to determine which Naruto character you are")

print("\n1) How do you manage your anger?")

dictionary1 = {
        '\ta': ' Physically exert your rage',
        '\tb': ' Talk it out/vent',
        '\tc': ' Bottle it up inside',
        '\td': ' Confront who/what is angering you',
        '\te': ' Analyze it and think it out',
        }

for letter, answer in sorted(dictionary1.items()):
    print(letter + ")" + answer )

response1 = raw_input("answer (letter only): ")
"-----------------------------------------------------------"

print("\n2) How would you approach an opponent in a fight?")

dictionary2 = {
        '\ta': ' Observe and study their movements, strike once you see their weakness',
        '\tb': ' Come at them like an uncontrollable barrage of force',
        '\tc': ' Move quickly, like a blur',
        '\td': ' Allow them to exhaust themselves',
        '\te': ' Work with a partner to defeat the adversary',
        }

for letter, answer in sorted(dictionary2.items()):
    print(letter + ")" + answer )

response2 = raw_input("answer (letter only): ")
"---------------------------------------------------------------"
print("\n3) What animal do you identify with most?") 

dictionary3 = {
        '\ta': ' Rabbit',
        '\tb': ' Crow',
        '\tc': ' Tiger',
        '\td': ' Hawk',
        '\te': ' Snake',
        }

for letter, answer in sorted(dictionary3.items()):
    print(letter + ")" + answer)

response3 = raw_input("answer (letter only): ")

"-----------------------------------------------------------------"

print("\n4) What element describes you best?")

dictionary4 = {
        '\ta': ' Earth',
        '\tb': ' Wind',
        '\tc': ' Fire',
        '\td': ' Water',
        '\te': ' Lightening',
        }

for letter, answer in sorted(dictionary4.items()):
    print(letter + ")" + answer)

response4 = raw_input("answer (letter only): ")

"-----------------------------------------------------------------"

print("\n5) Which pair of words describes you best?")

dictionary5 = {
        '\ta': ' Serious and hardworking',
        '\tb': ' Introverted and kind',
        '\tc': ' Independent and blunt',
        '\td': ' Outgoing and energetic',
        '\te': ' Smart and lazy',
        }

for letter, answer in sorted(dictionary5.items()):
    print(letter + ")" + answer)

response5 = raw_input("answer (letter only): ")

"-------------------------------------------------------------------"

# Find a way to accept the answer and then use all of the other answers together
# to make a personality portfolio on some1.

sakura_answer_list = {'a': response1, 'e': response2, 'a': response3,
                      'd': response4, 'b': response5}
shikamaru_answer_list = ['d', 'a', 'b', 'b', 'e']
kakashi_answer_list = {'e': response1, 'd': response2, 'd': response3,
                       'e': response4, 'c': response5}
naruto_answer_list = ['b', 'b', 'c', 'a', 'd']
sasuke_answer_list = ['c', 'c', 'e', 'c', 'a']

for key, value in sakura_answer_list.items():
    if sakura_answer_list >= Fraction(3, 5):
        print("Your are Sakura!") # find a way to somehow call the answers from response 1 -5 
    else:
        break

for key, value in kakashi_answer_list.items():
    if kakashi_answer_list >= Fraction(3, 5):
        print("You are Kakashi Sensei!")
        
























