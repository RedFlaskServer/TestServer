
# Step 1: Import Pickle
import pickle
# from 

# Step 2: Saving Variables
# ram = {"message":"hello there"}
file_path = 'names.pickle'

# Open the file in binary mode
def dump_pickle(file_path, list):
    with open(file_path, 'wb') as file:
        # Serialize and write the variable to the file
        pickle.dump(list, file)
# Step 3: Loading Variables
loaded_data = None

# Open the file in binary 
def get_pickle(file_path):
    with open(file_path, 'rb') as file:
        # Deserialize and retrieve the variable from the file
        return pickle.load(file)

print("The variable 'data' has been loaded successfully.")

print("Loaded Data:", loaded_data)