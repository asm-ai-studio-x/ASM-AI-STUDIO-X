import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
import random

# Data Processing
def load_data(file_path):
    data = pd.read_csv(file_path)
    # Cleaning and preprocessing
    data.dropna(inplace=True)
    return data

def preprocess_data(data):
    # Feature selection
    features = data[['feature1', 'feature2', 'feature3']]
    labels = data['price']
    return features, labels

# Model Training
def train_model(X_train, y_train):
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    return model

# Model Testing
def test_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')
    return mse

# Marketing Content Generation
def generate_marketing_content(predictions):
    content = []
    for price in predictions:
        content.append(f'This property is predicted to be valued at ${price:,.2f}.')
    return content

# Putting it all together
def main():
    data = load_data('housing_data.csv')
    X, y = preprocess_data(data)

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = train_model(X_train, y_train)
    test_model(model, X_test, y_test)

    # Generate content examples
    sample_predictions = model.predict(X_test[:5])
    marketing_content = generate_marketing_content(sample_predictions)
    for content in marketing_content:
        print(content)

    # Save the model
    joblib.dump(model, 'housing_model.pkl')

if __name__ == "__main__":
    main()