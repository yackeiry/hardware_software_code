def conversation(): 
 print("Do you like coding in python? Answer yes or no")
 answer =input().lower().strip()
 if answer == "yes":
 	print("Thats good - the United States needs more coders!!")
 elif answer == "no":
print("Perhaps you will change your mind ")
else: 
  print("I don't understand?")
  conversation()


def main():
   print("Welcome to any conversation program")
   conversation()
   print("Thanks for chatting with me")


if__name__== "__main__":
  main()