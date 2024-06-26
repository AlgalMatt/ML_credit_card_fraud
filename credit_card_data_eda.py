
from pathlib import Path
import os
import pandas as pd
import numpy as np
from zipfile import ZipFile 


#define paths
data_path=Path(os.getcwd())/"data"


# loading the temp.zip and creating a zip object 
with ZipFile(data_path/'credit_card_data_kaggle.zip') as zObject: 
    # Extracting all the members of the zip  
    # into a specific location. 
    zObject.extractall( 
        path=data_path)