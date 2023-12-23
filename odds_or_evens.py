def odds_or_evens():
    while True:
        try:
            num = int(input('What\'s the number? '))
            if not num:
                print('We are even! Bye-bye!')
                break
            if not num % 2:
                print(f'{num} is even!\nLet\'s play again? Press 0 to quit')
            else:
                print(f'{num} is odd!\nLet\'s play again? Press 0 to quit')

        except ValueError:
            print('Give me integer')


odds_or_evens()
