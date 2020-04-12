__author__="Amber Melton"


#Assigning Variables At The Beginning
score = 0
questionnum = 0
percentagecorrect = 0

#Beginning of Program
username = input("Hi there! What's your name?")
isready = input(username + "? Coolio! Are you ready to begin? (y/n)")


#Defines Function endsequence(reason) to end the quiz and present score when called.
def endsequence(reason):
	percentagecorrect = score*10/questionnum
	if reason == "quit":
		print("Really? You're quitting? Whatever. You got ", round(percentagecorrect, 2), r"% correct with a total of ", score, " points. What a loser...quitting...smh.")
		input("Press any key to continue...")
		exit("Game Over")
	else:
		print("Congratulations! Your finished the quiz! You got ", round(percentagecorrect, 2), " correct with a total of ", score, " points. I hope you had fun " + username + "!")
		input("Press any key to continute...")
		exit("Game Over")


#Defines Function continueplayfunct(continueplay) to check if the user wants to continue the quiz or end it before continuing with the program.
def continueplayfunct(continueplay):
	if continueplay == "y":
		input("Okie doke! Press any key to continue...")
	elif continueplay != "n":
		continueplay = input("Sorry! " + continueplay + " isn't an option. Try again! Keep playing? (y/n)")
		continueplayfunct(continueplay)
	else:
		endsequence("quit")


#Defines Function checkans(correctans,userans) that takes the assigned correct answer for the question and the user's answer and compares them to determine if the user got the right answer.
def checkans(correctans,userans):
	global questionnum
	global score
	if correctans == userans:
		questionnum += 1
		score += 10
		input("That's right! You have " + str(score) + " points. Press any key to continue...")
	else:
		questionnum += 1
		print("Wow. Way to go, loser. That's the wrong answer you dummy oh my god learn to trivia.")
		continueplay = input("Keep playing? (y/n)")
		continueplayfunct(continueplay)



#Defines Function checkisready() that runs once the user agrees that they are ready to begin the quiz, and once they do, the quiz proceeds until it eventually ends.
def checkisready():
	if isready == "n":
		print("oh...okay...see you later...")
		input("Press any key to continue...")
	elif isready != "y":
		input("Sorry, but " + isready + " isn't an option. Try again: are you ready to begin? (y/n)")
		checkisready()
	else:
		print("Perfect! Let's get right into it then!")
		input("Press any key to continue...")

		print("Question 1: What's the largest freshwater lake in the world?")
		print("a.Lake Superior")
		userans = input("b.Lake Inferior")
		checkans("a",userans)

		print("Question 2: What kind of weapon is a falchion?")
		print("a.A Bird")
		userans = input("b.A Sword")
		checkans("b",userans)

		print("Question 3: How many American states begin with the letter, 'P'?")
		print("a.Three")
		userans = input("b.One")
		checkans("b",userans)

		print("Question 4: What’s the only American state to begin with the letter ‘p’?")
		print("a.Pennsylvania")
		userans = input("b.Pencilvania")
		checkans("a",userans)

		print("Question 5: What is the capital city of Spain?")
		print("a.Barcelona")
		userans = input("b.Madrid ")
		checkans("b",userans)

		print("Question 6: How many valves does a trumpet have?")
		print("a.Three")
		userans = input("b.Two")
		checkans("a",userans)

		print("Question 7: When was William Shakespeare born?")
		print("a.April 22nd, 1564")
		userans = input("b.April 20th, 1567")
		checkans("a",userans)

		print("Question 8: When did the Cold War end?")
		print("a.1989")
		userans = input("b.1986")
		checkans("a",userans)

		print("Question 9: What is the most spoken language in the world?")
		print("a.English")
		userans = input("b.Chinese")
		checkans("b",userans)

		print("Question 10: What kind of tree do acorns grow on?")
		print("a.Maple Trees")
		userans = input("b.Oak Trees")
		checkans("b",userans)

		endsequence("complete")

#Calls Function checkisready() in order to begin the quiz
checkisready()
