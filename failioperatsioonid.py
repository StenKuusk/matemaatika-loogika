"""File operations."""
import csv

def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    In this exercise, we can assume the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    with open(filename) as f:
        content = f.read()
        return content
    pass

def read_file_contents_to_list(filename: str) -> list:
    r"""
    Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.
    The order of the list should be the same as in the file.

    List elements should not contain new line (\n).

    :param filename: File to read.
    :return: List of lines.
    """
    with open(filename) as f:
        content_list = f.readlines()
        for index in range(len(content_list)):
            content_list[index] = content_list[index].strip()
        return content_list
    pass

print(read_file_contents_to_list("test.txt"))

def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    list_of_rows = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for rida in csv_reader:
            list_of_rows.append(rida)
    return list_of_rows
    pass

print(read_csv_file("test2.csv"))

def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file does not exists, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    with open(filename, 'w') as content_file:
        content_file.write(contents)
    pass

write_contents_to_file("data.txt", "tere test 2")

def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    with open(filename, "w") as file:
        for index in range(len(lines)):
            if index < len(lines) - 1:
                file.write(lines[index] + "\n")
            else:
                file.write(lines[index])
    pass

lines = ['first line', 'second line', 'third line']
# print(len(lines))
# for index in range(len(lines)):
#     print(index)
write_lines_to_file("data.txt", lines)

def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        # header
        for row in data:
            # write list of values
            csv_writer.writerow(row)

test_data = [["name", "age"], ["john", "11"], ["mary", "15"]]
print(write_csv_file("test3.csv", test_data))

def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two files into one CSV file.

    Dates file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    Towns file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.
    There are no headers in the input files.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_filename: Input file with names and dates.
    :param towns_filename: Input file with names and towns.
    :param csv_output_filename: Output CSV-file with names, towns and dates.
    :return: None
    """
    towns = []
    with open(towns_filename) as f:
        towns = f.readlines()
        for index in range(len(towns)):
            towns[index] = towns[index].strip()
            towns[index] = towns[index].split(':')
    print(towns)

    dates = []
    with open(dates_filename) as f:
        dates = f.readlines()
        for index in range(len(dates)):
            dates[index] = dates[index].strip()
            dates[index] = dates[index].split(':')
    print(dates)

    # dates = []
    # with open(dates_filename) as f:
    #     dates = f.readlines()
    #     for index in range(len(dates)):
    #         dates[index] = dates[index].strip()
    # print(dates)

    data = []
    for index in range(len(towns)):
        uus_rida = []
        if(len(towns[index][0]) == 0):
            uus_rida.append('-')
        else:
            uus_rida.append(towns[index][0])
        if (len(towns[index][1]) == 0):
            uus_rida.append('-')
        else:
            uus_rida.append(towns[index][1])
        if (len(dates[index][1]) == 0):
            uus_rida.append('-')
        else:
            uus_rida.append(dates[index][1])
        data.append(uus_rida)

    print(data)


    with open(csv_output_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        # header
        csv_writer.writerow(['name', 'town', 'date'])
        for row in data:
            # write list of values
            csv_writer.writerow(row)


print(merge_dates_and_towns_into_csv('dates.txt', 'towns.txt', 'info.csv'))

#with open('info.csv') as f:
    #sisu = f.read()
    #print(sisu)

    dates = read_csv_file(dates_filename)
    towns = read_csv_file(towns_filename)
    date_dict = {}
    town_dict = {}
    names_list = []
    for line in dates:
        line = line[0].split(":")
        date_dict[line[0]] = line[1]
        names_list.append(line[0])
    for line in towns:
        line = line[0].split(":")
        town_dict[line[0]] = line[1]
        if line[0] not in names_list:
            names_list.append(line[0])
    data = []
    data.append(["name", "town", "date"])
    for name in names_list:
        row = [name]
        if name in town_dict:
            row.append(town_dict[name])
        else:
            row.append("-")
        if name in date_dict:
            row.append(date_dict[name])
        else:
            row.append("-")
        data.append(row)
        write_csv_file(csv_output_filename, data)