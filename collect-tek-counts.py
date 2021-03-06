# This Python script fetches Exposure Notification TEK count files for European Union countries from
# Trinity College Dublin's website (https://down.dsg.cs.tcd.ie/tact/tek-counts) and combines
# them into one CSV file, sorted by date.

import requests
from http import HTTPStatus

potentially_participating_countries = {
    'BE': 'Belgium',
    'EL': 'Greece',
    'LT': 'Lithuania',
    'PT': 'Portugal',
    'BG': 'Bulgaria',
    'ES': 'Spain',
    'LU': 'Luxembourg',
    'RO': 'Romania',
    'CZ': 'Czechia',
    'FR': 'France',
    'HU': 'Hungary',
    'SI': 'Slovenia',
    'DK': 'Denmark',
    'HR': 'Croatia',
    'MT': 'Malta',
    'SK': 'Slovakia',
    'DE': 'Germany',
    'IT': 'Italy',
    'NL': 'Netherlands',
    'FI': 'Finland',
    'EE': 'Estonia',
    'CY': 'Cyprus',
    'AT': 'Austria',
    'SE': 'Sweden',
    'IE': 'Ireland',
    'LV': 'Latvia',
    'PL': 'Poland',
    'IS': 'Iceland',
    'NO': 'Norway',
    'LI': 'Liechtenstein',
    'CH': 'Switzerland',
}

total_lines = []
for (country_code, country_name) in potentially_participating_countries.items():
    response = requests.get(f"https://down.dsg.cs.tcd.ie/tact/tek-counts/{country_code.lower()}-tek-times.csv")
    if response.status_code == HTTPStatus.OK:
        lines = response.content.decode('utf-8').splitlines()[1:]  # omit the CSV header line
        # filter out the dates before 01 sep 2020. Swap first and 2nd value in output.
        for line in lines:
            values = line.split(',')
            if values[1] >= '2020-09-01':
                total_lines.append("{},{},{},{}".format(values[1], values[0], values[2], values[3]))

# sort lines by date
total_lines.sort()

# print header and lines
print("Date,Country,TEKs,Cases")
for line in total_lines:
    print(line)
