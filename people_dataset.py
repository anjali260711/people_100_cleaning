import pandas as pd
import re

# Step 1: Load Data
df = pd.read_csv("people-100.csv")
print("Initial Shape:", df.shape)

# Step 2: Deduplication
print("Duplicates before:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("Duplicates after:", df.duplicated().sum())

# Step 3: Handle Missing Values
print("Missing values:\n", df.isna().sum())

# Fill missing Sex with 'Unknown'
if "Sex" in df.columns:
    df["Sex"].fillna("Unknown", inplace=True)

# Drop rows with missing User Id (critical field)
df.dropna(subset=["User Id"], inplace=True)

# Step 4: Date Standardization
if "Date of birth" in df.columns:
    df["Date of birth"] = pd.to_datetime(df["Date of birth"], errors="coerce")

# Step 5: Job Title Normalization
if "Job Title" in df.columns:
    df["Job Title"] = df["Job Title"].str.lower().str.strip()
    df["Job Title"] = df["Job Title"].replace({
        "software eng":"software engineer",
        "s/w engineer":"software engineer",
        "engineer, site":"site engineer",
        "scientist, clinical (histocompatibility and immunogenetics)":"clinical scientist",
        "biochemist, clinical":"clinical biochemist"
    })

# Step 6: Phone Number Cleaning
def clean_phone(phone):
    phone = str(phone)
    phone = re.sub(r"\D", "", phone)   # remove non-digits
    if len(phone) == 10:
        return "+91-" + phone
    elif len(phone) > 10:
        return "+91-" + phone[-10:]    # keep last 10 digits
    return phone

if "Phone" in df.columns:
    df["Phone"] = df["Phone"].apply(clean_phone)

# Step 7: Validation
assert df["User Id"].isna().sum() == 0
assert df.duplicated().sum() == 0

# Step 8: Save Cleaned File
df.to_csv("cleaned_people.csv", index=False)
print("✅ Cleaned dataset saved as cleaned_people.csv")
