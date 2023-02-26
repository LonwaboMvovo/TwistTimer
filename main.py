import time


def main():
    print("TwistTimer!")

    input("0.00")
    start_time = time.time()

    input("solve")
    end_time = time.time()

    time_passed = round(end_time - start_time, 2)
    print(time_passed)


if __name__ == "__main__":
    main()
