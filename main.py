import os

# This is a program to split text and translations into texts in a folder structure
# This makes it easy to implement translations into propresenter or other presentation software


# ask user if files are there and names correctly
if input("Are the files next to this program and named 'text.txt' and 'translation.txt'? [y/n]") == "n": exit()

# create constants for testing
title = input("title of the song: ")
TextLocation = "text.txt"
TranslationLocation = "translation.txt"


# get length to later create right amount of folders
TextLength = sum(1 for line in open(TextLocation))
TranslationLength = sum(1 for line in open(TranslationLocation))

# for testing, check number of lines
if TextLength != TranslationLength: print("Error: Translation and Text do not match"); exit()
print("Lines from text: " + str(TextLength))
print("Lines from translation: " + str(TranslationLength))

# create folders and files
try:
    os.mkdir(title)
except:
    print("Alert: folder already created")
    if input("Abort [y/n] ") == "y" or "Y": exit() # abort if user does not want to continue


i = 1
f = open(TextLocation)
# go throug all lines and add them to the
for x in f:
    try:
        os.mkdir(f"{title}/{i}")
    except:
        print(f"Subfolder {i} already created")

    # create files with text in folder
    try:
        txt = open(f"{title}/{i}/txt.txt", "w")
        txt.write(x)
    except: print("Error: could not write text")

    i += 1
f.close()

# do the same for the translation
i = 1
f = open(TranslationLocation)
for x in f:
    # create files with text in folder
    try:
        txt = open(f"{title}/{i}/trn.txt", "w")
        txt.write(x)
    except: print("Error: could not write translation")

    i += 1

print("Done.")