# Extract Phase Documentation Report

**DSA 2040A - Data Warehousing & Mining Mid Semester Exam**


---

##  Executive Summary

The Extract phase successfully processed and validated two datasets containing e-commerce transaction data. A total of **11,557 records** were extracted, profiled, and integrated, with comprehensive data quality assessment identifying three major issues requiring attention in the transformation phase.

---

##  Dataset Overview

### Raw Data Analysis
- **Records:** 10,050 rows × 8 columns
- **Memory Usage:** 3.55 MB
- **Date Range:** 2023-10-24 to 2025-10-22 (729 days)
- **Unique Customers:** 9,504
- **Product Categories:** 10 distinct categories

### Incremental Data Analysis
- **Records:** 1,507 rows × 8 columns
- **Memory Usage:** 0.53 MB
- **Contains:** Most recent transaction records
- **Unique Customers:** 1,489
- **Overlap with Raw Data:** 1,499 records (99.5%)

### Combined Dataset
- **Total Records:** 11,557 rows × 8 columns
- **Integration Method:** Append incremental to raw data
- **Validation:**  Row count matches expected (10,050 + 1,507)
- **Schema Compatibility:**  All columns match perfectly

---

##  Data Quality Assessment

### Issue #1: Missing Values (Nulls)
**Severity:** Medium | **Impact:** Data Completeness

#### Raw Data Missing Values:
| Column         | Missing Count | Missing Percentage |
| -------------- | ------------- | ------------------ |
| category       | 67            | 0.67%              |
| region         | 68            | 0.68%              |
| payment_method | 66            | 0.66%              |

#### Incremental Data Missing Values:
| Column         | Missing Count | Missing Percentage |
| -------------- | ------------- | ------------------ |
| category       | 7             | 0.46%              |
| region         | 5             | 0.33%              |
| payment_method | 13            | 0.86%              |

**Total Missing Values:** 226 across both datasets (~2% of all data points)

### Issue #2: Duplicate Records
**Severity:** Medium | **Impact:** Data Accuracy

- **Raw Data Duplicates:** 48 exact duplicate records
- **Incremental Data Duplicates:** 7 exact duplicate records
- **Overlapping Records:** 1,499 records appear in both datasets (99.5% overlap)
- **Total Duplicate Impact:** ~0.5% duplicate rate in individual datasets

### Issue #3: Data Type Inconsistencies
**Severity:** High | **Impact:** Data Processing & Analysis

#### Formatting Issues Identified:
1. **Customer ID Inconsistencies:**
   - 100 customer IDs with lowercase formatting (e.g., "cust_57057" instead of "CUST_57057")
   - Should follow standard format: "CUST_XXXXX"

2. **Date Type Issues:**
   - Order dates stored as object type instead of datetime
   - Prevents proper date-based operations and sorting

3. **Numerical Outliers:**
   - **Quantity Outliers:** 388 records with extreme values (7-964 units)
   - **Price Outliers:** 893 records with extreme prices ($766.93-$1,995.19)
   - Normal range: Quantity (1-6), Price ($3.05-$766.90)

---

##  Statistical Insights

### Data Distribution Summary:
- **Average Quantity per Order:** 2.98 units
- **Average Unit Price:** $267.03
- **Most Popular Category:** Toys & Games (1,030 occurrences)
- **Most Active Region:** Africa (2,516 transactions)
- **Preferred Payment Method:** Bank Transfer (1,173 transactions)

### Product Categories Distribution:
1. Electronics
2. Clothing  
3. Home & Garden
4. Sports & Outdoors
5. Books
6. Health & Beauty
7. Toys & Games
8. Automotive
9. Food & Beverages
10. Office Supplies

### Regional Distribution:
- Africa: 2,516 transactions
- North America: High activity
- Europe: Significant presence
- Asia Pacific: Active market
- Latin America: Growing segment
- Middle East: Emerging market

---

##  Data Integration Process

### Integration Strategy
**Method:** Append incremental data to raw data  
**Rationale:** Incremental dataset represents newer transactions that should be added to create a complete transaction history.

### Integration Results
-  **Schema Compatibility:** All columns match between datasets
-  **Row Count Validation:** Combined total matches expected (11,557)
-  **Overlap Warning:** 99.5% of incremental data overlaps with raw data
-  **Date Range Validation:** Continuous 2-year transaction history

### Files Generated
1. `data/validated_raw_data.csv` - Original raw dataset
2. `data/validated_incremental_data.csv` - Incremental dataset  
3. `data/validated_combined_data.csv` - Merged complete dataset
4. `data/extraction_quality_report.csv` - Quality metrics and metadata

---

##  Key Findings & Recommendations

### Critical Findings:
1. **High Data Overlap:** 99.5% overlap between raw and incremental suggests incremental data may not be truly "new" records
2. **Consistent Missing Patterns:** Missing values concentrated in categorical fields (category, region, payment_method)
3. **Extreme Outliers Present:** Significant outliers in quantity (up to 964 units) and pricing (up to $1,995) require investigation
4. **Formatting Inconsistencies:** Customer ID standardization needed

### Recommendations for Transform Phase:
1. **Immediate Actions:**
   - Remove exact duplicate records
   - Standardize customer ID formatting to uppercase
   - Convert order_date to proper datetime format

2. **Data Cleaning:**
   - Implement missing value imputation strategy
   - Flag or remove extreme outliers
   - Validate business rules for quantity and pricing

3. **Data Enhancement:**
   - Add calculated fields (total_cost = quantity × unit_price)
   - Create date-based features (year, month, quarter)
   - Implement categorical binning for analysis

---

##  Extract Phase Completion Checklist

-  **Data Loading:** Both datasets loaded successfully with error handling
- **Data Profiling:** Complete .head(), .info(), .describe() analysis performed
-  **Quality Assessment:** 3+ major data quality issues identified and documented
-  **Data Integration:** Successful merge with validation and overlap analysis
-  **Data Storage:** Validated datasets saved with comprehensive quality report
-  **Documentation:** Detailed findings documented with visualizations

---

##  Quality Metrics Summary

| Metric                      | Value         |
| --------------------------- | ------------- |
| **Total Records Processed** | 11,557        |
| **Data Completeness**       | 98.0%         |
| **Duplicate Rate**          | 0.5%          |
| **Schema Consistency**      | 100%          |
| **Date Range Coverage**     | 729 days      |
| **Processing Time**         | < 2 minutes   |
| **Memory Efficiency**       | 4.08 MB total |

---

##  Next Phase Preparation

**Transform Phase Requirements:**
- Address all identified data quality issues
- Implement 5+ transformations across 3+ categories
- Create before/after documentation for each transformation
- Generate clean, analysis-ready datasets

**Priority Transformations Needed:**
1. **Cleaning:** Handle missing values, remove duplicates
2. **Standardization:** Fix formatting, convert data types
3. **Enrichment:** Add calculated fields and derived metrics
4. **Filtering:** Handle outliers and invalid records
5. **Categorization:** Create business-relevant groupings

---

**Report Generated:** October 23, 2025, 3:09 PM  
**Phase Status:**  Extract Complete - Ready for Transform Phase