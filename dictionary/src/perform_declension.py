import pandas as pd
import numpy as np
import re

def perform_declension(word: str, 
                       paradigm: str,
                       paradigm_master: pd.DataFrame) -> dict:
    """
    This function extracts the gender and plural of a given noun
    based on the paradigm taxonomy described in the PDF
    Συμπυκνωμένη γραμματική της Τσακώνικης γλώσσας σε πίνακες
    """

    if re.match(r'^[ΑΘΥ]([0-9])?$', paradigm) is None:
        return {}
    
    # Create empty information dict
    info_dict = {}
    
    ### Gender ###
    gender_dict = {
        'Α' : 'o',
        'Θ' : 'η',
        'Υ' : 'το'
    }
    info_dict['gender'] = gender_dict[paradigm[0]]
    
    ### Plural and genitive ###
    if '0' not in paradigm: # Regular paradigms
        row = paradigm_master.loc[paradigm]
    else: # Irregular paradigms
        row = paradigm_master.loc[word]
    
    try:
        if row['plural'] is not np.nan:
            info_dict['plural'] = row['plural']
        if row['gen_sing'] is not np.nan:
            info_dict['gen_sing'] = row['gen_sing'] 
    except KeyError:
        pass

    ### Add irregular feminine genitives ###
    if info_dict['gender'] == 'η' and '0' not in paradigm:
        femenine_genitives = paradigm_master[paradigm_master['type'] == 'femenine_genitives']
        if word in femenine_genitives.index:
            info_dict['gen_sing'] = femenine_genitives.loc[word, 'gen_sing']

    ### Generate notes ###
    # Create base
    notes = info_dict['gender']

    if 'plural' in info_dict.keys():
        notes += f', πλ. {info_dict["plural"]}'
    if 'gen_sing' in info_dict.keys():

        notes += f', γεν. {info_dict["gen_sing"]}'

    # Add notes to info_dict
    info_dict['notes'] = notes

    return info_dict    