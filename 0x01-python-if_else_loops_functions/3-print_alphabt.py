#!/usr/bin/python3
# 3-print_alphabt.py - prints ASC alphabets except q and e
for letter in range(97, 123):
    if letter != 101 and letter != 113:
        print(f"{chr(letter)}", end="")
