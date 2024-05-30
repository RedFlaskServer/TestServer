import pickle
from pickles import dump_pickle

PICKLE_TO_RESET = "names.pickle"

with open(PICKLE_TO_RESET, 'wb') as file:
        # Serialize and write the variable to the file
        pickle.dump([], file)