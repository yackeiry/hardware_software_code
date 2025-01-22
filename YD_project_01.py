def main(): 
	name = input("What is your name?")
	print("We want to know if you like programming!")
	print()
	print("{}, Do you like progamming?" .format(name))
	answer = input()
	print("Great! You said {}?" .format(answer))
	print("Let's start learning some Python today")
	name = input("Are you attending guttman CC? answer yes or no?")
	if answer == "yes":
		interest = input("Do you like becoming an expert at technology in the future? yes or no?")
	else:
		print("yes i like becoming one!")
		print ("Thats Fantasic! and i would like to know about you more as your progress the semester!")
	insituations = input("What high school instituation did u attend?") 
	if answer == ("M303 The Facing History School"):
		print("Great! I love learning about your instituation Yackeiry!")
	print("It was nice speaking with you Yackeiry De la Cruz!")
	print("You are Currently attending, Guttman CC")
	print("I learned that you wanted to become a technology expert in the future")
	print("I learned also that your high school instituation name is M303 The Facing History School")
	print("You think that Guttman CC is more fun then M303 The Facing History School")
	print("It was fun learning about you!")
	print("See you soon!")



if __name__ == "__main__":
    main()


