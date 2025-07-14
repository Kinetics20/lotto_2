from functools import reduce
import random
from typing import Callable


def is_number(number_text: str) -> bool | str:
    return number_text if number_text.isdigit() else False


def to_number(number_text: str) -> bool | int:
    try:
        return int(number_text)
    except ValueError:
        return False


def is_in_range(number: int) -> bool | int:
    return number if number in range(1, 50) else False


def validate(number: str, validators: list[Callable]) -> bool | int:
    if len(validators) == 0:
        raise ValueError('No validators specified')
    return reduce(lambda acc, validator: validator(acc) if acc is not False else False, validators, number)
    # for validator in validators:
    #     if number is not False:
    #         number = validator(number)
    # return number


def get_user_numbers(amount: int) -> set[int]:
    user_numbers = set()

    validators = [is_number, to_number, is_in_range]

    while len(user_numbers) < amount:
        print('Please enter a number:\n')
        number = input()
        if number := validate(number, validators):
            user_numbers.add(number)

    return user_numbers


def draw_numbers(amount: int) -> set[int]:
    if amount == 0:
        raise ValueError('Amount must be a positive integer')
    return set(random.sample(range(1, 50), amount))


def check_hits(user_numbers: set[int], drawn_numbers: set[int]) -> set[int]:
    return user_numbers & drawn_numbers


def play(amount: int) -> None:
    while True:

        user_numbers = get_user_numbers(amount)
        drawn_numbers = draw_numbers(amount)
        hits = check_hits(user_numbers, drawn_numbers)
        print(hits)

        print('Do you want to play again? (y/n)')
        answer = input().lower()

        if answer not in ('y', 'yes'):
            break

    print('Game Over!')

if __name__ == '__main__':

    play(5)

