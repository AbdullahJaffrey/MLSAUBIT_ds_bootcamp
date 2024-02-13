# Exploring Credit Risk in Bank Loan Status: A Data Analysis Journey

## Introduction
In the realm of financial services, assessing credit risk is of paramount importance for banks and lending institutions. The ability to accurately predict whether a borrower will default on a loan is crucial for maintaining a healthy loan portfolio and minimizing financial losses. In this project, we embark on a journey to explore and analyze a dataset containing valuable information about bank loan applicants' credit risk. Our objective is to delve into the dataset, employ various analysis and visualization techniques, and ultimately develop a classification model using the Random Forest algorithm to categorize loan status based on diverse measurements.

## Dataset Overview
The dataset we are working with provides insights into the attributes of loan applicants, including demographic information, financial details, and loan characteristics. It comprises features such as:

- **ID**: Unique identifier for each loan applicant.
- **Age**: Age of the loan applicant.
- **Income**: Income of the applicant.
- **Home**: Home ownership status (e.g., OWN, RENT, ..).
- **Employment Length**: Number of years the applicant has been employed.
- **Intent**: Purpose of the loan (e.g., EDUCATION, PERSONAL, ..).
- **Amount**: Loan amount requested by the applicant.
- **Rate**: Interest rate associated with the loan.
- **Status**: Binary indicator of loan status (0 for non-default, 1 for default).
- **Percent Income**: Percentage of income dedicated to loan repayment.
- **Default**: Categorical indicator of default status (Y for default, N for non-default).
- **Credit Length**: Length of credit history in years.

The dataset offers a comprehensive view of the factors influencing loan approval and default rates, making it a valuable resource for our analysis.

## Project Objectives
Our primary objective is to perform an exploratory analysis of the dataset to uncover patterns, trends, and insights related to credit risk in bank loan status. Specifically, we aim to achieve the following:

1. **Data Exploration:** Gain a deep understanding of the dataset by examining descriptive statistics, distributions, and correlations among variables.

2. **Visualization:** Utilize visualizations such as histograms, scatter plots, and heatmaps to visualize the relationships between different features and loan status.

3. **Feature Engineering:** Engineer new features or preprocess existing ones to enhance the predictive power of our model.

4. **Model Development:** Develop a classification model using the Random Forest algorithm to predict loan status based on applicant attributes.

5. **Model Evaluation:** Assess the performance of the model using appropriate evaluation metrics such as accuracy, precision, recall, and F1-score.

## Instructions for Exploration
To begin our exploration, we first need to access the dataset. You can find the dataset [here](https://github.com/AbdullahJaffrey/MLSAUBIT_ds_bootcamp/tree/main/projects/grandproject/credit_risk.csv). Once you have obtained the dataset, follow these steps:

1. **Clone the Repository:** Use the command `git clone https://github.com/AbdullahJaffrey/MLSAUBIT_ds_bootcamp.git` to clone the repository containing the project files.

2. **Navigate to the Project Folder:** After cloning the repository, navigate to the project folder using the command `cd MLSAUBIT_ds_bootcamp/projects/grandproject/credit_risk_bank_loan_status`.

3. **Open and Run the Jupyter Notebook:** Open and run the Jupyter Notebook `FinalProject(credit_risk_bank_loan_status).ipynb` to explore the dataset, conduct analysis, and visualize loan information using the Random Forest algorithm.

4. **Modify Code or Dataset:** Feel free to modify the code or dataset as needed to conduct further analysis or experiment with different techniques.

5. **For Assistance:** If you have any questions or encounter issues during exploration, please open an issue in the GitHub repository for assistance.

## Conclusion
Exploring credit risk in bank loan status is a multifaceted endeavor that requires a combination of data analysis, visualization, and machine learning techniques. By leveraging the rich insights provided by the dataset and employing advanced analytical methods, we can gain valuable insights into the factors influencing loan approval and default rates. Through this project, we aim to contribute to the understanding of credit risk assessment in the financial domain and empower decision-makers with actionable insights for risk mitigation and portfolio management. 

Happy exploring! ❤️
