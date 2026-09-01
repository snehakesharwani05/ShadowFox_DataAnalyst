# 📊 HR Workforce & Attrition Dashboard

> An interactive **Power BI HR analytics dashboard** designed to explore workforce composition, employee attrition, and the key factors associated with employee turnover.


---

## 📌 Project Overview

The **HR Workforce & Attrition Dashboard** transforms employee-level HR data into an interactive business intelligence solution.

The dashboard enables HR teams and decision-makers to monitor workforce metrics, compare attrition across employee segments, and investigate the factors that may contribute to employee turnover.

The project focuses on three perspectives:

1. **Executive Overview** — a high-level view of workforce and attrition performance.
2. **Workforce Analysis** — demographic and organizational workforce composition.
3. **Attrition Drivers & Risk Analysis** — deeper analysis of factors associated with employee attrition.

---

## 🎯 Objectives

The main objectives of this project are to:

- Measure overall employee attrition.
- Monitor the organization's workforce size and composition.
- Identify departments and job roles with higher attrition.
- Analyze attrition across demographic and workplace factors.
- Understand relationships between employee satisfaction and turnover.
- Examine the effect of overtime, business travel, income, tenure, and other factors.
- Provide interactive filtering for more focused HR analysis.
- Use Power BI's **Key Influencers** visual to identify important attrition-related factors.

---

## 📑 Dashboard Pages

### 1️⃣ Executive Overview

The Executive Overview provides a quick snapshot of the organization's HR situation.

#### Key KPIs

- **Total Employees**
- **Attrition Count**
- **Attrition Rate**
- **Average Monthly Income**
- **Average Tenure**

#### Visual Analysis

- Attrition Rate by Department
- Attrition Rate by Job Role
- Attrition Rate by Age Group
- Attrition Rate by OverTime

#### Interactive Filter

- Department

This page is intended for managers and executives who need a quick understanding of the current workforce and turnover situation.

---

### 2️⃣ Workforce Analysis

The Workforce Analysis page focuses on employee demographics and workforce composition.

#### Key KPIs

- **Total Employees**
- **Average Monthly Income**
- **Average Age**
- **Average Tenure**

#### Visual Analysis

- Employee Count by Department
- Employee Count by Job Role
- Employee Count by Age Group
- Employee Count by Job Level

#### Interactive Filters

- Department
- Gender
- Job Level

This page helps HR teams understand how the workforce is distributed across organizational and demographic categories.

---

### 3️⃣ Attrition Drivers & Risk Analysis

This page focuses on understanding the factors associated with employee turnover.

#### Key KPIs

- **Attrition Count**
- **Attrition Rate**
- **Average Monthly Income**
- **Average Tenure**

#### Risk Factor Analysis

- Attrition Rate by Job Satisfaction
- Attrition Rate by Work-Life Balance
- Attrition Rate by Environment Satisfaction
- Attrition Rate by Job Involvement
- Attrition Rate by OverTime
- Attrition Rate by Business Travel
- Attrition Rate by Marital Status
- Attrition Rate by Distance Band

#### Key Influencers

The **Key Influencers** visual is used to identify employee characteristics associated with a higher likelihood of attrition.

#### Interactive Filters

- Department
- Gender
- Job Level
- OverTime

---

## 📈 Key Metrics

The dashboard contains several calculated HR measures.

### Total Employees

```DAX
Total Employees =
COUNTROWS(EmployeeData)
```

### Attrition Count

```DAX
Attrition Count =
CALCULATE(
    COUNTROWS(EmployeeData),
    EmployeeData[Attrition] = "Yes"
)
```

### Attrition Rate

```DAX
Attrition Rate =
DIVIDE(
    [Attrition Count],
    [Total Employees],
    0
)
```

Additional measures are used for metrics such as:

- Average Age
- Average Monthly Income
- Average Tenure
- Employee Count

> **Note:** The exact measure names and formulas may vary depending on the final Power BI model.

