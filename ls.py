import sys
from helpers import sequence_to_music21_chords, create_and_show_music21_score

CIRCLE = [
    ("C", "a"),
    ("C#", "a#"),
    ("D", "b"),
    ("D#", "c"),
    ("E", "c#"),
    ("F", "d"),
    ("F#", "d#"),
    ("G", "e"),
    ("G#", "f"),
    ("A", "f#"),
    ("A#", "g"),
    ("B", "g#")
]

MAJOR_KEYS = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
MINOR_KEYS = ['a', 'b-', 'b', 'c', 'd-', 'd', 'e-', 'e', 'f', 'g-', 'g', 'a-']

def chords_order(key, is_major=True):
    chords = []
    index = MAJOR_KEYS.index(key) if is_major else MINOR_KEYS.index(key)
    if is_major:
        new_order = MAJOR_KEYS[index:] + MAJOR_KEYS[:index]
        chords = [
            new_order[0], # I
            new_order[2].lower(), # ii
            new_order[4].lower(), # iii
            new_order[5], # IV
            new_order[7], # V
            new_order[9].lower(), # vi
            new_order[11].lower(), # vii
            ]
    else:
        new_order = MINOR_KEYS[index:] + MINOR_KEYS[:index]
        chords = [
            new_order[0], # i
            new_order[2], # ii
            new_order[3].upper(), # III
            new_order[5], # iv
            new_order[7], # v
            new_order[8].upper(), # VI
            new_order[10].upper(), # VII
        ]
    return chords

class LSystem:
    """
    A basic L-system class that provides functionality for generating sequences
    based on initial axiom and production rules.
    """

    def __init__(self, key):
        """
        Initialize the L-system with an axiom and production rules.

        Parameters:
        - axiom (str): The initial symbol.
        - rules (dict): A dictionary where keys are symbols and values are
            the corresponding replacement strings. For example, {"A": "ABC"}
        """
        is_major = key.isupper()
        self.axiom = '1451' if is_major else '1637'
        self.alphabet = chords_order(key, is_major)
        if len(self.alphabet) != 7:
            raise ValueError("Unable to generate chords for {0}".format(key))
        self.rules = {
            "1": "14",
            "2": "25",
            "3": "37",
            "4": "45",
            "5": "56",
            "6": "67",
            "7": "74",
        }
        self.output = self.axiom

    def iterate(self, n=1):
        """
        Apply the production rules to the current output n times.

        Parameters:
        - n (int): Number of times the rules are to be applied.

        Returns:
        - str: The output after applying the rules n times.
        """
        for i in range(n):
            next_output = self._iterate_once()
            self.output = next_output
            # print(f"Output after {i + 1} iteration(s): {self.output}")
        self._terminate()
        final_output = self.output
        self._reset_output()
        return final_output

    def _iterate_once(self):
        """
        Apply the production rules to the current output once.

        Returns:
        - str: The output after applying production rules once.
        """
        symbols = [self._apply_rule(symbol) for symbol in self.output]
        return "".join(symbols)

    def _apply_rule(self, symbol):
        """
        Apply production rules to a given symbol.

        Parameters:
        - symbol (str): The symbol to which rules are to be applied.

        Returns:
        - str: The transformed symbol or original symbol if no rules apply.
        """
        return self.rules.get(symbol, symbol)
    
    def _terminate(self):
        chords = []
        for symbol in self.output:
            index = int(symbol) - 1
            if index >= 0 and index < len(self.alphabet):
                chords.append(self.alphabet[index])
        if len(chords) > 0:
            self.output = "".join(chords)


    def _reset_output(self):
        """Reset the output to the initial axiom."""
        self.output = self.axiom


def main(start_key, n):
    """
    Main function to demonstrate the generation of chord progression using L-system.
    """

    l_system = LSystem(start_key)

    its = int(n)
    chord_sequence = l_system.iterate(its)
    print("Chord sequence:", chord_sequence)

    music21_chords = sequence_to_music21_chords(chord_sequence)
    create_and_show_music21_score(music21_chords)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python ls.py <number_of_iterations>")

