# EDNA_Merchandise_Sales_Report
![Main_Page](https://github.com/tirthvyas95/EDNA_Merchandise_Sales_Report/blob/00442ec2f12f2b57948e4801e11214f445b24fbd/Screenshots/Home%20Page.png)
## Introduction
This is a portfolio project made by using the dataset provided by [Enterprise DNA](https://enterprisedna.co/) in collaboration with Onyx Data, where we play a role as a Data Analyst who is proficient in [Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi) and [Python](https://www.python.org/) tasked with finding meaningful insights so that key stakeholders can make better data driven decisions. A Popular TickTok content creater named Lee Chatman who as more than 7 million follower has generously provided us with the [sales data](https://enterprisedna.co/challenges/merchandise-sales-dataset) of thier online merchandise store. This analysis looks at how his merchandise sales are going and what we can learn from the data.


The main feature of this report is that the calendar used for time analysis is the Retail 4-5-4 Calendar used by all the major players in this business segment. Also, we have incorporated sentiment analysis in this report by using Python.
## Dataset
Here we have sales data of an online merchandise store of a content creator starting from November 5, 2023 to November 4, 2024 along with the delivery location of the customer, thier age and the review they provided after using the product. Lets take a detailed look through the dataset:
### Sales Table
![Sales_table_view](https://github.com/tirthvyas95/EDNA_Merchandise_Sales_Report/blob/00442ec2f12f2b57948e4801e11214f445b24fbd/Screenshots/Sales_Data_View.png)
**Metadata**
1. Order ID: Unique ID of each product
2. Order Data: Date on which the order was placed
3. Product ID: Unique ID of each product
4. Product Category: The category in which the product belongs to (Clothing, Ornaments and Others)
5. Buyer Gender: Whether the customer is Male or Female
6. Buyer Age: The age of the customer
7. Order Location: The name of the state of residence of the customer
8. Latitude: Latitude coordinates of the state
9. Longitude: Longitude coordinates of the state
10. Internatioal Shipping: (Yes/No) If the customer is not residing in united states a shipping surcharge is placed
11. Sales Price: Sales unit price of the product ordered
12. Shipping Charges: Shipping charges if the customer has opted for international shipping
13. Sales Per Unit: Price of the order after adding the shipping charges
14. Quantity: Amount of product ordered
15. Total Sales: Total price of the order
16. Rating: Number of stars(1 to 5) provided by the customer as review
17. Review: A written text review given by the customer
18. Buyer Age Group: Age group of the buyer, optained by binning the Buyer Age

Some important things to note is that the Coordinates are the coordinates of the different states and same as the states in the product location and there are only 10 12 unique written review in the Reviews column but the sentiment analysis we are going to do happens individually for each review so any other dataset can use the same python logic.
### Calendar_454 Table:
In this project we are going to use the Retail 4-5-4 calendar with 364 days, 4 quarters containing 3 months, 52 weeks, 2 months with 4 weeks and 1 month with 5 weeks arraigned in the 4-5-4 manner and it starts from November 5, 2023 when the dataset that we have starts. You can substitue any date range in the CALENDAR(start_date, end_date) function and this template will generate for you a 4-5-4 calendar. Voici:
```
Calendar_454 = 
VAR cal = CALENDAR(MIN(Sales[Order Date]), MAX(Sales[Order Date]))
VAR BaseDate = MINX(cal, [Date])

RETURN
ADDCOLUMNS(
    cal,
    "DayIndex", DATEDIFF(BaseDate, [Date], DAY),
    "Fiscal YearIndex", QUOTIENT(DATEDIFF(BaseDate, [Date], DAY), 364),
    "Fiscal Year No", QUOTIENT(DATEDIFF(BaseDate, [Date], DAY), 364) + 2023,
    "Day of FIscal Year", MOD(DATEDIFF(BaseDate, [Date], DAY), 364) + 1,
    "Quarter", MOD(QUOTIENT(DATEDIFF(BaseDate, [Date], DAY), 91), 4) + 1,
    "Quarter Index", QUOTIENT(DATEDIFF(BaseDate, [Date], DAY), 91),
    "Week No.", MOD(QUOTIENT(DATEDIFF(BaseDate, [Date], DAY), 7), 52) + 1,
    "Week Index", QUOTIENT(DATEDIFF(BaseDate, [Date], DAY), 7),
    "454 Month No. in Quarter",
        VAR var1 = MOD(MOD(QUOTIENT(DATEDIFF(BaseDate, [Date], DAY), 7), 52), 13)
        VAR var2 = IF(var1 < 4, 1, 
            IF(
                var1 > 3 && var1 < 9, 2,
                IF(
                    var1 > 8, 3
                )
            )
        )
        RETURN var2,
    "454 Month Index",
        VAR var1 = MOD(MOD(QUOTIENT(DATEDIFF(BaseDate, [Date], DAY), 7), 52), 13)
        VAR var2 = IF(var1 < 4, 1, 
            IF(
                var1 > 3 && var1 < 9, 2,
                IF(
                    var1 > 8, 3
                )
            )
        )
        VAR var3 = QUOTIENT(QUOTIENT(DATEDIFF(BaseDate, [Date], DAY), 7), 13)
        RETURN (3*var3) + var2,
    "Day Name", FORMAT([Date], "DDDD")
)
```
I am still in the process of generating a more generalised version of this calendar which I will post in another repository but for our purposes in this project this should suffice. Lets look at the metadata of this calendar

**Metadata**
1. Date: List of dates starting from November 5, 2023 to November 4, 2024
2. DayIndex: The index of the day starting from 0
3. Fiscal YearIndex: Fiscal year index starting from 0 and incrementing after 364 days
4. Fiscal Year No: Fiscal YearIndex + 2023. As the dates start from 2023 November
5. Day of the Fiscal Year: Day number of the fiscal year starting from 1 ending with 364 and then starting again
6. Quarter: Quarter number in the Fiscal year (1, 2, 3). (1 day quarter)
7. Quarter Index: Quarter Index starting from 0 and incrementing every 91 days
8. Week No. : Week number in the year(1 to 52)
9. Week Index: Week index starting from 0
10. 454 Month No. in Quarter: Month number in quarter(1, 2, 3). 4 weeks in 1st month, 5 weeks in 2nd month and 4 weeks in 3rd month
11. 454 Month Index: Month Index starting from 0, following the 4-5-4 pattern
12. Day Name: Name of the day of the week

![Calendar_Data_View](https://github.com/tirthvyas95/EDNA_Merchandise_Sales_Report/blob/00442ec2f12f2b57948e4801e11214f445b24fbd/Screenshots/Calendar_Data_View.png)

You can substitue the start and end date in the CALENDAR() function of you want to use this template, also if you are looking for the template for 4-4-5 Retail calendar you can check out my other repository called [EDNA_Mobile_Phone_Sales_Analysis](https://github.com/tirthvyas95/EDNA_Mobile_Phone_Sales_Analysis). I will standardarize this DAX and upload it into another repository later.
### sentiment_scores Table:
Every porject that I do, I try to incorporate something new, for this project it is the sentiment analysis. In order to analysis the sentiment in the Reviews column we will use a python script by using import from a python script feature. We will need the NLTK python library for this task and since it is not supported on the Power BI service because python based visuals on Power BI service only supports some base libraries like Pandas and Numpy we would not get a chance to upload this to Power BI service. So we can just use the import from python script feature, I am sure there should be a way by using Power Automate but here we are demonstrating this report as a proof concept it should suffice.

**Libraries Used:**
1. [Pandas](https://pandas.pydata.org/): For importing from excel and converting and using the data as a pandas dataframe
2. [Numpy](https://numpy.org/): For matrix multipication
3. [NLTK](https://www.nltk.org/): Natural Language Toolkit for sentiment analysis
4. [TQDM](https://pypi.org/project/tqdm/): For monitoring and testing the script

Here is the python script used for importing sentiment scores into Power BI:
```
import pandas as pd
import numpy as np

import nltk

df = pd.read_excel('C:/Users/tirth/Documents/Projects/EDNA Merchandise Sales Report/Source Files/Onyx Data -DataDNA Dataset Challenge - Merchandise Sales Dataset - January 2025.xlsx')

dfsub = df[['Order ID']]

#nltk.download('punkt')
#nltk.download('punkt_tab')
#nltk.download('averaged_perceptron_tagger_eng')
#nltk.download('maxent_ne_chunker_tab')
#nltk.download('words')

from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm

sia = SentimentIntensityAnalyzer()

#nltk.download('vader_lexicon')

res = {}
for i, row in tqdm(df.iterrows(), total=len(df)):
    text = row['Review']
    myid = row['Order ID']
    res[myid] = sia.polarity_scores(text)

vaders = pd.DataFrame(res).T
vaders.reset_index(inplace=True)
vaders.rename(columns={'index': 'Order ID'}, inplace=True)

sentiment_scores = vaders.merge(dfsub, how='left', on='Order ID')
```
Here, an important thing to note is that I had to download some dependencies as you can see they are commented in the script since it is different for evey system, sometimes when you insall NLTK they are included sometimes they are not, read carefully the error messsage, it will recommend you if it needs any other dependencies.


After, you run this it will return a dimention table with columns: OrderID, Negative Score, Positive Score, Neutral Score and Compound Score. AS the name suggests Positive Score tells us how positive is the text, Negative Score shows us how Negative the text is and the Neutral shows us how Neutral the Review is. What we are more interested in is the Compound Score, it is the average of the other 3.


The returned Table should like this:
![Sentiment_Scores_Data_View](https://github.com/tirthvyas95/EDNA_Merchandise_Sales_Report/blob/00442ec2f12f2b57948e4801e11214f445b24fbd/Screenshots/Sentiment_Scores_Data_View.png)

## Data Model
We have here 3 table, where we will keep our Sales table as Fact Table and the other two namely Calendar and sentiment_score tables as dimentions.

**Relationships:**
1. Calendar_454[Date] -> Sales[Order Date]
2. sentiment_scores[Order ID] <-> Sales[Order ID]

Here is what our model looks like:
![Data_Model](https://github.com/tirthvyas95/EDNA_Merchandise_Sales_Report/blob/00442ec2f12f2b57948e4801e11214f445b24fbd/Screenshots/Model_View.png)
## Measures
Following are the measures used for this Report:
### Base Measures
1. **Average Rating**
```
Average Rating = AVERAGE(Sales[Rating])
```
2. **Count of Orders Shipped Internationally**
```
Count of Orders Shipped Internationally = CALCULATE(
    COUNTROWS('Sales'),
    Sales[International Shipping] = "Yes"
)
```
3. **Number of Orders**
```
Number of Orders = DISTINCTCOUNT(Sales[Order ID])
```
4. **Percentage Shipping Cost to Revenue = [Total Cost of Shipping] / [Total Revenue]**
```
Percentage Shipping Cost to Revenue = [Total Cost of Shipping] / [Total Revenue]
```
5. **Total Cost of Shipping**
```
Total Cost of Shipping = SUM(Sales[Shipping Charges])
```
6. **Total Quantity Sold**
```
Total Quantity Sold = SUM(Sales[Quantity])
```
7. **Total Revenue**
```
Total Revenue = SUM(Sales[Total Sales])
```
### Time Analysis Measures
1. **Revenue Month to Date ISO**
```
Revenue Month to Date ISO = 
VAR CurrentFiscalDay = MAX(Calendar_454[DayIndex])
VAR CurrentFiscalMonth = MAX(Calendar_454[454 Month Index])
VAR CurrentFiscalYear = MAX(Calendar_454[Fiscal YearIndex])

RETURN
CALCULATE(
    [Total Revenue],
    FILTER(
        ALL(Calendar_454),
        Calendar_454[454 Month Index] = CurrentFiscalMonth &&
        Calendar_454[Fiscal YearIndex] = CurrentFiscalYear &&
        Calendar_454[DayIndex] <= CurrentFiscalDay
    )
)
```
2. **Revenue Quarter to Date ISO**
```
Revenue Quarter to Date ISO = 
VAR CurrentFiscalDay = MAX(Calendar_454[DayIndex])
VAR CurrentFiscalQuarter = MAX(Calendar_454[Quarter Index])
VAR CurrentFiscalYear = MAX(Calendar_454[Fiscal YearIndex])

RETURN
CALCULATE(
    [Total Revenue],
    FILTER(
        ALL(Calendar_454),
        Calendar_454[Quarter Index] = CurrentFiscalQuarter &&
        Calendar_454[Fiscal YearIndex] = CurrentFiscalYear &&
        Calendar_454[DayIndex] <= CurrentFiscalDay
    )
)
```
3. **Revenue Week to Date ISO**
```
Revenue Week to Date ISO = 
VAR CurrentFiscalDay = MAX(Calendar_454[DayIndex])
VAR CurrentFiscalWeek = MAX(Calendar_454[Week Index])
VAR CurrentFiscalYear = MAX(Calendar_454[Fiscal YearIndex])

RETURN
CALCULATE(
    [Total Revenue],
    FILTER(
        ALL(Calendar_454),
        Calendar_454[Week Index] = CurrentFiscalWeek &&
        Calendar_454[Fiscal YearIndex] = CurrentFiscalYear &&
        Calendar_454[DayIndex] <= CurrentFiscalDay
    )
)

```
4. **Total Orders Month to Date ISO**
```
Total Orders Month to Date ISO = 
VAR CurrentFiscalDay = MAX(Calendar_454[DayIndex])
VAR CurrentFiscalMonth = MAX(Calendar_454[454 Month Index])
VAR CurrentFiscalYear = MAX(Calendar_454[Fiscal YearIndex])

RETURN
CALCULATE(
    [Number of Orders],
    FILTER(
        ALL(Calendar_454),
        Calendar_454[454 Month Index] = CurrentFiscalMonth &&
        Calendar_454[Fiscal YearIndex] = CurrentFiscalYear &&
        Calendar_454[DayIndex] <= CurrentFiscalDay
    )
)
```
5. **Total Orders Quarter to Date ISO**
```
Total Orders Quarter to Date ISO = 
VAR CurrentFiscalDay = MAX(Calendar_454[DayIndex])
VAR CurrentFiscalQuarter = MAX(Calendar_454[Quarter Index])
VAR CurrentFiscalYear = MAX(Calendar_454[Fiscal YearIndex])

RETURN
CALCULATE(
    [Number of Orders],
    FILTER(
        ALL(Calendar_454),
        Calendar_454[Quarter Index] = CurrentFiscalQuarter &&
        Calendar_454[Fiscal YearIndex] = CurrentFiscalYear &&
        Calendar_454[DayIndex] <= CurrentFiscalDay
    )
)
```
6. **Total Orders Week to Date ISO**
```
Total Orders Week to Date ISO = 
VAR CurrentFiscalDay = MAX(Calendar_454[DayIndex])
VAR CurrentFiscalWeek = MAX(Calendar_454[Week Index])
VAR CurrentFiscalYear = MAX(Calendar_454[Fiscal YearIndex])

RETURN
CALCULATE(
    [Number of Orders],
    FILTER(
        ALL(Calendar_454),
        Calendar_454[Week Index] = CurrentFiscalWeek &&
        Calendar_454[Fiscal YearIndex] = CurrentFiscalYear &&
        Calendar_454[DayIndex] <= CurrentFiscalDay
    )
)
```
## Visualizations and Report
### Home Page
![Home_Page](https://github.com/tirthvyas95/EDNA_Merchandise_Sales_Report/blob/00442ec2f12f2b57948e4801e11214f445b24fbd/Screenshots/Home%20Page.png)
### Orders Page
![Orders_page](https://github.com/tirthvyas95/EDNA_Merchandise_Sales_Report/blob/00442ec2f12f2b57948e4801e11214f445b24fbd/Screenshots/Orders_Page.png)
### Revenue Page
![Revenue_page](https://github.com/tirthvyas95/EDNA_Merchandise_Sales_Report/blob/00442ec2f12f2b57948e4801e11214f445b24fbd/Screenshots/Revenue_Page.png)
### Time & Demographic Analysis
![Time_Analysis](https://github.com/tirthvyas95/EDNA_Merchandise_Sales_Report/blob/00442ec2f12f2b57948e4801e11214f445b24fbd/Screenshots/Time_Demographic_Analysis.png)
### Shipping & Reviews
![Shipping_Reviews](https://github.com/tirthvyas95/EDNA_Merchandise_Sales_Report/blob/00442ec2f12f2b57948e4801e11214f445b24fbd/Screenshots/Shipping_review_Analysis.png)

## References
1. Microsoft Learn, Microsoft Learn's Data Analyst Career Path. Retrieved March 2, 2026, from https://learn.microsoft.com/en-us/training/career-paths/data-analyst
2. Enterprise DNA, Data Analytics Challenges by Enterprise DNA. Retrieved March 2, 2026, from https://enterprisedna.co/challenges
3. SQLBI, SQLBI's Website, Retrieved March 2, 2026. from https://www.sqlbi.com/
4. SQLBI, SQLBI's Article on Week Baseed Time Analysis Measures, Retrieved March 2, 2026. from https://www.sqlbi.com/articles/week-based-time-intelligence-in-dax/
5. DAX Patterns, Article on Week-related Calculations, Retrieved March 2, 2026. from  https://www.daxpatterns.com/week-related-calculations/
6. Microsoft Learn, Run Python scripts in Power BI Desktop, Retrieved March 2, 2026. from https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-python-scripts
7. Rob Mulla's Kaggle Notebook, Sentiment Analysis Python, Retrivied March 2, 2026. from https://www.kaggle.com/code/robikscube/sentiment-analysis-python-youtube-tutorial
