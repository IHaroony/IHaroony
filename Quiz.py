// Quiz //


import time  # for delays to work

# Greeting message
Greeting = "Welcome everyone!"
print(Greeting)
time.sleep(3)

def starting_messages():
    print("Starting the quiz.....")
    time.sleep(2)
    print("3")
    time.sleep(2)
    print("2")
    time.sleep(2)
    print("1")
    time.sleep(2)
    print(".....")
    time.sleep(3)

starting_messages()

def ask_question(question, choices, correct_answer):
    print(question)
    for choice in choices:
        print(choice)
    user_answer = input("Please enter the letter of your answer (A, B, C, or D): ").upper()
    
    if user_answer == correct_answer:
        print(" ::::::  Bingo! ::::::::  ")
        time.sleep(3)  
        return True
    else:
        print(f"Wrong! ): The correct answer was {correct_answer}")
        time.sleep(2)  
        return False


#

def provide_feedback(score, total):
    percentage = (score / total) * 100
    
    # Performance rating
    if percentage >= 90:
        rating = "Excellent"
    elif percentage >= 70:
        rating = "Good"
    elif percentage >= 50:
        rating = "Average"
    else:
        rating = "Needs Improvement"
    
    # Display rating
    print(f"\nYour final score is {score}/{total}.")
    print(f"Your score percentage is {percentage:.2f}%.")
    print(f"Performance: {rating}")


    #

questions = [
    ("What is the capital of France?", ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"], "C"),
    ("Where is the Statue of Liberty located?", ["A. Los Angeles", "B. Washington D.C.", "C. New York", "D. Miami"], "C"),
    ("The main character Luffy is in which show?", ["A. Naruto", "B. One Piece", "C. Hunter x Hunter", "D. Bleach"], "B"),
    ("Which NBA team has a green jersey and is located in Boston?", ["A. Chicago Bulls", "B. Miami Heat", "C. Boston Celtics", "D. Los Angeles Lakers"], "C"),
    ("Which team did Cristiano Ronaldo play for?", ["A. Barcelona", "B. Manchester United", "C. Liverpool", "D. Chelsea"], "B"),
    ("What is the name of the main character in The Sopranos?", ["A. Tony Soprano", "B. Michael Corleone", "C. Walter White", "D. Ghost"], "A"),
    ("Who wrote the novel '1984'?", ["A. George Orwell", "B. Aldous Huxley", "C. J.K. Rowling", "D. Ernest Hemingway"], "A")
]

# Score counter
score = 0

# Ask each question and update the score
for q in questions:
    if ask_question(q[0], q[1], q[2]):
        score += 1



def custom_end_messages():
    print("That was the last question, Wait... ")
    time.sleep(3)
    print("Let's see how well you did...")
    time.sleep(2)
    print("......")
    time.sleep(1.5)
    print("....")
    time.sleep(1.5)
    print("...")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print(".")
    time.sleep(1)

custom_end_messages()




# Provide feedback based on the score
provide_feedback(score, len(questions))
time.sleep(10)





def ending_message():
    print("Thanks for Playing")
    time.sleep(1.5)
    print(  "Please let me know if there are any improvements that can be made. :/ ")
    time.sleep(2)
    print(" Hopefully you enjoyed the quiz ")
    time.sleep(1.5)
    print(             "      ::::::::::      :) Goodbye! :)     :::::::::       "   )

ending_message()

