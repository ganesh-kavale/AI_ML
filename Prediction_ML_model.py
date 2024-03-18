import pandas as pd
from sklearn.ensemble import RandomForestClassifier


#Take data set as you want either in csv or like this for test 
data = {
    'ID': [1, 2, 3, 4, 5],
    'Client1': [0.1, 0.3, 0.2, 0.6, 0.7],
    'Client2': [0.5, 0.6, 0.4, 0.13, 0.2],
    'Client3': [0.8, 0.7, 0.9, 0.2, 1],
    'Type': ['IT', 'ROBOTICS', 'AI_ML', 'Gaming', 'SAP']
}

# Create Yours DataFrame
df = pd.DataFrame(data)

# Train your model, train means model which you have trained and testData for testing the model.
X_train = df[['Client1','Client2','Client3']]
y_train = df['Type']
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# New data point to predict
# testData = {

#     'Client1': [0.7],
#     'Client2': [0.2],
#     'Client3': [1]
# }

# Take input from the user
testData = {}
testData['Client1'] = [float(input("Enter Client1 value: "))]
testData['Client2'] = [float(input("Enter Client2 value: "))]
testData['Client3'] = [float(input("Enter Client3 value: "))]

# New data point to predict. so you need to match results for given input only
# testData = {
#     'ID': [6],
#     'Client2': [0.2]
# }

new_df = pd.DataFrame(testData)

# Predict the species for the new data point
# X_new = new_df[['Client2']]
# predictedType = clf.predict(X_new)
# print("Display result - Predicted Type:", predictedType)

# Check if new_data matches any existing data point
matching_data = df[(df['Client1'] == testData['Client1'][0]) &
                   (df['Client2'] == testData['Client2'][0]) &
                   (df['Client3'] == testData['Client3'][0])]
                   

if not matching_data.empty:
    # If matching data is found, make predictions
    X_new = new_df[['Client1','Client2','Client3']]
    predictedType = clf.predict(X_new)
    print("Display result - Predicted Type:", predictedType)

else:
    print("No matching data found.")



















