import pandas

''' When going through the assignment, keep in mind that to actually see these variables you need to use python's print() statement to see their values printed out in replit's console 
'''

# Step 1: Use the appropriate pandas method to read the titanic data into your python file 
titanic_data = pandas.read_csv('titanic.csv')
print(titanic_data)

# Step 2(a): Use the pandas method that reads the first 25 lines of the dataset
first_25_passengers = titanic_data.head(25)
first_25_passengers

# Step 2(b): Use the pandas method thats reads the last 25 lines of the dataset
last_25_passengers = titanic_data.tail(26)
first_25_passengers

# Step 3: Use the pandas method that only tells us the number of rows and columns in our data
titanic_shape = titanic_data.shape
titanic_shape

# Step 4: Describe the titanic data
titanic_description = titanic_data.describe()
titanic_description

# Step 5(a): How many passengers were between the ages of 0 to 16? 
children = titanic_data[(titanic_data['Age'] <= 16) & (titanic_data['Age'] >= 0)]
children

# Step 5(b): How many passengers were between the ages of 17 to 25?
young_adults =  titanic_data[(titanic_data['Age'] >= 17) & (titanic_data['Age'] <= 25)]
young_adults

# Step 5(c): How many passengers were between the ages of 26 to 40?
adults = titanic_data[(titanic_data['Age'] >= 26) & (titanic_data['Age'] <= 40)]
adults

# Step 5(d): How many passengers were between the ages of 41 to 59?
mature_adults = titanic_data[( titanic_data['Age'] >= 41) & ( titanic_data['Age'] <= 59)]
mature_adults

# Step 5(e): How many passengers were 60 or older?
seniors = titanic_data[titanic_data['Age'] >= 60]
seniors

missing_ages = titanic_data['Age'].isnull
missing_ages

# Step 6: How many values are missing from the "age" column
missing_ages = titanic_data[titanic_data['Age'].isnull() == False]
missing_ages
# Step 7 : List out all the available passengers' ages 
age_list = titanic_data['Age'].dropna().unique()
age_list
# Step 8: Filter the DataFrame to find all passengers who boarded the Titanic at Port Cherbourg
cherbourg_passengers = titanic_data[titanic_data['Embarked'] == "C"]
cherbourg_passengers

# Step 9(a): Find the average age of all female passengers
avg_fem_age = titanic_data[ (titanic_data['Sex'] == "female")].Age.mean()

avg_fem_age

# Step 9(b): Find the average age of all male passengers
avg_male_age = titanic_data[ (titanic_data['Sex'] == "male")].Age.mean()
avg_male_age


# Step 10(a): Find the survival percentage of passengers in group "C"
cherbourg_survival = titanic_data[titanic_data['Embarked'] == "C"]['Survived'].mean()*100
cherbourg_survival

# Step 10(b): Find the survival percentage of passengers in group "Q"
queenstown_survival = titanic_data[titanic_data['Embarked'] == "Q"]['Survived'].mean()*100
queenstown_survival

# Step 10(c): Find the survival percentage of passengers in group "S"
south_survival = titanic_data[titanic_data['Embarked'] == "S"]['Survived'].mean()*100
south_survival
