"""Set exercises."""


def create_set_from_numbers(a: int, b: int, c: int) -> set:
    """
    Create set from three integers.

    create_set_from_numbers(1, 2, 3) => {1, 2, 3}
    create_set_from_numbers(1, 2, 1) => {1, 2}
    create_set_from_numbers(1, 1, 1) => {1}
    """
    numbers = (a, b ,c)
    numbers_set = set(numbers)
    return numbers_set
    # code here
print(create_set_from_numbers(1, 2, 3))


def add_one(set_a: set) -> set:
    """
    Take a set of integers and increment each integer by one, return new set.

    add_one({1, 2, 3}) => {2, 3, 4}
    add_one({-10, 0, 10}) => {-9, 1, 11}

    :param set_a: given set
    :return: new set where all elements have been incremented by one.
    """
    new_set = []
    for element in set_a:
        new_set.append(element + 1)
    return set(new_set)
    # code here
print(add_one({1, 2, 3}))
print(add_one({-10, 0, 10}))

def remove_six(set_a: set) -> set:
    """
    Take a set of digits and remove the number six from it if its there, return set.

    remove_six({1, 2, 3, 4, 5, 6, 7, 8, 9}) => {1, 2, 3, 4, 5, 7, 8, 9}
    remove_six({1, 5, 7}) => {1, 5, 7}

    :param set_a: given set
    :return: set without sixes.
    """
    set_a.discard(6)
    return set_a
    # code here
print(remove_six({1, 2, 3, 4, 5, 6, 7, 8, 9}))

def convert_to_set(list_a: list) -> set:
    """
    Take a list, convert it to a set and return it.

    convert_to_set([1, 2, 3, 1]) => {1, 2, 3}
    convert_to_set([1, 2, 3, 4]) => {1, 2, 3, 4}

    :param list_a: given list
    :return: set made from given list.
    """
    list_a_set = set(list_a)
    return list_a_set
    # code here
print(convert_to_set([1, 2, 3, 1]))
print(convert_to_set([1, 2, 3, 4]))

def count_unique_elements(input_list: list) -> int:
    """
    Count unique elements in the list.

    Hint: set only has unique elements.

    Hint: no loop required

    count_unique_elements([1, 2, 3]) => 3
    count_unique_elements([1, 1, 1]) => 1
    count_unique_elements([]) => 0
    """
    #count = 0
    #item = []
    #for items in input_list:
        #if items not in item:
            #count += 1
            #item.append(items)
    #return count
    set_list = set(input_list)
    count = len(set_list)
    return count
    # code here
print(count_unique_elements([1, 2, 3]))
print(count_unique_elements([1, 1, 1]))

def common_characters_in_words(word1: str, word2: str) -> set:
    """
    Find common characters in two words.

    No loops required.

    common_characters_in_words("hello", "hi") => {"h"}
    common_characters_in_words("world", "low") => {"l", "o", "w"}
    """

    # code here
    common_characters = []
    for symbol in word1:
        if symbol in word2:
            common_characters.append(symbol)
    return set(common_characters)

print(common_characters_in_words("hello", "hi"))
print(common_characters_in_words("world", "low"))

def exam_conditions_not_met(names1: list, names2: list) -> set:
    """
    Who has NOT met the conditions for the exam.

    To get to the exam, two tests have to be passed.
    There is one list with the names who passed the first test.
    And another list with the names who passed the second test.
    All the names are unique in this exercise.
    All the names are case-sensitive ("Kati" != "kati").

    So, the names who are in both lists, get to do the exam.
    This function has to return the names who DID NOT get to the exam.

    No loops required.

    exam_conditions_not_met(["Mati"], ["Mati", "Kati"]) => {"Kati"}
    exam_conditions_not_met(["Mati", "Kati"], ["Mati", "Kati"]) => {}
    exam_conditions_not_met(["Mati", "Kaja"], ["Mati", "Kati"]) => {"Kaja", "Kati"}
    """
    not_allowed_to_do_exam = []
    for name in names1:
        if name not in names2:
            not_allowed_to_do_exam.append(name)
    for name in names2:
        if name not in names1:
            not_allowed_to_do_exam.append(name)
    return set(not_allowed_to_do_exam)

    #no_pass = set()
    #for names in names2:
        #for x in names2:
            #if (names == x):
                #no_pass.add(x)
    #return no_pass
    # code here
print(exam_conditions_not_met(["Mati"], ["Mati", "Kati"]))
print(exam_conditions_not_met(["Mati", "Kati"], ["Mati", "Kati"]))
print(exam_conditions_not_met(["Mati", "Kaja"], ["Mati", "Kati"]))

def uninvited_friends_count(friends: list, invited: list) -> int:
    """
    How many friends were not invited.

    There is a list of friends and a list of invited people.
    How many of the friends were not invited?

    No loops required.

    uninvited_friends_count(["mati", "kati"], []) => 2
    uninvited_friends_count(["mati", "kati"], ["kati"]) => 1
    uninvited_friends_count(["mati", "kati"], ["kati", "rein"]) => 1
    """

    uninvited_friends = 0
    for names in friends:
        if names not in invited:
            uninvited_friends = uninvited_friends + 1
    return uninvited_friends
    # code here
print(uninvited_friends_count(["mati", "kati"], ["mati"]))

def contains_duplicates(input_list: list) -> bool:
    """
    Return whether the list contains duplicate elements.

    No loops required.

    contains_duplicates([1, 2, 3]) => False
    contains_duplicates([1, 2, 1]) => True
    contains_duplicates([1, 1]) => True
    contains_duplicates([1]) => False
    contains_duplicates([]) => False
    """
    # code here
    result = False
    if len(input_list) == len(set(input_list)):
        result = False
    else:
        result = True
    return  result
print(contains_duplicates([]))

def find_numbers_divisible_by_3(numbers: list) -> set:
    """
    Return a set of numbers from the input list which are divisible by 3.

    Numbers are between 0 and 1000 (inclusive).

    Hint: this function can be done without a loop.
    As we know the limit of numbers, we can create
    a set of all the numbers in the range which are
    divisible by 3.
    Hint: use range().

    find_numbers_divisible_by_3([1, 2, 3]) => {3}
    find_numbers_divisible_by_3([3, 2, 3, 12]) => {3, 12}
    """
    # code here
    divisible_numbers = []
    for number in numbers:
        if number % 3 == 0:
            divisible_numbers.append(number)
    return set(divisible_numbers)
print(find_numbers_divisible_by_3([3, 2, 3, 12]))