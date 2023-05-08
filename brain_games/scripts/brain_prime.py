#!/usr/bin/env python3
from brain_games.games.prime import init_game
from brain_games.logic import play
hi1 = 'Answer "yes" if given number is prime.'
hi2 = 'Otherwise answer "no".'
welcome_statement = hi1 + hi2


def main():
    # запускаем игру
    play(init_game, welcome_statement)


if __name__ == '__main__':
    main()
