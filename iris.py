import pandas as pd
import numpy as np
import pickle

df = pd.read_csv('iris.data')

# X=pd.drop("PCOS level",axis=1)
# y=pd["PCOS level"]
# pd.dropna(axis=1,inplace=True)

X = np.array(df.iloc[:, :13])
y = np.array(df.iloc[:, 13:])

# from sklearn.preprocessing import LabelEncoder
# le = LabelEncoder()
# y = le.fit_transform(y.reshape(-1))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.ensemble import RandomForestClassifier
# sv = SVC(kernel='linear').fit(X_train,y_train)

clf = RandomForestClassifier(n_estimators = 1000) 
clf.fit(X_train,np.ravel(y_train,order="C"))

pickle.dump(clf, open('iri.pkl', 'wb'))
