# Laptop Pricing: Exploratory Analysis

Course-derived project by Xie Yihan, from CISC7204 Assignment 01 Module 03 Lab 02.

**Research question:** How do hardware attributes and manufacturer groups relate to laptop prices?

**Main finding:** In 238 records, prices are right-skewed (skewness 1.274), RAM-price correlation is 0.549 and manufacturer-group ANOVA p = 0.00313. These exploratory associations do not establish causation.

**Limitation:** A small teaching sample does not represent current market prices. Manufacturer group sizes differ, and hardware features may confound manufacturer comparisons.

Methods: missing-value treatment, feature conversion, histogram, manufacturer means, correlation heatmap, regression plots and one-way ANOVA.

## Reproduce
Verified on Python 3.14.6 with versions pinned in laptop-pricing_requirements.txt. In a fresh environment, run:

```sh
python -m pip install -r laptop-pricing_requirements.txt
python laptop-pricing_analysis.py
```

Internet access is required to read the [IBM Skills Network CSV](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod1.csv). To use a locally obtained authorized copy:

```sh
python laptop-pricing_analysis.py --data /path/to/laptop.csv --output-dir laptop-results
```

The script saves four PNG figures and results.json in the output directory. The rerun completed, all cleaned missing-value counts were zero, and key results matched prior coursework outputs. See reproduction-report.md for validation.

Raw course CSV is omitted from this public repository because redistribution permission for the modified course resource has not been independently verified. The script reads the provider resource rather than republishing raw data.
