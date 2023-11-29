# open alice_in_wonderland.txt file in reading mode and assign all the context to the context variable
file = open("alice_in_wonderland.txt", 'r')
context = file.read()
# Convert all the words in the alice_in_wonderland.txt into lowercase
context_lower = context.lower()
# While loop until the condition gets False
while True:
    # Ask the user to enter a word and assign it as a string to the variable user_word
    user_word = str(input("Please enter a word to count occurrences of or \"exit\" to end: "))        
    # Convert the word that the user input into lowercase
    user_word_lower = user_word.lower()
    # If the user's input is not "exit" ＝ True
    if user_word.lower() != "exit":
        # Count the lowercase word that the user input in the lowercase contexts and assign it the word_count variable 
        word_count = context_lower.count(user_word_lower)
        # Show the number of times the word appears in context
        print("The word " + user_word + " appears " + str(word_count) + " times in this book")
        # Continue the while loop
        continue
    # If the user input "exit"
    else:
        # Display "END"
        print("END!")
        # While loop break
        break
