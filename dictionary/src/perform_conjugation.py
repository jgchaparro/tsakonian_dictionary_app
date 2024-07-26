import pandas as pd
from dictionary.models import VerbParadigm

def perform_conjugation(verb: str,
                        paradigm: str) -> dict:
    
    """
    Extracts the conjugation endings 
    for a given verb based on the paradigm taxonomy
    """

    ### Irregular paradigms ###
    if paradigm == "Ρ0":
        conjugation_info = VerbParadigm.objects.filter(paradigm = verb)
        conjugation_info = pd.DataFrame(list(conjugation_info.values())).loc[0].dropna().to_dict()                           

    elif paradigm == "Ρ":
        conjugation_info = {}
    
    else:
        ### Regular paradigms ###
        # Get paradigm subset
        # paradigm_subset = paradigm_master.loc[paradigm]
        paradigm_subset = VerbParadigm.objects.filter(paradigm = paradigm)
        # Extract ending column   
        endings_list = [verb_paradigm.ending for verb_paradigm in paradigm_subset]
        
        # Detect the ending
        for ending_str in endings_list:
            if verb.endswith(ending_str):
                ending = ending_str
                break

        # Extract conjugation information
        conjugation_info = VerbParadigm.objects.filter(paradigm = paradigm, ending = ending)
        conjugation_info = pd.DataFrame(list(conjugation_info.values())).loc[0].dropna().to_dict()

        # Update conjugation with ending
        conjugation_info['ending'] = f'-{ending}'

    ### Generate notes ###
    notes = ''

    if 'orist_aoristos' in conjugation_info.keys():
        notes += f'αόρ. {conjugation_info["orist_aoristos"]}'
    if 'ypot_aoristos' in conjugation_info.keys():
        notes += f', υπ. αόρ. {conjugation_info["ypot_aoristos"]}'
    if 'metochi' in conjugation_info.keys():
        notes += f', μετ. {conjugation_info["metochi"]}'
    if 'ypot_enestotas' in conjugation_info.keys():
        notes += f', υπ. ενεστ. {conjugation_info["ypot_enestotas"]}'
    
    # Create generic notes if no specific notes exist
    if notes == '':
        notes = 'ρήμα'

    # Add notes to conjugation_info
    conjugation_info['notes'] = notes

    return conjugation_info