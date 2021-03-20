#!/usr/bin/env python3

import dice


def attrib():
    all_dice = []

    for index in range(0, 4):
        all_dice += [dice.d(6)]

    print(f"Dice:   {all_dice}")
    print(f"Min:    {min(all_dice)}")
    print(f"Sum:    {sum(all_dice)}")
    print(f"Actual: {sum(all_dice) - min(all_dice)}")

    return sum(all_dice) - min(all_dice)


def char():
    all_attribs = []
    retry = 1

    while retry:
        retry = 0

        for index in range(0, 6):
            all_attribs += [attrib()]
            print()

        print("Attribs:", sorted(all_attribs, reverse=True))
        if max(all_attribs) <= 14:
            print("< Invalid character - no attrib above 14, retrying >")
            retry += 1
        all_attribs = []
