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

# This is where the game begins by asking the player for their name and their first choice.

def main():

    player_name = input("What is your name?: ").strip().title()
    print()
    input("[Press Enter to Continue]")
    print()
    input("You wake up alone on a beach.")
    print()
    input("You don't remember:")
    print()
    input("- Who you are")
    print()
    input("- How you got here")
    print()
    input("- How long you've been unconscious")
    print()
    input("You can see the ocean, a forest, some rocks, and something strange in the distance.")
    print()
    input("You check your pockets.")
    print()
    input("You find:")
    print()
    input("- A small rusty key")
    print()
    input("- A lighter")
    print()
    input("- A piece of paper with a strange symbol on it")
    print()
    input("You look around.")
    print()
    choice_1 = input("""
    What do you do?:

    1. Look at the ocean
    2. Explore the beach
    3. Enter the forest
    4. Examine the items in your pockets """).strip()
    print()
    
    if choice_1 == "1":
        print("Test, you picked 1") #TODO
    elif choice_1 == "2":
        print("Test, you picked 2") #TODO
    elif choice_1 == "3":
        print("Test, you picked 3") #TODO
    elif choice_1 == "4":
        print("Test, you picked 4") #TODO
    else:
        print("That's not an option right now " + player_name)



#TODO

    
if __name__ == "__main__":
    main()
