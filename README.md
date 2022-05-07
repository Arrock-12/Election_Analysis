# Election Analysis
## Project Overview
An employee of a Colorado Board of Elections tasked us with an audit of a local congressional election, specifically requesting that we write a Python script to:
1.	Calculate the total number of votes cast
2.	Calculate the voter turnout for each county
3.	Calculate the percentage of votes from each county based on the total votes cast
4.	Determine which county had the highest turnout
5.	Get a complete list of candidates who received votes
6.	Calculate the total numbers of votes each candidate received
7.	Calculate the percentage of votes each candidate won
8.	Determine the winner of the election based on popular vote
9.	Calculate the voter turnout for each county
10.	Calculate the percentage of votes from each county based on the total votes cast
11.	Determine which county had the highest turnout
12.	Print the information to a text file
 
 ## Election-Audit Results
 The analysis of the election show:
  - There were 369,711 votes cast in the election
  - The counties listed below and their respective percentage of votes and total votes
   - Jefferson County received 10.5% of the total votes cast with 38,855 votes
   - Denver County received 82.8% of the total votes cast with 272,892 votes
   - Arapahoe County received 6.7% of the total votes cast with 24,801 votes
  - The county with most votes was Denver County with 272,892 votes and 82.8% of total votes cast
  
  Below is an image of part of the code used to analyze results based on county.
  ![Python Sript for County Results](https://user-images.githubusercontent.com/101822948/167261288-4b13f069-6d9e-4d51-8b72-8931ad6fffa5.png)
  
  - The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
  -The candidates' results were:
    - Charles Caseper Stockham received 23.0% of the vote and 85,213 votes
    - Diane DeGette received 73.8% of the vote and 272,892 votes
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes
  - The winner of the election was Diane DeGette with 73.8% of the vote and 272,892 votes
 
 Below is an image of the part of code used to analyze results based on candidate.
 ![Python Script for Candidate Results](https://user-images.githubusercontent.com/101822948/167261290-02d3835d-604d-4f64-a592-86b63b681355.png)
 
The results were printed to a text file and submitted the Election Board of Colorado, which looked like this:

![Results Printout](https://user-images.githubusercontent.com/101822948/167261286-884d408c-c2d4-408d-9102-189d34d9e0b5.png)
 

## Election Audit Summary
The script used to audit the election results of this congressional race can be adjusted to not only run audits on other congressinal races both in Coloardo and in other states, but also for statewide and even nationwide elections provided there is a reliable data upon which to run the audits. For statewide audits, the script would need to be modified to include not just congressional races, but statewide elections (like governor or attorney general). The county data aspect of the script would need to be modified to show the results of both congressional and statewide races likely using various conditionals to make sure the data for both races are accurately tabulated. Variables would need to be adjusted and added to account for the different tiers in election races and to provide as much detail as possible for audits.
    
     



