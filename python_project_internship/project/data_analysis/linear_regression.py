import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score

df = pd.read_csv("house_rent_data.csv")

le = LabelEncoder()
df['LocationIndex'] = le.fit_transform(df['Location'])

# define features and target variable
X = df[["Size_sqft", "Bedrooms","LocationIndex"]]
y = df["Rent_INR"]

#split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#train the linear model
model = LinearRegression()
model.fit(X_train, y_train)

# make predictions
pred = model.predict(X_test)
print("R2 Score:", r2_score(y_test, pred))

# # compare actual vs predicted
compare_df = pd.DataFrame({'Actual': y_test, 'Predicted': pred.astype(int)})
print("\nActual vs Prediction:\n", compare_df.head(10))

# predict rent for a new data point
new_location = 'Mumbai'
new_location_index = le.transform([new_location])[0]
new_data = [[1200, 3,new_location_index]]  # Size_sqft, Bedrooms, LocationIndex
predict = model.predict(new_data)
print(f"\nPredicted Rent for a data in {predict}")