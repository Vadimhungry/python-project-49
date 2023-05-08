#!/usr/bin/env python3
from brain_games.games.progression import init_game
from brain_games.logic import play


def main():
    # запускаем игру
    play(init_game, 'What number is missing in the progression?')


if __name__ == '__main__':
    main()
