'''2.9: Read a CSV file'''

# Get the ca-500.csv file
filename: str = 'ca-500.ca'

# Open the file within a context manager with the keyword with
with open('./ca-500.csv', 'r', encoding='utf-8') as f:

    # Read the first line. The header.
    headers: list[str] = f.readline().rstrip('\n').split(';')

    # In a for loop through all lines.
    for line in f:

        # For each line strip the newline character from the end with strip
        # Split the line into a list of values with split
        values: list[str] = line.rstrip('\n').split(';')
        d: dict[str, str] = dict(zip(headers, values))

        # Only select lines with city 'Montreal'
        if d['city'] == 'Montreal':

            # Print firstname, lastname, city and email
            print(
                f"{d['first_name']:15} {d['last_name']:20} {d['city']:25} {d['email']:35}"
            )

# Output:
# > python .\read_csv.py
# Mammie          Cisney               Montreal                  mammie@cox.net
# Tesha           Brang                Montreal                  tesha@aol.com
# Harris          Sheck                Montreal                  harris@cox.net
# Maddie          Foulds               Montreal                  maddie@hotmail.com
# Steffanie       Meinen               Montreal                  steffanie.meinen@cox.net
# Val             Bigaud               Montreal                  val_bigaud@aol.com
# Denny           Zeanah               Montreal                  denny_zeanah@zeanah.com
# Luann           Michon               Montreal                  luann@cox.net
# Verona          Jobst                Montreal                  verona_jobst@jobst.org
# Rikki           Montalgo             Montreal                  rikki@montalgo.com
# Ricki           Traux                Montreal                  ricki.traux@traux.com
# Clemencia       Momplaisir           Montreal                  cmomplaisir@yahoo.com
