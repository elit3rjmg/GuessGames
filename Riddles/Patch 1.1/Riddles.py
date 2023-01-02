# Answer the riddles
# author: RJ

import random as rd   

wordGuess = {
    'What has to be broken before you can use it?' : 'egg',
    'I am tall when I am young, and I am short when I am old. What am I?' : 'candle',
    'What is full of holes but still holds water?' : 'sponge', 
    'I am an odd number. Take away a letter and I become even. What number am I?' : '7',
    'A little girl goes to the store and buys one dozen eggs. As she is going home, all but three break. How many eggs are left unbroken?' : '3',
    'If there are three apples and you take away two, how many apples do you have?' : '2'
}

wordList = list(wordGuess.keys())
wordAns = list(wordGuess.values()) #not used

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
            
            match word:
                case 'What has to be broken before you can use it?':
                    print('Hint: Something you eat in breakfast')
                
                case 'I am tall when I am young, and I am short when I am old. What am I?':
                    print('Hint: You burn it')
                
                case 'What is full of holes but still holds water?':
                    print('Hint: Who lives in a pineapple and under the sea?')
                
                case 'I am an odd number. Take away a letter and I become even. What number am I?':
                    print('Hint: no')

                case 'A little girl goes to the store and buys one dozen eggs. As she is going home, all but three break. How many eggs are left unbroken?':
                    print('Hint: Odd number')

                case 'If there are three apples and you take away two, how many apples do you have?':
                    print('Hint: First Prime number')
                    
        else:
            continue


if count == 0:
    print('YOU LOSE')
   
else:
    print('YOU WIN')