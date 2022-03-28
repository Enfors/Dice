#!/usr/bin/env python3

import dice


def main():
    value = dice.d(12) - 1
    change = 0
    prev_desc = None
    prev_day = 0
    wetness = dice.d(50) + dice.d(50)
    all_wetness = [ ]

    # print("| Day  | Watch | Weather              | Wind |")
    # print("|------+-------+----------------------+------|")
    print("| Day  | Watch | Ch | Vl | Weather              | Wind |")
    print("|------+-------+----+----+----------------------+------|")

    for day in range(1, 1500):
        for watch in range(1, 4):
            if day != prev_day:
                print(f"| {day:-4d} ", end="")
            else:
                print(f"|" + "      ", end="")
            print(f"| {watch:-5d} ", end="")
            print(f"| {change:-2} ", end="")

            print(f"| {value:-2} ", end="")
            desc = get_desc(value)

            # print(f"({desc}:{prev_desc})")
            if desc != prev_desc:
                print(f"| {desc:20} ", end="")
            else:
                print("|" + " " * 22, end="")

            print(f"|  {get_wind():3s} ", end="")

            # Wetness (Not sure what to call it - amount of water in ground)
            if value < 4:
                wetness += (4 - value) * 2

            if wetness > 0:
                runoff = wetness // 20 or 1

                wetness -= runoff # Decrease by 20%

            print(f"| {wetness:-3d} |")
            all_wetness.append(wetness)

            prev_day = day
            prev_desc = desc

            change = dice.d(8) + dice.d(8) - 9
            value += change
            if value > 11:
                value = 11
            if value < 0:
                value = 0

    avg = sum(all_wetness) / len(all_wetness)

    print(f"Average wetness: {avg:-2.2f}")


def get_desc(val: int):
    desc = [
        "Thunder",              # 0
        "Heavy precipitation",  # 1
        "Precipitation",        # 2
        "Light precipitation",  # 3
        "Overcast",             # 4
        "Overcast",             # 5
        "Mostly cloudy",        # 6
        "Partly cloudy",        # 7
        "Scattered clouds",     # 8
        "Clear skies",          # 9
        "Clear skies",          # 10
        "Clear skies"           # 11
    ]

    return desc[val]


def get_wind():

    return str(dice.d(3) + dice.d(3) - 2) + "/5"


if __name__ == "__main__":
    main()
