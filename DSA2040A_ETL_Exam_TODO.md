# DSA 2040A FS 2025 – Mid Semester Exam TODO List
**Course:** Data Warehousing & Mining  
**Instructor:** Austin Odera  
**Total Marks:** 50  
**Submission:** Public GitHub Repository

## Project Overview
Create an ETL pipeline handling 8,000-10,000 rows of data with extraction, transformation, and documentation phases.

## 📁 Project Structure Setup
- [ ] Create main project folder: `ET_Exam_<FirstName>_<IDLast3Digits>/`
- [ ] Create subdirectories:
  - [ ] `data/` - for raw and incremental data files
  - [ ] `transformed/` - for processed data files
- [ ] Create required files:
  - [ ] `etl_extract.ipynb` - extraction notebook
  - [ ] `etl_transform.ipynb` - transformation notebook  
  - [ ] `README.md` - project documentation
  - [ ] `.gitignore` - Git ignore file

## 🗂️ Data Source Selection & Acquisition
### Option 1: Real-World Dataset (Recommended)
- [ ] Choose dataset from approved sources:
  - [ ] Kaggle Datasets
  - [ ] data.gov
  - [ ] Our World in Data
  - [ ] UCI Machine Learning Repository
- [ ] Verify dataset has ≥8,000 rows
- [ ] Consider suggested themes:
  - [ ] Online Retail/Sales Transactions
  - [ ] COVID-19 Statistics/Vaccinations
  - [ ] Education Performance/Student Scores
  - [ ] Social Media Analytics
  - [ ] Environmental/Weather Data
- [ ] Download main dataset as `raw_data.csv`
- [ ] Create incremental subset as `incremental_data.csv`

### Option 2: Synthetic Dataset (Alternative)
- [ ] Generate ≥8,000 rows with 8-12 columns using:
  - [ ] Mockaroo
  - [ ] Python faker library
  - [ ] Excel random data generator
- [ ] Include realistic fields: customer_id, product, quantity, unit_price, order_date, region, payment_method, category
- [ ] Save as `raw_data.csv` and create `incremental_data.csv`

## 📊 EXTRACT Phase (20 Marks) - etl_extract.ipynb
- [ ] **Data Loading**
  - [ ] Load both datasets using Pandas
  - [ ] Display `.head()` for both datasets
  - [ ] Display `.info()` for both datasets
  - [ ] Display `.describe()` for both datasets

- [ ] **Data Quality Assessment**
  - [ ] Identify and document ≥3 data quality issues:
    - [ ] Null values analysis
    - [ ] Duplicate records detection
    - [ ] Inconsistent data types
    - [ ] Other quality issues (outliers, formatting, etc.)
  - [ ] Document findings with explanations

- [ ] **Data Integration**
  - [ ] Merge datasets if relevant (e.g., append incremental records)
  - [ ] Explain merging rationale and methodology
  - [ ] Validate merged dataset integrity

- [ ] **Data Validation & Storage**
  - [ ] Save validated copies to `/data/` directory
  - [ ] Add comprehensive markdown cells explaining each observation
  - [ ] Ensure notebook is well-commented and documented

## 🔄 TRANSFORM Phase (30 Marks) - etl_transform.ipynb
- [ ] **Apply ≥5 Transformations from ≥3 Categories:**

### Cleaning Category
- [ ] Handle missing values (imputation, removal, etc.)
- [ ] Remove duplicate records
- [ ] Fix data inconsistencies

### Standardization Category  
- [ ] Rename columns for consistency
- [ ] Fix case formatting (upper/lower/title case)
- [ ] Standardize units of measurement
- [ ] Format dates consistently

### Enrichment Category
- [ ] Add derived columns (e.g., total_cost = quantity * unit_price)
- [ ] Calculate aggregated metrics
- [ ] Create computed fields

### Structural Category
- [ ] Convert data types appropriately
- [ ] Split combined columns
- [ ] Combine related columns

### Filtering Category
- [ ] Drop irrelevant rows
- [ ] Remove unnecessary columns
- [ ] Filter based on business rules

### Categorization Category
- [ ] Create bins or tiers (age groups, sales brackets)
- [ ] Generate categorical variables
- [ ] Create classification labels

- [ ] **Documentation & Output**
  - [ ] Show before & after for each transformation
  - [ ] Explain rationale for each transformation
  - [ ] Save final outputs:
    - [ ] `transformed_full.csv` in `/transformed/`
    - [ ] `transformed_incremental.csv` in `/transformed/`
  - [ ] Ensure notebook runs end-to-end without manual intervention

## 📝 README.md Documentation (2 Marks)
- [ ] **Project Overview** - Summary of exam project objectives
- [ ] **Data Source** - Dataset link and brief description
- [ ] **ET Phases** - Detailed explanation of extract & transform processes
- [ ] **Tools Used** - Python, Pandas, Jupyter, other libraries
- [ ] **Steps to Run the Project** - Clear execution instructions
- [ ] **Sample Outputs/Screenshots** - Visual documentation of results
- [ ] Professional formatting and clear writing

## 🐙 GitHub Repository Setup (3 Marks)
- [ ] Create public repository: `DSA2040A_ET_Exam_<FirstName>_<ID3>`
- [ ] Initialize repository with proper structure
- [ ] Create meaningful `.gitignore` file
- [ ] Make logical, well-documented commits
- [ ] Ensure repository is clean and organized
- [ ] Test reproducibility by cloning and running notebooks
- [ ] Submit repository link on Blackboard/LMS

## ✅ Quality Assurance Checklist
- [ ] Both notebooks run completely without errors
- [ ] All file paths are relative and work across systems
- [ ] Data files are properly saved in correct directories
- [ ] All transformations are clearly documented
- [ ] Code is well-commented and readable
- [ ] README.md is comprehensive and professional
- [ ] Repository structure matches requirements exactly
- [ ] All required files are present and named correctly

## 🎯 Bonus Opportunities (+3 Marks)
- [ ] Choose exceptional/unique dataset
- [ ] Implement insightful transformations
- [ ] Add meaningful data visualizations
- [ ] Demonstrate advanced analytical thinking
- [ ] Show creative problem-solving approaches

## 📋 Final Submission Checklist
- [ ] Verify dataset has ≥8,000 rows
- [ ] Confirm ≥5 transformations from ≥3 categories
- [ ] Test notebook reproducibility
- [ ] Review README.md completeness
- [ ] Check GitHub repository accessibility
- [ ] Submit repository link on LMS
- [ ] Verify submission before deadline

---
**Important Notes:**
- Focus on data quality and meaningful transformations
- Document everything thoroughly with markdown cells
- Ensure reproducibility across different environments
- Professional presentation and clear explanations are crucial
- Test your notebooks multiple times before submission