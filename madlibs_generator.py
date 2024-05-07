
try:
    with open("madlibs_generator/story_base.txt", "r") as f:
            all_story = f.read()  # Concatenate each line to the all_story variable
except FileNotFoundError:
    print("The file 'story_base.txt' was not found.")

# get al the keys into the text
words = set()
start_of_word = -1
target_start = "<"
target_end = ">"

for i, char in enumerate(all_story):
    if char == target_start:
        start_of_word = i
    
    if char == target_end and start_of_word != -1:
        word = all_story[start_of_word:i+1]
        words.add(word)
        start_of_word =-1

#{'<animal>', '<adjective>', '<noun>', '<place>', '<character>'}

#create a dictionary with the keys and words
answers = {}

for word in words:
    user_reply = input(f"Enter a word for {word}: ")
    answers[word] = user_reply

#replace the key of the story with the new words
for word in words:
    all_story = all_story.replace(word,answers[word])

print(all_story)



