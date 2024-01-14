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
        conjugation = paradigm_master.loc[(verb, 'irr')].dropna().to_dict()
        return conjugation
    
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
    conjugation = paradigm_subset.loc[ending].dropna().to_dict()

    # Update conjugation with ending
    conjugation['ending'] = f'-{ending}'

    # Add word type
    # conjugation['word_type'] = 'Ρήμα'

    return conjugation