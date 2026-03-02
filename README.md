# EDNA_Merchandise_Sales_Report
## Introduction
This is a portfolio project made by using the dataset provided by Enterprise DNA in collaboration with Onyx Data, where we play a role as a Data Analyst who is proficient in Power BI and Python tasked with finding meaningful insights so that key stakeholders can make better data driven decisions. A Popular TickTok content creater named Lee Chatman who as more than 7 million follower has generously provided us with the sales data of thier online merchandise store. This analysis looks at how his merchandise sales are going and what we can learn from the data.


The main feature of this report is that the calendar used for time analysis is the Retail 4-5-4 Calendar used by all the major players in this business segment. Also, we have incorporated sentiment analysis in this report by using Python.
## Dataset
Here we have sales data of an online merchandise store of a content creator starting from November 5, 2023 to November 4, 2024 along with the delivery location of the customer, thier age and the review they provided after using the product. Lets take a detailed look through the dataset:
### Sales Table
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
Date: List of dates starting from November 5, 2023 to November 4, 2024
