# NUIST Quiz Game with LED feedback
import RPi.GPIO as GPIO
import time

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up LED pins
RED_LED = 17    # Pin for red LED (wrong answers)
GREEN_LED = 18  # Pin for green LED (correct answers)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)

# Turn off both LEDs initially
GPIO.output(RED_LED, GPIO.LOW)
GPIO.output(GREEN_LED, GPIO.LOW)

def quiz():
    print("Welcome to the Python Knowledge Quiz!")
    print("Answer the following questions:")

    # Questions and Answers
    questions = [
        "1) Which of the following is NOT a python data type?\na) int\nb) float\nc) rational\nd) string\ne) bool",
        "2) Which of the following is NOT a built-in operation in Python?\na) +\nb) %\nc) abs()\nd) sqrt()",
        "3) In a mixed-type expression involving ints and floats, Python will convert:\na) floats to ints\nb) ints to strings\nc) floats and ints to strings\nd) ints to floats",
        "4) The best structure for implementing a multi-way decision in Python is:\na) if\nb) if-else\nc) if-elif-else\nd) try",
        "5) What statement can be executed in the body of a loop to cause it to terminate?\na) if\nb) exit\nc) continue\nd) break"
    ]
    
    answers = [
        "c",  # rational is not a Python data type
        "d",  # sqrt() is from math module, not built-in
        "d",  # ints are converted to floats
        "c",  # if-elif-else is best for multi-way decisions
        "d"   # break terminates loops
    ]
    
    score = 0

    # Ask questions
    for i in range(len(questions)):
        user_answer = input(questions[i] + "\nYour answer: ").strip().lower()
        if user_answer == answers[i]:
            print("Correct!")
            # Light up green LED for correct answer
            GPIO.output(GREEN_LED, GPIO.HIGH)
            time.sleep(1)  # LED stays on for 1 second
            GPIO.output(GREEN_LED, GPIO.LOW)
            score += 1
        else:
            print(f"Incorrect! The correct answer is {answers[i]}.")
            # Light up red LED for wrong answer
            GPIO.output(RED_LED, GPIO.HIGH)
            time.sleep(1)  # LED stays on for 1 second
            GPIO.output(RED_LED, GPIO.LOW)

    # Provide final score
    print("\nQuiz completed!")
    print(f"You got {score}/{len(questions)} questions correct.")
    
    # Clean up GPIO
    GPIO.cleanup()

# Run the quiz function
quiz()
