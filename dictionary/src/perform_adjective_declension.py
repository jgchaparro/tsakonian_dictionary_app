import pandas as pd
import re
from dictionary.models import AdjectiveParadigm

def perform_adjective_declension(word: str,
                                 paradigm: str) -> dict:
    ### Create general information dictionary ###
    info_dict = {}

    # If paradigm contains a number, add the form
    if re.match(r'^[Ε]([0-9])?$', paradigm) is not None:
        forms = AdjectiveParadigm.objects.filter(paradigm = paradigm)[0].forms
        info_dict['forms'] = forms

    ### Generate notes ###
    notes = info_dict['forms'] if 'forms' in info_dict.keys() else 'επίθ.'
    info_dict['notes'] = notes

    return info_dict