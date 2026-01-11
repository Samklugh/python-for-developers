# Open the file
f = open("life-expectancy.csv", "r", encoding="utf-8")

# Skip the header line
next(f)

# Variables for Question 1 (overall lowest)
lowest_overall = 1000
lowest_country = ""
lowest_year = 0

# Variables for Question 2 (overall highest)
highest_overall = 0
highest_country = ""
highest_year = 0

# Read every line
for line in f:
    line = line.strip()
    if line == "":
        continue
    
    parts = line.split(",")
    
    country = parts[0]          # Entity name
    year = int(parts[2])        # Year
    life = float(parts[3])      # Life expectancy
    
    # Question 1: update overall lowest
    if life < lowest_overall:
        lowest_overall = life
        lowest_country = country
        lowest_year = year
    
    # Question 2: update overall highest
    if life > highest_overall:
        highest_overall = life
        highest_country = country
        highest_year = year

f.close()

# Print answers for Question 1 and 2
print("1. Lowest life expectancy in the entire dataset:")
print(f"   Country: {lowest_country}")
print(f"   Year: {lowest_year}")
print(f"   Life expectancy: {lowest_overall} years")
print()
print("2. Highest life expectancy in the entire dataset:")
print(f"   Country: {highest_country}")
print(f"   Year: {highest_year}")
print(f"   Life expectancy: {highest_overall} years")
print()

# Question 3: Ask user for a year
print("3. Now let's check a specific year")
year_input = int(input("Enter the year you are interested in: "))

# Re-open file to check the specific year
f = open("life-expectancy.csv", "r", encoding="utf-8")
next(f)  # skip header again

total_life = 0.0
count = 0
min_life = 1000
max_life = 0
min_country = ""
max_country = ""

for line in f:
    line = line.strip()
    if line == "":
        continue
    
    parts = line.split(",")
    
    country = parts[0]
    code = parts[1]             # We use this to skip continents (they have empty code)
    year = int(parts[2])
    life = float(parts[3])
    
    # Only look at rows for the year the user entered
    # and only real countries (code is not empty)
    if year == year_input and code != "":
        total_life = total_life + life
        count = count + 1
        
        if life < min_life:
            min_life = life
            min_country = country
        
        if life > max_life:
            max_life = life
            max_country = country

f.close()

# Show results for the chosen year
if count > 0:
    average = total_life / count
    print(f"\nFor the year {year_input}:")
    print(f"   Average life expectancy: {average:.2f} years")
    print(f"   Country with lowest: {min_country} ({min_life} years)")
    print(f"   Country with highest: {max_country} ({max_life} years)")
else:
    print(f"No country data found for the year {year_input}")
