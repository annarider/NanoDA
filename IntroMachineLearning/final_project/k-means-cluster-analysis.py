import operator
import pickle
import json
import numpy as np
from sklearn.cluster import KMeans

KMEANS_FILE_NAME_PATH = "k-means_60clusters_subset.pkl"
#FROM_TO_FILE_NAME_PATH = "from_to_kmeans_60clusters_subset.pkl"
WORD_DATA_FILE_PATH = "word_data.pkl"
FINAL_PROJECT_DATASET = "final_project_dataset.pkl"
TFIDF_MATRIX_PATH = "tfidf_matrix.pkl"
CACHE_EMAIL_TOPIC_CLUSTERS = "email_topic_clusters.pkl"
CACHE_EMAIL_SUSPICIOUS_RATIO = "email_suspicious_ratio.pkl"
CACHE_EMAIL_SUSPICIOUS_RATIO_JSON = "email_suspicious_ratio.json"
CLUSTER_RATIO_SUBSET_PERCENT = 0.2
N_CLUSTERS = 60
TOP_N_CLUSTERS = 5

#from_to_data = from_to_data_subset

with open(KMEANS_FILE_NAME_PATH, 'r') as km:
    #pred, clf, cluster_centers, labels = pickle.load(km)
    pred, cluster_centers, labels = pickle.load(km)
#with open(FROM_TO_FILE_NAME_PATH, 'r') as ft:
#    from_to_data = pickle.load(ft)
with open(FINAL_PROJECT_DATASET, "r") as fpd:
    final_project_dataset = pickle.load(fpd)
with open(TFIDF_MATRIX_PATH, "r") as tm:
    term_document_matrix = pickle.load(tm)
with open(WORD_DATA_FILE_PATH, "r") as wd:
    word_data, from_to_data = pickle.load(wd)
    
#forgot to pickle clf, so reconstruct it.
clf = KMeans(n_clusters=cluster_centers.shape[0],init=cluster_centers)
clf.fit(cluster_centers)

#get the cluster label of each email
email_topic_clusters = clf.predict(term_document_matrix)
with open(CACHE_EMAIL_TOPIC_CLUSTERS, "w") as etc:
    pickle.dump(email_topic_clusters, etc, protocol = pickle.HIGHEST_PROTOCOL)


## calculate email & POI occurences
clusters_poi_count = np.zeros(N_CLUSTERS)
clusters_total_email_count = np.zeros(N_CLUSTERS)

# dict for checking if POI using email address 
check_email_poi = dict([(final_project_dataset[person]['email_address'], final_project_dataset[person]['poi']) for person in final_project_dataset])

# counting total emails & num of POIs
for i, cluster_num in enumerate(email_topic_clusters):
    email, _ = from_to_data[i]
    # count how many emails in each topic cluster
    clusters_total_email_count[cluster_num] += 1
    # count how many emails from pois in each topic cluster
    if email in check_email_poi and check_email_poi[email] == True:
        clusters_poi_count[cluster_num] += 1 
        

## calculate ratio of total email vs. POI occurences             
clusters_poi_ratio = np.zeros(N_CLUSTERS)
for i, c in enumerate(clusters_poi_count):
    clusters_poi_ratio[i] = clusters_poi_count[i] / clusters_total_email_count[i]

# sort by clusters ratio of POI/total email ascending
clusters_poi_ratio_sorted = np.argsort(clusters_poi_ratio)
# Find the top corresponding clusters, i.e. "suspicious clusters"
clusters_poi_ratio_top_sorted = clusters_poi_ratio_sorted[-TOP_N_CLUSTERS:] 


#the plan to make a feature:
# identify the 5 clusters that have the most POI emails. Call these "suspicious clusters"
# for each user, count the number of emails in suspicious clusters
# divide that by the total emails from that users. The resulting float is the new feature 

email_suspicious_cluster_count = dict([(final_project_dataset[person]['email_address'], 0) for person in final_project_dataset])
email_total_count = dict([(final_project_dataset[person]['email_address'], 0) for person in final_project_dataset])

for i, cluster_num in enumerate(email_topic_clusters):
    email, _ = from_to_data[i]
    if email in email_total_count:
        email_total_count[email] += 1
        if cluster_num in clusters_poi_ratio_top_sorted: 
            email_suspicious_cluster_count[email] += 1

email_suspicious_total_ratio = {}
for email in email_total_count:
    if email_total_count[email] != 0:
        email_suspicious_total_ratio[email] = email_suspicious_cluster_count[email] / email_total_count[email]
    else:
        email_suspicious_total_ratio[email] = 0        

with open(CACHE_EMAIL_SUSPICIOUS_RATIO, "w") as esr:
    pickle.dump(email_suspicious_total_ratio, esr, protocol = pickle.HIGHEST_PROTOCOL)

with open(CACHE_EMAIL_SUSPICIOUS_RATIO_JSON, 'w') as esrj:
    json.dump(email_suspicious_total_ratio, esrj)