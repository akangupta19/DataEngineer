df = pd.DataFrame(data, columns=('YearsExperience', 'Salary'))
    df=df.iloc[1:,:]
    X=df[('YearsExperience')].values
    y=df[('Salary')].valuesl
