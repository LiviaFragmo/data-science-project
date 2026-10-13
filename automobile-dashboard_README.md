# Automobile Sales Dashboard

Course-derived project by Xie Yihan, CISC7204 Assignment 02 Module 05 Final Lab 02.

Research question: How do automobile sales and advertising patterns vary between recession periods and selected years?

Methods: pandas aggregation, Plotly visualizations and Dash callbacks. Two report modes provide four charts each.

Run `python -m pip install -r automobile-dashboard_requirements.txt`; obtain `historical_automobile_sales.csv` from the [IBM course resource](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv), place it next to `automobile-dashboard_app.py`, then run `python automobile-dashboard_app.py` and open the localhost address shown.

In the local course CSV, average sales are approximately 649 during recession observations and 2,817 during other observations (113 and 415 records). The dashboard supports exploring this difference by vehicle type and year. These observations describe the teaching dataset and should not be generalized to a real manufacturer.

Raw course data is not redistributed here; its usage permissions must be verified before public release. Screenshots show prior course runs. Syntax checked; interactive rerun remains pending. Aggregated descriptive patterns cannot establish the causal effect of recessions or advertising. GitHub Pages serves the portfolio and screenshots; the Python dashboard must run locally or on a Python-capable host.
