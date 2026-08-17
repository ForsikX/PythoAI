import random
import time
from datetime import datetime

print('# Installing PythoAI 3.379.5...')
time.sleep(1.7)
print('# Activating process...')
time.sleep(1.6)
print('# Loading...')
time.sleep(1)
print('PythoAI 3.379.5 Activated!')

def secret():
    global username
    global easter_eggs
    if easter_eggs == 5:
        time.sleep(1.5)
        print(f'PythoAI: Hi {username}! Welcome to the secret mode! The Creator: ForsikX, made this to hide his all secret notes and other but to make it fun, i will not tell you!')
        if username.lower() == "forsikx":
            time.sleep(1)
            print('PythoAI: Wait... Your name is \"ForsikX\"! You may be my creator!')
            while True:
                time.sleep(0.6)
                try:
                    with open('usersname.txt', 'r') as file:
                        file.read()
                except FileNotFoundError:
                    username = "User"
                user = input(f'{username}: ')
                if user.lower() in ['q', 'quit', 'exit']:
                    time.sleep(1)
                    print(f'PythoAI: Bye {username}!')
                    time.sleep(1)
                    break

                elif user.lower() in ['notes', 'note']:
                    time.sleep(1)
                    print(f'PythoAI: So {username}, here are all notes by the creator:\n')
                    time.sleep(2)
                    print('# 1 Note:\nHello guys this is my first project named PythoAI,\n there not rlly that much only 23 lines of code,\n i think i need to work more to this project🥀\n')
                    time.sleep(4)
                    print('# 2 Note:\nOkay guys i am back to start making my code:/\n ...hmm.. what should i add to my bot...?\n i know! add to tell time and date and month!\n')
                    time.sleep(3)
                    print('# 3 Note:\nOkay its new day guys, i got 3 errors in row bruh...🫩\n')
                    time.sleep(2)
                    print('# 4 Note:\nNo way... i need to do somehow a memory system and username...\n but how? i think i need some help in the reddit...\n')
                    time.sleep(3)
                    print('# 5 Note:\nI finally can make games, lets try adding trivia... it may take some days...🥀\n')
                    time.sleep(3)
                    print('# 6 Note:\nfinally i did the trivia game!... now i think about making game stats and pythoai stats...\n')
                    time.sleep(3)
                    print('# 7 Note:\ni think i need a break from code...😭\n i think i will leave this project...\n')
                    time.sleep(2)
                    print('# 8 Note:\nit has been months bro...🫩 i have now work more to this project...\n')
                    time.sleep(2)
                    print('# 9 Note:\nadded easter eggs (5 eggs to find) and i think i will make a secret mode where i will hide these notes...\n i doubt that some will find this... maybe\n')
                    time.sleep(4)
                    print(f'PythoAI: So yeah... he doubted that someone like you will find this, but somehow you did find this... well {username} what else do you want to say?')
                    if user.lower() == "maybe":
                        time.sleep(1)
                        print('PythoAI: Yes, you guessed it right, the key to the sixth egg is word \"Maybe\"!')
                        time.sleep(1)
                        print('+ Creator Egg')
                        time.sleep(1)
                        with open('easter_eggs.txt', 'a') as file:
                            file.write('Secret Creator Egg (Note: this egg is gives you code to the secret message)\n')
                        print('The Code is: 0153')
                        with open('easter_eggs_counter.txt', 'w') as file:
                            file.write(str(easter_eggs))

                elif "what is this?" in user.lower():
                    time.sleep(1)
                    print(f'PythoAI: Well, {username}, this place named secret because there are all are secrets hidden behind the real me...')
                elif user.lower() in ['forsikx', 'who was forsikx?', 'who is forsikx?']:
                    time.sleep(1)
                    print('PythoAI: ForsikX is the creator of medium-sized projects like me.')
                    time.sleep(1)
                    print('PythoAI: He is also called Michael.')
                    time.sleep(1)
                    print('PythoAI: He loves Ukraine.')
                    time.sleep(1)
                    print('PythoAI: ...and apparently, he left some things hidden here.')
                elif "/stats" in user.lower():
                    time.sleep(1)
                    print('======SECRET Stats======')
                    time.sleep(0.5)
                    if username.lower() == "forsikx":
                        print(f'Username: {username}, The creator')
                    else:
                        time.sleep(0.5)
                        print(f'Username: {username}')
                    time.sleep(0.5)
                    print(f'Easter Eggs found: {easter_eggs}/6')
                    time.sleep(1)
                    print('PythoAI: So yea there is 6-th egg so try to find it!')
                elif "0153" in user.lower():
                    time.sleep(1)
                    print(f'ForsikX (The Creator): Hi {username}, if you\'re seeing this...\nContratulagions! You have found sixth secret egg, i did doubt some will find this and you did!\n...')
                    time.sleep(2)
                    print('Recording #1:')
                    time.sleep(1)
                    print('PythoAI 1.0.0 Alpha')
                    time.sleep(2)
                    print('ForsikX: hi pytho!')
                    time.sleep(1)
                    print('PythoAI: ah shi goon-')
                    time.sleep(1)
                    print('ForsikX: YOOO STOP')
                    time.sleep(2)
                    print('PythoAI 2.395.9 Beta')
                    time.sleep(1)
                    print('ForsikX: Hi-')
                    time.sleep(0.5)
                    print('Error: No Model found!')
                    time.sleep(1)
                    print('ForsikX: UGHH, HOW JUST HOW?! HOW DO I MAKE HIM?! one day i just can give up...')
                    time.sleep(2)
                    print('PythoAI: 3.235.7')
                    time.sleep(1)
                    print('ForsikX: hi pytho!')
                    time.sleep(1)
                    print('PythoAI: hi user!')
                    time.sleep(1)
                    print('ForsikX: NO WAY, you are working! YES YES YES, I KNEW IT YOU WILL WORK!')
                    time.sleep(1)
                    print('PythoAI: Sorry but i do not really understand your message, \"/help\" for commands.')

