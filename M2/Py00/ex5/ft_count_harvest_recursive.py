def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def print_day(i):
        if i <= days:
            print(f"Day {i}")
            print_day(i + 1)
        else:
            print("Harvest time!")
    print_day(1)
