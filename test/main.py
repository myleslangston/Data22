def filter_list(list):

    for i in list:
        if i == str:
            del list[i]

            print(list)


filter_list([1, 2, '3', '4'])
