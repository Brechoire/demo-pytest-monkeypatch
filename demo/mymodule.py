from random import choice

def f(data):
    return choice(data)

def main():
    print(f([1, 2, 3, 4, 5]))

if __name__ == "__main__":
    main()