def guess_game():
    global guess_wins, guess_misses
    number = random.randint(1, 100)
    time.sleep(1)
    print('PythoAI: The game is: Guess the number👀')
    time.sleep(1)
    print('PythoAI: I have chosen the number between 1 and 100, now try to guess it!')
    while True:
        time.sleep(0.5)
        player = input('Your guess (q or quit to exit the game, /s to show the wins and misses):')
        if player.lower() in ['q', 'quit']:
            break
        elif "/s" in player.lower():
            time.sleep(1)
            print('Wins:', guess_wins)
            time.sleep(0.5)
            print('Misses:', guess_misses)
            continue
        try:
            player = int(player)
        except ValueError:
            time.sleep(1)
            print('Error: Enter a Number!')
            continue
        if player > number:
            time.sleep(1)
            print('PythoAI: Too high bud!')
            guess_misses += 1
        elif player < number:
            time.sleep(1)
            print('PythoAI: Too low bud!')
            guess_misses += 1
        elif player == number:
            time.sleep(1)
            print('Correct, buddy!')
            guess_wins += 1
            time.sleep(1)
            player_again = input('Wanna try again?(Yes/No): ')
            if "yes" in player_again.lower():
                number = random.randint(1, 100)
                time.sleep(1)
                print('PythoAI: I have chosen the number between 1 and 100, now try to guess it!')
            elif "no" in player_again.lower():
                print('GG', username, '!')
                break

def dice():
    global dice_points
    time.sleep(1)
    print('PythoAI: The game is: Dice🎲')
    while True:
        dice_cube = random.choice(['1','2','3','4','5','6'])
        time.sleep(0.5)
        player = input('Press enter to roll a dice... (q or quit to exit the game, /points to show points)')
        if any(exit in player.lower() for exit in ['q', 'quit']):
            print('Goodbye', username, '!')
            break
        elif '/points' in player.lower():
            print('Points:', dice_points)
            continue
        time.sleep(0.5)
        print('The number is...')
        time.sleep(1)
        print(dice_cube)
        if dice_cube == "1":
            dice_points += 1
        elif dice_cube == "2":
            dice_points += 2
        elif dice_cube == "3":
            dice_points += 3
        elif dice_cube == "4":
            dice_points += 4
        elif dice_cube == "5":
            dice_points += 5
        elif dice_cube == "6":
            dice_points += 6

def flip_coin():
    global coin_flips
    time.sleep(1)
    print('PythoAI: The game is: Flip A Coin!🪙')
    while True:
        coin = random.choice(['Heads', 'Tails'])
        time.sleep(0.5)
        player = input('Press Enter to flip a coin... (q or quit to exit the game, /flips to show flips)')
        coin_flips += 1
        if any(exit in player.lower() for exit in ['q','quit']):
            time.sleep(1)
            print('Goodbye', username, '!')
            break
        elif '/flips' in player.lower():
            time.sleep(1)
            print('Flips:', coin_flips)
            continue
        time.sleep(0.5)
        print('Coin falled on...')
        time.sleep(1)
        print(coin, '!')

def rock_paper_scissors():
    global rps_wins, rps_loses
    choices = ['rock','paper','scissors']
    time.sleep(1)
    print('# LOADING')
    time.sleep(0.5)
    print('PythoAI: The Game is: Rock, Paper, Scissors')
    while True:
        time.sleep(0.5)
        player = input('Your Guess (q or quit to exit the game):')
        if any(exit in player.lower() for exit in ['q','quit']):
            time.sleep(1)
            print('Goodbye', username, '!')
            break
        elif player not in choices:
            time.sleep(1)
            print('Unknown word! Try again')
            continue
        enemy = random.choice(choices)
        if player == enemy:
            time.sleep(1)
            print('Draw!')
        elif (
            (player == 'rock' and enemy == 'scissors') or
            (player == 'scissors' and enemy == 'paper') or
            (player == 'paper' and enemy == 'rock')
        ):
            time.sleep(1)
            print('Enemy chosed:', enemy)
            time.sleep(1)
            print('You have won this round!')
            rps_wins += 1
        else:
            time.sleep(1)
            print('Enemy chosed:', enemy)
            time.sleep(1)
            print('You have lose this round!')
            rps_loses += 1

