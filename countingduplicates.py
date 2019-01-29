#!/usr/bin/python3

def duplicate_count(text):
    
    count = {}
    total = 0

    for char in text:
        char=char.lower()
        if char.lower not in count.keys():
            count[char] = 0
        count[char] += 1
    
    for charcount in count.values():
        if charcount > 1:
            total += 1

    return total


if __name__ == "__main__":
    print(duplicate_count("abcde"))
    print(duplicate_count("abcdea"))
    print(duplicate_count("indivisibility"))