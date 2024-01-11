def generate_notes(paradigm):
    """Creates simple word marks for every entry."""

    word_types = {
                'Α' : 'ουσ.',
                'Θ' : 'ουσ.',
                'Υ' : 'ουσ.',
                'Ρ' : 'ρήμα',
                'Ε' : 'επίθ.',
            }
    if paradigm[0] in word_types.keys():
        notes = word_types[paradigm[0]]
    else:
        notes = None

    return notes