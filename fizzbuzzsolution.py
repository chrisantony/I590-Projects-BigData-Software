def fizzbuzz(start, end):
    def int_to_fizzbuzz(i):
        entry = ''
        if i%2 == 0:
            entry = "fizz"
        if i%3 == 0:
            entry = "buzz"
        if i%2 == 0 and i%3 == 0:
            entry = "fizzbuzz"
        if i%2 != 0 and i%3 != 0:
            entry = i
        return entry

    return [int_to_fizzbuzz(i) for i in range(start, end+1)]

if __name__ == "__main__":
    start = int(input("Start Value:"))
    end = int(input("End Value:"))
    for i in fizzbuzz(start, end):
        print(i)