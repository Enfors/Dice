#!/usr/bin/env python3

import random

num_values = 6
max_value = 4
default_personality = [2 for x in range(0, num_values)]


def gen_personality():
    p = default_personality.copy()

    while max(p) < max_value:
        value_to_inc = random.randint(0, num_values - 1)
        p[value_to_inc] += 1

        done = False

        while not done:
            value_to_dec = random.randint(0, num_values - 1)
            if value_to_dec == value_to_inc:
                continue
            if p[value_to_dec] < 1:
                continue
            p[value_to_dec] -= 1
            done = True

    assert(sum(p) == num_values * 2)

    print(p)
    return p


def gen_rel_matrix(num_p: int):
    men = []
    women = []
    current = 0

    # Generate personalities
    while current < num_p:
        print(f"Man   {current+1:-2}: ", end="")
        men.append(gen_personality())
        print(f"Woman {current+1:-2}: ", end="")
        women.append(gen_personality())
        current += 1

    row = 0
    total = 0
    total_matches = 0
    print("   ", end="")
    [print(f"{x+1:-3}", end="") for x in range(0, num_p)]
    print()
    while row < num_p:
        col = 0
        print(f"{row+1:-2}: ", end="")
        while col < num_p:
            if col + row < num_p:
                total += 1
                matches = compare_ps(men[row], women[col])
                # If more than half the numbers are matches:
                if matches > num_values / 2 + 1:
                    flag = "+"
                    total_matches += 1
                else:
                    flag = " "

                print(f"{matches:-2}{flag}", end="")
            col += 1

        print()
        row += 1

    print(f"Total: {total}, matches: {total_matches}")


def compare_ps(p1: int, p2: int):
    current = 0
    num_matches = 0

    while current < num_values:
        if abs(p1[current] - p2[current]) <= 1:
            num_matches += 1
        current += 1

    return num_matches


if __name__ == "__main__":
    gen_rel_matrix(12)
