import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions, StandardOptions
from apache_beam.options.pipeline_options import SetupOptions
import re

from apache_beam.io.gcp.internal.clients import bigquery
from google.cloud import storage

options = PipelineOptions()
google_cloud_options = options.view_as(GoogleCloudOptions)
google_cloud_options.project = 'serene-vehicle-247610'
google_cloud_options.job_name = 'testingjob'
google_cloud_options.staging_location = 'gs://akanksha_bucket_1/staging'
google_cloud_options.temp_location = 'gs://akanksha_bucket_1/temp'
#options.view_as(StandardOptions).runner = 'DataFlowRunner'
options.view_as(StandardOptions).runner = 'DirectRunner'

import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from wordcloud import WordCloud,STOPWORDS
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.pipeline import make_pipeline
import warnings
warnings.filterwarnings("ignore")
import pickle

from nltk.tokenize import WordPunctTokenizer

table_spec = bigquery.TableReference(
        projectId='serene-vehicle-247610',
        datasetId='my_new_dataset',
        tableId='twitter')

table_schema = {'fields': [
{'name': 'Id', 'type': 'STRING', 'mode': 'REQUIRED'},
{'name': 'Tweet', 'type': 'STRING', 'mode': 'REQUIRED'},
{'name': 'Label', 'type': 'STRING', 'mode': 'REQUIRED'}
]}

def MLmodel(data):
    train  = pd.read_csv("train_E6oV3lV.csv")
    X = train.iloc[:, :-1].values
    y = train.iloc[:, 1].values
    #test = pd.read_csv("test_tweets_anuFYb8.csv")
    #train.sample(2)
    print(train)
    #print



   # print(train.shape)

    #print(test.shape)

    #df = train.append(test, ignore_index = True)
    #df.shape
    #print(df)

    train['cleaned_tweet'] = train.tweet.apply(lambda x: ' '.join([word for word in x.split() if not word.startswith('@')]))
    #test['cleaned_tweet'] = test.tweet.apply(lambda x: ' '.join([word for word in x.split() if not word.startswith('@')]))


    #Select all words from normal tweet
    normal_words = ' '.join([word for word in train['cleaned_tweet'][train['label'] == 0]])
    #Collect all hashtags
    pos_htag = [htag for htag in normal_words.split() if htag.startswith('#')]
    #Remove hashtag symbol (#)
    pos_htag = [pos_htag[i][1:] for i in range(len(pos_htag))]
    #Count frequency of each word\
    pos_htag_freqcount = nltk.FreqDist(pos_htag)
    pos_htag_df = pd.DataFrame({'Hashtag' : list(pos_htag_freqcount.keys()),
                           'Count' : list(pos_htag_freqcount.values())})

    #Select top 20 most frequent hashtags and plot them
    most_frequent = pos_htag_df.nlargest(columns="Count", n = 20)
    #plt.figure(figsize=(16,5))
   # ax = sns.barplot(data=most_frequent, x= "Hashtag", y = "Count")
    #ax.set(ylabel = 'Count')
   # plt.show()

    #Repeat same steps for negative tweets
    negative_words = ' '.join([word for word in train['cleaned_tweet'][train['label'] == 1]])
    neg_htag = [htag for htag in negative_words.split() if htag.startswith('#')]
    neg_htag = [neg_htag[i][1:] for i in range(len(neg_htag))]
    neg_htag_freqcount = nltk.FreqDist(neg_htag)
    neg_htag_df=pd.DataFrame({'Hashtag' : list(neg_htag_freqcount.keys()),
                        'Count' : list(neg_htag_freqcount.values())})

    most_frequent = neg_htag_df.nlargest(columns="Count", n = 20)
    #plt.figure(figsize=(16,5))
    #ax = sns.barplot(data=most_frequent, x= "Hashtag", y = "Count")
    #plt.show()

    print(train.head())

    X_train, X_val, y_train, y_val = train_test_split(train['cleaned_tweet'], train['label'], random_state = 0)
    X_train.shape, X_val.shape


    # cv = CountVectorizer()
    # X_train_vectorized = cv.fit_transform(train['cleaned_tweet'])

    cv = CountVectorizer()
    vect = cv.fit(X_train)

    X_train_vectorized = vect.transform(X_train)
   # print(X_train_vectorized)

    # Save the preprocessing object to pickle file
    with open('preprocessing.pkl','wb') as file:
     pickle.dump(cv, file)



    naive_base_model = MultinomialNB()
    naive_base_model.fit(X_train_vectorized, y_train)
    pred = naive_base_model.predict(vect.transform(X_val))
    print('F1 :', f1_score(y_val, pred))

    logistic_model_cv = LogisticRegression()
    logistic_model_cv.fit(X_train_vectorized, y_train)
    pred = logistic_model_cv.predict(vect.transform(X_val))
    print('F1 :', f1_score(y_val, pred))

    with open('preprocessing.pkl','wb') as file:
      pickle.dump(logistic_model_cv, file)



    # Fit the TfidfVectorizer to the training data specifiying a minimum document frequency of 5
    # print('Total Features =', len(vect.get_feature_names()))
    #X_train_vectorized = vect.transform(X_train)


    logistic_model_tf = LogisticRegression()
    logistic_model_tf.fit(X_train_vectorized, y_train)
    pred = logistic_model_tf.predict(vect.transform(X_val))
    print('Accuracy: ', f1_score(y_val, pred))

    with open('model.pkl','wb') as file:
        pickle.dump(logistic_model_cv, file)

       #filename = "gs://akanksha_bucket_1/model.pkl"
      #with tf.io.gfile.GFile(filename, 'wb') as f:
        #pickle.dump(logistic_model_cv, f)
        #red = logistic_model_cv.predict( X_train)

      #storage_client = storage.Client()
      #bucket = storage_client.get_bucket("akanksha_bucket_1")
      #blob = bucket.blob("model.pkl")
     #model_local = "model.pkl"
     #blob.download_to_filename(model_local)
      ## Step 8: Test the model\n",
    pre_processing = pickle.load(open('preprocessing.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))


p = beam.Pipeline(options=options)

lines=\
         (p |"ReadFromFile" >> beam.io.ReadFromText('gs://akanksha_bucket_1/train_E6oV3lV.csv')

           # |"ReadFromFile" >> beam.io.ReadFromText('test_tweets_anuFYb8.csv')
            |'Map record to key' >> beam.Map(lambda record: ('Data', record))
            | 'GroupBy data' >> beam.GroupByKey()
           # | "print data" >> beam.ParDo(printdata)
            |'Build Model' >> beam.ParDo(MLmodel)

# | 'Combine' >> beam.CombineValues(beam.combiners.Dict)
         # | 'Write output to file' >> beam.io.WriteToText('gs://akanksha_bucket_1/TwitterFile3.csv')
          | beam.io.WriteToBigQuery(
                     table_spec, schema=table_schema,
                     write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
                     create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED)
)

p.run()