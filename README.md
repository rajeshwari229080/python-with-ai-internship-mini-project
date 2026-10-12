# Student Performance Analytics Using Python

A complete, professional, and beginner-friendly data analytics application built with **Python**, **Pandas**, and **NumPy**. This project demonstrates core Python fundamentals, functions, loops, conditions, CSV dataset validation, analytical computations, statistical summaries, automated unit testing, and structured reporting.

Developed in compliance with the **EWB Courses – Python with AI Project Guidelines**.

---

## 📌 Project Overview & Objectives

Analyzing academic performance and attendance records manually is time-consuming and error-prone. This project provides an automated, locally runnable analytics pipeline that:
- Loads and rigorously validates student records from a CSV file.
- Calculates total marks, percentage averages, educational grade bands, and academic pass/fail results.
- Tracks and flags low attendance independently of academic grades.
- Computes subject-wise, department-wise, and semester-wise statistical metrics using Pandas and NumPy.
- Generates a clean, human-readable terminal report answering 12 critical analytical questions.
- Validates all core calculation logic and edge cases using an automated `unittest` test suite.

---

## 🚀 Key Features

1. **Robust Data Validation**:
   - Detects missing files, empty datasets, duplicate student IDs, missing values, empty strings, and malformed numeric values.
   - Enforces valid academic ranges (marks between 0–100, attendance between 0–100, positive integer semesters).
2. **Standardized Grading & Pass/Fail Logic**:
   - Assigns letter grades (`A+`, `A`, `B`, `C`, `D`, `E`, `F`) based on overall percentage.
   - Applies clear academic pass rule: a student must score $\ge 35$ in all three subjects.
   - Evaluates attendance eligibility ($\ge 75\%$) separately without corrupting academic pass/fail results.
3. **Statistical Aggregations (Pandas & NumPy)**:
   - Computes means, standard deviations, medians, minimums, maximums, and quartiles ($Q_1, Q_2, Q_3$).
   - Evaluates department and semester performance breakdowns.
4. **Resilient Architecture**:
   - Resolves dataset paths dynamically relative to script location.
   - Pure functions that do not mutate input DataFrames.
5. **Comprehensive Unit Testing**:
   - 18 automated unit tests covering all boundary conditions, calculations, ties, and validation errors.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3.11+** | Core programming language, functions, loops, and conditions |
| **Pandas** | DataFrame manipulation, grouping, sorting, filtering, and summaries |
| **NumPy** | High-performance array operations, vector summation, standard deviations, percentiles |
| **unittest** | Automated testing framework for edge cases and grading policies |
| **Pathlib** | OS-independent filesystem path resolution |

*No paid APIs, cloud services, databases, web servers, or machine learning models are required.*

---

## 📁 Repository Structure

```text
student-performance-analytics/
│
├── main.py                     # Main application entry point & CLI reporting
├── functions.py                # Reusable analytical functions and data validation
├── data/
│   └── students.csv            # Synthetic educational dataset (25 student records)
├── tests/
│   └── test_functions.py       # Comprehensive unit tests (18 tests)
├── README.md                   # Project overview, installation, and usage instructions
├── Project_Documentation.md    # 10-section formal academic documentation
├── requirements.txt            # Python dependencies (pandas, numpy)
├── .gitignore                  # Git exclusions for Python cache and virtual environments
└── screenshots/
    └── README.md               # Guide and placeholders for output screenshots
```

---

## 📊 Dataset Schema

The dataset is stored in `data/students.csv` and contains **25 records** across 8 columns:

| Column Name | Data Type | Permitted Range | Description |
|---|---|---|---|
| `student_id` | String | Unique non-empty | Unique student identifier (e.g. S101, S102) |
| `student_name` | String | Non-empty | Student full name (fictional) |
| `department` | String | Non-empty | Academic department (CS, IT, Electronics, Data Science) |
| `semester` | Integer | $\ge 1$ | Current academic semester (e.g. 4, 6) |
| `python_marks` | Float/Int | 0 – 100 | Marks scored in Python programming |
| `mathematics_marks`| Float/Int | 0 – 100 | Marks scored in Mathematics |
| `statistics_marks` | Float/Int | 0 – 100 | Marks scored in Statistics |
| `attendance_percentage` | Float | 0.0 – 100.0 | Overall attendance percentage |

> **Privacy Notice**: This dataset is completely synthetic and generated for educational and analytical purposes. It contains no real personal identifiable information.

---

## 📜 Grading and Academic Policy

### Grade Bands (Based on Overall Average)
- **90% – 100%** : `A+`
- **80% – < 90%** : `A`
- **70% – < 80%** : `B`
- **60% – < 70%** : `C`
- **50% – < 60%** : `D`
- **35% – < 50%** : `E`
- **Below 35%** : `F`

### Academic Pass / Fail Rule
- A student passes an individual subject by scoring $\ge 35$.
- A student achieves an **overall Pass** only if **all three subjects** have marks $\ge 35$. If any subject mark is $< 35$, the overall status is **Fail**.

