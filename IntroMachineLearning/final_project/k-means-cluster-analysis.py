import operator
import pickle
import numpy as np
#from sklearn.cluster import KMeans

KMEANS_FILE_NAME_PATH = "k-means_60clusters_subset.pkl"
#FROM_TO_FILE_NAME_PATH = "from_to_kmeans_60clusters_subset.pkl"
WORD_DATA_FILE_PATH = "word_data.pkl"
FINAL_PROJECT_DATASET = "final_project_dataset.pkl"
TFIDF_MATRIX_PATH = "tfidf_matrix.pkl"
CLUSTER_RATIO_SUBSET_PERCENT = 0.2


#from_to_data = from_to_data_subset

with open(KMEANS_FILE_NAME_PATH, 'r') as km:
    pred, clf, cluster_centers, labels = pickle.load(km)
#with open(FROM_TO_FILE_NAME_PATH, 'r') as ft:
#    from_to_data = pickle.load(ft)
with open(FINAL_PROJECT_DATASET, "r") as fpd:
    final_project_dataset = pickle.load(fpd)
with open(TFIDF_MATRIX_PATH, "r") as tm:
    term_document_matrix = pickle.load(tm)
with open(WORD_DATA_FILE_PATH, "r") as wd:
    word_data, from_to_data = pickle.load(wd)
    
#forgot to pickle clf, so reconstruct it.
#clf = KMeans(cluster_centers,n_clusters=cluster_centers.shape[0],init=cluster_centers)

#use clf.predict(fullTfIdfMatrix) to get the cluster label of each email

email_topic_clusters = clf.predict(term_document_matrix)

#clusters_poi_count = np.zeros(60)
clusters_poi_count = dict.fromkeys(range(0, 60))
clusters_total_email_count = dict.fromkeys(range(0, 60))

# dict for checking if POI using email address 
check_email_poi = dict([(final_project_dataset[person]['email_address'], final_project_dataset[person]['poi']) for person in final_project_dataset])

# counting total emails & num of POIs
for i, cluster_num in enumerate(email_topic_clusters):
    email, _ = from_to_data[i]
    # count how many emails in each topic cluster
    if clusters_total_email_count[cluster_num] is not None:
        clusters_total_email_count[cluster_num] += 1
    else:
        clusters_total_email_count[cluster_num] = 1
    # count how many emails from pois in each topic cluster
    if email in check_email_poi and check_email_poi[email] == True:
        if clusters_poi_count[cluster_num] is not None:
            clusters_poi_count[cluster_num] += 1
        else: 
            clusters_poi_count[cluster_num] = 1 
    
                
            
                    
clusters_poi_ratio = {}
for c in clusters_poi_count:
    if clusters_poi_count[c] is not None:
        clusters_poi_ratio[c] = clusters_poi_count[c] / clusters_total_email_count[c]

clusters_poi_ratio_sorted = sorted(clusters_poi_ratio.items(), key=operator.itemgetter(1), reverse = True)               
clusters_poi_ratio_top_sorted = clusters_poi_ratio_sorted[:int(len(clusters_poi_ratio_sorted) * CLUSTER_RATIO_SUBSET_PERCENT)]

#the plan to make a feature:
# identify the 5 clusters that have the most POI emails. Call these "suspicious clusters"
# for each user, count the number of emails in suspicious clusters
# divide that by the total emails from that users. The resulting float is the new feature 