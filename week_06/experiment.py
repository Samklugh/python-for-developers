with open ("life-expectancy.csv") as life_file:

    next(life_file)

    for life in life_file:
        parts=life.split(",")

        country=parts[0]
        country_code=parts[1]
        year=int(parts[2])
        life_expectancy=float(parts[3])


        miin=min(life_expectancy)

        print(miin)