import pandas as pd
from .perform_declension import perform_declension
from .perform_conjugation import perform_conjugation
from .perform_adjective_declension import perform_adjective_declension

def extract_word_info(word: str,
                      paradigm: str):
    """helper function to extract all necessary information
    about a word based on the paradigms."""

    ### Detect word type ###
    word_types = {
                'Α' : 'noun',
                'Θ' : 'noun',
                'Υ' : 'noun',
                'Ρ' : 'verb',
                'Ε' : 'adjective',
            }
    if paradigm[0] in word_types.keys():
        word_type = word_types[paradigm[0]]
    else:
        print(f'No manageable word type not found for {word}: paradigm {paradigm}')
        return {}
    
    ### Nouns ###
    if word_type == 'noun':
        # Read paradigm master table
        filepath = 'data/tables/paradigms_nouns.xlsx'
        paradigm_master = pd.read_excel(filepath).set_index('paradigm')

        # Perform declension
        info_dict = perform_declension(word, paradigm, paradigm_master)

        # Debug
        print(f'Declination: {info_dict}')

    elif word_type == 'verb':
        # Read paradigm master table
        filepath = 'data/tables/paradigms_verbs.xlsx'
        paradigm_master = pd.read_excel(filepath)
        paradigm_master.set_index(['paradigm', 'ending'], inplace=True)

        # Perform conjugation
        info_dict = perform_conjugation(word, paradigm, paradigm_master)

        # Debug
        print(f'Conjugation: {info_dict}')

    ### Adjectives ###
    elif word_type == 'adjective':
        # Read paradigm master table
        filepath = 'data/tables/paradigms_adjectives.xlsx'
        paradigm_master = pd.read_excel(filepath).set_index('paradigm')

        # Perform declension
        info_dict = perform_adjective_declension(word, paradigm, paradigm_master)

        # Debug
        print(f'Forms: {info_dict}')

    return info_dict
