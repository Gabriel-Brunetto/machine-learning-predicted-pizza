# 🍕 Pizza Price Predictor

A simple Machine Learning application that predicts pizza prices based on pizza diameter using Linear Regression.

## 📌 Project Overview
This project demonstrates the practical application of a supervised Machine Learning model to solve a simple regression problem. The application predicts the price of a pizza based on its diameter (in centimeters) and provides an interactive interface for user input.

The goal of this project is educational, focusing on the integration of data processing, model training, and user interaction through a web interface.

## 🧠 Model Description
A Linear Regression model from the scikit-learn library is used to model the relationship between pizza diameter and price. The model is trained using historical data stored in a CSV file.

## 🚀 Features
- Interactive web interface built with Streamlit  
- Linear Regression model for price prediction  
- Real-time price calculation based on user input  
- Simple and intuitive user interface  

## 🛠️ Technologies Used
- Python 3
- Streamlit
- Pandas
- Scikit-learn

## 📦 Requirements
- Python 3.x
- streamlit
- pandas
- scikit-learn

## 🔧 Installation
```bash
pip install streamlit pandas scikit-learn


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
