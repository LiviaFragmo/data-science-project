# Laptop Pricing: Exploratory Analysis

Course-derived project by Xie Yihan, from CISC7204 Assignment 01 Module 03 Lab 02.

Research question: How do hardware attributes and manufacturer groups relate to laptop prices?

Methods: missing-value treatment, feature conversion, descriptive statistics, histograms, group means, correlations, regression plots, and one-way ANOVA. Manufacturers are named in this course dataset. Associations do not establish causation. The dataset is a limited course sample and cannot represent all current laptop models.

Run: `python -m pip install -r laptop-pricing_requirements.txt`, then `python laptop-pricing_analysis.py`.
The script downloads the course CSV from the URL in its first cell; Internet access is required.
Data provider: IBM Skills Network course resource. The raw CSV is omitted from this public upload package because redistribution permission for this modified course resource has not been independently verified.

Findings from the saved notebook outputs: laptop prices are right-skewed (skewness 1.274); RAM and price correlation is 0.549; manufacturer-group ANOVA p = 0.00313. These are exploratory associations, not adjusted causal estimates.

Charts are existing notebook outputs. Code syntax checked; full rerun remains pending because this environment lacks the plotting/scientific dependencies.
