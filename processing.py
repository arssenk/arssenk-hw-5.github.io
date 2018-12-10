def process_file():
    processed_file = open("processed_data.csv", "w")

    with open("population_by_age_sex_year.csv", "r") as f:

        f.readline()

        processed_file.write("year,number,gender\n")
        i = 0
        tmp_men = 0
        tmp_women = 0

        while True:
            while i <= 81:
                line = f.readline()

                //EOF
                if not line:
                    return "Finished processing"

                line = line.strip().split(",")

                if line[-1][:2] != "NA":
                    tmp_women += int(line[-1])

                if line[-2][:2] != "NA":
                    tmp_men += int(line[-2])
                i += 1

            processed_file.write(line[0] + ","+str(tmp_men)+",man\n" )
            processed_file.write(line[0] + ","+str(tmp_women)+",woman\n" )
            i = 0
            tmp_men = 0
            tmp_women = 0

print(process_file())

