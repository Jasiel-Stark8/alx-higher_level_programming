import os


if not os.path.exists('file.txt'):
    open('file.txt', "w").close()

    f = open('file.txt', 'w')
    f.write("Hi there, you've done very well...")
    f.close()
