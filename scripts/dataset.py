import zipfile
import os

def unzipfile(filepath: str):
    """
    This function takes in the path to the zip file and extracts it to the data folder
    """
    data_path ="data"
    if not os.path.exists(str(data_path)):
        # Create a directory for the extracted data
        print("Creating data directory...")
        os.makedirs(data_path, exist_ok=True)
    else:
        print("Data Directory already exists")
        
    # Extract the contents of the file
    if not os.listdir(data_path):
        print("Extracting files...")
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            zip_ref.extractall(data_path)
            
    else:
        print("Data already extracted, Skipping Extraction")
        
        
if __name__ == "__main__":
    unzipfile(filepath="Partcipants_Dataset_DSSC_2024.zip")
