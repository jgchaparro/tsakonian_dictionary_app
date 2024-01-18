import pandas as pd
import re

def perform_adjective_declension(word: str,
                                 paradigm: str,
                                 paradigm_master: pd.DataFrame) -> dict:
    
    ### Create general information dictionary ###
    info_dict = {}

    # If paradigm contains a number, add the form
    if re.match(r'^[Ε]([0-9])?$', paradigm) is not None:
        info_dict['forms'] = paradigm_master.loc[paradigm, 'forms']

    ### Generate notes ###
    notes = info_dict['forms'] if 'forms' in info_dict.keys() else 'επίθ.'
    info_dict['notes'] = notes

    return info_dict