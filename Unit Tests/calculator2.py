def main():
    x = int(input("What is x? "))
    result = square(x)
    print(f"Square of {x} is {result}")


def square(n):
    return n * n


if __name__ == "__main__":
    main()
    