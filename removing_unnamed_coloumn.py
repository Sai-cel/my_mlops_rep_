# import pandas as pd
# import os

# def removed_unwanted_column(file1):
#     df=pd.read_csv(file1)
#     remove_c = df.drop("Unnamed: 0" , axis =1 , inplace = True)
#     return df



# def removed_unwanted_column1(file1):
#     df=pd.read_csv(file1)
#     remove_c =df.drop("Unnamed: 0" , axis =1 , inplace = True)
#     return df


# def main(file1 , file2):
#     orginal_data = removed_unwanted_column(file1)
#     orginal_data2 = removed_unwanted_column1(file2)
    
#     data_path = os.path.join("./data" , "interim")
#     os.makedirs(data_path , exist_ok = True)
    
    
#     test_processed1_path= os.path.join(data_path , "test_processed.csv")
#     train_processed1_path = os.path.join(data_path , "train_processed.csv")
    
#     orginal_data.to_csv(test_processed1_path)
#     orginal_data2.to_csv(train_processed1_path)
#     return "sucesfully crated files and remove the files "            

# file1 = "C:\\Users\\2000a\\my_ownproject_mlops\\data\\interim\\test_processed.csv"
# file2 = "C:\\Users\\2000a\\my_ownproject_mlops\\data\\interim\\train_processed.csv"
# print(main(file1 ,  file2))

import pandas as pd
df = pd.read_csv("C:\\Users\\2000a\\my_ownproject_mlops\\data\\interim\\test_processed.csv")
print(df.columns)
