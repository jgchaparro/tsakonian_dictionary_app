from Levenshtein import distance as lev_distance
import pandas as pd

def obtain_entry_suggestions(input_string: str, 
                             list_of_strings: list, 
                             threshold: int = 2,
                             orthography: str = 'nowakowski',
                             top_k: int = 10) -> list:
  """
  Generates search suggestions based on Levenshtein distance.
  Entries with a distance less than or equal to the threshold are returned.

  Parameters:
  - input_string (str): The input string to compare against.
  - list_of_strings (list): A list of strings to compare against.
  - threshold (int): The maximum distance allowed for a string to be considered a match.
  - orthography (str): The orthography to use for the distance calculation. 
    Options are 'nowakowski' (default) and 'kostakis'.
  """
  # Compute distances
  distances = {target_string : lev_distance(input_string, target_string) for target_string in list_of_strings}

  # Convert to pd.Series
  distances_df = pd.Series(distances)

  # Filter based on threshold
  close_suggestions = distances_df[distances_df <= threshold].sort_values().index.tolist()[:top_k]

  return close_suggestions