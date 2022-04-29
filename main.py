import random
import time


def get_random():
    number = random.randint(1, 6)
    return number


def max_of(a, b):
    return int((a + b + abs(a - b)) / 2)


def min_of(a, b):
    return int((a + b - abs(a - b)) / 2)


def main():
    vin = 0
    loose = 0
    print('Hello, pretty!\n')
    start_time = time.time()

    while True:
        try:
            user_input = int(input('Give a number from 1 to 6 to play or 0 to exit: '))

            if user_input == 0:

                if vin and loose != 0:
                    print(f'\nYou are {round((min_of(vin, loose) / max_of(vin, loose)) * 100)}% lucky!')
                    print(f'It took {round(time.time() - start_time)} seconds to find it! \n')

                print('Bye')

                break

            elif user_input < 0 or user_input > 6:
                raise ValueError

        except ValueError:
            print('Use only numbers from 1 to 6!\n')

        else:
            if get_random() == user_input:
                print('You win')
                vin += 1

            else:
                print('You loose')
                loose += 1

        time.sleep(0.3)


if __name__ == '__main__':
    main()
