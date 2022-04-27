import random


def get_random():
    cube_number = random.randint(1, 6)
    return cube_number


def main():
    while True:
        try:
            user_input = int(input('Give number 1 to 6 to play or 0 to exit: '))

            if user_input == 0:
                print('Bye')
                break

            elif user_input < 0 or user_input > 6:
                print('Use only numbers from 1 to 6!')
                continue

        except ValueError:
            print('Use only numbers from 1 to 6!')

        if get_random() == user_input:
            print('you win')

        else:
            print('You loose')

if __name__ == '__main__':
    main()
