import pandas as pd
import os 

df= pd.read_csv("C:\\Users\\2000a\\my_ownproject_mlops\\data\\d1.csv")

new_data = df.head(6000)
output_dir = "data"

# Create the folder
os.makedirs(output_dir, exist_ok=True)

# Save the new data (optional)
new_data.to_csv(os.path.join(output_dir, "new_d1.csv"), index=False)