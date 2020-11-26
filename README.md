## SBA_Guaranteed_Loans_Default_Prediction
This project aims to predict SBA loans default by making Machine Learning through historical data.

#### What is the SBA?
The SBA was created in 1953 and is a U.S. federal government agency tasked with providing counseling, capital and contracting expertise for entrepreneurs. SBA loans are just a part of what it offers. Small business owners can also get free counseling through resource partners such as Small Business Development Centers, SCORE, Veteran’s Business Centers and Women’s Business Centers. It also provides assistance and expertise for businesses that want to qualify for government contracts or export to other countries. It is funded by taxpayers through Congressional appropriations. That means your tax dollars help it help small business owners, so be sure you take advantage of what it has to offer.

The Small Business Administration (SBA) was founded in 1953 to assist small businesses in obtaining loans. Small businesses have been the primary source of employment in the United States. Helping small businesses help with job creation, which reduces unemployment. Small business growth also promotes economic growth. One of the ways the SBA helps small businesses is by guaranteeing bank loans. This guarantee reduces the risk to banks and encourages them to lend to small businesses. If the loan defaults, the SBA covers the amount guaranteed, and the bank suffers a loss for the remaining balance.

There have been several small business success stories like FedEx and Apple. However, the rate of default is very high. Many economists believe the banking market works better without the assistance of the SBA. Supporter claim that the social benefits and job creation outweigh any financial costs to the government in defaulted loans.

#### Problem
More than 1 in 6 loans (17.4%) awarded from 2006 through 2015 went into default. It means that SBA would have loss due to Small Business couldn’t make repayment

#### Goals
Being able to early detected of SBA loan default could reduce the risk of loss for Small Business Administration.

#### Steps of work
- Cleaning Dataset including missing Values, deleting some noise, feature engineering and feature selection
- Data Analyst and Visualization
- Building Machine Learning Using Base Algorithms
- Conclusion and Recommendation

### Here are the Results:
#### Data Analyst and Visualization
- Percentage of borrower who pain in full (PIF) around 75.72% while borrower who charge off around 24.27%
- Loan backed up by real estate has lower CHGOFF (4.43%) rather than not backed up by real estate (25.49%)
- Whether the business was Existing Business or New Business, both of them has same risk of CHGOFF
- Most of CHGOFF come from Urban with percentage 86.40%
- Mostly for small business that has default loan (CHGOFF) didn't come from LowDoc. The percentage of LowDoc that CHGOFF only 15.86%
- CHGOFF with low DisbursementGross has higher percentage 27.4% rather than high DisbursementGross. Its means that mostly CHGOFF come from small business with low DisbursementGross
- Sector Feature :
    - Retail trade and Manufacturing has significantly loan disbursement compare to another sector
    - Mining, quarrying, and oil and gas extraction  has highest median of Gross amount of loan approved by bank around 165000.0, followed by Agriculture, forestry, fishing    and hunting 
    - Sector that has highest default was Public Administration (39.13%), followed by Finance and Insurance (30.54%) and retail Trade (29.29%)
    
#### Machine Learning
In this Final Project, I just use algorithms of machine learning that based on tree. From the results showed that Random Forest after Tuning has error that more tolerate. So for the deploying, I use this model.

Please kindly see my ipynb file to know the process...\
Thankyouu:)



