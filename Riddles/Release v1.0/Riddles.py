# Answer the riddles
# author: RJ

import random as rd
        

wordGuess = {
    'What has to be broken before you can use it?' : 'egg',
    'I am tall when I am young, and I am short when I am old. What am I?' : 'candle',
    'What is full of holes but still holds water?' : 'sponge' 
}

wordGuess1 = {
    'I am an odd number. Take away a letter and I become even. What number am I?' : '7',
    'A little girl goes to the store and buys one dozen eggs. As she is going home, all but three break. How many eggs are left unbroken?' : 'three',
    'If there are three apples and you take away two, how many apples do you have?' : 'two'
}

wordGuess.update(wordGuess1)
wordList = list(wordGuess.keys())
word = rd.choice(wordList)

count = 3
while count > 0:
   
    ask = input((word)+': ')
    if ask == wordGuess[word]:
        break
    
    else:
        count -= 1
        print('You have',count,'chances')
        continue

if count == 0:
    print('YOU LOSE')

    
else:
    print('YOU WIN')