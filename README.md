# Chess Game Outcome Predictor: Project Overview
* Created a tool that predicts the winner (accuracy of .88) of a chess game
* Explored and analyzed a 20,000+ row dataset
* Found optimal hyperparameters for KNN, decision tree, naive bayes, random forest, logistic regression, and gradient boost classifiers using GridSearchCV

# Packages and versions used
* Python 3.9.6
* Pandas 1.3.1
* Numpy 1.19.5
* Scikit-learn 0.24.2
* Matplotlib 3.4.3
* Seaborn 0.11.1

# The Data
Dataset from https://www.kaggle.com/datasnaek/chess

The features included in the dataset were the following:
* Game ID: Lichess gives every game played a unique ID
* Rated: Whether or not the game was rated
* Start time: The time the game started
* End time: The time the game ended
* Number of turns: The total number of turns played per player
* Victory status: How the game was won (checkmate, resignation, runnning out of time)
* Winner: Who won the game
* Increment: The time format played
* White's ID: The player with the white pieces' lichess username
* White's rating: The ELO rating of the player with the white pieces
* Black's ID: The player with the black pieces' lichess username
* Black's rating: The ELO rating of the player with the black pieces
* Moves: The algebraic notation of the moves played in the game

# Exploration
