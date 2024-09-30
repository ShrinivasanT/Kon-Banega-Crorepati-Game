"""
Hello Guys, This is a code for the infamous show "Kon Banega Crorepati" hosted by Mr.Amitabh Bachan. 
I have included some his language in thos code 😜. This Code uses basic datatypes and loops for the most part,
There is a timer inculcated within to have the time limit of 30sec for each question.
"""

import time
import sys
import threading

#variable definations
player_input = None
Win_amt = 100
#Questions and options stored in list
Q = [["Where is Taj Mahal Located:", ["A) Chennai", "B) Pune", "C) Bhopal", "D) Agra"]],
     ["Who was Ramachandra in Hindu Mythology :", ["A) Danav", "B) Human", "C) Vishnu Avatar", "D) None of these"]],
     ["Name of Villain in Singham :", ["A) Appu", "B) Dande", "C) Gopal", "D) Jayakant Shikre"]],
     ["Highest amount of rainfall in India :", ["A) Mawsynram", "B) Banglore", "C) Cherrapunji", "D) Lonavla"]],
     ["Python is a :", ["A) IDE", "B) User Interface", "C) Programming Language", "D) Computer"]],
     ["Akshay Kumar's real name is :", ["A) Salim", "B) Abbu", "C) Rajiv", "D) Hrishikesh"]]]
# Correct answers of each question w.r.t index in Q
A = ["D", "C", "D", "A", "C", "C"]
#Function to handle input
def get_input():
    global player_input
    player_input = input("Konsa option lock kiya jaye? : ").upper()

Game = input("Welcome to Kon Banega Crorepati \"hain\". Shall We Start the game? (y/n): ")
if Game.lower() == "n":
    print("Ok, thank you...")

elif Game.lower() == "y":
    print("Chaliye Suru Karte hai Kon Banega Crorepati! hain")  
    for i in range(len(Q)):
        T_limit = 30 #Time limit
        player_input = None  # Reset player input for each question
        question, answers = Q[i]
        print("Sawal Ye raha apke screen par")
        print(f"{i+1}.",question)
        print("Your options are:")
        print(*answers)
        # Input thread is created
        input_thread = threading.Thread(target=get_input)
        input_thread.start()
        # Main Thread (Logic,timer)
        start_T = time.time()
        while time.time() - start_T < T_limit:
            if player_input is not None:
                break
            time.sleep(1)
        
        if player_input is None:
            print("\n-------------------------------------------------------------")
            print("Sorry, time ran out!")
            break

        if player_input == A[i]:
            print("Bohot Khub!!")
            Win_amt = Win_amt*10
            print(f"Congrats, aap jitte hain pure {Win_amt} Rs")
        else:
            print("Oofff...Wrong Answer🥲")
            break
        print("-------------------------------------------------------------")
else:
    print("Wrong Choice")
