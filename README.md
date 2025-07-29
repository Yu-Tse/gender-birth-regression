# gender-birth-regression
Analyze the correlation between male and female births in Taiwan using linear regression on open government data.

This project performs a simple linear regression to analyze the relationship between the number of female and male births using publicly available government data from Taiwan.

## 📊 Dataset Source

- Dataset: [Monthly Birth Statistics by Gender](https://data.gov.tw/dataset/104296)
- License: [Open Government Data License, Version 1.0](https://data.gov.tw/license)

## 📈 Description

We use the ordinary least squares (OLS) method to fit a linear model:

Male_Births = beta_0 * Female_Births + beta_1


Where:
- `Female_Births`: X-axis (independent variable)
- `Male_Births`: Y-axis (dependent variable)
- `beta_0`: Slope
- `beta_1`: Intercept

The program uses Python with NumPy and Matplotlib to compute the coefficients and visualize the data.

## 📦 Requirements

- Python 3.x
- NumPy
- Matplotlib

Install dependencies with:

```bash
pip install numpy matplotlib

```
---
## 🙋‍♂️ Author

**Yu-Tse Wu** (吳雨澤)  
*Master’s Student at the Institute of Innovation and Semiconductor Manufacturing, National Sun Yat-sen University*
