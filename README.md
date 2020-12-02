## SBA_Loans_Default_Prediction
This project aims to predict SBA loans default by making Machine Learning through historical data.

### What is the SBA?
The SBA was created in 1953 and is a U.S. federal government agency tasked with providing counseling, capital and contracting expertise for entrepreneurs. SBA loans are just a part of what it offers. Small business owners can also get free counseling through resource partners such as Small Business Development Centers, SCORE, Veteran’s Business Centers and Women’s Business Centers. It also provides assistance and expertise for businesses that want to qualify for government contracts or export to other countries. It is funded by taxpayers through Congressional appropriations. That means your tax dollars help it help small business owners, so be sure you take advantage of what it has to offer.

Small businesses have been the primary source of employment in the United States. Helping small businesses help with job creation, which reduces unemployment. Small business growth also promotes economic growth. One of the ways the SBA helps small businesses is by guaranteeing bank loans. This guarantee reduces the risk to banks and encourages them to lend to small businesses. If the loan defaults, the SBA covers the amount guaranteed, and the bank suffers a loss for the remaining balance.

There have been several small business success stories like FedEx and Apple. However, the rate of default is very high. Many economists believe the banking market works better without the assistance of the SBA. Supporter claim that the social benefits and job creation outweigh any financial costs to the government in defaulted loans.

### Problem
The default rate for the 10-year period ending in 2008, when nearly 1 in 4 (24.7%) SBA loans weren’t paid back. It means that SBA would have loss due to Small Business couldn’t make repayment

### Goals
Being able to early detected of SBA loan default could reduce the risk of loss for Small Business Administration.

### Steps of work
- Cleaning Dataset including missing Values, deleting some noise, feature engineering and feature selection
- Data Analyst and Visualization
- Building Machine Learning Using Base Algorithms
- Conclusion and Recommendation
- Deployment

### Here are the Results:
#### Data Analyst and Visualization
1. Percentage of borrower who pain in full (PIF) around 72.33% while borrower who charge off around 27.67%
2. Loan backed up by real estate has lower CHGOFF (4.41%) rather than not backed up by real estate (28.51%)
3. Whether the business was Existing Business or New Business, both of them has same risk of CHGOFF
4. Most of CHGOFF come from Urban with percentage 86.24%
5. Small busines with revolving line of credit has lower risk of default loan with percentage 26.26%
6. Mostly for small business that has default loan (CHGOFF) didn't come from LowDoc. The percentage of LowDoc that CHGOFF only 15.44%
7. CHGOFF with low DisbursementGross has higher percentage 30.67% rather than high DisbursementGross. Its means that mostly CHGOFF come from small business with low DisbursementGross
8. Sector Feature :
    - Retail trade and Manufacturing has significantly loan disbursement compare to another sector
    - Mining, quarrying, and oil and gas extraction  has highest median of Gross amount of loan approved by bank around 100000.0, followed by    Agriculture, forestry, fishing and hunting 
    - Sector that has highest default was Real estate and rental and leasing (37.51%), followed by Finance and Insurance (34.91%) and Transportation and warehousing (31.44%)

    
#### Machine Learning
In this Final Project, I just use algorithms of machine learning that based on tree (Decision Tree, Random Forest and XGBoost). Here are the results of the algorithms:\
![Eval Matrix](Eva_mat_all_model.png)

From the results showed that Random Forest after Tuning has recall positif around 0.93. So for the deploying model, I used this model.

### Conclusion and Recommendation
#### Conclusion
`Here are some conclusion that should become concern on to reduce the risk of default from Data Analyst:`
- Small Business that has **Term of loan less than 240 month** tend to has high risk of default. The percentage reach 28.51%.
- Small Business with **low amount disbursement** tend to  has high risk of default. The percentage reach 30.67%.
- Small Business that come from **sector Real estate and rental and leasing** has high risk of default with percentage reach 37.51%
- Small Business that come from **different State** tend to has high risk of default. The percentage reach 77.98%.

`Here are some conclusion from Building Model :`
 - Random Forest Tuning has good Recall around 0.93
 - Receiver Operating Characteristic has value 0.89. It means that model good enough to separate the target (CHGOFF or PIF)

#### Recommendation
`Here are some suggestion to reduce the risk of default:`
- Small Business with low amount disbursement, term less than 240 month, and come from sector Real estate and rental and leasing should more get attention by lender. Lender could recommend counseling to Business owners through SBA Program to make reduce the risk of default in future.
- Lender should more pay attention to Small Business location to prevent default due to different State. When the borrowers has different State with Lender, lender could offer another lender that has same State.
- Recommendation for Modelling:
    - Try to use machine learning algorithms base distance
    - Try another way to handling Imbalance Data like Oversampling


Please kindly see my ipynb file to know the process...\
Thankyouu:)



