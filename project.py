#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2026 Alexander Bartek <dev.alexander3892@proton.me>
# SPDX-License-Identifier: GPL-3.0-or-later

"""
    Beach-Adventure: A CLI game where the player wakes up on a beach
    with no memory of what happened or how they got here.

    Copyright (C) 2026 Alexander Bartek <dev.alexander3892@proton.me>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

def say(text):
    """Show a line of story, wait for enter, then add a blank line."""
    input(text)
    print()

def look_at_ocean(player_name, inventory):
    say("You walk to the edge of the water.")
    say("The ocean is calm and endless.")
    say("Something glints beneaththe surface...")

def explore_beach(player_name, inventory):
    say("You walk along the shoreline.")
    say("(Test: nothin here yet.)")

def enter_forest(player_name, inventory):
    say("You step between the trees.")
    say("(Test: nothin here yet.)")

def examine_items(player_name, inventory):
    say("You take out everything you found:")
    for item in inventory:
        say(f"- {item}")


def intro():
    story = [
        "You wake up alone on a beach.",
        "You don't remember:",
        "- Who you are",
        "- How you got here",
        "- How long you've been unconscious.",
        "You can see the ocean, a forest, some rocks, and something strange in the distance.",
        "You check your pockets.",
        "You find:",
        "- A small rusty key",
        "- A lighter",
        "- A piece of paper with a strange symbol on it",
        "You look around.",
]
    for line in story:
        say(line)

def main():
    player_name = input("What is your name?: ").strip().title()
    print()
    input("[Press the Enter to Continue]")
    print()

    inventory = ["Small rusty key", "Lighter", "Paper with a strange symbol"]

    intro()

    while True:
        choice = input("""What do you do?:
        
1. Look at the ocean
2. Explore the beach
3. Enter the forest
4. Examine the items in your pockets

> """).strip()
        print()

        if choice == "1":
            look_at_ocean(player_name, inventory)
        elif choice == "2":
            explore_beach(player_name, inventory)
        elif choice == "3":
            enter_forest(player_name, inventory)
        elif choice == "4":
            examine_items(player_name, inventory)
        else:
            print(f"That's not an option right now {player_name}.")
            print()

if __name__ == "__main__":
    main()
