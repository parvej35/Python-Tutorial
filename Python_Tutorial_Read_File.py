
segment_list = ["Activities", "Sleep"]

sleep_array = []
activity_array = []

with open("file/fitbit_exported_data_20211011.csv") as txt_file:

    print(txt_file.readlines())

    counter = 0
    valid = True

    srtSegment = ""

    for line in txt_file:

        counter += 1

        print(line.strip())

        # if line.strip() == "Sleep":    
        if activity_array.count(line.strip()):

            # counter = 0

            # strSegment = line.strip()

            data_values = txt_file.readlines()[counter - 1:]
            print(x)

            for value in data_values:
                counter += 1

                if value.strip() == "":
                    print("This is the end of " + strSegment)
                    break
                else:
                    print("-> " + value)

            # while valid:
                # print(str(counter) +") "+ line)        
                # counter += 1

                # print(line)


        # else: valid = False
