# DSA 2040A FS 2025 – Mid Semester Exam TODO List
**Course:** Data Warehousing & Mining  
**Instructor:** Austin Odera  
**Total Marks:** 50  
**Submission:** Public GitHub Repository

## Project Overview
Create an ETL pipeline handling 8,000-10,000 rows of data with extraction, transformation, and documentation phases.

## 📁 Project Structure Setup
- [x] Create main project folder: `ET_Exam_<FirstName>_<IDLast3Digits>/` (using current directory)
- [x] Create subdirectories:
  - [x] `data/` - for raw and incremental data files
  - [x] `transformed/` - for processed data files
- [x] Create required files:
  - [x] `etl_extract.ipynb` - extraction notebook
  - [x] `etl_transform.ipynb` - transformation notebook  
  - [x] `README.md` - project documentation
  - [x] `.gitignore` - Git ignore file

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
- [x] Generate ≥8,000 rows with 8-12 columns using:
  - [ ] Mockaroo
  - [x] Python faker library
  - [ ] Excel random data generator
- [x] Include realistic fields: customer_id, product, quantity, unit_price, order_date, region, payment_method, category
- [x] Save as `raw_data.csv` and create `incremental_data.csv`

## 📊 EXTRACT Phase (20 Marks) - etl_extract.ipynb
- [x] **Data Loading**
  - [x] Load both datasets using Pandas
  - [x] Display `.head()` for both datasets
  - [x] Display `.info()` for both datasets
  - [x] Display `.describe()` for both datasets

- [x] **Data Quality Assessment**
  - [x] Identify and document ≥3 data quality issues:
    - [x] Null values analysis
    - [x] Duplicate records detection
    - [x] Inconsistent data types
    - [x] Other quality issues (outliers, formatting, etc.)
  - [x] Document findings with explanations

- [x] **Data Integration**
  - [x] Merge datasets if relevant (e.g., append incremental records)
  - [x] Explain merging rationale and methodology
  - [x] Validate merged dataset integrity

- [x] **Data Validation & Storage**
  - [x] Save validated copies to `/data/` directory
  - [x] Add comprehensive markdown cells explaining each observation
  - [x] Ensure notebook is well-commented and documented
  - [x] Create detailed documentation report in `/documentation/` folder

## 🔄 TRANSFORM Phase (30 Marks) - etl_transform.ipynb
- [x] **Apply ≥5 Transformations from ≥3 Categories:** (6 transformations, 4 categories)

### Cleaning Category
- [x] Handle missing values (imputation, removal, etc.)
- [x] Remove duplicate records
- [x] Fix data inconsistencies

### Standardization Category  
- [x] Rename columns for consistency
- [x] Fix case formatting (upper/lower/title case)
- [x] Standardize units of measurement
- [x] Format dates consistently

### Enrichment Category
- [x] Add derived columns (e.g., total_cost = quantity * unit_price)
- [x] Calculate aggregated metrics
- [x] Create computed fields

### Structural Category
- [x] Convert data types appropriately
- [x] Split combined columns
- [x] Combine related columns

### Filtering Category
- [x] Drop irrelevant rows
- [x] Remove unnecessary columns
- [x] Filter based on business rules

### Categorization Category
- [x] Create bins or tiers (age groups, sales brackets)
- [x] Generate categorical variables
- [x] Create classification labels

- [x] **Documentation & Output**
  - [x] Show before & after for each transformation
  - [x] Explain rationale for each transformation
  - [x] Save final outputs:
    - [x] `transformed_full.csv` in `/transformed/`
    - [x] `transformed_incremental.csv` in `/transformed/`
  - [x] Ensure notebook runs end-to-end without manual intervention

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
- [x] Initialize repository with proper structure
- [x] Create meaningful `.gitignore` file
- [ ] Make logical, well-documented commits
- [ ] Ensure repository is clean and organized
- [ ] Test reproducibility by cloning and running notebooks
- [ ] Submit repository link on Blackboard/LMS

## ✅ Quality Assurance Checklist
- [x] Both notebooks run completely without errors
- [x] All file paths are relative and work across systems
- [x] Data files are properly saved in correct directories
- [x] All transformations are clearly documented
- [x] Code is well-commented and readable
- [ ] README.md is comprehensive and professional
- [x] Repository structure matches requirements exactly
- [x] All required files are present and named correctly

## 🎯 Bonus Opportunities (+3 Marks)
- [x] Choose exceptional/unique dataset (comprehensive synthetic e-commerce data)
- [x] Implement insightful transformations (6 transformations with business value)
- [x] Add meaningful data visualizations (distribution plots, outlier analysis)
- [x] Demonstrate advanced analytical thinking (customer segmentation, business categories)
- [x] Show creative problem-solving approaches (outlier handling, categorical enrichment)

## 📋 Final Submission Checklist
- [x] Verify dataset has ≥8,000 rows (10,050 rows generated)
- [x] Confirm ≥5 transformations from ≥3 categories (6 transformations, 4 categories)
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