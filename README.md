# python-challenge
An assignment on PyBank and PyPoll Challenges

**************************************************************************************

# PyBank - Financial Analysis

This Python script analyzes financial data from a budget_data.csv file and calculates important financial metrics, such as the total number of months, net total amount of Profit/Losses, average change, greatest increase in profits, and greatest decrease in profits.

## Prerequisites

To run this code, you need to have:
- Python installed on your system. 
- Install visual studio code (optional) and git bash (Windows user)

Additionally, you should have a CSV file named "budget_data.csv" with the following columns: "Date" and "Profit/Losses."

## How to Use the python script

1. Clone this repository to your local machine or download the Python script.

2. Ensure you have the required CSV file ("budget_data.csv") in the same directory as the Python script, or update the 'csvpath' variable to specify the correct file path.

3. Open a terminal or command prompt and navigate to the directory containing the Python script.

4. Run the Python script using the following command:

    python main.py

    The script will analyze the financial data and display the results on the terminal. It will also create a text file named "financial_analysis.txt" in the "analysis" directory within the same directory.

    Review the analysis results on the terminal and in the "financial_analysis.txt" file.

Output Format

The analysis results include the following information:

    Total number of months
    Net total amount of Profit/Losses
    Average change
    Greatest increase in profits
    Greatest decrease in profits

Output File

The results are saved in a text file named "financial_analysis.txt" in the "analysis" directory. You can find the detailed financial analysis in this file.

References
    
Data for this dataset was generated by edX Boot Camps LLC, and is intended for educational purposes only.
Python - Official Python website.
 CSV Module Documentation - Python documentation on working with CSV files.

Author

Godswill Anyasor

License

## This project is open-source and is made available under the terms of the MIT License. The MIT License is a permissive open-source license that allows you to use, modify, and distribute this software for your own purposes. For the full details of the MIT License, please refer to https://choosealicense.com/licenses/mit/.

**************************************************************************************
# PyPoll - Election Data Analysis

This Python script analyzes election data from election_data.CSV file and calculates key statistics, including the total number of votes, candidates' performance, and the election winner.

## Prerequisites

- Python installed on your system
- Install visual studio code (optional) and git bash (Windows user)
- A CSV file named "election_data.csv" with columns: "Ballot ID," "County," and "Candidate."

## How to use the python script

1. Clone or download this repository.

2. Ensure the "election_data.csv" file is in the same directory as the script or update the 'csvpath' variable.

3. Run the script:

    python main.py

    The script will analyze the election data and display the results on the terminal. It will also create a text file named "election_results.txt" in the "analysis" directory with the same results.

Output Format

The analysis results include the following information:

    Total number of votes cast
    List of candidates who received votes
    Percentage of votes each candidate won
    Total number of votes each candidate won
    The winner of the election based on the popular vote

Output File

The results are saved in a text file named "election_results.txt" in the "analysis" directory. You can find the detailed analysis in this file.

References

Data for this dataset was generated by edX Boot Camps LLC, and is intended for educational purposes only.
Python - Official Python website
CSV Module Documentation - Python documentation on working with CSV files

Author

Godswill Anyasor

## License

This project is open-source and is made available under the terms of the MIT License. The MIT License is a permissive open-source license that allows you to use, modify, and distribute this software for your own purposes. For the full details of the MIT License, please refer to https://choosealicense.com/licenses/mit/.
