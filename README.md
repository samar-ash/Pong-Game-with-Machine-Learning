# pongml
ML lab for Pong
Since this is a supervised learning and it has countinious data for the y so I used linear regression model, I got the score of 0.92 and then I applied SVM but my scores was lower so I used the first linear regression model.
x_train, x_test, y_train, y_test = train_test_split(data, y, test_size=0.2, shuffle=True)
model = LinearRegression(fit_intercept=True)
The average length of 3 games played by AI, in seconds is 21 sec.
In fact when the ball plays fast I myself cannot play the game and obviously I cannot train it vry well because I lose exactly in the begining of the game. However, when the speed of ball decrease I can play very well and I get a better result so I can train much better.
So that is why I get 4.15 or 8.23 when the ball plays fast but I get 73.39 sec when the ball plays slowly.
