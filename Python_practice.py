print("Hello World")

#If-else practice with counties
counties = ["Arapahoe", "Denver", "Jefferson"]

if "El Paso" in counties:
    print("El Paso is in the list of counties. ")

else:

    print("El Paso is not in the list of counties. ")


if "Arapahoe" in counties or "El Paso" in counties:
    
    print("Arapahoe or El Paso are in the list of counties. ")

else:

    print("Araphoe or El Paso is not in the list of counties")


if "Arapahoe" in counties and "El Paso" not in counties:

   print("Only Arapahoe is in the list of counties.")

else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:

    print(county)


#Using the range() function
for i in range(len(counties)):
    print(counties[i])



#Skill drill original
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys():
    print(county)

for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters")



#Getting keys and values from a dictionary
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:

    for value in county_dict.values():

        print(value)

#Updated skill drill using f-string
for county, voters in counties_dict.items():

    print(f"{county} county has {voters} registered voters.")

#Multiline f-string
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)
    