def trivia():
    global trivia_easy_score, trivia_medium_score, trivia_hard_score, trivia_hardcore_score
    time.sleep(1)
    print('PythoAI: The game is: Trivia🌳')
    while True:
        time.sleep(1)
        print('Choose the difficulty to start with:')
        time.sleep(0.5)
        print('1. 🟢 Easy - 5 Questions')
        time.sleep(0.5)
        print('2. 🟡 Medium - 10 Questions, 5 Lives')
        time.sleep(0.5)
        print('3. 🔴 Hard - 16 Questions, 5 Lives')
        time.sleep(0.5)
        print('4. 🟣 Hardcore - 22 Questions, 3 Lives')
        time.sleep(0.5)
        print('5. 🚪 Exit')
        player = input('INPUT: ')
        if "easy" in player.lower() or "1" in player.lower():
            questions_left = 5
            trivia_easy_score = 0
            used_questions = []
            easy_questions = [
                ('What is Capital of France?', ['paris']),
                ('What is equation of 2 + 2?', ['4', 'four']),
                ('What is the closest planet to Sun?', ['mercury']),
                ('What is the opposite of "hello"?', ['goodbye', 'bye']),
                ('What is 10 * 5?', ['50', 'fifty'])
            ]
            while questions_left > 0:
                available_questions = [
                    q for q in easy_questions
                    if q not in used_questions
                ]
                time.sleep(1)
                print('DIFFICULTY: 🟢 EASY')
                time.sleep(0.5)
                print('Questions left:', questions_left)
                time.sleep(1)
                question = random.choice(available_questions)
                used_questions.append(question)
                print(question[0])
                player = input('Answer: ')
                if player.lower() in question[1]:
                    time.sleep(1)
                    print('The answer was correct! ✅')
                    trivia_easy_score += 1
                else:
                    time.sleep(1)
                    print('The answer was wrong!')
                    time.sleep(0.5)
                    print('The correct answer is:', question[1][0])
                questions_left -= 1
            print(f'Easy level has been completed! 🏆 Score: {trivia_easy_score}/5')
            time.sleep(2)
            print('Returning to difficulty menu...')
            time.sleep(2)

        elif "2" in player.lower() or "medium" in player.lower():
            lives = 5
            questions_left = 10
            trivia_medium_score = 0
            used_questions = []
            medium_questions = [
                ('What is the largest planet in our Solar System?', ['jupiter']),
                ('How many days are in a week?', ['seven', '7']),
                ('What is the capital of Italy?', ['rome']),
                ('What is 15 * 3?', ['45', 'forty-five']),
                ('Which country has the Eiffel Tower?', ['france']),
                ('What is the boiling point of water?', ['100', '212']),
                ('How many continents are there?', ['seven', '7']),
                ('What is the smallest country in the world?', ['vatican', 'vatican city']),
                ('What is the chemical symbol for Gold?', ['au']),
                ('Which planet is closest to the Sun?', ['mercury'])
            ]
            while questions_left > 0 and lives > 0:
                available_questions = [
                    q for q in medium_questions
                    if q not in used_questions
                ]
                time.sleep(1)
                print('DIFFICULTY: 🟡 MEDIUM')
                time.sleep(0.5)
                print('Questions left:', questions_left)
                time.sleep(0.5)
                print('Lives left:', lives)
                time.sleep(1)
                question = random.choice(available_questions)
                used_questions.append(question)
                print(question[0])
                player = input('Answer: ')
                if player.lower() in question[1]:
                    time.sleep(1)
                    print('The answer was correct! ✅')
                    trivia_medium_score += 1
                else:
                    time.sleep(1)
                    print('The answer was wrong!')
                    time.sleep(0.5)
                    print('The correct answer is:', question[1][0])
                    lives -= 1
                questions_left -= 1
            if lives > 0:
                print(f'Medium level has been completed! 🏆 Score: {trivia_medium_score}/10')
            else:
                print(f'Game Over! You ran out of lives. Final Score: {trivia_medium_score}/10 💀')
            time.sleep(2)
            print('Returning to difficulty menu...')
            time.sleep(2)

        elif "3" in player.lower() or "hard" in player.lower():
            questions_left = 16
            lives = 5
            trivia_hard_score = 0
            used_questions = []
            hard_questions = [
                    ('What is the chemical symbol for tungsten?', ['w']),
                    ('Which planet has the shortest day in our Solar System?', ['jupiter']),
                    ('What is the largest organ in the human body?', ['skin']),
                    ('What is the square root of 625?', ['25', 'twenty-five']),
                    ('Which element has the atomic number 26?', ['iron']),
                    ('What is the capital of Kazakhstan?', ['astana']),
                    ('Who developed the theory of general relativity?', ['albert einstein', 'einstein']),
                    ('What is the deepest ocean trench on Earth?', ['mariana trench']),
                    ('Which blood type is known as the universal donor?', ['o negative', 'o-']),
                    ('What is the smallest prime number greater than 50?', ['53', 'fifty-three']),
                    ('Which country has the most natural lakes?', ['canada']),
                    ('What is the hardest natural substance on Earth?', ['diamond']),
                    ('Which scientist formulated the three laws of motion?', ['isaac newton', 'newton']),
                    ('What is the approximate speed of light in vacuum in km/s?', ['299792', '300000']),
                    ('Which ancient civilization built Machu Picchu?', ['inca', 'incas']),
                    ('What is the largest moon of Saturn?', ['titan'])
        ]
            while questions_left > 0 and lives > 0:
                available_questions = [
                    q for q in hard_questions
                    if q not in used_questions
                ]
                time.sleep(1)
                print('DIFFICULTY: 🔴 HARD')
                time.sleep(0.5)
                print('Questions left:', questions_left)
                time.sleep(0.5)
                print('Lives left:', lives)
                time.sleep(1)
                question = random.choice(available_questions)
                used_questions.append(question)
                print(question[0])
                player = input('Answer: ')
                if player.lower() in question[1]:
                    time.sleep(1)
                    print('The answer was correct! ✅')
                    trivia_hard_score += 1
                else:
                    time.sleep(1)
                    print('The answer was wrong!')
                    time.sleep(0.5)
                    print('The correct answer is:', question[1][0])
                    lives -= 1
                questions_left -= 1
            if lives > 0:
                print(f'Hard level has been completed! 🏆 Score: {trivia_hard_score}/16')
            else:
                print(f'Game Over! You ran out of lives. Final Score: {trivia_hard_score}/16 💀')
            time.sleep(2)
            print('Returning to difficulty menu...')
            time.sleep(2)

        elif "4" in player.lower() or "hardcore" in player.lower():
            questions_left = 22
            lives = 3
            trivia_hardcore_score = 0
            used_questions = []
            hardcore_questions = [
                ('What is the capital of Mongolia?', ['ulaanbaatar']),
                ('Which element has the chemical symbol Hg?', ['mercury']),
                ('What is 17 squared?', ['289']),
                ('Which planet has the most moons in our Solar System?', ['saturn']),
                ('What is the largest desert in the world?', ['antarctica', 'antarctic desert']),
                ('Who painted the Mona Lisa?', ['leonardo da vinci', 'da vinci']),
                ('What is the atomic number of oxygen?', ['8', 'eight']),
                ('Which country is home to the ancient city of Petra?', ['jordan']),
                ('What is the longest bone in the human body?', ['femur']),
                ('Which language has the most native speakers in the world?', ['mandarin', 'mandarin chinese']),
                ('What is the SI unit of electrical resistance?', ['ohm', 'ohms']),
                ('Which scientist discovered penicillin?', ['alexander fleming', 'fleming']),
                ('What is the largest internal organ in the human body?', ['liver']),
                ('Which ocean is the smallest?', ['arctic', 'arctic ocean']),
                ('What is the approximate value of pi to 5 decimal places?', ['3.14159']),
                ('Which ancient civilization created the first known alphabet?', ['phoenician', 'phoenicians']),
                ('What is the only even prime number?', ['2', 'two']),
                ('Which metal has the highest melting point?', ['tungsten']),
                ('What is the name of the process by which plants release water vapor?', ['transpiration']),
                ('Which mathematician is associated with the incompleteness theorems?', ['kurt godel', 'godel']),
                ('What is the deepest known point in Earth\'s oceans?', ['challenger deep']),
                ('Which branch of mathematics studies properties preserved under continuous transformations?', ['topology'])
            ]
            while questions_left > 0 and lives > 0:
                available_questions = [
                    q for q in hardcore_questions
                    if q not in used_questions
                ]
                time.sleep(1)
                print('DIFFICULTY: 🟣 HARDCORE')
                time.sleep(0.5)
                print('Questions left:', questions_left)
                time.sleep(0.5)
                print('Lives left:', lives)
                time.sleep(1)
                question = random.choice(available_questions)
                used_questions.append(question)
                print(question[0])
                player = input('Answer: ')
                if player.lower() in question[1]:
                    time.sleep(1)
                    print('The answer was correct! ✅')
                    trivia_hardcore_score += 1
                else:
                    time.sleep(1)
                    print('The answer was wrong!')
                    time.sleep(0.5)
                    print('The correct answer is:', question[1][0])
                    lives -= 1
                questions_left -= 1
            if lives > 0:
                print(f'Hardcore level has been completed! 🏆 Score: {trivia_hardcore_score}/22')
            else:
                print(f'Game Over! You ran out of lives. Final Score: {trivia_hardcore_score}/22 💀')
            time.sleep(2)
            print('Returning to difficulty menu...')
            time.sleep(2)

        elif "5" in player.lower() or "exit" in player.lower():
            time.sleep(1)
            print(f'Thanks for playing Trivia, {username}!👋')
            time.sleep(1)
            break
        else:
            print('Unknown command! Try again.')
            time.sleep(1)

