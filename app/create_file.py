import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('-d', nargs='+', help='directory parts')
parser.add_argument('-f', help='file name')
args = parser.parse_args()


if args.d:
    path = os.path.join(*args.d)
    os.makedirs(path, exist_ok=True)


lines = []
while True:
    line = input("Enter content line: ")
    if line == "stop":
        break
    lines.append(line)
