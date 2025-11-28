def mul(a, b):
    return a * b


def main():
    import sys

    def to_number(x):
        try:
            return int(x)
        except ValueError:
            return float(x)

    if len(sys.argv) >= 3:
        try:
            a = to_number(sys.argv[1])
            b = to_number(sys.argv[2])
        except Exception:
            print('Please provide two numeric arguments.')
            sys.exit(1)
    else:
        try:
            a = to_number(input('Enter first number: '))
            b = to_number(input('Enter second number: '))
        except Exception:
            print('Invalid input. Expecting numbers.')
            sys.exit(1)

    result = mul(a, b)
    print(result)


if __name__ == '__main__':
    main()
