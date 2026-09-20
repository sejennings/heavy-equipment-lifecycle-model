# Heavy Equipment Lifecycle Model

An interactive machine-learning project that estimates the resale value of heavy construction equipment based on its equipment class, age, operating hours, and sale year.

## Live Streamlit App

[Open the Heavy Equipment Resale Value Calculator](https://heavy-equipment-lifecycle-model.streamlit.app/)

The Streamlit application provides a simple interface for generating estimates from the trained model. Users can select an equipment category and subcategory, enter the machine’s age and operating hours, and receive an estimated resale value without downloading the repository or running the modeling notebook.

## What This Repository Does

This repository contains the full process used to build and deploy the resale-value model:

* Cleans historical equipment auction data from Kaggle’s *Blue Book for Bulldozers* dataset
* Investigates missing, zero, and physically unrealistic operating-hour values
* Engineers equipment-age, sale-year, and transformed operating-hour features
* Compares progressively more detailed regression models
* Accounts for differences among equipment classes and market years
* Evaluates performance using a future-year holdout set
* Measures prediction reliability by equipment class
* Exports the trained model for use in the Streamlit application

The final model predicts auction sale price using:

* Detailed equipment class
* Equipment age
* Operating hours
* Sale year

## Model Performance

On the 2012 holdout data, the selected model achieved:

* **Log-scale R²:** 0.766
* **Mean absolute error:** approximately $10,290
* **Median absolute percentage error:** approximately 23%

Performance varies by equipment class, particularly when relatively few historical sales are available.

## Project Purpose

The project was created as an initial component of a broader heavy-equipment decision tool. Estimated residual value is important when comparing whether to continue using an owned machine, replace it, purchase another machine, or rent equipment for a project.

The current application focuses specifically on making the resale-value model accessible. It does not yet calculate a complete rent-versus-own decision using rental rates, maintenance expenses, transportation costs, financing, or downtime.

## Important Limitations

* The model is trained on historical auction data ending in 2012.
* Estimates are not automatically adjusted for current inflation or equipment-market conditions.
* Machine condition, manufacturer, model, location, attachments, and auction-specific factors are not included in the final model.
* Equipment classes with limited historical data may produce less reliable estimates.
* Results should be treated as analytical estimates rather than formal equipment appraisals.

## Technologies

* Python
* pandas and NumPy
* statsmodels
* scikit-learn
* Streamlit
* GitHub
