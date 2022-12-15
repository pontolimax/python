'''2.8: Writing to and reading from a file'''

# First create a file with open and write mode
filename: str = 'file_io.csv'

with open(filename, 'w', encoding='utf-8') as outfile:
    # Write a header line to the file.
    outfile.write('ID,var1,var2,var3\n')
    # Write a couple of lines to the file.
    outfile.write('1001,5,1.23,"Y"\n')
    outfile.write('1002,6,4.56,"N"\n')
    outfile.write('1003,7,7.89,"Y"\n')
    outfile.write('1004,8,0.12,"N"\n')
    outfile.close()

# Output:
# > python .\file_io_write.py
# ID,var1,var2,var3
# 1001,5,1.23,"Y"
# 1002,6,4.56,"N"
# 1003,7,7.89,"Y"
# 1004,8,0.12,"N"
