'''2.9: Reading a CSV file with csv'''

# csv module from Python Standard Library
import csv

# Get the ca-500.csv file
filename: str = 'ca-500.csv'
colnames: tuple = ('first_name', 'last_name', 'city', 'email')

# Open the file within a context manager with the keyword with
with open(filename, 'r', encoding='utf-8') as f:

    # csv file reader
    reader: csv.DictReader = csv.DictReader(f, delimiter=';', quotechar='"')

    # In a for loop through all lines.
    for d in reader:

        # Only select lines with city 'Montreal'
        if d['city'] in 'Montreal':

            # Print firstname, lastname, city and email
            print(
                f"{d['first_name']:15} {d['last_name']:20} {d['city']:25} {d['email']:35}"
            )

# Output:
# > python .\read_csv_with_csv.py
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
