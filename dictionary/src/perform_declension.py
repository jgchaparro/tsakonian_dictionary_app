import pandas as pd
import numpy as np
import re

def perform_declension(word: str, 
                       paradigm: str,
                       paradigm_master: pd.DataFrame) -> dict:
    """
    This function extracts the gender and plural of a given word
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

    return info_dict    