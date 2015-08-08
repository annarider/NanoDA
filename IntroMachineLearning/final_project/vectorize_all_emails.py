#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

CACHE_FILE_NAME = "word_data.pkl"
TDIDF_MATRIX = "tdidf_matrix.pkl"

def process_email_data(use_cache = False):
    if use_cache and os.path.isfile(CACHE_FILE_NAME):
        with open(CACHE_FILE_NAME, "r") as wd:
            return pickle.load(wd)    
    else:
        from_to_data = []
        word_data = []
        
        ### temp_counter helps you only look at the first 200 emails in the list
        temp_counter = 0
        
        emails_directory = os.listdir("../final_project/emails_by_address")
        for filename in emails_directory:
            with open("../final_project/emails_by_address/" + filename, "r") as file_contents:
                
                for email_path in file_contents:
                    temp_counter += 1
                    print temp_counter, filename
                    if temp_counter: # < 1000:
                        path = os.path.join('../', email_path[:-1])
            #            print filename  
                        
                        # don't continue if the email doesn't exist 
                        if os.path.isfile(path):                        
                            with open(path, "r") as email:
                                parsed_email = parseOutText(email)
                    #            print parsed_email
                                word_data.append(parsed_email)
                                
                                m = re.search('from_(.+?).txt', filename)
                                if m:
                                    from_email_found = m.group(1)
                                    from_to_data.append((from_email_found, 'from'))
                                else:
                                    m = re.search('to_(.+?).txt', filename)
                                    if m:
                                        to_email_found = m.group(1)
                                        from_to_data.append((to_email_found, 'to'))
        
        with open(CACHE_FILE_NAME, "w") as wd:
            pickle.dump((word_data, from_to_data), wd, protocol = pickle.HIGHEST_PROTOCOL)
            return (word_data, from_to_data)
        print "all emails processed"
    
            
def vectorize_email_data(word_data, use_cache = False):
#    do TfIdf vectorization here
    if use_cache and os.path.isfile(TDIDF_MATRIX):
        with open(TDIDF_MATRIX, "r") as tm:
            return pickle.load(tm)
    else: 
        from sklearn.feature_extraction.text import TfidfVectorizer
        vectorizer = TfidfVectorizer(stop_words = "english", use_idf = True)
        term_document_matrix = vectorizer.fit_transform(word_data)
#        features = vectorizer.get_feature_names()
        with open(TDIDF_MATRIX, 'w') as tm:
            pickle.dump(term_document_matrix, tm, protocol = pickle.HIGHEST_PROTOCOL)
            print "term document matrix object saved to pickle"
            return term_document_matrix

if __name__ == '__main__':
    word_data, from_to_data = process_email_data(use_cache=False)
    term_document_matrix=  vectorize_email_data(word_data, use_cache=False)
    print term_document_matrix
    