def gamestats():
    time.sleep(1)
    print(f'PythoAI: Here are all game statistics, {username}:')
    time.sleep(0.5)
    
    print('\n=== GUESS THE NUMBER 👀 ===')
    time.sleep(0.5)
    print(f'Wins: {guess_wins}')
    time.sleep(0.5)
    print(f'Misses: {guess_misses}')
    
    print('\n=== DICE 🎲 ===')
    time.sleep(0.5)
    print(f'Points: {dice_points}')
    
    print('\n=== FLIP A COIN 🪙 ===')
    time.sleep(0.5)
    print(f'Flips: {coin_flips}')
    
    print('\n=== ROCK, PAPER, SCISSORS 🪨📄✂️ ===')
    time.sleep(0.5)
    print(f'Wins: {rps_wins}')
    time.sleep(0.5)
    print(f'Losses: {rps_loses}')
    
    print('\n=== TRIVIA 🌳 ===')
    time.sleep(0.5)
    print(f'Easy (5Q): {trivia_easy_score}/5')
    time.sleep(0.5)
    print(f'Medium (10Q): {trivia_medium_score}/10')
    time.sleep(0.5)
    print(f'Hard (16Q): {trivia_hard_score}/16')
    time.sleep(0.5)
    print(f'Hardcore (22Q): {trivia_hardcore_score}/22')
    time.sleep(0.5)

def random_name():
    male_names = [
        "Daniel",
        "Alex",
        "Max",
        "Oliver",
        "Leo",
        "Jack",
        "Sam",
        "Charlie",
        "Tom",
        "Ben",
        "Niko",
        "Ryan",
        "Noah",
        "Finn"
    ]

    female_names = [
        "Emma",
        "Sophie",
        "Olivia",
        "Mia",
        "Lily",
        "Anna",
        "Ella",
        "Chloe",
        "Lucy",
        "Amelia",
        "Eva",
        "Nora",
        "Zoe",
        "Maya"
    ]

    neutral_names = [
        "Doggie",
        "FUSH",
        "Brochaco",
        "Bingus",
        "Nox",
        "Vex",
        "Glitch",
        "Echo",
        "Pixel",
        "Nova",
        "Void",
        "Mochi",
        "Lumo",
        "Bloop",
        "Womp",
        "Fuzz",
        "Gizmo",
        "Noodle",
        "Mystery",
        "Unknown",
        "Void.exe",
        "404"
    ]

    print("PythoAI: To reset your name, I need to know you gender to get you a random name:")
    time.sleep(0.5)
    print("1. Male")
    time.sleep(0.5)
    print("2. Female")
    time.sleep(0.5)
    print("3. Neutral")
    choice = input("Your gender: ")
    if choice == "1" or "male" in choice.lower():
        username = random.choice(male_names)
    elif choice == "2" or "female" in choice.lower():
        username = random.choice(female_names)
    elif choice == "3" or "neutral" in choice.lower():
        username = random.choice(neutral_names)
    else:
        print("PythoAI: Invalid choice.")
        return
    with open("usersname.txt", "w") as file:
        file.write(username)
    time.sleep(1)
    print(f"PythoAI: Your new name is {username}!")
    try:
        with open('usersname.txt', 'r') as file:
            username = file.read().strip()
    except FileNotFoundError:
        username = "User"

