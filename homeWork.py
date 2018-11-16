
print("Predictions")

hey = "Hey, it's Jo!"
there = "there"

# My prediction is that it is going to print the 4th character
hey[:4]
## My prediction was wrong but instead prints up to the 4th character

# Comparing this to the last one im guessing that it will print the first character backwards, so in this case it will be "!"
hey[-1]
## I was correct in my prediction as it prints the first character but works from the other end

# Im guessing that this will print the sentence twice
hey*2
## I was correct because this one was farely obvious

# Using what i found out from the other examples i predict it will read "! there !"
hey[:-1] + there + hey[-1]
## I was wrong in my prediction because i was confused on how the ":-1" would print. I realised that it subtracts the character from the back then continues the sentence

# Using the last one as an example im guesisng it will read "Hey, it's Jo there !"
hey[:-1] + '' + there + hey[-1]
## I was somewhat correct however for some reason it doesnt print a space between the two strings. I dont understand what the '' command did as it doesnt look to make a difference

# I think that it is going to print the first character
there [1]
## It printed the second character because I forgot that it lists things starting from 0. However I dont understand why that rule doesnt apply to the previous strings

# Based on what I foundout this should be ' ' because the 5th character is a space
hey[4]
## I was correct

# This will read something like "Hey, it's Jo! Hey, it's Jo! therthere!"
hey *2 + there [:-1] + there + hey [-1]
## I was correct in my prediction

# I think this will print "oh"
hey[-2:1]
## It just printed a space, i dont understand why, thik it has something to do with counting 3 characters back instead of -2
