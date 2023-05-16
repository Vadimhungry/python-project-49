#!/usr/bin/env python3
import brain_games.games.even as even
from brain_games import game_logic as logic


def main():
    # запускаем игру
    logic.play(even)


if __name__ == '__main__':
    main()
