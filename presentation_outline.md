# Presentation: SpaceX Falcon 9 First-Stage Landing Prediction
**Malvika Pathak | 30 October 2026**

## Slide 1 — Title
SpaceX Falcon 9 First-Stage Landing Prediction. Student, course, date.

## Slide 2 — Executive Summary
State the business question, data sources, analytical methods, best measured model, and 2–3 key findings. Fill in model/EDA numbers from your executed notebook.

## Slide 3 — Introduction and Business Problem
Explain reusability and why predicting landing outcome can support launch-cost and bid planning. Define the target label exactly as used in the course data.

## Slide 4 — Methodology Overview
API collection → web scraping → wrangling → EDA/SQL → visualizations → Folium → Dash → classification and evaluation.

## Slide 5 — Data Collection: SpaceX API
Show API GET request workflow, JSON normalization, Falcon 9 filtering, relevant fields, missing-value treatment, and a screenshot/output from your notebook. Add the course/GitHub URL required by the rubric.

## Slide 6 — Data Collection: Web Scraping
Show request + BeautifulSoup parsing workflow, the launch-history table, extracted columns, and a screenshot/output. Add the GitHub URL required by the rubric.

## Slide 7 — Data Wrangling
Explain date/type conversion, missing-value handling, duplicate/category checks, binary target, and one-hot encoding. Include before/after dimensions and missing-value summary from actual output.

## Slide 8 — EDA with Visualization
Insert generated figures: landing class counts, success proportion by launch site, success by orbit, payload by class, flight number vs class. Describe actual patterns and sample sizes.

## Slide 9 — EDA with SQL
Include queries and outputs for unique launch sites, launch counts by site, min/max payload mass, and mission outcome counts. Explain one meaningful result.

## Slide 10 — Folium Launch-Site Analysis
Insert screenshot of the interactive map. Explain marker locations, cluster layer, and proximity interpretation. Include any proximity/nearby-site result actually computed in your course lab.

## Slide 11 — Plotly Dash Dashboard
Insert screenshots of a working dashboard, including the site dropdown and payload slider with at least two filter settings. Explain callback inputs and output graphs.

## Slide 12 — Predictive Analysis
Describe the train/test split and models: Logistic Regression, SVM, Decision Tree, KNN. Explain preprocessing and validation/hyperparameter selection.

## Slide 13 — Model Evaluation
Insert the actual model-comparison table, confusion matrix, and classification report. Identify the best model using the chosen validation metric; distinguish validation results from test results.

## Slide 14 — Conclusions and Limitations
State 3–5 evidence-based findings, business implications, limitations, and next steps. Do not claim causation from correlation or guarantee a future landing outcome.

## Slide 15 — References
Course materials, IBM Skills Network dataset, SpaceX API, pandas, scikit-learn, Plotly Dash, Folium. Use the exact URLs required by the course rubric.
