import matplotlib.pyplot as plt

activity_date_list = []
activity_step_list = []
activity_burned_calorie_list = []

with open("file/fitbit_exported_data_20211011.csv") as txt_file:
    line_number = 0

    for str_line in txt_file:

        line_number += 1

        if str_line.strip() == "Activities":
            print(line_number)
            data_values = txt_file.readlines()
            # txt_file.read/)
            print(data_values)

            # Date, Calories Burned, Steps, Distance, Floors, Minutes Sedentary, Minutes Lightly Active,
            # Minutes Fairly, Active, Minutes Very Active, Activity Calories

            # "2021-10-05", "3,085", "11,516", "8.42", "7", "1,000", "63", "33", "81", "1,334"

            for value in data_values:
                line_number += 1

                if len(value.strip()) == 0:
                    break

                else:
                    print(str(line_number) + ") " + value.strip())

                    data_array = value.replace("\n", "").split('\",\"')
                    print(data_array)
                    print(data_array[0])
                    print(data_array[1])
                    print(data_array[2])

                    activity_date_list.append(data_array[0].replace('\"', ''))
                    activity_burned_calorie_list.append(int(data_array[1].replace(',', '')))
                    activity_step_list.append(data_array[2])

            fig = plt.figure(figsize=(10, 6))

            plt.bar(activity_date_list, activity_burned_calorie_list)
            plt.title('Date-wise Burning Calories')
            # plt.xlabel('Date')
            plt.ylabel('Calories Burned')
            plt.show()
