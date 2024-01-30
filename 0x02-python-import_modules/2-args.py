#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    count = len(sys.argv)

    if count == 0:
        print("0 argument.")
    elif count ==1 :
        print(f"{count} argument:")
    else:
        print(f"{count} arguments:")

    for i in range(count):
        print(f"{i+1}: {sys.argv[i+1]}")
