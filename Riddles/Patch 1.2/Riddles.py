import random as rd      

class game:
    
    def word(word):
        match word:
                case 'What has to be broken before you can use it?':
                    return 'Hint: Something you eat in breakfast'
                
                case 'I am tall when I am young, and I am short when I am old. What am I?':
                    return 'Hint: You burn it'
                
                case 'What is full of holes but still holds water?':
                    return 'Hint: Who lives in a pineapple and under the sea?'
                
                case 'I am an odd number. Take away a letter and I become even. What number am I?':
                    return 'Hint: no'

                case 'A little girl goes to the store and buys one dozen eggs. As she is going home, all but three break. How many eggs are left unbroken?':
                    return 'Hint: Odd number'

                case 'If there are three apples and you take away two, how many apples do you have?':
                    return 'Hint: First Prime number'
                
                case 'The more of this there is, the less you see. What is it?':
                    return 'Hint: Masochist character from Konosuba'

                case 'What is 3/7 chicken, 2/3 cat and 2/4 goat?':
                    return 'Hint: American state'

                case 'I am a word of letters three; add two and fewer there will be. What word am I?':
                    return 'Hint: It is very few'
                
                case 'What word of five letters has one left when two are removed?':
                    return 'Hint: The Rock'
                
                case 'What word is pronounced the same if you take away four of its five letters?':
                    return "Hint: It's waiting"

                case 'What is so fragile that saying its name breaks it?':
                    return "Hint: It's very much quite"

                case  'What can fill a room but takes up no space?':
                    return "Hint: It's very light"         


wordGuess = {
    'What has to be broken before you can use it?' : 'egg',
    'I am tall when I am young, and I am short when I am old. What am I?' : 'candle',
    'What is full of holes but still holds water?' : 'sponge', 
    'I am an odd number. Take away a letter and I become even. What number am I?' : '7',
    'A little girl goes to the store and buys one dozen eggs. As she is going home, all but three break. How many eggs are left unbroken?' : '3',
    'If there are three apples and you take away two, how many apples do you have?' : '2',
    'The more of this there is, the less you see. What is it?' : 'darkness',
    "David's parents have three sons: Snap, Crackle, and what is the name of the third son?" :'david',
    'What is 3/7 chicken, 2/3 cat and 2/4 goat?' : 'chicago',
    'I am a word of letters three; add two and fewer there will be. What word am I?': 'few',
    'What word of five letters has one left when two are removed?': 'stone',
    'What word is pronounced the same if you take away four of its five letters?' : 'queue',
    'What is so fragile that saying its name breaks it?' : 'silence',
    'What can fill a room but takes up no space?' : 'light'
}

wordList = list(wordGuess.keys())
wordAns = list(wordGuess.values()) 

word = rd.choice(wordList)

count = 3

print(word)
while count > 0:
   
    ask = input('Enter: ').lower()
    if ask == wordGuess[word]:
        break
    
    
    else:
        count -= 1
        print('You have',count,'chances')
        print('Try again\n')
        
        if count >= 2:
            print(game.word(word))
                               
        else:
            continue

if count == 0:
    print('YOU LOSE')
    
else:
    print('YOU WIN')