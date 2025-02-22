import itertools
from itertools import product
import string

def parse_brackets(word: str, start_position: int) -> (str, int):
    """Find the word in [] staring from start_position and return the word and next_position.
    Assuming that start position is already ["""
    find = word.find(']', start_position)
    if find == -1:
        raise Exception('Malformed input', word)

    return word[start_position+1: find], find+1

def load_dictionary() -> list[str]:

    possible_passwords = []
    with open('dictionary.txt', 'r') as file:
        for line in file:  # Reads one line at a time
            possible_passwords.append(line.strip())

    return possible_passwords


def build_clues(clue)->list:
    """
    Building array of all possible clues assuming that all clues have the same length and
    exact numbers always have priority over combinations
    """
    parts = []
    i = 0

    while i < len(clue):

        letter = clue[i]
        # Combination
        if letter == '[':

            words, next_i = parse_brackets(clue, i)
            parts.append(words.split(','))
            i = next_i

        # Unknown character
        elif letter == '$':
            parts.append(list(string.ascii_lowercase))
            i += 1
        else:
            parts.append(letter)
            i += 1

    clues = itertools.product(*parts)

    return clues

def find_password() -> str:

    password = ''

    possible_passwords = load_dictionary()

    with open('clues.txt', 'r') as file:
        for line in file:  # Reads one line at a time

            clues = build_clues(line.strip())
            for possible_password in possible_passwords:
                for clue in clues:
                    if possible_password == ''.join(clue):
                        password = possible_password

    return password if password !='' else 'Password not found'

if __name__ == '__main__':

    print(find_password())