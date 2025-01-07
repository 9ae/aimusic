from music21 import chord, metadata, stream, environment

us = environment.UserSettings()
us['musescoreDirectPNGPath'] = "/Applications/MuseScore 4.app/Contents/MacOS/mscore"
us['musicxmlPath'] = "/Applications/MuseScore 4.app/Contents/MacOS/mscore"

CHORD_NOTES = {
        "c": ["C", "E-", "G"],  # Cmin
        "C": ["C", "E", "G"],  # Cmaj
        "D": ["D", "F#", "A"],  # Dmaj
        "d": ["D", "F", "A"],  # Dmin
        "E": ["E", "G#", "B"],  # Emaj
        "e": ["E", "G", "B"],  # Emin
        "F": ["F", "A", "C"],  # Fmaj
        "f": ["F", "A-", "C"],  # Fmin
        "G": ["G", "B", "D"],  # Gmaj
        "g": ["G", "B-", "D"],  # Gmin
        "A": ["A", "C#", "E"],  # Amaj
        "a": ["A", "C", "E"],  # Amin
        "B": ["B", "D#", "F#"],  # Bmaj
        "b": ["B", "D", "F#"],  # Bmin
    }

def sequence_to_music21_chords(chord_sequence):
    """
    Translate the L-system generated chord sequence into a list of music21 
    chords.

    Parameters:
    - chord_sequence (str): The L-system generated chord sequence.

    Returns:
    - list of music21.chord.Chord: The corresponding chord progression in music21 format.
    """
    return [chord.Chord(CHORD_NOTES[chord_name]) for chord_name in
            chord_sequence if chord_name in CHORD_NOTES]


def create_and_show_music21_score(music21_chords):
    """
    Create and display a music score using the music21 library.

    This function takes a list of music21 chord objects and creates a score
    with them. It then displays this score. The score is titled "L-System Chord Progression".

    Parameters:
    - music21_chords (list): A list of music21 chord objects.
    """

    # Create a new music21 stream.Score object
    score = stream.Score()

    # Set the metadata for the score with a title
    score.metadata = metadata.Metadata(title="L-System Chord Progression")

    # Create a new music21 stream.Part object
    part = stream.Part()

    # Loop through each chord in the music21_chords list
    for chord in music21_chords:
        # Append each chord to the Part object
        part.append(chord)

    # Append the Part object containing chords to the Score object
    score.append(part)

    # Display the score
    score.show()