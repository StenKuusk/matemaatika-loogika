"""Dictionary exercises."""


def get_hobbies(hobbies_dict: dict, name: str) -> list:
    """
    Return the hobbies of a given person.

    hobbies = {
    "Tom": ["running", "reading"],
    "John": ["movies", "music", "swimming"]
    }

    get_hobbies(hobbies, "Tom")  => ["running", "reading"]
    get_hobbies(hobbies, "Timmy")  => "name not in dictionary"

    :param hobbies_dict: dictionary with peoples' hobbies.
    :param name: name of person whose hobbies are to be returned.

    :return: List of hobbies of the person with given name or "name not in dictionary".
    """
    # your code goes here
    if name in hobbies_dict:
        return hobbies_dict[name]
    else:
        return "name not in dictionary"

hobbies = {
    "Tom": ["running", "reading"],
    "John": ["movies", "music", "swimming"]
    }

print(get_hobbies(hobbies, "Timmy"))

def find_tallest(height_dict: dict) -> str:
    """
    Return the name of the tallest peron in given dictionary.

    find_tallest({"Tom": 186, "Mari": 175, "Jhon": 190}) => "Jhon"

    :param height_dict: dictionary with peoples' names and heights
    :return name of tallest person in given dict.
    """
    # your code goes here
    height = 0
    tallest = ""

    for name in height_dict.keys():
        if height_dict[name] > height:
            height = height_dict[name]
            tallest = name
    return tallest

def remove_sixes(six_dict: dict) -> dict:
    """
    Return a dictionary where all keys which's values are dividable by six are removed.

    remove_sixes({"a": 4, "b": 8, "c": 6, "d": 18}) => {"a": 4, "b": 8}

    :param six_dict: dictionary to be modified.
    :return: dict without values that are dividable by six.
    """
    # your code goes here
    for key, value in list(six_dict.items()):
        if value % 6 == 0:
            del six_dict[key]
    return six_dict

print(remove_sixes({"a": 4, "b": 8, "c": 6, "d": 18}))

def exchange_keys_and_values(exchange_dict: dict) -> dict:
    """
    Return a dict where keys and values have been exchanged.

    exchange_keys_and_values({"a": "b", "c": "d"}) => {"b": "a", "d": "c"}

    :param exchange_dict: dictionary to be modified.
    :return dictionary where values and keys have been exchanged.
    """
    new_dict = {}
    for key, value in exchange_dict.items():
        new_dict[value] = key
    return new_dict

print(exchange_keys_and_values({"a": "b", "c": "d"}))


def count_symbol_appearances(stringy: str) -> dict:
    """
    Return dict where key is the symbol and the value is the count this symbol is present in the string.

    count_symbol_appearances("hello hi") => {'h': 2, 'e': 1, 'l': 2, 'o': 1, ' ': 1, 'i': 1}

    :param stringy: string to be processed.
    :return: dictionary with symbol counts.
    """
    # your code goes here
    symbol_count_dict = {}
    for symbol in stringy:
        if symbol not in symbol_count_dict:
            symbol_count_dict[symbol] = 1
        else:
            symbol_count_dict[symbol] = symbol_count_dict[symbol] + 1
    return symbol_count_dict

print(count_symbol_appearances("hello hi"))


def organise_by_first_symbol(strings: list) -> dict:
    """
    Return dict where key the is a symbol and the value is a list of words starting with this symbol.

    organise_by_first_symbol(["hello", "word", "world", "welcome", "yes"]) =>
        {'h': ['hello'], 'w': ['word', 'world', 'welcome'], 'y': ['yes']}

    :param strings: list of strings.
    :return: dict with starting symbol and corresponding words in order of appearance.
    """
    # your code goes here
    string_dict = {}
    for string_element in strings:
        if string_element[0] not in string_dict:
            string_dict[string_element[0]] = []
            string_dict[string_element[0]].append(string_element)
        else:
            string_dict[string_element[0]].append(string_element)
    return  string_dict

print(organise_by_first_symbol(["hello", "word", "world", "welcome", "yes"]))