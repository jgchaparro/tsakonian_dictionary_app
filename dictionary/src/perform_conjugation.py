import pandas as pd

def perform_conjugation(verb: str,
                        paradigm: str,
                        paradigm_master: pd.DataFrame) -> dict:
    
    """
    Extracts the conjugation endings 
    for a given verb based on the paradigm taxonomy
    """

    ### Irregular paradigms ###
    if paradigm == "Ρ0":
        conjugation_info = paradigm_master.loc[(verb, 'irr')].dropna().to_dict()

    elif paradigm == "Ρ":
        conjugation_info = {}        
    
    else:
        ### Regular paradigms ###
        # Get paradigm subset
        paradigm_subset = paradigm_master.loc[paradigm]

        # Extract specific subset
        endings_list = paradigm_subset.index.tolist()

        # Detect the ending
        for ending_str in endings_list:
            if verb.endswith(ending_str):
                ending = ending_str
                break

        # Extract conjugation information
        conjugation_info = paradigm_subset.loc[ending].dropna().to_dict()

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