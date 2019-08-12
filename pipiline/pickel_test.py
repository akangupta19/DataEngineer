pic_out = open('salaries.pickle', 'wb')
pickle.dump(pred, pic_out)
pic_out.close()
# loading a pickle
pickle_in = open('salaries.pickle', 'rb')
regressor = pickle.load(pickle_in)
# print (type(reg))
pred = regressor.predict(pred)

storage_client = storage.Client()
bucket = storage_client.get_bucket("akanksha_bucket_1")
blob = bucket.blob("salary_data2.pkl")
model_local = "salary_data2.pkl"
blob.download_to_filename(model_local)

pkk = pickle.load(open(model_local, 'rb'))
pred = pkk.predict(X_test)
l = [{

    'Years': ''.join(e for e in str(X[0]) if e.isalnum()),
    'Salary': ''.join(e for e in str(pred[0]) if e.isalnum()),

}]