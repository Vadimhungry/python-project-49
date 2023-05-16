#!/usr/bin/env python3
import brain_games.games.progression as progression
from brain_games import game_logic as logic


def main():
    # запускаем игру
    logic.play(progression)


if __name__ == '__main__':
    main()
