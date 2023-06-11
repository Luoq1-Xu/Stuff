import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r".*http://www.youtube.com/embed/([^\"]+).*", s):
        src = match.group(1)
    print("https://youtu.be/" + src)

if __name__ == "__main__":
    main()