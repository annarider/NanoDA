import pandas as pd

def wrangle_csv(file):
    df = pd.read_csv(file)
    subset = df.ix[:,'id':'yrs_on_list']
    subset.to_csv("Inc5000_Companies_2014_subset.csv", sep= ',')




if __name__ == '__main__':
    wrangle_csv("Inc5000_Companies_2014.csv")