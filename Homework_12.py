############################################
#Homework_12 Task_1
############################################
import csv

# Open the input Titanic CSV file
with open('titanic.csv', mode='r', newline='') as infile:
    reader = csv.reader(infile)

    # Read the header (first row)
    header = next(reader)

    # Open the output survived CSV file
    with open('survived.csv', mode='w', newline='') as outfile:
        writer = csv.writer(outfile)

        # Write the header to the output file
        writer.writerow(header)

        # Filter rows where the 'Survived' column is 1
        survived_index = header.index('Survived')  # Find the index of 'Survived' column

        # Iterate through rows, write only those who survived
        for row in reader:
            if row[survived_index] == '1':  # Check if the passenger survived
                writer.writerow(row)

print("Survived passengers' data has been written to 'survived.csv'.")

############################################


############################################
#Homework_12 Task_2
############################################
import csv

# Read the input CSV file
with open('organizations-100.csv', mode='r', newline='') as infile:
    reader = csv.reader(infile)

    # Read the header (first row)
    header = next(reader)

    # Read the rest of the data into a list
    data = list(reader)

# Find the index of the 'Number of Employees' column (assuming it's named something like that)
employees_index = header.index('Number of employees')

# Sort the data based on the 'Number of Employees' column (convert to integer for numeric sorting)
sorted_data = sorted(data, key=lambda x: int(x[employees_index]))

# Write the sorted data to a new CSV file
with open('sorted_csv.csv', mode='w', newline='') as outfile:
    writer = csv.writer(outfile)

    # Write the header
    writer.writerow(header)

    # Write the sorted data
    writer.writerows(sorted_data)

print("Sorted data by number of employees has been written to 'sorted_csv.csv'.")

############################################


############################################
#Homework_12 Task_3
############################################
import csv

# Open the input organizations CSV file
with open('organizations-100.csv', mode='r', newline='') as infile:
    reader = csv.reader(infile)

    # Read the header (first row)
    header = next(reader)

    # Extract the necessary column indices
    id_index = header.index('Organization Id')
    company_name_index = header.index('Name')
    website_index = header.index('Website')
    industry_index = header.index('Industry')
    employees_index = header.index('Number of employees')

    # Open the output CSV file to write the filtered data
    with open('ssl_companies.csv', mode='w', newline='') as outfile:
        writer = csv.writer(outfile)

        # Write the new header to the output file
        writer.writerow(['ID', 'Company Name', 'Website', 'Industry', 'Number of Employees'])

        # Iterate through the rows and filter companies with SSL-protected websites (HTTPS)
        for row in reader:
            if row[website_index].startswith('https'):  # Check if website starts with 'https'
                # Write the selected columns to the new file
                writer.writerow([row[id_index], row[company_name_index], row[website_index], row[industry_index],
                                 row[employees_index]])

print("Filtered SSL-protected companies' data has been written to 'ssl_companies.csv'.")

############################################