---

## 🛠️ Tools & Technologies

| Technology | Purpose |
|---|---|
| **Microsoft Power BI** | Dashboard development and visualization |
| **Power Query** | Data cleaning and transformation |
| **DAX** | Measures and calculated metrics |
| **Power BI Key Influencers** | Attrition driver analysis |
| **Interactive Slicers** | Dynamic filtering and exploration |

---

## 🗃️ Dataset

The dashboard is based on an employee-level HR dataset containing information related to workforce demographics, employment characteristics, compensation, satisfaction, and attrition.

### Example attributes include:

- Employee demographics
- Age
- Gender
- Department
- Job Role
- Job Level
- Monthly Income
- Years at Company
- Job Satisfaction
- Environment Satisfaction
- Work-Life Balance
- Job Involvement
- Business Travel
- Overtime
- Distance Band
- Marital Status
- Attrition

The primary Power BI table used in the model is:

```text
EmployeeData
```

---

## 🔎 Business Questions

The dashboard helps answer questions such as:

1. What is the overall employee attrition rate?
2. Which departments experience the highest attrition?
3. Which job roles have higher employee turnover?
4. Which age groups show higher attrition?
5. Does overtime appear to be associated with employee attrition?
6. How does job satisfaction relate to turnover?
7. Does work-life balance influence attrition?
8. Does job involvement have a relationship with employee turnover?
9. How does business travel relate to attrition?
10. Which factors are identified as important by the Key Influencers visual?

---

## 💡 Business Value

This dashboard can support HR decision-making by helping organizations:

- Identify high-attrition departments and roles.
- Detect employee segments that may require attention.
- Understand workforce demographics.
- Analyze employee satisfaction patterns.
- Investigate potential retention challenges.
- Compare attrition across multiple employee characteristics.
- Support data-driven workforce planning.
- Prioritize areas for employee retention initiatives.

---

## 🎨 Dashboard Features

### Interactive Analysis

Users can select values in slicers and interact with charts to dynamically filter the dashboard.

### KPI Cards

Important HR metrics are displayed prominently for quick monitoring.

### Comparative Visualizations

Bar and column charts make it easy to compare attrition across departments, roles, satisfaction levels, and other factors.

### Key Influencers

Power BI's Key Influencers visual provides an analytical view of factors associated with employee attrition.

### Multi-Page Design

The dashboard separates executive-level monitoring, workforce composition, and risk analysis into dedicated pages.

---

## 📂 Project Structure

A typical repository structure can be:

```text
HR-Workforce-Attrition-Dashboard/
│
├── PowerBI/
|   └── HR_Attrition_Dashboard.pbix
├── README.md
│
├── dataset/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
└── screenshots/
    ├── executive-overview.png
    ├── workforce-analysis.png
    └── attrition-drivers.png
```

> Update the filenames/folders to match your actual GitHub repository structure.

---

## 📊 Example Dashboard Summary

The current dashboard provides metrics such as:

| Metric | Dashboard Value |
|---|---:|
| Total Employees | ~1K |
| Attrition Count | 237 |
| Attrition Rate | 16.1% |
| Average Monthly Income | 6.50K |
| Average Age | 36.92 |
| Average Tenure | 7.01 |

> Values shown above reflect the current dashboard state and may change when filters are applied.

---


## 📚 Skills Demonstrated

This project demonstrates practical experience with:

- Business Intelligence
- Data Visualization
- Power BI
- Power Query
- DAX
- Data Modeling
- KPI Development
- Interactive Dashboard Design
- Exploratory Data Analysis
- HR Analytics
- Business-Oriented Data Storytelling

---

## 📜 License

This project is intended for **educational, portfolio, and data analytics demonstration purposes**.

If the underlying dataset has its own license or attribution requirements, those terms should be followed separately.

---

**Built with Microsoft Power BI to turn HR data into actionable workforce insights.**


