##############################################
# Homework_11 Task_1
##############################################
with open("output_1000_lines.txt", "w") as file:
    for line_num in range(1, 1001):
        file.write(f"Line {line_num}: Sample text for line {line_num}\n")

print("File 'output_1000_lines.txt' has been created with 1000 lines.")

filled_lines_count = 0
with open("output_1000_lines.txt", "r") as file:
    for line in file:
        # Strip whitespace and check if the line is non-empty
        if line.strip():
            filled_lines_count += 1

print(f"Number of filled lines: {filled_lines_count}")
##############################################



##############################################
# Homework_11 Task_2
##############################################
numbers = {
    2: "Second",
    8: "Eighth",
    10: "Tenth",
    13: "Thirteenth",
    17: "Seventeenth"
}

with open("output_specific_lines.txt", "w") as file:
    for line_num in range(1, 18):
        if line_num in numbers:
            file.write(f"{numbers[line_num]} line: {line_num}\n")
        else:
            file.write("\n")

print("File 'output_specific_lines.txt' has been created with the specified numbers on the correct lines.")
#############################################



##############################################
# Homework_11 Task_3
##############################################

file1 = 'file1.txt'
file2 = 'file2.txt'

merged_file = 'merged_output.txt'

with open(merged_file, 'w') as output_file:
    with open(file1, 'r') as f1:
        output_file.write(f1.read())

    with open(file2, 'r') as f2:
        output_file.write(f2.read())

print(f"Files '{file1}' and '{file2}' have been merged into '{merged_file}'.")

with open(merged_file, 'r') as f:
    combined_content = f.read()
    print("\nCombined file content:\n")
    print(combined_content)

#############################################


