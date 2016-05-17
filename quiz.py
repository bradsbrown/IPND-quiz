import random

# define all strings for levels, answers, difficulty levels, responses, etc.
# ---------- #
string1 = '''Row, row, row your ___1___. Gently down the ___2___.
Merrily, merrily, merrily, merrily. ___3___ is but a ___4___.'''
string2 = '''When I find ___1___ in times of ___2___
Mother ___3___ comes to me
Speaking ___4___ of ___5___, let it be'''
string3 = '''Once upon a midnight ___1___, while I pondered, weak and ___2___,
Over many a ___3___ and curious volume of forgotten lore -
While I ___4___, nearly napping, suddenly there came a tapping,
As of some one gently rapping, rapping at my chamber door.
"'Tis some ___5___," I muttered, "tapping at my chamber door -
Only this and nothing more."'''
string_set = [string1, string2, string3]

answer_key1 = ['boat', 'stream', 'life', 'dream']
answer_key2 = ['myself', 'trouble', 'Mary', 'words', 'wisdom']
answer_key3 = ['dreary', 'weary', 'quaint', 'nodded', 'visitor']
answer_set = [answer_key1, answer_key2, answer_key3]

difficulty_index = ["Easy", "Medium", "Difficult"]
difficulty_desc = ["I mean, I *guess* we can still call this a 'game'.",
                   "Ok, this should be respectably challenging.",
                   "Now youre talking!"]

wrong_responses = ["Listen, maybe I'm asking too much of you here, but nope.",
                   "I'm sure that's the right answer to some question, but not\
                    to this one.",
                   "Well...no."]

intro_string = '''Of course you would!
Ok, here's what we're going to do. We're going to have a little quiz.
I'll give you some sentences with blanks in them.
If you can correctly fill in the blanks, you win and...
...I guess that better feel good, because there is no other prize.
First, you'll need to tell me how smart you're feeling today.
Choose your difficulty level:
1 - Easy (you big pansy)
2 - Medium (at least you can probably read)
3 - Difficult (someone thinks they know things)'''
# ---------- #


def make_it_pretty(stuff):
    '''This simply produces 15 lines with a single '.'char each preceding the
    called string, to seperate the most current version of the string from
    previous terminal text.
    input: any string
    ouput: 15 printed lines of '.' followed by the string'''
    numrows = 15
    for i in range(0, numrows):
        print "."
    print stuff


def oops():
    '''When called (for an incorrect guess), returns a random response from
    the list of responses that indicate the user has not chosen the correct
    answer.
    input: none
    ouput: a printed 'wrong guess' string'''
    doofus = wrong_responses[random.randint(0, len(wrong_responses)-1)]
    print doofus


def get_level():
    '''Asks user to choose a difficulty level, based on the
    number of levels in the index, and verifies the input is valid.
    For any non-integer entry, or entry outside the range, returns a
    notification and persists in reqeuesting the level until valid
    input returned.
    input: none passed to function, user inputs level selection as raw
    output: passes selected level'''
    level = 0
    level_min = 1
    level_max = len(difficulty_index)
    level_range_to_print = "("+str(level_min)+"-"+str(level_max)+")"
    while True:
        try:
            level = raw_input("Choose your poison "+level_range_to_print+":")
            level = int(level)
        except ValueError:
            pass
        if level in range(level_min, level_max+1):
            break
        print "You have either picked a wrong number, or typed something else \
        altogether. Genius."
    return level


def play_game(ilevel):
    '''Take level passed in, plays the game given that level, pulling
    the string and answer key from the correct index in their respective
    sets. As each correct answer is given, replaces blank in string with
    the correct answer, and neatly displays the string again, asking for
    the next blank, until all have been filled.
    input: level selection
    output: nothing returned, interacts with user in terminal to play game'''
    print "Ok, let's do this thing."
    print "You have chosen: " + difficulty_index[ilevel]
    print difficulty_desc[ilevel]
    working_string = string_set[ilevel]
    print working_string
    for answer in answer_set[ilevel]:
        answers = answer_set[ilevel]
        pos = answers.index(answer)+1
        input_query = "What goes in blank #"+str(pos)+"?"
        guess = raw_input(input_query)
        while guess != answer:
            oops()
            print "Let's try this again."
            guess = raw_input(input_query)
        working_string = working_string.replace('___'+str(pos)+'___', answer)
        make_it_pretty(working_string)

    print "****Looks like you figured this one out! Now go away.****"


def start_game():
    '''This will print the introduction to the game and get a difficulty
    selection from the user, then pass that selection over to the actual
    game play.
    input: none
    output: nothing returned, interacts with user to start game,
            call play_game()'''
    print "Would you like to play a game?"
    numrows = 10
    for i in range(0, numrows):
        print "."
    print intro_string
    ilevel = get_level()-1
    play_game(ilevel)

start_game()
