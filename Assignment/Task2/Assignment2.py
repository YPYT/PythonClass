# open alice_in_wonderland.txt file in reading mode and assign all the context to the context variable
file = open("alice_in_wonderland.txt", 'r')
context = file.read()
# Convert all the words in the alice_in_wonderland.txt into lower case
context_lower = context.lower()
# While loop until the condition gets False
while True:
    # Ask user to input a word as string and assign into the user_word variable
    user_word = str(input("Please enter a word to count occurrences of or \"exit\" to end: "))        
    # Convert the word that user input into lower case
    user_word_lower = user_word.lower()
    # If the user's input is not "exit" is True
    if user_word.lower() != "exit":
        # Count the lower case word that user input in the lower case contexts and assign into the word_count variable 
        word_count = context_lower.count(user_word_lower)
        # Display how many times the word appeared in the context
        print("The word " + user_word + " appears " + str(word_count) + " times in this book")
        # Continue the while loop
        continue
    # If the user input "exit"
    else:
        # Display "END"
        print("END!")
        # While loop break
        break
