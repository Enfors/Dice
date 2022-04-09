#!/usr/bin/env python3

"""
I have devised a system for controlling random encounters in dungeons.
The purpose of this program is to test this system through simulation, to
check if it is balanced or not - does it produce enough enounters, or
perhaps too few?
"""

import dice


def main():
    room = 0
    max_rooms = 15   # How many rooms we will traverse (including backtracking)
    threat_level = 0 # How dangerous the dungeon currently is
    num_enc = 0      # Number of encounters so far
    remaining = 8    # Max number of encounters in this dungeon

    print("| Room | Doors | Remaining | Roll | Risk | Encounter | Threat level |")
    print("|------|-------|-----------|------|------|-----------|--------------|")

    while room < max_rooms:
        room += 1
        num_doors = dice.d(3) + dice.d(3) - 1

        # The risk of encounters depends on how many doors the room has, plus
        # the general threat level right now.
        enc_chance = threat_level + num_doors

        # However, the risk will never be higher than the remaining amount of
        # encounters. If there are no more monsters in the dungeon in total,
        # then the risk is zero.
        if enc_chance > remaining:
            enc_chance = remaining

        # Check if the characters bash a door and make noise.
        if dice.d(4) == 1:
            threat_level = change_threat_level(threat_level, 1)

        risk = int((enc_chance / 12)*100)

        # Check if there is an enounter.
        trigger_roll = dice.d(12)

        # If the trigger roll is lower than the enc_chance, then there is an
        # encounter.
        enc = trigger_roll <= enc_chance

        # If there is an encounter:
        if enc:
            num_enc += 1  # Increase the number of encounters we've had.

            # There is an encounter. This causes noise. Increase threat level.
            threat_level = change_threat_level(threat_level, 1)

            # If monsters get away, they could alert their friends which
            # increases the threat level.
            if dice.d(2) == 1:
                # A monster got away! Increase threat level.
                threat_level = change_threat_level(threat_level, 1)

        elif trigger_roll >= 9:
            # If there was no encounter, and the trigger roll is at least
            # 9 or higher, reduce the threat level.
            threat_level = change_threat_level(threat_level, -2)

        print(f"| {room:-4} | {num_doors:-5} | {remaining:-9} | "
              f"{trigger_roll:-4} | {risk:-3}% | {enc:9} | {threat_level:-12} |")
        if enc:
            remaining -= 1

    print(f"Number of encounters: {num_enc}")


def change_threat_level(old_threat_level: int, change: int):
    new_threat_level = old_threat_level + change

    if new_threat_level < 0:
        new_threat_level = 0

    if new_threat_level > 9:
        new_threat_level = 9

    return new_threat_level


if __name__ == "__main__":
    main()
