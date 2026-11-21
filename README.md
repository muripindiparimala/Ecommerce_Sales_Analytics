# E-Commerce Sales Analytics

A comprehensive data analytics project built for the **EduSkills Internship** using **Python, PostgreSQL, and Power BI**.

---

## 📁 Project Architecture
```
Ecommerce_Sales_Analytics/
├── data/
│   ├── raw/                  # Original raw dataset from EduSkills
│   └── processed/            # Cleaned and validated data files
├── sql/
│   ├── schema/               # DDL scripts (table structures, constraints)
│   ├── queries/              # Analytical SQL queries (KPIs, RFM, cohorts)
│   └── views/                # Views optimized for Power BI import
├── src/                      # Modular Python processing scripts
│   ├── data_ingestion.py     # Loading & validation
│   ├── data_cleaning.py      # Cleansing, type conversion & handling nulls
│   ├── db_connection.py      # SQLAlchemy & PostgreSQL connector
│   └── eda_analysis.py       # Exploratory analysis & KPIs
├── notebooks/                # Interactive exploratory analysis
├── power_bi/                 # Power BI dashboards & DAX documentation
│   ├── reports/
│   └── docs/
├── docs/                     # Project documentation & data dictionaries
├── tests/                    # Pipeline validation tests
├── requirements.txt          # Python library dependencies
└── README.md
```

---

## 🛠️ Tech Stack
* **Python 3.13** (Pandas, NumPy, SQLAlchemy, Seaborn, Matplotlib)
* **PostgreSQL** (Relational Data Modeling & Analytical SQL)
* **Power BI** (Interactive Dashboard, DAX Measures & Data Modeling)
