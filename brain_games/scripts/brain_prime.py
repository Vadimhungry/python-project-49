#!/usr/bin/env python3
from brain_games.games.prime import init_game
from brain_games.logic import play

welcome_statement = 'Answer "yes" if given number is prime.' \
                    ' Otherwise answer "no".'


def main():
    # запускаем игру
    play(init_game, welcome_statement)


if __name__ == '__main__':
    main()
