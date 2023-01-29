#!/usr/bin/env python3

import dice


def ui():
    user_input = ""
    old_input = "1"

    while user_input != "q":
        try:
            user_input = input("Number of battledice (q: quit): ").strip()
        except KeyboardInterrupt:
            user_input = "q"
            print()
            continue

        if user_input == "":
            user_input = old_input

        user_input = user_input.lower()
        if user_input == "q":
            continue

        old_input = user_input

        try:
            num = int(user_input)
        except ValueError:
            continue

        if num < 1:
            print("Number must be a positive integer.")
            continue

        roll_battledice(num)


def roll_battledice(num: int = 1):
    index = 0
    total_swords = 0
    total_shields = 0

    print(f"Rolling {num} battledice...")

    while index < num:
        result = dice.d(6, 1)

        if result == 1:
            total_swords += 2
            print("[1: Two swords] ", end="")
        elif result > 1 and result < 5:
            print(f"[{result}: One sword] ", end="")
            total_swords += 1
        elif result == 5:
            print("[5: One shield] ", end="")
            total_shields += 1
        else:
            print("[6: Two shields] ", end="")
            total_shields += 2
        index += 1

    print()
    print(f"Swords: {total_swords}, shields: {total_shields}\n")


if __name__ == "__main__":
    ui()
