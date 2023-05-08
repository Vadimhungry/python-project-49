#!/usr/bin/env python3
from brain_games.games.even import init_game
from brain_games.logic import play


def main():
    # запускаем игру
    play(init_game, 'Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == '__main__':
    main()
