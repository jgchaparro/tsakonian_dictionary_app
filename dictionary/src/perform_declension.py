import pandas as pd
import numpy as np
import re
from dictionary.models import NounParadigm

def perform_declension(word: str, 
                       paradigm: str) -> dict:
    """
    This function extracts the gender and plural of a given noun
    based on the paradigm taxonomy described in the PDF
    Συμπυκνωμένη γραμματική της Τσακώνικης γλώσσας σε πίνακες
    """
    # Return empty dictionary is paradigm is empty
    if re.match(r'^[ΑΘΥ]([0-9])?$', paradigm) is None:
        return {}

    # Create empty results dict
    results_dict = {}

    ### Get paradigm info ###
    key = paradigm if '0' not in paradigm else word
    paradigm_info = NounParadigm.objects.filter(paradigm = key)
    paradigm_info = pd.DataFrame(list(paradigm_info.values())).loc[0]
    paradigm_info = paradigm_info.dropna() # Keep only non-null values
    
    ### Gender ###
    gender_dict = {
        'Α' : 'o',
        'Θ' : 'α',
        'Υ' : 'το'
    }
    results_dict['gender'] = gender_dict[paradigm[0]]
    
    ### Plural and genitive ###   
    if 'plural' in paradigm_info.keys():
        results_dict['plural'] = paradigm_info['plural']

    if 'gen_sing' in paradigm_info.keys():
        results_dict['gen_sing'] = paradigm_info['gen_sing']

    ### Add irregular feminine genitives ###
    if results_dict['gender'] == 'α' and '0' not in paradigm:
        femenine_genitive_query = NounParadigm.objects.filter(type = 'femenine_genitives', paradigm = word)
        if len(femenine_genitive_query) > 0:
            results_dict['gen_sing'] = femenine_genitive_query[0].gen_sing

    ### Generate notes ###
    # Create base
    notes = results_dict['gender']

    if 'plural' in results_dict.keys():
        notes += f', πλ. {results_dict["plural"]}'
    if 'gen_sing' in results_dict.keys():
        notes += f', γεν. {results_dict["gen_sing"]}'

    # Add notes to info_dict
    results_dict['notes'] = notes

    return results_dict    