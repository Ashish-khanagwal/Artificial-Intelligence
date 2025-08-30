import csv

"""
FIRST METHOD -->

data = []
with open("people_data.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

header = data[0]

sorted_data = sorted(data[1:], key=lambda row: row[0])

final_data = [header] + sorted_data
for row in final_data:
    print(row)

with open("Sorted_people_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(final_data)
"""

"""
SECOND METHOD -->
"""


def sort_contacts(input_file, output_file, sort_key="Name"):
    try:
        with open(input_file, newline="", encoding="utf-8") as infile:
            reader = csv.DictReader(infile)
            contacts = list(reader)

        if not contacts:
            print("No contact data found in the file.")
            return

        contacts.sort(key=lambda x: x[sort_key].lower())

        with open(output_file, "w", newline="", encoding="utf-8") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(contacts)

        print(f"Contacts sorted by '{sort_key}' and saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except KeyError:
        print(f"Error: The key '{sort_key}' is not present in the CSV headers.")
    except Exception as e:
        print(f"An error occurred: {e}")


sort_contacts("people_data.csv", "Sorted_people_data.csv")
