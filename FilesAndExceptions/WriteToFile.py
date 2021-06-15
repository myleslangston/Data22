def write_to_file(file, order_item):
    try:
        list1 = ["oranges", "apples", "peaches"]
        with open(file, 'a') as opened_file:  # w has overwritten the original file. 'a' appends a file
            for i in list1:
                opened_file.write(i + '\n')
    except FileNotFoundError:
        print("File cannot be found in directory")
        raise

write_to_file("orders.txt", "list1")