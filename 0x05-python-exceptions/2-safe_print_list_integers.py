def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for element in my_list:
            if isinstance(element, int):
                if count < x:
                    print("{:d}".format(element), end=" ")
                    count += 1
                else:
                    break
        print()
        return count
    except IndexError:
        print("An error occurred while printing the list.")
        return count
