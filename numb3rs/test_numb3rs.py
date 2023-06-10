from numb3rs import validate

def main():
    test_validate()

def test_validate():
    try:
        assert validate("255.255.255.255") == "True"
    except AssertionError:
        print("Valid input was rejected")
    try:
        assert validate("258.255.255.255") == "False"
    except AssertionError:
        print("Invalid input was accepted")
    try:
        assert validate("256.247.255.255.3") == "False"
    except AssertionError:
        print("Invalid input was accepted")







if __name__ == "__main__":
    main()