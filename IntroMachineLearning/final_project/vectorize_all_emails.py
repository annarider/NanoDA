#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

CACHE_FILE_NAME = "word_data.pkl"

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
                    if temp_counter: # < 500:
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
                                    to_email_found = m.group(1)
                                    from_to_data.append((to_email_found, 'to'))
        
        with open(CACHE_FILE_NAME, "w") as wd:
            pickle.dump((word_data, from_to_data), wd, protocol = pickle.HIGHEST_PROTOCOL)
            return (word_data, from_to_data)
        print "all emails processed"
    
            
def vectorize_email_data(word_data):
#    do TfIdf vectorization here

    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer(stop_words = "english")
    vectorizer.fit_transform(word_data)
    vocab_list = vectorizer.get_feature_names()
    return vectorizer.idf_

if __name__ == '__main__':
    word_data, from_to_data = process_email_data(use_cache=False)
    print vectorize_email_data(word_data)
    
    

'''

from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")




for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        temp_counter += 1
        if temp_counter < 200:
            path = os.path.join('..', path[:-1])
            print path
            email = open(path, "r")

            ### use parseOutText to extract the text from the opened email
            parsed_email = parseOutText(email)
            
            ### use str.replace() to remove any instances of the words
            replacements = {"sara": "", "shackleton": "", 
                            "chris": "", "germani":"",
                            "sshacklensf": "",
                            "cgermannsf": ""}
                            
#                            
#            replacements = dict((re.escape(k), v) 
#                              for k, v in replacements.iteritems())
#            pattern = re.compile("|".join(replacements.keys()))
#            parsed_email_stripped_common_words = pattern.sub(
#                    lambda m: replacements[re.escape(m.group(0))], parsed_email)
                            
            parsed_email_stripped_common_words = parsed_email
            for word in replacements.keys():
                parsed_email_stripped_common_words = parsed_email_stripped_common_words.replace(word, "")

            ### append the text to word_data
            word_data.append(parsed_email_stripped_common_words)

            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            if name == 'sara':
                from_data.append(0)
            elif name == 'chris':
                from_data.append(1)

            email.close()

print "emails processed"
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )

print word_data[152]
'''