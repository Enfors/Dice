#!/usr/bin/env python3

import random


def ui():
    user_input = ""
    old_input = "1d6"

    while user_input != "q":
        user_input = input("Dice (Enter: repeat, q: quit)> ")

        if user_input == "":
            user_input = old_input

        if user_input.lower() == "q":
            continue

        modifier = 0

        try:
            (num, size) = user_input.split("d")
            num = int(num)
        except ValueError:
            size = user_input

        if "+" in size:
            (size, modifier) = size.split("+")
            modifier = int(modifier)
        if "-" in size:
            (size, modifier) = size.split("-")
            modifier = -int(modifier)

        size = int(size)

        i = 0
        total = 0

        while i < num:
            die = random.randint(1, size)
            print(f"1d{size}: {die}")
            total += die
            i += 1

        if modifier:
            if modifier > 0:
                print(f"Modifier: +{modifier}")
            else:
                print(f"Modifier: {modifier}")

            total += modifier

        print(f"Total: {total}")
        old_input = user_input


def d(size: int, num: int = 1):
    total = 0
    index = 0

    while index < num:
        total += random.randint(1, size)
        index += 1

    return total


def test_advantage():
    adv_results = []
    norm_results = []
    for i in range(0, 10_000_000):
        adv_results.append(max(d(20), d(20)))
        norm_results.append(d(20))

    adv_result = sum(adv_results) / len(adv_results)
    norm_result = sum(norm_results) / len(norm_results)

    print(f"Advantage: {adv_result}, normal: {norm_result}, diff: "
          f"{adv_result-norm_result}")


if __name__ == "__main__":
    ui()
