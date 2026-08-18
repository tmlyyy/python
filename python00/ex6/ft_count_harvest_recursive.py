def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def counter(current_day):
        if current_day > days:
            return
        print("Day", current_day)
        counter(current_day + 1)

    counter(1)
    print("Harvest time!")
