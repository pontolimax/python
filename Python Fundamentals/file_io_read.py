'''2.8: Writing to and reading from a file'''

# Then create a new program
filename: str = 'file_io.csv'
key: str = 'var3'
value: str = '"Y"'

# Open the file in read mode
with open(filename, 'r', encoding='utf-8') as infile:
    # Read the header and split into a list of headers
    headers: list[str] = infile.readline().strip().split(',')
    # For each line split the line into values
    for line in infile:
        fields: list[str] = line.strip().split(',')
        # Create a dictionary with the header and the values using zip()
        dictionary: dict[str, str] = dict(zip(headers, fields))
        # Filter on one off the fields and print the lines
        if dictionary[key] == value:
            print(line, end='')
    infile.close()

# Output:
# > python .\file_io_read.py
# 1001,5,1.23,"Y"
# 1003,7,7.89,"Y"
