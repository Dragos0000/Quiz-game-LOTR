# Project : Code your own Quiz
# By Dragos Paun
print("\n Welcome to my quiz about The Lord Of the Rings. Let's see if you loved the movies or if you need to watch them.\n")
print("\n Just type in the missing blanks: ___1___ ___2___ ___3___ ___4___ ___5___ ___6___ ___7___ ___8___ ___9___ ___10___ \n")

# easy
easy1 = "The ___1___ has ___2___ , it is ___3___ its masters ___4___ ."
easy2 = "Even the ___5___ person can ___6___ the course of the future . " 
easy3 = " ___7___ raises his ___8___ and ___9___ together into the air and said You shall not ___10___!"
easy = easy1 + easy2 + easy3

#medium
medium1 = "I am Gandalf the ___1___ . And I ___2___ back to you now .. at the ___3___ of the ___4___."
medium2 = "Oh, it is quite simple. If you are a ___5___ , you speak the ___6___ , and the ___7___ will ___8___"
medium3 = "A ___9___ may come when the ___10___ of men fails ... but it is not this ___9___ ."
medium = medium1 + medium2 + medium3

#hard
hard1 = "There is no curse in ___1___ , entish , or the ___2___ of ___3___ for this ___4___ ." 
hard2 = "We ___5___ , to ___6___ the ___7___ of the ___8___ . We will ___6___ on ... on the ___8___!" 
hard3 = "___9___ . The one place in ___10___ we dont want to see any closer. And it is the one place we are trying to get to. Let us face it were lost"
hard = hard1 + hard2 + hard3

# answers
easy_solutions = ["ring", "awoken", "heard", "call", "smallest", "change", "Gandalf", "sword", "staff", "pass"]

medium_solutions = ["white", "come", "turn", "tide", "friend", "password", "doors", "open", "day","courage"]

hard_solutions = ["elvish", "tongues", "men", "treachery", "swear", "serve", "master", "precious", "Mordor", "Middle-Earth"]

# blanks
blanks = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___", "___7___", "___8___", "___9___", "___10___"]

print("Below are the game levels...")
level_choice = ["easy", "medium", "hard"]
print(level_choice)

# This fuction takes as input the level desired by the user. Depending of the user input the variable quizText and answers 
# will have different values assigned according to the level choice.
def level():
    level_chosen = input("Select game level by typing it in.")
    if level_chosen.lower() == "easy" :
        quizText = easy
        answers = easy_solutions
        return quizText, answers, level_chosen
    elif level_chosen.lower() == "medium":
        quizText = medium
        answers = medium_solutions
        return quizText, answers, level_chosen
    elif level_chosen.lower() == "hard" :
        quizText = hard
        answers = hard_solutions
        return quizText, answers, level_chosen
    else :
        print("That option is not right.....Try again ....concentrate please")
        return level()
    
# This function takes guess (this is the word that the user will type in), the list of the possible answers and a number as inputs
#This function will check if the word typed in by the user is in the list of answers
def word_in_solution(guess, answers, n):
    if guess == answers[n]:
        # taking the guess of user and checking if in the answers.
        return guess
    else:
        return None

#this function will take as input the quiz text, the blank space that the user needs to fill in and the quess typed in by the user
#It will replace the blank with quess
def replacementFunction(quizText, currentBlank, guess):
    quizText = quizText.split()
    replaced = []
    for word in quizText:#looping through quizText
        if currentBlank in word:
            word = word.replace(currentBlank, guess)
            replaced.append(word)
        else:
            replaced.append(word)
    quizText = " ".join(replaced)
    return quizText
    
#this function is the game mechanics and will use all fuctions defined till now
#variables needed : quizText, answers and level_chosen
def play_game():
    quizText, answers, level_chosen = level() 
    replaced = []
    blanks = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___", "___7___", "___8___", "___9___", "___10___"]
    index = 0 #takes the current position and references moving forward a position. 
    print(quizText + "\n")
    while index < len(blanks):#while the current position is less than the total
        currentBlank = blanks[index]#blanks left
        guess = input("So what is the correct word for" + currentBlank + ":")
        if word_in_solution(guess, answers, index):#checks users input from the list.
            print("Awesome, good job! ... You might be a fan" + "\n")
            quizText = replacementFunction(quizText, currentBlank, guess)
            index = index + 1 #moves forward a blank
            print(quizText + "\n")#it will show the text after replacement
            if index == len(blanks):# shows the user they have completed the quiz.
                print("You have completed the quiz and I know now that you are a fan of Lord of the Rings.")
        else:
              print("Sorry, that is not correct.")

play_game()
