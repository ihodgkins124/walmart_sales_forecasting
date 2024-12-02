# Walmart Sales Forecasting

## Project Overview
This is a proof-of-concept machine learning project created to demonstrate the use of Keras Tuner for hyperparameter tuning on a neural network, with the goal of forecasting weekly sales at Walmart. 

To reduce compute time for this demonstration, hyperparameter tuning has been limited to 30 trials. Typically, thousands of trials would be performed in a production setting to find the ideal combination of parameters.

---

## Features

### Simple EDA
- Basic data **summarization** 
- Data **visualization**

### Neural Network Architecture
- The number of **Dense layers** and their units are tuned.
- **Dropout layers** are included for regularization, with the dropout rate being a tunable parameter.
- Different **activation functions** for the layers are evaluated.

### Optimization
- **Learning rate** of the optimizer is tuned.
- The **Hyperband** optimization strategy is used for efficient tuning.

### Metrics
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)

### Callbacks
 - **Early stopping** is implemented to prevent overfitting and save computation.

---

## Technical Approach

### Neural Networks

Neural networks are a fascinating type of machine learning that have garnered a lot of attention in the media for popular adaptations such as chatGPT. These models are composed of a network of perceptrons that process input data to output predictions, similar to that of a brain. Neural networks are known for their flexibility, ability to learn non-linear relationships, and scalability.
This project uses a dense feedforward neural network (FNN).

### Hyperband Tuning

All neural networks contains an array of parameters called hyperparameters that affect the training of the network. Choosing the right hyperparameters such as number of layers, nodes per layer, and activation function can lead to thousands of model combinations. In order to efficiently test thousands of combinations of parameters, a hyperparameter tuner must be used. Some tuners such as a grid search will create a model for every combination and compare them, but this can take vast amounts of time and computational resources. 

A Hyperband can be used to methodically test every combination of parameters while also saving computational resources. The hyperband works by creating a trial for each combination of parameters. It then sets them up in a bracket style playoff where each round, two trials are put up against each other, and the trial with the better metrics moves forward. The first level of the brackets has a very low epoch for each model in order to save time and resources, and it slowly increases with each successive round in the bracket. 

---

## Files in the Repository
- **`notebook.ipynb`**: Jupyter Notebook containing the full implementation, from data preprocessing to hyperparameter tuning and evaluation.
- **`raw_data.py`**: Python script for downloading the Kaggle dataset locally and returning the file path.
- **`README.md`**: Project description and usage instructions.


---

## Requirements

Ensure the following libraries are installed:
- **Python 3**
- `pandas`
- `kagglehub`
- `tensorflow`
- `sklearn`
- `keras`
- `keras_tuner`