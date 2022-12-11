from sklearn.model_selection import train_test_split
from pandas import read_csv
from sklearn.linear_model import LinearRegression
import pandas as pd
import joblib
from joblib import dump
data = pd.read_csv('pong_data.csv')
X=data.loc[:,["ball_x","ball_y","ball_vx","ball_vy","paddle_direction"]]
y = data.loc[:,["paddle_y"]].values.reshape(-1,1)
# labels = data.paddle_y.reshape(-1,1)
data.drop(['paddle_y',"Ball.RADIUS","Paddle.L","Paddle.STEP","WIDTH","HEIGHT","BORDER","VELOCITY","FPS"], axis=1, inplace=True)
x_train, x_test, y_train, y_test = train_test_split(data, y, test_size=0.2, shuffle=True)
model = LinearRegression(fit_intercept=True)
model.fit(x_train, y_train)
y = model.predict(x_test)
print(model.score(x_test, y_test))
joblib.dump(model, 'mymodel.joblib')
