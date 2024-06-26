def main():
    while True:
        number = int(input('Enter a number'))
        if 0 < number < 100:
            break
        else:
            print('Invalid')

    print(number)

    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
