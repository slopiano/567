import json
import time
import MRTD
import unittest
from MRTD import incode_string, checksum
from Passport import Passport


f = open('records_decoded.json')
data = json.load(f)
# This function loads the given sample from the json file
records = data.get("records_decoded", [])
f.close()

# Calculates the runtime for the first 100 records
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


# Calculates the run time for the records 1000 up to 10000 stepping 1000 each time.
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


f = open('records_encoded.json')
data = json.load(f)
# This function loads the given sample from the json file
records_encoded = data.get("records_encoded", [])
f.close()

class TestForErrors(unittest.TestCase):
    def test_first_100(self):
        # Calculates the runtime for the first 100 records
        first100 = records[0:100]
        start_time = time.time()
        idx=0
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
            self.assertEqual(';'.join(MRTD.passport_string), records_encoded[idx])
            idx+=1
        print(f'Total time to complete first 100 with unit tests is : {time.time()-start_time} seconds')

    def test_10000(self):
        # Calculates the run time for the records 1000 up to 10000 stepping 1000 each time.
        prev_i = 0
        start_time = time.time()
        for i in range(1000, 10001, 1000):
            records_to_test = records[prev_i:i]
            idx = prev_i
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
                self.assertEqual(';'.join(MRTD.passport_string), records_encoded[idx])
                idx+=1
            print(f'Total time to complete {i} records with unit tests is : {time.time()-start_time} seconds')


if __name__ == '__main__':
    unittest.main()