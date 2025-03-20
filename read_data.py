import csv
import statistics


# This function reads the data stored in a given csv file with headings.
def read_csv_data(csv_file_path):

    content = []

    with open(csv_file_path, 'r', newline='') as input_data:
        reader = csv.DictReader(input_data)

        field_names = reader.fieldnames

        for row in reader:
            content.append(row)

    return {"field_names": field_names, "content": content}


# This function takes the full Iris data and
# write data of a given species into a new csv file.
def write_data_by_species(species, data):

    species_data = []
    field_names = data['field_names']

    for row in data['content']:
        if species == row['species']:
            species_data.append(row)

    with open(species + "_data.csv", 'w', newline='') as output:
        writer = csv.DictWriter(output, fieldnames=field_names)

        writer.writeheader()
        writer.writerows(species_data)


if __name__ == "__main__":
    data_path = "Data/Iris.csv"

    full_data = read_csv_data(data_path)['content']

    petal_length_data = []

    for line in full_data:
        petal_length_data.append(float(line['petal_length']))

    print(petal_length_data)
    print(statistics.mean(petal_length_data))

