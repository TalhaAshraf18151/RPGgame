#Develop Room3 function here before plugging into main game

import time

correct_answers = 0

def intractQuiz_room():
    t0 = time.time()
    global correct_answers
    q1 = input("\nQ1) What should you do to a plastic food wrapper after you have eaten the food? \na) Eat the wrapper as well\nb) Dispose of it in a bin\nc) Throw it on the ground\n>")
    if q1 == "a":
        print("Good job correct answer")
        correct_answers += 1
    else:
        print("Oops, seems like you are incorrect the correct answer is actually \nb) Dispose of it in a bin.")

    q2 = input("\nQ2) How much plastic does the average New Zealander recycle? \na7.3 kg\nb)5.58 kg\nc)6.9 kg\n>")
    if q2 == "b":
        print("Good job correct answer")
        correct_answers += 1
    else:
        print("Oops, seems like you are incorrect the correct answer is actually \nb)5.58 kg")

    q3 = input("How long can it take plastic to break down? \na)9000 years\nb)100 years\nc)1000 years\n>")
    if q3 == "c":
        print("Good job correct answer")
        correct_answers += 1
    else:
        print("Oops, seems like you are incorrect the correct answer is actually \nc)1000 years")

    q4 = input("Recycling a single plastic bottle conserves enough energy to power a 60W bulb for how long?\na)60 mins\nb)30 mins\nc)20 mins\n>")
    if q4 == "b":
        print("Good job correct answer")
        correct_answers += 1
    else:
        print("Oops, seems like you are incorrect the correct answer is actually \nb)30 mins")
















    t1 = time.time() - t0


intractQuiz_room()
