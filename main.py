
def main():
    questions = ("Who is Naruto's father?: ",
                 "Which character has the title of 'Copy Ninja'?: ",
                 "What village does Naruto belong to?: ",
                 "Who was Naruto's first teacher at the Ninja Academy?: ",
                 "Which clan is known for their Sharingan?: ")

    options = (("A. Minato Namikaze", "B. Jiraiya", "C. Kakashi Hatake", "D. Hiruzen Sarutobi"),
               ("A. Might Guy", "B. Itachi Uchiha", "C. Kakashi Hatake", "D. Tsunade"),
               ("A. Village Hidden in the Sand", "B. Village Hidden in the Mist", "C. Village Hidden in the Leaves", "D. Village Hidden in the Clouds"),
               ("A. Iruka Umino", "B. Kakashi Hatake", "C. Hiruzen Sarutobi", "D. Ebisu"),
               ("A. Hyuga", "B. Uzumaki", "C. Akimichi", "D. Uchiha"))

    answers = ("A", "C", "C", "A", "D")
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print("----------------------")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct answer")
        question_num += 1

    print("----------------------")
    print("       RESULTS        ")
    print("----------------------")

    print("answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int(score / len(questions) * 100)
    print(f"Your score is: {score}%")

if __name__ == '__main__':
    main()