### Attendance Rule
- Minimum attendance threshold is **75.0%**.
- Students with attendance $< 75.0\%$ are flagged as having low attendance.
- Low attendance is reported separately and does **not** automatically change academic pass/fail status.

---

## 💻 Installation and Setup

### Prerequisites
- Python 3.10 or higher installed on your system.

### Step 1: Clone or Open the Repository
```bash
git clone https://github.com/rajeshwari229080/python-with-ai-internship-mini-project.git
cd python-with-ai-internship-mini-project
```

### Step 2: Create and Activate a Virtual Environment (Recommended on Windows)
```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Step 3: Install Required Dependencies
```powershell
python -m pip install -r requirements.txt
```

---

## 🏃 Execution and Testing

### Run the Main Analytics Application
```powershell
python main.py
```

### Run the Automated Unit Test Suite
```powershell
python -m unittest discover -s tests -v
```

---

## 📈 Verified Program Output & Analytical Findings

When executed against the 25-record dataset in `data/students.csv`, the application computes the following verified results:

```text
================================================================================
      STUDENT PERFORMANCE ANALYTICS SYSTEM
      Powered by Python 3, Pandas, and NumPy
================================================================================
Dataset Path  : data/students.csv
Total Records : 25 students across 4 departments and 2 semesters
```

### Key Statistical Summary
- **Class Academic Pass Rate** : `84.00%` (21 Passed, 4 Failed)
- **Overall Class Average** : `65.35%` (Std Dev: 18.98%, Median: 65.00%)
- **Average Attendance** : `79.00%` (Min: 58.00%, Max: 96.00%)
- **Low Attendance Count** : `6 students` (24.00% of class)

### Answers to the 12 Analytical Questions
1. **Highest Performing Student**: Aarav Sharma (`S101`) with **93.67%** (Grade A+)
2. **Subject with Highest Class Average**: **Statistics** (Average: 67.56%, compared to Python: 64.88%, Math: 63.60%)
3. **Students Passing All Three Subjects**: **21 students**
4. **Students Failing At Least One Subject**: **4 students**
5. **Overall Class Average**: **65.35%**
6. **Class Average Attendance**: **79.00%**
7. **Students with Attendance Below 75%**: 6 students (`S118`, `S119`, `S120`, `S121`, `S123`, `S125`)
8. **Top 5 Students**:
   1. Aarav Sharma (`S101`) – Computer Science – 93.67% (A+)
   2. Diya Patel (`S102`) – Information Technology – 90.33% (A+)
   3. Simran Kaur (`S122`) – Data Science – 90.00% (A+)
   4. Ananya Iyer (`S104`) – Computer Science – 88.00% (A)
   5. Meera Menon (`S124`) – Information Technology – 86.00% (A)
9. **Lowest Performing Student**: Riya Banerjee (`S118`) with **26.00%** (Grade F)
10. **Class Academic Pass Percentage**: **84.00%**
11. **Department Variation**:
    - Highest: **Computer Science** (Average: 72.05%, Pass Rate: 85.71%)
    - Lowest: **Electronics** (Average: 54.44%, Pass Rate: 83.33%)
12. **Distribution Insights**:
    - Interquartile Range ($Q_3 - Q_1$): $82.00\% - 55.00\% = 27.00\%$
    - Distribution reflects a balanced distribution with top performers in high percentiles and identified remediation needs for failing students.

---

## 🧪 Unit Test Verification

The test suite contains 18 tests executed via `unittest`:

```text
Ran 18 tests in 0.195s
OK
```

Tests verify:
- All grade band cutoffs (0, 34.9, 35, 49.9, 50, 59.9, 60, 69.9, 70, 79.9, 80, 89.9, 90, 100) and out-of-range rejection.
- Single-subject failures vs multi-subject passes.
- Correct calculation of totals, averages, and attendance flags.
- Statistical calculations (mean, standard deviation, pass percentage).
- Handling ties in rankings.
- Detection of corrupted CSV inputs (empty files, missing columns, duplicate IDs, negative marks, attendance > 100, non-integer semesters).

---

## 📋 GitHub Submission Checklist

Before submitting your repository link to the EWB evaluation form:
- [x] All source code files (`main.py`, `functions.py`) are committed.
- [x] Dataset `data/students.csv` contains at least 20 valid records.
- [x] Test suite `tests/test_functions.py` is passing.
- [x] `requirements.txt` specifies only required dependencies (`pandas`, `numpy`).
- [x] `.gitignore` prevents `.venv` and `__pycache__` from being pushed.
- [x] Formal `Project_Documentation.md` contains all 10 academic sections.
- [ ] Add your name and student details to `Project_Documentation.md`.
- [ ] Capture real screenshots and save them into `screenshots/`.
- [ ] Push repository to GitHub:
  ```powershell
  git init
  git add .
  git commit -m "feat: complete student performance analytics project"
  git branch -M main
  git remote add origin https://github.com/rajeshwari229080/python-with-ai-internship-mini-project.git
  git push -u origin main
  ```
- [ ] Ensure the repository is set to **Public** so reviewers can access it.

---

## 📄 License & Disclaimer

This project is created for educational purposes as part of the **EWB Courses – Python with AI** program. The dataset is entirely synthetic.
