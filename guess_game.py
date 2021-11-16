import random
while True:
    print("Guess what number I'm thinking of... ")
    rn = random.randrange(11)
    choice = int(input('Guess: '))
    if choice == rn:
        print('Mindreader...')
    elif choice > rn:
        print('Too much')
    elif choice < rn:
        print('Not enough')
    next = input('One more time? y/n ')
    if next == 'y':
        continue
    if next == 'n':
        print('bye')
    break
