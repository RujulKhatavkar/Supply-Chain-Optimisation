# 📦 Supply Chain Optimization with Demand Forecasting

## 🚀 Overview  
This project focuses on optimizing supply chain operations using **machine learning-driven demand forecasting**. By predicting weekly sales across multiple stores, the system enables better inventory planning, reduces stockouts, and improves overall operational efficiency.

The model leverages historical retail data and advanced analytics to provide **data-driven insights for smarter supply chain decisions**.

---

## 🎯 Objectives  
- Predict **weekly sales** for retail stores using historical data  
- Improve **inventory management and demand planning**  
- Identify **key drivers influencing sales performance**  
- Enable **data-driven decision-making** in supply chain operations  

---

## 🧠 Approach  

### 1. Data Processing  
- Merge multiple datasets containing store info, features, and sales  
- Clean and preprocess data for modeling  

### 2. Feature Engineering  
- Incorporate factors such as:  
  - Promotions  
  - Holidays  
  - Store type  
  - External conditions  

### 3. Model Development  
- Use **Random Forest Regressor** for prediction  
- Train on historical sales data  
- Evaluate model performance using regression metrics  

### 4. Insights & Visualization  
- Analyze feature importance  
- Visualize trends and seasonal patterns  
- Derive actionable business insights  

---

## 📊 Dataset  

The project uses four datasets:  

| File | Description |
|------|------------|
| `features.csv` | Store-level features like promotions, holidays, etc. |
| `stores.csv` | Store metadata (type, size, etc.) |
| `train.csv` | Historical sales data for training |
| `test.csv` | Data used for model evaluation |

---

## 🗂️ Project Structure  

Supply-Chain-Optimisation/
│
├── Supply_Chain_Opt.py # Main script for modeling
├── features.csv # External features dataset
├── stores.csv # Store information
├── train.csv # Training dataset
├── test.csv # Testing dataset
└── README.md # Project documentation


---

## ⚙️ Installation  

```bash
git clone https://github.com/RujulKhatavkar/Supply-Chain-Optimisation.git
cd Supply-Chain-Optimisation
pip install -r requirements.txt
```

## ▶️ Usage

Run the main script:

python Supply_Chain_Opt.py

## 📈 Key Outcomes
Accurate weekly sales predictions
Improved inventory optimization
Insights into sales drivers (seasonality, promotions, etc.)
Better supply chain efficiency and planning

## 🛠️ Tech Stack
Python
Pandas, NumPy
Scikit-learn (RandomForestRegressor)
Matplotlib / Seaborn

## 🔮 Future Improvements
Implement advanced models (XGBoost, LSTM)
Add real-time forecasting pipeline
Deploy as a web dashboard or API
Integrate optimization algorithms for logistics

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo, create a branch, and submit a pull request.

## 📜 License

This project is open-source and available under the MIT License.
