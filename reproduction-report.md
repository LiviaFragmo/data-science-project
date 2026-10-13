# Reproduction report — 13 October 2026

Executed in the local validation environment; this is not a claim of compatibility with every platform.

- Housing: descriptive script passed on the original course CSV (21,613 rows; area-price correlation 0.605567).
- Laptop: script executed against a fresh provider CSV (238 records); zero missing values after cleaning; skewness 1.273530, RAM-price correlation 0.549297, ANOVA p 0.00312725. Four PNGs and JSON results generated.
- Dashboard: 528 records; page, layout and dependency endpoints returned HTTP 200; actual Dash update requests produced four non-empty figures for recession and selected yearly reports (1980, 2010, 2023). Year selection disable/enable behavior passed.

Environment: Python 3.14.6, pandas 3.0.3, NumPy 2.4.6, Matplotlib 3.11.0, Seaborn 0.13.2, SciPy 1.18.0, Dash 4.4.1, Plotly 7.1.0.

Changes: replace chained inplace assignments for pandas compatibility; export laptop figures and results; permit local CSV arguments for both projects; download dashboard data from the provider when a local file is absent; clarify research question, main finding and limitation.

These improvements followed self-review and AI assistance. Real classmate feedback and an improvement based on it remain pending.
