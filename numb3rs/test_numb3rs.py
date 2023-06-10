from numb3rs import validate

def main():
    test_validate()

def test_validate():
        assert validate("255.255.255.255") == "True"
        assert validate("258.255.255.255") == "False"
        assert validate("1.1.1.1.1") == "False"



if __name__ == "__main__":
    main()