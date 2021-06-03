import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


#excel files containing our data
xlsx_files = ['africanwildlifefoundation.xlsx','animalplanet.xlsx','bbc_travel.xlsx','bbcearth.xlsx','bbcnews.xlsx','brianskerry.xlsx','christianziegler.xlsx','cnn.xlsx','cntraveler.xlsx','coryrichards.xlsx','davidlloyd.xlsx','discovery.xlsx','earthpix.xlsx','joelsartore.xlsx','margotraggettphotography.xlsx','nasa.xlsx','newscientist.xlsx','oceanconservancy.xlsx','passionpassport.xlsx','richardpetersphoto.xlsx','stevenchikosi.xlsx','stevewinterphoto.xlsx','travelandleisure.xlsx','travelchannel.xlsx','willbl.xlsx','wonderful_places.xlsx','world_wildlife.xlsx']

#merging all excel files into a large dataset
dataset = []
i = 0
while i < len(xlsx_files):
    data = pd.read_excel('https://github.com/ReZarrected/DESC/blob/main/'+xlsx_files[i]+'?raw=true')
    dataset.append(data)
    i+=1
dataset = pd.concat(dataset,ignore_index=True)
