# 🍽️ Waiter’s Tip Prediction using TensorFlow

## 📌 Project Overview
This project demonstrates a **simple regression model using TensorFlow** to predict the **tip amount** based on the **total bill value**.  
Since people tip **inconsistently**, the relationship is **not a fixed percentage**, making it a realistic machine learning problem.

---

## 🎯 Problem Statement
Given historical data of restaurant bills and corresponding tips, predict the **tip amount for a new bill value**.

**Example:**  
Predict the tip for a **$125 bill**.

---

## 📊 Dataset (Sample Used)

| Bill Amount ($) | Tip ($) |
|-----------------|---------|
| 20  | 2.50 |
| 50  | 5.00 |
| 60  | 7.50 |
| 100 | 11.00 |
| 150 | 16.00 |

---

## 🧠 Core Logic

The relationship between bill amount and tip is **approximately linear**, but not perfectly proportional.

We model it as:

Tip ≈ weight × Bill + bias


This allows the model to handle real-world tipping inconsistency.

---

## 📐 Mathematical Approximation (Baseline Formula)

From observing the trend in the data:

Tip ≈ 0.10 × Bill + 0.4


This formula is used to **compare** against the TensorFlow model’s prediction.

---

## 🤖 Machine Learning Approach

- **Type**: Supervised Learning (Regression)
- **Model**: Single Dense neuron
- **Framework**: TensorFlow (Keras)
- **Loss Function**: Mean Squared Error (MSE)
- **Optimizer**: Adam
- **Epochs**: 500

The model learns:
- **Weight** → how tip increases with bill
- **Bias** → base tipping behavior

---

## 🧪 Prediction Example

**Input**
Bill Amount = $125


**TensorFlow Output**
Predicted Tip ≈ $13.6


---

## 📊 Actual vs Predicted Comparison

| Method | Formula Used | Predicted Tip ($) |
|------|-------------|------------------|
| Manual Linear Formula | `0.10 × 125 + 0.4` | 12.9 |
| TensorFlow Model | Learned weights & bias | **13.6** |

### ✅ Observation
- TensorFlow prediction closely matches the mathematical estimate
- Minor difference exists due to learning from all data points
- Confirms the model learned the correct trend

---

## 📌 Key Takeaways

- Real-world data is noisy and inconsistent
- Machine learning learns patterns instead of fixed rules
- Even a simple linear model can produce meaningful predictions
- TensorFlow automatically optimizes weights using loss minimization

---

## 🚀 Possible Extensions

- Add more features (party size, day, time)
- Visualize regression line
- Use non-linear models
- Train using a full Kaggle tipping dataset
- Deploy as a web application or API

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- NumPy

---

## ✅ Final Result

✔ Model successfully predicts tip amounts  
✔ Prediction for $125 bill ≈ **$13.6**  
✔ Matches real-world intuition and trend analysis
