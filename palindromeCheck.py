# 50 Projects Project Number 01
# Checks if a string is a palindrome or not by comparing it with a reversed slice.

import sys

# Checks if input is valid:
if len(sys.argv) > 2:
	print("Please enter just one word.")
	quit()
elif not sys.argv[1].isalpha():
	print("Please enter a word with no numbers or symbols")
	quit()

word = sys.argv[1]

# Compares input with reverse slice, prints answer.
if word.lower() == word.lower()[::-1]:
	print(word + " is a palindrome!")
else:
	print(word + " is NOT a palidrome!")


