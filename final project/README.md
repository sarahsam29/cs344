Unstructured Text Analysis: 

The aim of this project is to analyze raw text data and use it to create association which will predict a hardware part for a 
specified mechanical problem. I am using a dataset named “5yearshistoricaldata” which includes the TcaProblem field (unstructured text),
and the TcaParts field (categorical data) to create make associations and predictions. In this historical dataset, all observations are
“closed tickets” meaning every TcaProblem has been fixed and the TcaPart field holds the information of the hardware part that fixed the
issue. 

The program is structured as follows:

 1. Load historical data, clean and restructure it into a data frame.
 2. Parse the TcaProblem fields in the “5yearshistoricaldata”into n-grams
 3. Parse new “unclosed ticket” into n-grams
 4. Join new ticket to parsed TcaProblems in “5yearshistoricaldata” on the n-gram column
 5. Replicate Softmax logic to get probabilities for each hardware part in the results. 

My code and the results of my code are below the report section in the “report.ipynb”. 
