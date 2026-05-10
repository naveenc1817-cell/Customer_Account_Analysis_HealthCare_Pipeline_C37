# Customer_Account_Analysis_HealthCare_Pipeline_C37
# Healthcare Patient Data Pipeline

## Project Overview
This project demonstrates an end-to-end healthcare data engineering pipeline using Azure cloud technologies.

The solution includes:
- Raw patient data ingestion into ADLS
- Data transformation using Azure Databricks and PySpark
- Cleaned healthcare data storage in Azure SQL Database
- Validation and analytics

---

## Technologies Used
- Azure Data Lake Storage Gen2
- Azure Databricks
- PySpark
- Azure SQL Database
- Azure Data Factory

---

##Repository Structure

```text
Documentation/
Code/
Screenshots/
README.md
```

---

## Project Workflow

Raw CSV → ADLS Raw → Databricks Cleaning → Silver Layer → Azure SQL Database

---

## Validation Performed
- Removed NULL values
- Removed duplicates
- Fixed invalid Age and Cost values
- Standardized patient names
- Verified SQL loads

---

## Contributor
Naveen
