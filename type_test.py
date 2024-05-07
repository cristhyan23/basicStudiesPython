import time
import random
def text():
    try:
        with open("wpm_type_test/text.txt", "r") as f:
            lines = f.readlines()
            text = random.choice(lines).strip()
        return text
    except FileNotFoundError:
        print("File not found")
        

TEXT = text()
MAX_POINTS = 50
MIN_POINTS = 10

def calculate_result(typing,text):
    points = 0
    if text not in typing:
            points -= MAX_POINTS
    for i in range(len(typing)):
        if typing[i] == text[i]:
            points += MAX_POINTS
        else:
            points -= MIN_POINTS
    return points

def main():
    print("Welcome to This Typing Test You'll be given a block of text and need to type it as fast as possible")
    key = input("Press any key to start!")
    print("------------------------------")
    total_points = len(TEXT) * MAX_POINTS
    if key.strip():
        print(f"Max possible points:{total_points} ")
        start_time = time.time()
        wpm = 0
        while True:
            print(TEXT)
            type = input("Type: ")
            time_elapsed = max(time.time()-start_time,1) #max so we don't get a zero division error
            wpm = round((len(type)/(time_elapsed/60))/5) # index words per minute
            print(f"WPM: {wpm}")
            if type.strip():
                break
            elif "".join(type) == print(TEXT):
                break
        end_time = time.time()
        total_time = end_time - start_time
        points = calculate_result(type.strip(),TEXT)
        print(f"Congrats you've finished in {total_time:.2f} seconds  with a total points of: {points} n Your acurracy: {(points/total_points)*100:.2f}%")


if __name__ == "__main__":
    main()