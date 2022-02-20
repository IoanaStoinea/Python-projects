print('Welcome to  Quiz')
answer = input('Are you ready to play the Quiz ? (yes/no) :')
score = 0
total_questions = 3

if answer.lower() == 'yes':
    answer = input('Question 1: What python  your Favourite programming language?')
    if answer.lower() == 'python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer = input('Question 2: With what library can we generate random numbers? ')
    if answer.lower() == 'random':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer = input('Question 3: Does openpyxl help us with excel workbooks?')
    if answer.lower() == 'yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

print('Thank you for Playing this small quiz game, you attempted', score, "questions correctly!")
mark = (score / total_questions) * 100
print('Marks obtained:', mark)
print('BYE!')