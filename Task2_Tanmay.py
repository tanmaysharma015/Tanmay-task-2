import pandas as pd
travel = pd.read_csv("first_years_dataset_2.csv")
type(travel)

#query_1

print(travel.sort_values('Fare', ascending = False ).head(1))
print(" \n\n")

#query_2
find_fare = (travel['Name'] == 'O\'Driscoll, Miss. Bridget')

print("\n The fare paid by the passenger named O'Driscoll, Miss. Bridget is: ")
print(travel.loc[find_fare, 'Fare'])
print(" \n\n")

#query_3
num = int(0)
a = len(travel)
no_age = travel['Age']
no_age = no_age.apply (pd.to_numeric, errors='coerce')       #for dropping all the elements with NaN values
no_age = no_age.dropna()
b = len(no_age)
num_of_noage = a - b
 
for i in range(num_of_noage):
    num = num + 1

print("The number of missing values in the column Age is:")
print(num)