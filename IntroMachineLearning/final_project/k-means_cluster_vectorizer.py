#!/usr/bin/python 

""" 
    k-means clustering for email vectorizer

"""

import pickle
import numpy as np
import matplotlib.pyplot as plt
import sys
import random
from scipy.sparse import vstack
#sys.path.append("../tools/")
#from feature_format import featureFormat, targetFeatureSplit
#import vectorize_all_emails

#word_data, from_to_data = vectorize_all_emails.process_email_data(use_cache=False)
#vectorize_all_emails.vectorize_email_data(word_data, use_cache=False)

TFIDF_MATRIX_PATH = "tfidf_matrix.pkl"
CACHE_KMEANS_FILE_NAME = "k-means_60clusters_subset.pkl"
CACHE_FROM_TO_FILE_NAME = "from_to_kmeans_60clusters_subset.pkl"
WORD_DATA_PATH = "word_data.pkl"


from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
#features_list = ["poi", feature_1, feature_2, feature_3]
with open(WORD_DATA_PATH, "r") as wd:
    word_data, from_to_data = pickle.load(wd)
print "done loading " + WORD_DATA_PATH + " pickle"

# delete word_data object to free up memory5
del word_data
print "got rid of word_data for extra space, kept from_to_data"

with open(TFIDF_MATRIX_PATH, "r") as tm:
    term_document_matrix = pickle.load(tm)
print "done loading " + TFIDF_MATRIX_PATH + " pickle"
    
term_document_matrix_normalized = normalize(term_document_matrix)
print "finished normalizing term_document_matrix" 
del term_document_matrix
print "got rid of term_document_matrix for extra space"

# Take subset of data because taking too long
term_document_matrix_normalized_subset = None
from_to_data_subset = []
SUBSET_PERCENT = 0.05

for i in range(term_document_matrix_normalized.shape[0]):
    if random.random() < SUBSET_PERCENT:
        if term_document_matrix_normalized_subset is not None:
            term_document_matrix_normalized_subset = vstack([term_document_matrix_normalized_subset, term_document_matrix_normalized[i]])
        else:
            term_document_matrix_normalized_subset = term_document_matrix_normalized[i]
        from_to_data_subset.append(from_to_data[i])
print "finish subsetting data"

# Turn the list back to array for k-means algorithm
#term_document_matrix_normalized_subset = np.array(term_document_matrix_normalized_subset)

del term_document_matrix_normalized
print "got rid of term_document_matrix_normalized for extra space"
 
clf = KMeans(n_clusters = 60)
pred = clf.fit_predict(term_document_matrix_normalized_subset)
print "finished fitting and clustering data"

cluster_centers = clf.cluster_centers_
labels = clf.labels_
    
with open(CACHE_KMEANS_FILE_NAME, "w") as kmc:
    pickle.dump((pred, cluster_centers, labels), kmc, protocol = pickle.HIGHEST_PROTOCOL)
    
with open(CACHE_FROM_TO_FILE_NAME, "w") as fte:
    pickle.dump(from_to_data_subset, fte, protocol = pickle.HIGHEST_PROTOCOL)

print "finished dumping file into pickle"

