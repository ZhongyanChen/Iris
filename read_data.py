import csv


if __name__ == "__main__":
    data_path = "Data/Iris.csv"

    setosa_data = []

    with open(data_path, 'r', newline='') as input_data:
        reader = csv.DictReader(input_data)

        for row in reader:
            if "setosa" == row['species']:
                setosa_data.append(row)

    with open("setosa_data.csv", 'w', newline='') as output:
        writer = csv.writer(output)

        writer.writerows(setosa_data)