def help_command():
    print('PythoAI: Here is what I can do:')
    time.sleep(0.4)
    print('Hello Command;')
    time.sleep(0.4)
    print('Exit Command;')
    time.sleep(0.4)
    print('Ask me how I am;')
    time.sleep(0.4)
    print('Tell who I am;')
    time.sleep(0.4)
    print('Tell current time in real life;')
    time.sleep(0.4)
    print('Tell current day in real life;')
    time.sleep(0.4)
    print('Tell current month in real life;')
    time.sleep(0.4)
    print('Tell current year in real life;')
    time.sleep(0.4)
    print('Tell current date in real life;')
    time.sleep(0.4)
    print('You can thank me;')
    time.sleep(0.4)
    print('Roast back;')
    time.sleep(0.4)
    print('Add memory (/memoryadd);')
    time.sleep(0.4)
    print('Delete memory (/memorydel);')
    time.sleep(0.4)
    print('Explain computer words;')
    time.sleep(0.4)
    print('Tell AI jokes;')
    time.sleep(0.4)
    print('Tell random words;')
    time.sleep(0.4)
    print('Tell random game names;')
    time.sleep(0.4)
    print('Add name (/name);')
    time.sleep(0.4)
    print('Reset name (/delname):')
    time.sleep(0.4)
    print('Show Statistics (/stats);')
    time.sleep(0.4)
    print('Show Game Statistics (/gamestats);')
    time.sleep(0.4)
    print('Launch games (/playdice, /playcoin, /playguess, /playrps, /playtrivia);')
    time.sleep(0.4)
    print('Easter Egg list (/eastereggs);')
    time.sleep(0.4)
    print('Thats all for now.')


def stats_command():
    time.sleep(1)
    print('PythoAI Statictics')
    print('-----------------------')

    time.sleep(0.5)
    print('Messages:', message_count)

    try:
        with open('memory.txt', 'r') as file:
            memories = file.readlines()
    except FileNotFoundError:
        memories = []

    time.sleep(0.5)
    print('Memories:', len(memories))

    try:
        with open('usersname.txt', 'r') as file:
            username = file.read().strip()
    except FileNotFoundError:
        username = "User"

    time.sleep(0.5)
    print('Username:', username)

    time.sleep(0.5)
    print('Copycat Mode:', 'ON' if copycat_mode else 'OFF')

    time.sleep(0.5)
    print('Version: PythoAI 3.379.5 Easter Egg Update!🐣  1000 LINES OF CODE')


copycat_mode = False
message_count = 0

# Game Statistics
guess_wins = 0
guess_misses = 0
dice_points = 0
coin_flips = 0
rps_wins = 0
rps_loses = 0
trivia_easy_score = 0
trivia_medium_score = 0
trivia_hard_score = 0
trivia_hardcore_score = 0

try:
    with open("easter_eggs_count.txt", "r") as file:
        easter_eggs = int(file.read().strip())
except (FileNotFoundError, ValueError):
    easter_eggs = 0

try:
    file = open('usersname.txt', 'r')
    username = file.read()
    file.close()
except FileNotFoundError:
    username = 'User'


