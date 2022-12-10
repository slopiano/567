import json
import time
import MRTD
from MRTD import decode_string

f = open('records_encoded.json')
data = json.load(f)
# This function loads the given sample from the json file
records = data.get("records_encoded", [])
f.close()

first100 = records[0:100]
start_time = time.time()
for record in first100:
    MRTD.passport_string = record.split(';')
    decode_string()
print(f'Total time to complete first 100 is : {time.time()-start_time} seconds')

prev_i = 0
start_time = time.time()
for i in range(1000, 10001, 1000):
    records_to_test = records[prev_i:i]
    prev_i = i
    for record in records_to_test:
        MRTD.passport_string = record.split(';')
        decode_string()
    print(f'Total time to complete {i} records is : {time.time()-start_time} seconds')
