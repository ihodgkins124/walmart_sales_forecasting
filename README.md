# Walmart Sales Forecasting

## Project Overview
This is a **proof-of-concept machine learning project** created to demonstrate the use of **Keras Tuner** for hyperparameter tuning on a neural network, with the goal of forecasting weekly sales at Walmart. 

To reduce compute time for this demonstration, hyperparameter tuning has been limited to **30 trials**. Typically, thousands of trials would be performed in a production setting to find the ideal combination of parameters.

---

## Features

### Neural Network Architecture
- The number of **Dense layers** and their units are tuned.
- **Dropout layers** are included for regularization, with the dropout rate being a tunable parameter.
- Different **activation functions** for the layers are evaluated.

### Optimization
- **Learning rate** of the optimizer is tuned.
- The **Hyperband** optimization strategy is used for efficient tuning.

### Metrics
- **Loss**: Mean Squared Error (MSE)
- **Metrics**:
  - Root Mean Squared Error (RMSE)
  - Mean Absolute Error (MAE)

### Callbacks
- **Early stopping** is implemented to prevent overfitting and save computation.

---

## How It Works

### 1. Model Building:
The model architecture is defined in the `model_builder` function. Hyperparameters such as:
- Number of units,
- Activation functions,
- Dropout rates,
- Learning rate 

are specified as tunable variables.

### 2. Hyperparameter Tuning:
**Keras Tuner's Hyperband algorithm** is used to efficiently search for the best combination of hyperparameters within a predefined search space.

### 3. Model Training:
Once the best hyperparameters are identified, the final model is trained for the **optimal number of epochs**.

### 4. Evaluation:
The model is evaluated on a test dataset using:
- **Root Mean Squared Error (RMSE)**
- **Mean Absolute Error (MAE)**
- **Loss metrics**

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

