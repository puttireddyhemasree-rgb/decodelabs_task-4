print("Welcome to the General Knowledge Quiz!")
print("Answer the following 3 questions.\n")
score = 0
print("Question 1: What is the capital of France?")
answer1 = input("Your answer: ")
answer1 = answer1.strip().lower()
if answer1 == "paris":
    print("Correct! +1 point\n")
    score = score + 1  # State update
else:
    print("Wrong! The correct answer is Paris.\n")
  
print("Question 2: Which planet is known as the Red Planet?")
answer2 = input("Your answer: ")
answer2 = answer2.strip().lower()

if answer2 == "mars":
    print("Correct! +1 point\n")
    score = score + 1
else:
    print("Wrong! The correct answer is Mars.\n")

print("Question 3: How many days are there in a leap year?")
answer3 = input("Your answer: ")
answer3 = answer3.strip().lower()

if answer3 == "366":
    print("Correct! +1 point\n")
    score = score + 1
else:
    print("Wrong! The correct answer is 366.\n")

print("-------------------------")
print(f"Quiz Complete! Your final score is: {score}/3")
print("-------------------------")

if score == 3:
    print("Perfect! You are a quiz master.")
elif score == 2:
    print("Good job! Almost perfect.")
elif score == 1:
    print("Nice try! Keep learning.")
else:
    print("Better luck next time!")
