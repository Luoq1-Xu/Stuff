def do(x):
    try:
        return x[0] + x[1]
    except IndexError:
        print("Bad")
    except TypeError:
        print("Good")
    finally:
        return x[0] + x

print(do([[1], 2]))