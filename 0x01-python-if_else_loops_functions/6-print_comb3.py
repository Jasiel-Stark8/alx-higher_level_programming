#!/usr/bin/python3
nums = []
for i in range(0, 10):
    for j in range(0, 10):
        if i != j and not (f"{i}{j}" in nums or f"{j}{i}" in nums):
            nums.append(f"{i}{j}")
            print(f"{i}{j}", end=", " if not (i == 9 and j == 9) else "\n")
