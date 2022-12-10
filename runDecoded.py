import json
import time
import MRTD
from MRTD import incode_string, checksum
from Passport import Passport

f = open('records_decoded.json')
data = json.load(f)
# This function loads the given sample from the json file
records = data.get("records_decoded", [])
f.close()


first100 = records[0:100]
start_time = time.time()
for record in first100:
    record1 = record.get("line1")
    record2 = record.get("line2")
    name = record1.get("given_name").split(' ')
    if len(name) < 2:
        first_name = name[0]
        middle_name = ""
    else:
        first_name = name[0]
        middle_name = name[1]
    MRTD.passport_class = Passport("P",record1.get("issuing_country"),record1.get("last_name"),first_name,middle_name,
    record2.get("passport_number"),checksum(record2.get("passport_number")),record2.get("country_code"),
    record2.get("birth_date"),checksum(record2.get("birth_date")),record2.get("sex"),
    record2.get("expiration_date"),checksum(record2.get("expiration_date")),
    record2.get("personal_number"),checksum(record2.get("personal_number")))
    incode_string()
print(f'Total time to complete first 100 is : {time.time()-start_time} seconds')
# record = records[0]

# record1 = record.get("line1")
# record2 = record.get("line2")

# print(record1.get("issuing_country"))
# print(record1.get("last_name"))
# print(record1.get("given_name").split(' '))
# print('#################################################')
# print(record2.get("passport_number"))
# print(record2.get("country_code"))
# print(record2.get("birth_date"))
# print(record2.get("sex"))
# print(record2.get("expiration_date"))
# print(record2.get("personal_number"))

prev_i = 0
start_time = time.time()
for i in range(1000, 10001, 1000):
    records_to_test = records[prev_i:i]
    prev_i = i
    for record in records_to_test:
        record1 = record.get("line1")
        record2 = record.get("line2")
        name = record1.get("given_name").split(' ')
        if len(name) < 2:
            first_name = name[0]
            middle_name = ""
        else:
            first_name = name[0]
            middle_name = name[1]
        MRTD.passport_class = Passport("P",record1.get("issuing_country"),record1.get("last_name"),first_name,middle_name,
        record2.get("passport_number"),checksum(record2.get("passport_number")),record2.get("country_code"),
        record2.get("birth_date"),checksum(record2.get("birth_date")),record2.get("sex"),
        record2.get("expiration_date"),checksum(record2.get("expiration_date")),
        record2.get("personal_number"),checksum(record2.get("personal_number")))
        incode_string()
    print(f'Total time to complete {i} records is : {time.time()-start_time} seconds')
