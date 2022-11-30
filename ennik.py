"""Tuple exercises."""


def get_sum_and_diff(a: int, b: int) -> tuple:
    """
    Return sum of a and b and diff of a and b.

    The function should return two values:
    the first one is the sum of parameters a and b;
    the second one is the diff of parameters a anb b (subtract b from a).

    If a function returns several values:
    return a, b, c
    then this is actually a tuple.

    It is the same as:
    return (a, b, c).

    get_sum_and_diff(1, 2) => (3, -1)
    get_sum_and_diff(1, 1) => (2, 0)
    get_sum_and_diff(5, 1) => (6, 4)
    """
    sum = (a + b)
    diff = (b - a)
    return sum , diff
    pass
print(get_sum_and_diff(3, 5))


def create_tuple_from_two_numbers(a: int, b: int) -> tuple:
    """
    Create a tuple.

    If the values of a and b are the same, then create a tuple with one element.
    If the values are different, create tuple of a and b (in that order).

    create_tuple_from_two_numbers(1, 2) => (1, 2)
    create_tuple_from_two_numbers(1, 1) => (1,)
    """
    empty_tuple = ()
    if a == b:
        empty_tuple = tuple([a])
    else:
        empty_tuple = tuple([a, b])
    return empty_tuple
    pass


def create_tuple_up_to_n(n: int) -> tuple:
    """
    Create tuple with numbers from 0 up to n (inclusive).

    If n < 0, return empty tuple.

    create_tuple_up_to_n(2) => (0, 1, 2)
    create_tuple_up_to_n(0) => (0, )
    create_tuple_up_to_n(-10) => ()
    """
    if n < 0:
        return tuple()
    else:
        return tuple(list(range(n+1)))
    pass

print(create_tuple_up_to_n(2))
print(create_tuple_up_to_n(0))
print(create_tuple_up_to_n(-10))

def merge_tuples(a: tuple, b: tuple) -> tuple:
    """
    Merge two tuples by adding b elements after a elements.

    merge_tuples((1, 2), (3, 4)) => (1, 2, 3, 4)
    merge_tuples((1, ), (3, )) => (1, 3)
    merge_tuples((1, 2, 3), (1, 2)) => (1, 2, 3, 1, 2)
    """
    merged_tuple = a + b
    return merged_tuple
    pass

print(merge_tuples((1, 2), (3, 4)))
print(merge_tuples((1, ), (3, )))
print(merge_tuples((1, 2, 3), (1, 2)))


def remove_odd_numbers(numbers: tuple) -> tuple:
    """
    Return a tuple where all the odd numbers are removed from the input tuple.

    The order of the elements should remain the same.

    remove_odd_numbers((1, 2, 3)) => (2, )
    remove_odd_numbers((1, 5, 3)) => ()
    remove_odd_numbers((2, 4, 6)) => (2, 4, 6)
    """
    removed_tuple = []
    for number in numbers:
        if number % 2 == 0:
            removed_tuple.append(number)
    return tuple(removed_tuple)
    pass
print(remove_odd_numbers((2, 4, 6)))


def insert_tuple_inside_tuple(outer_tuple: tuple, position: int, inner_tuple: tuple) -> tuple:
    """
    Insert inner_tuple inside outer_tuple at the given position.

    All the elements at position and after the position are shifted
    so that the whole inner_tuple fits at the position.

    The position is non-negative and max value is length of outer_tuple.
    If the position is the length of outer_tuple, the inner_tuple will be
    appended at the end of the outer_tuple.

    insert_tuple_inside_tuple((1, 2), 0, (3, 4)) => (3, 4, 1, 2)
    insert_tuple_inside_tuple((1, 2), 1, (3, 4)) => (1, 3, 4, 2)
    insert_tuple_inside_tuple((1, 2), 2, (3, 4)) => (1, 2, 3, 4)
    insert_tuple_inside_tuple((1, 2, 3), 1, (1, )) => (1, 1, 2, 3)
    """
    inserted_tuple = []
    inserted_tuple = inserted_tuple + list(outer_tuple)
    inserted_tuple = inserted_tuple[:position] + list(inner_tuple) + inserted_tuple[position:]
    return tuple(inserted_tuple)
    pass
print(insert_tuple_inside_tuple((1, 2), 0, (3, 4)))
print(insert_tuple_inside_tuple((1, 2), 1, (3, 4)))
print(insert_tuple_inside_tuple((1, 2), 2, (3, 4)))