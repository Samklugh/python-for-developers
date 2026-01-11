#open file

with open("hr_system.txt") as hr_file:
    next(hr_file) #- this skips the header line

    #read through the file line by line

    for line in hr_file:
        # get the various parts of the record into variables
        #split each line into components

        parts=line.split(" ")

        name=parts[0]
        id=parts[1]
        job_title=parts[2]
        salary=int(parts[3])

        paycheck_amount=salary/24

        if job_title=="Engineer":
            paycheck_amount.lower()=paycheck_amount+1000

        #print the components

        print(f"Name: {name}, ID: {id}, Job Title: {job_title}- ${paycheck_amount:.2f}")