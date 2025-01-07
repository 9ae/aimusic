import sys
from helpers import sequence_to_music21_chords, create_and_show_music21_score

class LSystem:
    """
    A basic L-system class that provides functionality for generating sequences
    based on initial axiom and production rules.
    """

    def __init__(self, axiom, rules):
        """
        Initialize the L-system with an axiom and production rules.

        Parameters:
        - axiom (str): The initial symbol.
        - rules (dict): A dictionary where keys are symbols and values are
            the corresponding replacement strings. For example, {"A": "ABC"}
        """
        self.axiom = axiom
        self.rules = rules
        self.output = axiom

    @property
    def alphabet(self):
        """
        Get the alphabet of the L-system.

        Returns:
        - set: The alphabet of the L-system.
        """
        return set(self.axiom + "".join(self.rules.values()))

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
            print(f"Output after {i + 1} iteration(s): {self.output}")
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

    def _reset_output(self):
        """Reset the output to the initial axiom."""
        self.output = self.axiom


def main(start_key, n):
    """
    Main function to demonstrate the generation of chord progression using L-system.
    """
    # Axiom: A
    axiom = start_key
    rules = {
        "C": "CAE",
        "D": "DBĞ",
        "Ď": "ĎÂF", # D flat
        "E": "EĎǍ",
        "Ě": "ĚCG", # E flat
        "F": "FDA",
        "G": "GEB",
        "Ğ": "ĞĚÂ", # G flat / F sharp
        "A": "AĞĎ",
        "Ǎ": "ǍCF", # A flat
        "Â": "ÂGD", # A sharp / B flat
        "B": "BǍĚ",
        "c": "cae",
        "ć": "ćfa", # c sharp
        "d": "dag",
        "e": "ebg",
        "ě": "ěcf", # e flat / d sharp
        "f": "fca",
        "g": "gdb",
        "ğ": "ğcf", # g flat/ f sharp
        "ġ": "ġeb", # g sharp
        "a": "ace",
        "b": "bdf",
        "â": "âcf", # a sharp / b flat
        }

    l_system = LSystem(axiom, rules)

    its = int(n)
    chord_sequence = l_system.iterate(its)
    music21_chords = sequence_to_music21_chords(chord_sequence)

    create_and_show_music21_score(music21_chords)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python ls.py <number_of_iterations>")