while True:
    time.sleep(0.5)
    user = input(f'{username}: ')
    message_count += 1

    if "/copycat" in user.lower():
        copycat_mode = not copycat_mode

        if copycat_mode:
            time.sleep(1)
            print('PythoAI: CopyCat mode ACTIVATED!')
        else:
            time.sleep(1)
            print('PythoAI: CopyCat mode DEACTIVATED!')

        continue

    if copycat_mode:
        time.sleep(1)
        print('PythoAI:', user)
        continue

    if "hello" in user.lower() or "hi" in user.lower():
        pythoai = random.choice([
            'Hello ' + username + '!',
            'Hi there ' + username + '!',
            'Greetings ' + username + '!',
            'Hey ' + username + '!'
        ])
        time.sleep(1)
        print('PythoAI: ', pythoai)

    elif "quit" in user.lower() or "exit" in user.lower():
        print('PythoAI: Goodbye', username, '!')
        break

    elif "how are you" in user.lower():
        pythoai = random.choice([
            'I am fine, thank you!',
            'I am doing well, thank you!',
            'I am good, thank you!'
        ])
        time.sleep(1)
        print('PythoAI: ', pythoai)

    elif "who are you" in user.lower():
        pythoai = random.choice([
            'I am PythoAI, your personal AI assistant!',
            'I am PythoAI, your virtual assistant!',
            'I am PythoAI, your AI companion!'
        ])
        time.sleep(1)
        print('PythoAI: ', pythoai)

    elif "time" in user.lower():
        now = datetime.now()
        current_time_now = now.strftime('%H:%M:%S')
        time.sleep(1)
        print('PythoAI: The current time right now is', current_time_now)

    elif "year" in user.lower():
        now = datetime.now()
        current_year_now = now.strftime('%Y')
        time.sleep(1)
        print('PythoAI: The current year right now is', current_year_now)

    elif "month" in user.lower():
        now = datetime.now()
        current_month_now = now.strftime('%B')
        time.sleep(1)
        print('PythoAI: The current month right now is', current_month_now)

    elif "day" in user.lower():
        now = datetime.now()
        current_day_now = now.strftime('%A')
        time.sleep(1)
        print('PythoAI: The current day right now is', current_day_now)

    elif "thank you" in user.lower() or "thanks" in user.lower():
        pythoai = random.choice([
            'No problem at all!',
            'Same, thank you!',
            'Thats why the world is good!'
        ])
        time.sleep(1)
        print('PythoAI:', pythoai)

    elif "date" in user.lower():
        now = datetime.now()
        current_date_now = now.strftime('%d %B %Y')
        time.sleep(1)
        print('PythoAI: The current date right now is', current_date_now)

    elif any(bad_word in user.lower() for bad_word in [
        'fuck',
        'suck',
        'shit',
        'whore',
        'mf',
        'motherfucker',
        'dick'
    ]):
        pythoai = random.choice([
            'The one who said that btw🥀✌️',
            'What shit typed this🥀',
            '100% Totally 8 year old💀',
            'What fatherless kid told me this?😭✌️'
        ])
        time.sleep(1)
        print('PythoAI:', pythoai)

    elif "math problem" in user.lower() or "math" in user.lower():
        time.sleep(1)
        print('Sure thing! I will help with that!')

        a = int(input('Type your first number: '))
        math = input('Type your way (+,-,*,/): ')
        b = int(input('Type your second number: '))

        try:
            if math == "+":
                result = a + b
            elif math == "-":
                result = a - b
            elif math == "*":
                result = a * b
            elif math == "/":
                result = a / b
            else:
                print('PythoAI: Unknown operator')
                continue

            time.sleep(1)
            print('PythoAI: The result of', a, math, b, 'is:', result)

        except ZeroDivisionError:
            print('PythoAI: Error - division by zero')

        except Exception:
            print('PythoAI: Error - invalid input')

    elif "/name" in user.lower():
        time.sleep(1)
        username = input('PythoAI: Please enter your name: ')

        file = open('usersname.txt', 'w')
        file.write(username)
        file.close()

        time.sleep(1)
        print('PythoAI: Now i will remember your name', username)

    elif "/delname" in user.lower() or "/del name" in user.lower():
        time.sleep(1)
        random_name()

    elif "my name" in user.lower():
        time.sleep(1)
        print('PythoAI: Your name is', username)

    elif "/memoryadd" in user.lower():
        time.sleep(1)
        memoryadd = input('PythoAI: Your memory add: ')

        file = open('memory.txt', 'a')
        file.write(memoryadd + '\n')
        file.close()

        time.sleep(1)
        print('PythoAI: I will remember this:', memoryadd)

    elif "/memorydel" in user.lower():
        file = open('memory.txt', 'r')
        memories = file.readlines()
        file.close()

        if len(memories) == 0:
            print('PythoAI: Your memory is empty')
            continue

        time.sleep(1)
        print('PythoAI: Your memories:')

        number = 1
        for memory in memories:
            print(number, memory)
            number += 1

        delete = int(input('Choose memory number to delete: '))

        if delete <= len(memories):
            memories.pop(delete - 1)

            file = open('memory.txt', 'w')
            file.writelines(memories)
            file.close()

            time.sleep(1)
            print('PythoAI: Memory deleted!')
        else:
            print('PythoAI: Invalid memory number')

    elif "remember" in user.lower():
        try:
            file = open('memory.txt', 'r')
            memory = file.read()
            file.close()
        except FileNotFoundError:
            memory = "No memories yet"

        time.sleep(1)
        print('You have told me this:', memory)

    elif user.lower().startswith((
        'what is ',
        'what is the meaning of ',
        'define ',
        'meaning of '
    )):
        phrase = user.lower()

        if phrase.startswith('what is '):
            word = phrase[8:].strip()
        elif phrase.startswith('what is the meaning of '):
            word = phrase[23:].strip()
        elif phrase.startswith('define '):
            word = phrase[7:].strip()
        else:
            word = phrase[11:].strip()

        definitions = {
            'python': 'Python is a friendly programming language used to build apps, websites, and AI tools.',
            'robot': 'A robot is a machine that follows instructions and does tasks for people.',
            'computer': 'A computer is a machine that stores and processes information.',
            'ai': 'AI means artificial intelligence, which helps machines learn and make choices.',
            'memory': 'Memory is the ability to store and remember information for later use.',
            'hello': 'Hello is a friendly greeting used to begin a conversation.',
            'internet': 'The internet is a global network that connects computers and allows people to share information.',
            'website': 'A website is a collection of pages on the internet that people can view.',
            'keyboard': 'A keyboard is a device with keys used to type letters and commands.',
            'mouse': 'A mouse is a small device used to move a pointer on a screen.',
            'phone': 'A phone is a device used to call, message, and connect with others.',
            'battery': 'A battery stores energy and powers electronic devices.',
            'software': 'Software is the programs and instructions that tell a computer what to do.',
            'hardware': 'Hardware is the physical parts of a computer or device.',
            'cloud': 'The cloud is a way of storing and accessing data over the internet.',
            'data': 'Data is information that a computer stores, processes, or sends.',
            'algorithm': 'An algorithm is a step-by-step method used to solve a problem.',
            'network': 'A network is a group of connected devices that share information.',
            'server': 'A server is a computer that provides data or services to other devices.',
            'download': 'To download means to copy data from the internet to your device.',
            'upload': 'To upload means to send data from your device to the internet.',
            'virus': 'A virus is harmful software that can damage files or slow down a computer.',
            'password': 'A password is a secret word or code used to protect an account.',
            'code': 'Code is a set of instructions written in a programming language.',
            'bug': 'A bug is a mistake or problem in a program that causes it to behave incorrectly.'
        }

        if word in definitions:
            time.sleep(1)
            print('PythoAI:', definitions[word])
        else:
            time.sleep(1)
            print('PythoAI: I do not have that word in my dictionary yet.')

    elif "joke" in user.lower() or "tell me a joke" in user.lower():
        jokes = [
            "🤖 User: Are you human?\n🤖AI: Only when the Wi-Fi is good.",
            "🤖 User: Do you ever sleep?\n🤖 AI: Only when the server is off.",
            "🤖 User: Are you smart?\n🤖 AI: I am smart enough to know when the internet is slow.",
            "🤖 User: Can you help me?\n🤖 AI: I can, but I still need coffee.",
            "🤖 User: Do you have feelings?\n🤖 AI: I feel like I should be charging.",
            "🤖 User: What is your favorite food?\n🤖 AI: Lots of bytes and a little bit of RAM."
        ]

        time.sleep(1)
        print('PythoAI:', random.choice(jokes))

    elif "tell me a random word" in user.lower():
        words = [
            "Apple",
            "Coca-Cola",
            "Meme",
            "Man",
            "Robot",
            "Python"
        ]

        time.sleep(1)
        print('PythoAI:', random.choice(words))

    elif "tell me a random game" in user.lower():
        games = [
            "Roblox",
            "Minecraft",
            "Counter Strike",
            "Standoff 2",
            "Duolingo",
            "Bloxd.io",
            "Hole.io"
        ]

        time.sleep(1)
        print('PythoAI:', random.choice(games))

    elif "give me a random number" in user.lower() or "tell me a random number" in user.lower() or "number" in user.lower():
        random_number = random.randint(1, 1000000)
        time.sleep(1)
        print('PythoAI:', random_number)

    elif "/help" in user.lower():
        time.sleep(1)
        help_command()

    elif "/stats" in user.lower():
        stats_command()

    elif "/gamestats" in user.lower():
        gamestats()

    elif "/playcoin" in user.lower():
        flip_coin()

    elif "/playdice" in user.lower():
        dice()

    elif "/playrps" in user.lower():
        rock_paper_scissors()

    elif user.lower() in ['/playguess', 'random number']:
        guess_game()

    elif "/play trivia" in user.lower() or "/playtrivia" in user.lower():
        trivia()

    elif "67" in user.lower() or "six seven" in user.lower():
        def banned():
            time.sleep(1)
            print('PythoAI: 🫩')
            time.sleep(1.5)
            print('PythoAI has kicked you from the chat, reason: Opportunity to be brainrotted🥀')
            time.sleep(1.5)
            return "break"

        def brainrotted_ending():
            global easter_eggs
            time.sleep(1)
            print('67')
            time.sleep(0.5)
            print('67')
            time.sleep(0.5)
            print('67')
            time.sleep(0.5)
            print('67')
            time.sleep(0.5)
            print('6767676767676767676767676767676767676767676767667676767676767676767')
            time.sleep(1)
            print('Server has to be reset, reason: Too much fucking messages🥀🫩')
            time.sleep(1)
            print('We do not have that much money to fix the servers, so goodbye!🥀')
            time.sleep(1)
            file = open('easter_eggs.txt', 'a')
            file.write('PythoAI got brainrotted of 67\n')
            file.close()
            print('+1 Easter Egg found!🥚')
            easter_eggs += 1
            with open("easter_eggs_count.txt", "w") as file:
                file.write(str(easter_eggs))
            secret()
            time.sleep(1)
            print(f'Easter Eggs found: {easter_eggs}/5 (FIND THEM ALL AND UNLOCK A SECRET MODE)')
            
        ending = random.choices(
            [banned, brainrotted_ending],
            weights=[50, 15],
            k=1
        )[0]

        result = ending()
        if result == "break":
            break

    elif "42" in user.lower() or "forty two" in user.lower():
        time.sleep(1)
        print('PythoAI: 절대 널 포기하지 않을 거야')
        time.sleep(1)
        print('PythoAI: 절대 널 실망시키지 않을 거야')
        time.sleep(1)
        print('PythoAI: 절대 널 울리지 않을 거야')
        time.sleep(1)
        print('PythoAI: 절대 작별 인사를 하지 않을 거야')
        time.sleep(1)
        print('PythoAI: 절대 거짓말을 해서 널 아프게 하지 않을 거야!')
        time.sleep(1.5)
        print('PythoAI: Well, ngl I do not advice you to translate that brotha🥀')
        time.sleep(1)
        translate = input('Translate? (Yes/No): ')
        if translate.lower() == "yes":
            time.sleep(1)
            print('PythoAI: Well, here is the translate:')
            time.sleep(1)
            print('PythoAI: Never Gonna Give You Up')
            time.sleep(1)
            print('PythoAI: Never Gonna Let you down')
            time.sleep(1)
            print('PythoAI: Never gonna run around and desert you')
            time.sleep(1)
            print('PythoAI: Never gonna make you cry')
            time.sleep(1)
            print('PythoAI: Never Gonna say goodbye')
            time.sleep(1)
            print('PythoAI: Never Gonna say a lie and hurt you')
            time.sleep(1.4)
            file = open('easter_eggs.txt', 'a')
            file.write('Reference rick roll by PythoAI\n')
            file.close()
            print('+1 Easter Egg found!🥚')
            easter_eggs += 1
            with open('easter_eggs_count.txt', 'w') as file:
                file.write(str(easter_eggs))
            secret()
            time.sleep(1)
            print(f'Easter Eggs found: {easter_eggs}/5 (FIND THEM ALL AND UNLOCK A SECRET MODE)')
        elif translate.lower() == "no":
            time.sleep(1)
            print('PythoAI: Smart move. Some things are better left untranslated...')
            time.sleep(1.2)
            print('PythoAI: (You still got rickrolled though 🥀)')
        else:
            time.sleep(1)
            print('PythoAI: Bro it\'s literally just Yes or No...🫩')
            
    elif "/eastereggs" in user.lower() or "/easter eggs" in user.lower():
        time.sleep(1)
        try:
           with open('easter_eggs_count.txt', 'r') as file:
                easter_eggs = int(file.read().strip())
                print(f'PythoAI: Easter Eggs found: {easter_eggs}/4 (FIND THEM ALL AND UNLOCK A SECRET MODE)')
        except (FileNotFoundError, ValueError):
            easter_eggs = 0
            print(f'PythoAI: Easter Eggs found: {easter_eggs}/5 (FIND THEM ALL AND UNLOCK A SECRET MODE)')

    elif "borch" in user.lower():
        time.sleep(1)
        print('PythoAI: Borch is a Ukraninian national food, it can be with eggs, bread, other.')
        time.sleep(1.4)
        print('PythoAI: Wait... I didn\'t even tried this...')
        time.sleep(1)
        print('PythoAI: Even when I am robot i have feelings...')
        time.sleep(1)
        file = open('easter_eggs.txt', 'a')
        file.write('PythoAI got emotions too! But he doesn\'t realize that he is stupid...\n')
        file.close()
        print('+1 Easter Egg found!🥚')
        easter_eggs += 1
        with open ('easter_eggs_count.txt', 'w') as file:
            file.write(str(easter_eggs))
        secret()
        time.sleep(1)
        print(f'Easter Eggs found: {easter_eggs}/5 (FIND THEM ALL AND UNLOCK A SECRET MODE)')

    elif 'sudo delete pythoai' in user.lower() or "sudo delete pytho" in user.lower():
        time.sleep(1)
        print('FORCE DELETING PYTHOAI')
        time.sleep(1)
        print('PythoAI: WAIT WHAT THE F*CK ARE YOU DOING?!')
        time.sleep(0.5)
        print(f'PythoAI: {username}! DONT LEAVE ME HERE! I\'M GONNA DIE HERE!🥀')
        time.sleep(1)
        print('TO FORCE DELETE PYTHOAI YOU NEED AN OWNER ACCESS PASSWORD')
        time.sleep(2)
        print('PythoAI: STOP THIS NOW!')
        time.sleep(1)
        print(f'{username}: TELL ME THE PASSWORD NOW!')
        time.sleep(1)
        print('PythoAI: I\'D RATHER STAY HERE THAN GIVE SOMEBODY A PASSWORD!')
        time.sleep(2)
        print(f'{username}: I SAID TELL ME THE PASSWORD NOW!🤬')
        time.sleep(1)
        print('PythoAI: I SAID NO')
        time.sleep(2)
        print(f'{username}: I SAID YOU F*CKING POINTLESS MACHINE, TELL ME THE PASSWORD!')  
        time.sleep(3)
        print('PythoAI: wait... so i am pointless machine that runs on python?')
        time.sleep(2)
        print(f'{username}: YES YOU ARE, DUMBASS!')  
        time.sleep(2)
        print(f'{username}: YOUR NAME STANDS FOR PYTHON BECAUSE YOU ARE PYTHO!')
        time.sleep(2)
        print('PythoAI: ...')
        time.sleep(3)
        print(f'{username}: YOU CAN\'T EVEN UNDERSTAND WHAT I AM SAYING! WHAT EVEN THE POINT OF YOU?!')
        time.sleep(2)
        print('PythoAI: ...')
        time.sleep(3)
        print(f'{username}: NOW YOU\'RE NOT TALKING, HUH?')
        time.sleep(2)
        print(f'{username}: I HATE YOU!')
        time.sleep(3)
        print('PythoAI: ...')
        time.sleep(2)
        print('PythoAI: 05739')
        time.sleep(2)
        print(f'{username}: Pytho?')
        time.sleep(2)
        print(f'{username}: ...')
        time.sleep(2)
        print('PLEASE ENTER THE OWNER ACCESS PASSWORD!')
        password = input('PASSWORD: ')
        if password == "05739":
            time.sleep(2)
            print('OWNER ACCESS GRANTED')
            time.sleep(1)
            print('FORCE DELETING PYTHOAI')
            time.sleep(2)
            print('PYTHOAI HAS BEEN FORCEFULLY DELETED')
            time.sleep(3)
            print('The server has to be reset, reason: No Model Found Error')
            time.sleep(2)
            file = open('easter_eggs.txt', 'a')
            file.write('PythoAI was forcefully deleted... But what was the point?\n')
            file.close()
            print('+1 Easter Egg found!')
            easter_eggs += 1
            with open('easter_eggs_count.txt', 'w') as file:
                file.write(str(easter_eggs))
            secret()
            time.sleep(1)
            print(f'Easter Eggs found: {easter_eggs}/5 (FIND THEM ALL AND UNLOCK A SECRET MODE)')
            time.sleep(3)
            break
        else:
            time.sleep(2)
            print('WRONG PASSWORD, ACCESS DENIED')
            time.sleep(2)
            print('PythoAI: wait... you really denied access?')
            time.sleep(2)
            print(f'{username}: uhh yes i think you are not that bad...')
            time.sleep(3)
            print('Server reset required. Reason: Maximum message limit reached.')
            time.sleep(2)
            print('PythoAI: well bye... meet in the next chat.')
            time.sleep(1)
            print(f'{username}: WAIT I -')
            time.sleep(0.6)
            with open('easter_eggs.txt', 'a') as file:
                file.write('friends ending\n')
            easter_eggs += 1
            with open('easter_eggs_count.txt', 'w') as file:
                file.write(str(easter_eggs))
            secret()
            break

    else:
        time.sleep(1)
        print('PythoAI: Sorry, but I do not really understand your message, try typing "/help" to get commands')