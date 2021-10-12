
segment_list = ["Activities", "Sleep"]

sleep_array = []
activity_array = []

with open("file/fitbit_exported_data_20211011.csv") as txt_file:

    # print(txt_file.readlines())

    line_number = 0
    valid = True

    srtSegment = ""

    for str_line in txt_file:

        line_number += 1

        if str_line.strip() == "Activities":

            strSegment = str_line.strip()

            data_values = txt_file.readlines()[line_number - 1:]
            # print(data_values)

            for value in data_values:
                line_number += 1

                # print("V: " + value.strip())

                if value.strip() != "":
                    print("-> " + value.strip())
                else:
                    print("This is the end of " + strSegment)
                    continue

        else:
            print("---")
            # continue
