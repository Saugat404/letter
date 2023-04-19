import random

# List of words to use in the letter
words = [
    'Dear ',
    'Friend, ',
    'I hope this letter finds you well. ',
    'I wanted to reach out and let you know that ',
    'Recently, I have been thinking about ',
    'I appreciate your friendship and support. ',
    'Take care and best wishes, '
]

# Generate a random name to address the letter
names = (input("Enter Name :"))
random_name = random.choice(names)

# Write the letter to a text file
with open(input("Enter File Name :"), 'w') as file:
    for i in range(5):
        file.write(words[i])
    file.write(random_name)
    file.write('\\')
    for i in range(5, len(words)):
        file.write(words[i])

    # Get machine assistance to write a closing sentence
    closing = 'Sincerely, '
    for i in range(10):
        next_word = random.choice('abcdefghijklmnopqrstuvwxyz ')
        closing += next_word
    closing += '\'
    file.write(closing)

print('Letter successfully written to file.')
exit()