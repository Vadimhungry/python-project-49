#!/usr/bin/env python3
from brain_games.games.prime import init_game
from brain_games.logic import play


def main():
    # запускаем игру
    play(init_game, 'Answer "yes" if given number is prime. Otherwise answer "no".')


if __name__ == '__main__':
    main()
