# Election-analysis: An Analysis of Election Data


## Overview of Election Audit
The purpose of this audit was to review the election data of a congressional district and to determine who was the winner of the election.  As part of this analysis we read data from a csv file and then performed the analysis and wrote the results to an output document.


## Election Audit Results

### Election and Candidate results
In this election there were over 65534 votes cast.  These votes were cast for one of three candidates who were Charles Stockham, Anthony Doane, and Dianna Degette.  Referring to the code all the requsite parts to retrieve each candidates name and vote count and percentage of the total vote did not run as expected.  The only candidate who appeared when saving results to the output file was Anthony Doane who received 1169 votes which was 1.8%.  In past iterations of the script being ran Charles Stockham did receive 48% of the vote and Diana Degette received 23.0% of the vote.  Below is a block of code where the candidate names were retrieved and votes tallied up.

Charles Stockham won the election with 48% of the vote or 31,456 votes according to past iterations of the code script.



 for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county = row[1]


        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        
        
### County results
The counties were also tallied up for total vote coun in each county and the percentage.
Jefferson: 38855 votes 50.9%
Denver: 26679 40.7%

There is a third county, Arapahoe, in this congressional district that was tallied or retrieved by the code script. Jefferson county had the largest turnout.  Here is a code block using the same method as above to get the candidate name to get the county name.



       if county not in county_options:


            # 4b: Add the existing county to the list of counties.
            county_options.append(county)


            # 4c: Begin tracking the county's vote count.
            county_votes[county] = 0


        # 5: Add a vote to that county's vote count.
        county_votes[county] += 1


## Election Audit Summary

### Proposal
I think this code script can be used for other elections and it could be used on even larger elections such as for the whole nation not just a single congressional district.  Some modifications that would have to be made to the script is that with each district it was counties that were being tracked but for other elections the state might have to be tracked in addition.  Also the code would have to be able to take into account there are smaller third party candidates that may not have actually won the election.  For example it could be a presidential election in which case the entire country is voting but the votes are cast within each county within each state.  A smaller more manageable example would be a governors race in a single state in which case this code could be applied.

### Drawbacks 
As stated earlier there were earlier iterations as the code was tested to make sure it was working and all the component parts did what they were supposed to.  Since the code as it is has some issues actually catching both candidate names and county names and thus is not able to put them into the output as expected some further reccommendations are needed.  First, testing the blocks of code as you go or completely separate to make sure they are doing what is needed.  Then once they are working getting them to work together and determining if there is another underlying problem that is causing output problems.
