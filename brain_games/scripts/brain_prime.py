#!/usr/bin/env python3
import brain_games.games.prime as prime
from brain_games import game_logic as logic


def main():
    # запускаем игру
    logic.play(prime)


if __name__ == '__main__':
    main()
