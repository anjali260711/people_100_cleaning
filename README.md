# People Dataset Cleaning & Preprocessing

## 📌 Project Overview
This project demonstrates **data cleaning and preprocessing** techniques on a demographic dataset (`people-100.csv`).  
The dataset contains mixed date formats, inconsistent job titles, missing values, and malformed phone numbers.  
The goal is to transform raw demographic data into a **clean, standardized format** suitable for analytics.

---

## 🛠 Steps Performed
1. **Data Ingestion** – Loaded dataset using Pandas.
2. **Deduplication** – Removed duplicate records.
3. **Missing Values** – Filled missing values (e.g., Sex), dropped rows with missing IDs.
4. **Date Standardization** – Converted mixed date formats into standard datetime.
5. **Job Title Normalization** – Standardized inconsistent job titles.
6. **Phone Number Cleaning** – Converted phone numbers into uniform format (+91-XXXXXXXXXX).
7. **Validation** – Ensured no duplicates or missing IDs remain.
8. **Export** – Saved cleaned dataset as `cleaned_people.csv`.

---

## 📂 Files in Repository
- `people-100.csv` → Raw dataset  
- `people_cleaning.py` → Python script with cleaning workflow  
- `cleaned_people.csv` → Final cleaned dataset  
- `README.md` → Project documentation  

---

## 🎯 Outcome
The final dataset is **clean, consistent, and analysis-ready**, enabling reliable demographic insights such as workforce distribution, job role analysis, and contact validation.

---

## 🚀 Skills Demonstrated
- Python (Pandas, Regex)  
- Data cleaning & preprocessing  
- Handling missing values & duplicates  
- Text normalization & categorical encoding  
- Professional project documentation
