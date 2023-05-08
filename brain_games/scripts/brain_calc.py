#!/usr/bin/env python3
from brain_games.games.calc import init_game
from brain_games.logic import play


def main():
    # запускаем игру
    play(init_game, 'What is the result of the expression?')


if __name__ == '__main__':
    main()
