import csv

with open("user_details.csv", newline='\n') as csvfile:  # same as opening text file, but need the csv reader function too
    csvreader = csv.reader(csvfile, delimiter=',')  # comma tells pycharm when a new item is specified

    print(list(csvreader))
    # iterable_csv = iter(csvreader) # allows you to iterate through the file
    # next(iterable_csv)  # skips the first row
    # for row in iterable_csv:
    #     print(row[-1])
    #
    # counter = 0
    # for row in csvreader:
    #     counter += 1
    #     if counter > 1:
    #         print(row[-1])
    #     else:
    #         continue
