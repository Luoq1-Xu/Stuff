import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if re.search(r"^[\d{1,2}]?([0-2][0-5][0-5])?\.[(0-255)]\.[(0-255)]\.[(0-255)]$",ip):
        return "True"
    else:
        return "False"



if __name__ == "__main__":
    main()