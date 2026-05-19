import argparse
import os
from datetime import datetime


parser = argparse.ArgumentParser()
parser.add_argument("-d", nargs="+", help="directory parts")
parser.add_argument("-f", help="file name")
args = parser.parse_args()


if args.f:
    if args.d:
        filepath = os.path.join(*args.d, args.f)
        os.makedirs(os.path.join(*args.d), exist_ok=True)
    else:
        filepath = args.f
        dir_path = os.path.dirname(filepath)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
elif args.d:
    filename = input("Enter file name: ")
    filepath = os.path.join(*args.d, filename)
    os.makedirs(os.path.join(*args.d), exist_ok=True)
else:
    filepath = None

if filepath is None:
    print("Error: No file path specified")
    exit(1)


lines = []
while True:
    line = input("Enter content line: ")
    if line == "stop":
        break
    lines.append(line)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
content = timestamp + "\n"
if os.path.exists(filepath):
    content = "\n" + timestamp + "\n"

for i, line in enumerate(lines, 1):
    content += f"{i} {line}\n"
with open(filepath, "a") as f:
    f.write(content)
