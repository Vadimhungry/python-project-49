#!/usr/bin/env python3
from brain_games.games.gcd import init_game
from brain_games.logic import play


def main():
    # запускаем игру
    play(init_game, 'Find the greatest common divisor of given numbers.')


if __name__ == '__main__':
    main()
