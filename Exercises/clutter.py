#Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder.

import os

files = os.listdir("Exercises/clutteredFolder")
i = 1
for file in files:
  if file.endswith(".png"):
    print(file)
    os.rename(f"Exercises/clutteredFolder/{file}", f"Exercises/clutteredFolder/{i}.png")
    i = i + 1
