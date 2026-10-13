# Automobile Sales Dashboard

Course-derived project by Xie Yihan, CISC7204 Assignment 02 Module 05 Final Lab 02.

**Research question:** How do sales and advertising patterns vary between recession periods and selected years?

**Main finding:** In 528 teaching observations, mean automobile sales are approximately 649 in recession observations and 2,817 in other observations (113 and 415 records).

**Limitation:** This is an instructional dataset; grouped comparisons cannot establish the causal effect of recessions or advertising, or generalize to a real manufacturer.

Methods: pandas aggregation, Plotly charts and Dash callbacks. Recession and yearly reports provide four charts each.

## Reproduce
Verified on Python 3.14.6 with versions pinned in automobile-dashboard_requirements.txt.

```sh
python -m pip install -r automobile-dashboard_requirements.txt
python automobile-dashboard_app.py
```

Open the localhost address printed by Dash. The script uses a neighboring historical_automobile_sales.csv if present; otherwise it reads the [IBM course CSV](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv). To use a locally obtained authorized copy:

```sh
python automobile-dashboard_app.py --data /path/to/historical_automobile_sales.csv --port 8050
```

Validation passed: HTTP page, layout and dependencies, four graph callbacks for recession and yearly reports (1980, 2010, 2023), and report-dependent year selection. See reproduction-report.md.

GitHub Pages displays the portfolio and screenshots. The Python dashboard runs locally or on a compatible Python host. Raw course CSV is not redistributed; modified course resource redistribution permission remains unverified.
