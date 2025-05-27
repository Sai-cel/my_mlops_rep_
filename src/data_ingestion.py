import pandas as pd
import os  
from sklearn.model_selection import train_test_split
import logging
import yaml
    
import re
import string


log_dir ="logs"
os.makedirs(log_dir , exist_ok = True)
logger = logging.getLogger("data_ingestion")
logger.setLevel("DEBUG")

console_handler = logging.StreamHandler()
console_handler.setLevel("DEBUG")

log_file_path = os.path.join(log_dir, 'data_ingestion.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def load_data(url:str) -> pd.DataFrame:
    try:
        df =pd.read_csv(url)
        logger.debug("Data loaded from %s", url)
        return df
    except pd.errors.ParserError as e:
        logger.error("Failed to parse the CSV file:%s" , e)
        raise
    except Exception as e:
        logger.error("unexcepted error occured while loading the data %s" , e)
        raise
        
        

def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    try:
        def clean_text(text):
            try:
                text = text.lower()
                text = re.sub(r'<.*?>', '', text)
                text = text.translate(str.maketrans('', '', string.punctuation))
                text = re.sub(r'\s+', ' ', text).strip()
                return text
            
            except Exception as e:
                logger.error("Error cleaning text: %s", e)
                return ""
        data['clean_review'] = data['review'].apply(clean_text)
        data.drop("review" , axis=1 , inplace = True)
        logger.debug("data cleaned suseccessfully %sqqq")
        return data

    except KeyError as e:
        logger.error("Missing 'review' column in input data: %s", e)
        raise
    except Exception as e:
        logger.error("Unexpected error occurred during preprocessing: %s", e)
        raise
    
def save_data(train_data:pd.DataFrame , test_data:pd.DataFrame , data_path:str)-> None:
    try:
        raw_data_path =os.path.join(data_path, "raw")
        os.makedirs(raw_data_path , exist_ok = True)
        train_data.to_csv(os.path.join(raw_data_path , "train.csv"))
        test_data.to_csv(os.path.join(raw_data_path , "test.csv"))
        logger.debug("train and test data save at %s" , raw_data_path)
    except Exception as  e:
        logger.error("unexpected exxror occured during at saving %s" , e)
        raise
    
    
    
        
def main():
    try:
        df = load_data("C:\\Users\\2000a\\my_ownproject_mlops\\data\\new_d1.csv")
        pre_data = preprocess_data(df)
        train_data , test_data = train_test_split(pre_data ,test_size=0.30 , random_state=2) 
        save_data(train_data , test_data ,data_path="./data")
    except Exception as e:
        logger.error("Failde to complete the data ingestion process")
    

print(main())
    
    
    
    
    
    
