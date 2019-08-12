dataset = pd.read_csv('Salary_Data.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 1].values
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    pred=regressor.predict(X_test)
    return pred


    data = data[1]
    df = pd.DataFrame(data, columns=('YearsExperience', 'Salary'))
    df = df.iloc[1:, :]
    x = df[['YearsExperience']].values

    y = df[['Salary']].values
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
    from sklearn.linear_model import LinearRegression
    regresor = LinearRegression()
    regresor.fit(x_train, y_train)
    pred = regresor.predict(x_test)
    # return pred

storage_client = storage.Client()
bucket = storage_client.get_bucket("akanksha_bucket_1")
blob = bucket.blob("salary_data.pkl")
model_local = "salary_data.pkl"
blob.download_to_filename(model_local)

pickle_in = open('salary_data.pkl', 'rb')
regressor = pickle.load(pickle_in)
# print (type(reg))
pre = regressor.predict(X_test)
print(pre)
