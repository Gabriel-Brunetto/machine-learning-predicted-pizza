# Pizza Price Predictor

A simple machine learning application that predicts pizza prices based on diameter using linear regression.

## Description

This Streamlit application uses a linear regression model to predict pizza prices based on their diameter in centimeters. The model is trained on data from a CSV file containing pizza diameters and their corresponding prices.

## Features

- Interactive web interface built with Streamlit
- Linear regression model for price prediction
- Real-time price calculation based on user input
- Simple and intuitive UI

## Requirements

- Python 3.x
- streamlit
- pandas
- scikit-learn

## Installation

```bash
pip install streamlit pandas scikit-learn
```

## Usage

1. Ensure you have a `pizzas.csv` file in the same directory with columns: `diametro` and `preco`
2. Run the application:

```bash
streamlit run app.py
```

3. Enter the pizza diameter in centimeters
4. View the predicted price in Brazilian Reais (R$)

## File Structure

```
project-ml/
├── app.py          # Main application file
├── pizzas.csv      # Training data
└── README.md       # This file
```

## How it Works

The application loads pizza data from a CSV file, trains a linear regression model on the diameter-price relationship, and provides an interactive interface for users to input pizza diameters and receive price predictions.
