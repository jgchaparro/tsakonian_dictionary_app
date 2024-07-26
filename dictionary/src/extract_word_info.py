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
    info_functions = {
        'noun' : perform_declension,
        'verb' : perform_conjugation,
        'adjective' : perform_adjective_declension
    }
    info_dict = info_functions[word_type](word, paradigm)

    # Debug
    print(f'Information dictionary: {info_dict}')

    return info_dict
