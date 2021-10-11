
with open("file/fitbit_exported_data_20211011.csv") as txt_file:

    counter = 0
    valid = True

    srtSegment = ""

    for line in txt_file:

        counter += 1

        if line.strip() != "":
            srtSegment = line.strip()

            x = txt_file.readlines()[counter - 1:]
            # print(x)
            for i in x:
                print(i)

            # while valid:
                # print(str(counter) +") "+ line)        
                # counter += 1

                # print(line)


        # else: valid = False
