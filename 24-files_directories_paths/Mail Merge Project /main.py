# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
with open("./Input/Letters/starting_letter.txt") as file:
    content = file.read()

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

for name in names:
    with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode='w') as file:
        tailored_content = content.replace('[name]', name.strip())
        file.write(tailored_content)
