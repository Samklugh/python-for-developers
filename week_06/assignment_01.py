# Open the file
with open(r"C:\Users\user\Desktop\BYU\01. Introduction to Programming\week_06\life-expectancy.csv", "r", encoding="utf-8") as f:
    next(f)  # skip header

    lowest_overall = 1000
    lowest_country = ""
    lowest_year = 0

    highest_overall = 0
    highest_country = ""
    highest_year = 0

    for line in f:
        line = line.strip()
        if line == "":
            continue

        parts = line.split(",")

        country = parts[0]
        year = int(parts[2])
        life = float(parts[3])

        if life < lowest_overall:
            lowest_overall = life
            lowest_country = country
            lowest_year = year

        if life > highest_overall:
            highest_overall = life
            highest_country = country
            highest_year = year

# Print answers for Question 1 and 2
print("1. Lowest life expectancy in the entire dataset:")
print(f"   Country: {lowest_country}")
print(f"   Year: {lowest_year}")
print(f"   Life expectancy: {lowest_overall} years\n")

print("2. Highest life expectancy in the entire dataset:")
print(f"   Country: {highest_country}")
print(f"   Year: {highest_year}")
print(f"   Life expectancy: {highest_overall} years\n")

# Question 3
year_input = int(input("Enter the year you are interested in: "))

with open(r"C:\Users\user\Desktop\BYU\01. Introduction to Programming\week_06\life-expectancy.csv", "r", encoding="utf-8") as f:
    next(f)

    total_life = 0
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
        code = parts[1]
        year = int(parts[2])
        life = float(parts[3])

        if year == year_input and code != "":
            total_life += life
            count += 1

            if life < min_life:
                min_life = life
                min_country = country

            if life > max_life:
                max_life = life
                max_country = country

if count > 0:
    average = total_life / count
    print(f"\nFor the year {year_input}:")
    print(f"   Average life expectancy: {average:.2f} years")
    print(f"   Country with lowest: {min_country} ({min_life} years)")
    print(f"   Country with highest: {max_country} ({max_life} years)")
else:
    print(f"No country data found for the year {year_input}")
