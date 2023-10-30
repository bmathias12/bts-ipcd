import configparser
import os
import sys

import pandas as pd

c = configparser.ConfigParser()
c.read('config.ini')

KEEP_COLS = ['CITY', 'STATE', 'ZIPCODE', 'FAC_NAME', 'LONGITUDE', 'LATITUDE', 
             'FAC_TYPE', 'MODE_BUS', 'MODE_RAIL', 'MODE_AIR', 'MODE_FERRY', 'MODE_BIKE',
             'MODES_SERV']

FAC_TYPE_MAP = {
    "1": "Airport",
    "2": "Intercity Bus",
    "5": "Intercity Rail",
    "6": "Transit or Local Ferry",
    "8": "Light Rail Transit",
    "9": "Heavy Rail Transit",
    "10": "Station Intercity Train",
    "11": "Station Commuter Train",
    "12": "Bike Share",
}

def main():
    df = pd.read_csv(c['default']['input_path'], dtype='str', usecols=KEEP_COLS)
    df['FAC_TYPE_DESC'] = df['FAC_TYPE'].map(FAC_TYPE_MAP)
    
    # Check if output exists, if so, exit
    if os.path.exists(c['default']['output_path']):
        print('Output file already exists. Please delete it first.')
        sys.exit(1)
    
    # Lowercase columns
    df.columns = [x.lower() for x in df.columns]

    # Write output
    df.to_csv(c['default']['output_path'], index=False)

if __name__ == '__main__':
    main()

