#!/usr/bin/env python3
import brain_games.games.gcd as gcd
from brain_games import game_logic as logic


def main():
    # запускаем игру
    logic.play(gcd)


if __name__ == '__main__':
    main()
