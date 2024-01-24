import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import joblib

hitters = pd.read_csv('cards/data/hitters.csv')
pitchers = pd.read_csv('cards/data/pitchers.csv')

# synthetic WAR data hitters
hitters['war_last_year'] = hitters['WAR'] + np.random.uniform(-0.5, 0.5, size=len(hitters))
hitters['war_year_before_last'] = hitters['war_last_year'] + np.random.uniform(-.5, .5, size=len(hitters))

# synthetic WAR data pitchers
pitchers['war_last_year'] = pitchers['WAR'] + np.random.uniform(-0.5, 0.5, size=len(pitchers))
pitchers['war_year_before_last'] = pitchers['war_last_year'] + np.random.uniform(-.5, .5, size=len(pitchers))

# random forest for hitters and pitchers
for group, name in [(hitters, 'hitters'), (pitchers, 'pitchers')]:
    features = group[['war_last_year', 'war_year_before_last']]
    labels = group['WAR']
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    model_rf = RandomForestRegressor(n_estimators=100, random_state=42)
    model_rf.fit(X_train, y_train)
    predictions_rf = model_rf.predict(X_test)
    
    mse_rf = mean_squared_error(y_test, predictions_rf)
    print(f"Mean Squared Error for {name}: {mse_rf}")
    joblib.dump(model_rf, f'war_prediction_model_{name}_rf.pkl')
