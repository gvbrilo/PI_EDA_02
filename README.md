# <p align=center>`Individual Project 02 : EDA of the S&P 500`<p>
<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

####  _Ingeniero: Lorenzo Prado Melgarejo_

#
### This Project is meant to display the technical abilities that a Data Engineer must have in order to be efficient in this new era full of changes - Feel free to fork this project  , i use basic techniques in this project and i know that you can improve and contribute.
#

## <p align=center> _Enjoy Learning from this project or Improving it_ <p>
#

## Content Of the Project:

- ## **Main code**
    - main.py

- ## **EDA Process :** 
    - EDA.ipynb

- ## **Visualization of the 3 KPI'S**
    - PI02_BI.pibx


- ## **Initial Databases :** 
    - Databases
        - snp500_index.csv
        - snp500.csv
        - sp500_totalcsv

- ## **Explanatory Summary :** 
    - README.md

- ## **Required API Dependencies :** 
    - Requeriments.txt

#
# <p align=center>General Steps <p><p align=center><img src=Images_src\ETL.png><p>

## **1**: _Downloading the information using pandas to variables in my notebook EDA.ipynb._

## **2**: _Exploratory analysis of the data in my notebook, either univariate analysis or correlations._

## **3**: _Saving of the file snp500_index.csv ,np500.csv and sp500_total._

## **4**: _Creation of the dashboard in POWER BI._

        - File : PI02_BI.ipbx

## **5**: _Creation of KPIs._

## **6**: _Graphics creation._


#
# <p align=center>IMPORTANT EVENTS AFFECTING THE S&P500<p><p align=center><img src=Images_src\API_1.png><p>

## **hecho 1**: _Around the year 2003, the collapse of the companies could have been caused by the war with Iraq. There was a chance of losing to Iraq, despite initial optimism_ :

## **Request 2**: _In the year 2008, there was a crisis in the United States. There was a collapse of the housing bubble, which first impacted the United States_


 ## **Request 3**: _The situation had been brewing since 2006 and the recovery was gradual until 2020, when the COVID 19 event happened._


 ## **Request 4**: _prices increased over time, with a small drop since 2022. In general, the main stock markets in the world have experienced this drop._

# <p align=center>KPIS CREATION - POWERBI<p><p align=center><img src=Images_src\KPI.png><p>

## **Note**: _Theres in the PI02_KPIS.pibx a csv called sp500_PowerBI and it was created inside PowerBI merging and transforming data_ :

## **KPI 1**: _**Average annual return**_

 ## **KPI 2**: _**Volume sum per quarter**_


 ## **KPI 3**: _**Annual volatility**_


#
# <p align=center>EDA - Exploratory Data Analysis<p><p align=center><img src=Images_src\PEX.png><p>

## _investigate relationships between variables in datasets, see if there are outliers or anomalies, null values, and see if there are any interesting patterns worth exploring in further analysis ,_

    - File : EDA.ipynb

#
# <p align=center>Project execution<p><p align=center><img src=Images_src\POX.png><p>

## **Step 1**:  Clone the repository to your local computer.

## **Step 2**:  Create a virtual environment using the tool of your choice.

 ## **Step 3**:  Run the notebook to perform the analysis.

 ## **Step  4**: Open the .pbix file using Power BI Desktop to access the created dashboard.   


# <p align=center>CONCLUTIONS <p><p align=center><img src=Images_src\CLS.png><p>

## **Conclusion 1**: _Stock market analysis allowed us to identify patterns and trends in stock prices that can be useful for investment decision-making. Certain companies with high values ​​increase the overall average value._ 

## **Conclusion 2**: _The visualization dashboard in Power BI allows you to explore this data interactively and obtain valuable information quickly and efficiently._

## **Conclusion 3**: _The decision of which company or companies to invest in will depend on the available capital, the preferred sector and how much risk you are willing to assume._

# <p align=center>FUENTE DE DATOS <p><p align=center><img src=Images_src\SRC.png><p>

##  Para este trabajo se utilizará la API de yahoo finance, la cual posee su librería https://pypi.org/project/yfinance/ y pagina oficial https://finance.yahoo.com/

##  Lista índice SP500 : https://en.wikipedia.org/wiki/List_of_S%26P_500_companies