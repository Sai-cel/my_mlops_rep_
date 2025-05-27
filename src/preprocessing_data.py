import os
import logging
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string
import nltk
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
nltk.download('stopwords')
nltk.download('punkt')
import logging 



log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger('data_preprocessing')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dir, 'data_preprocessing.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

from nltk.stem import PorterStemmer
ps = PorterStemmer()


def transform_test(test):
    words =  test.split()
    filtered_words = [i for i in words if i not in ENGLISH_STOP_WORDS]
    stemmed_words = [ps.stem(i) for i in filtered_words ]
    return " ".join(stemmed_words)


def encoding_function(df   , test_column = "sentiment" ,target_column='clean_review'):
    try:
        logger.debug("starting preprocesing for datframe")
        encoder = LabelEncoder()
        df[test_column]= encoder.fit_transform(df[test_column])
        df[target_column] = df[target_column].apply(transform_test)
        logger.debug("Target column encoed")
        return df
    
    except KeyError as e:
        logger.error("column not found : %s" , e)
        
    except Exception as e :
        logger.error("errror duing test normalization" , e)
    
        
def main(text_column='text'):
    try:
        train_data = pd.read_csv('./data/raw/train.csv')
        test_data = pd.read_csv('./data/raw/test.csv')
        logger.debug('Data loaded properly')
        
        train_processed_data = encoding_function(train_data)
        test_processed_data = encoding_function(test_data)
        data_path = os.path.join("./data" , "interim")
        os.makedirs(data_path , exist_ok = True)
        
        train_processed_data.to_csv(os.path.join(data_path , "train_processed.csv"), index=False)
        test_processed_data.to_csv(os.path.join(data_path,"test_processed.csv"),index= False)
        logger.debug("processed data saved to %s" ,data_path)
        
    except KeyError as e:
        logger.error("File not found: %s" , e)
    except pd.errors.EmptyDataError as e:
        logger.error('No data: %s', e)
    except Exception as e:
        logger.error('Failed to complete the data transformation process: %s', e)
        print(f"Error: {e}")
        
if __name__ == '__main__':
    main()
