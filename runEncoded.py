"""This file takes the raw data and puts the respective fields into the Passport class"""
import json
import time
import unittest
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

f = open('records_decoded.json')
data = json.load(f)
# This function loads the given sample from the json file
records_decoded = data.get("records_decoded", [])
f.close()

# "issuing_country"
# "last_name"
# "given_name"

# "passport_number"
# "country_code"
# "birth_date"
# "sex"
# "expiration_date"
# "personal_number"

class TestForErrors(unittest.TestCase):
    def test_first_100(self):
        first100 = records[0:100]
        start_time = time.time()
        idx = 0
        for record in first100:
            record_decoded = records_decoded[idx]
            record_decoded1 = record_decoded.get("line1")
            record_decoded2 = record_decoded.get("line2")
            MRTD.passport_string = record.split(';')
            decode_string()
            self.assertEqual(MRTD.passport_class.c_code_top, record_decoded1.get("issuing_country"))
            self.assertEqual(MRTD.passport_class.l_name, record_decoded1.get("last_name"))
            if MRTD.passport_class.m_name == "": 
                space = ""
            else:
                space = " "
            self.assertEqual(MRTD.passport_class.f_name+space+MRTD.passport_class.m_name, record_decoded1.get("given_name"))
            self.assertEqual(MRTD.passport_class.pass_num, record_decoded2.get("passport_number"))
            self.assertEqual(MRTD.passport_class.c_code_bot, record_decoded2.get("country_code"))
            self.assertEqual(MRTD.passport_class.birth_date, record_decoded2.get("birth_date"))
            self.assertEqual(MRTD.passport_class.sex, record_decoded2.get("sex"))
            self.assertEqual(MRTD.passport_class.expiration, record_decoded2.get("expiration_date"))
            self.assertEqual(MRTD.passport_class.personal_number, record_decoded2.get("personal_number"))
            idx+=1
        print(f'Total time to complete first 100 with unit tests is : {time.time()-start_time} seconds')
        
    def test_10000(self):
        start_time = time.time()
        prev_i = 0
        for i in range(1000, 10001, 1000):
            records_to_test = records[prev_i:i]
            idx = prev_i
            prev_i = i
            for record in records_to_test:
                record_decoded = records_decoded[idx]
                record_decoded1 = record_decoded.get("line1")
                record_decoded2 = record_decoded.get("line2")
                MRTD.passport_string = record.split(';')
                decode_string()
                self.assertEqual(MRTD.passport_class.c_code_top, record_decoded1.get("issuing_country"))
                self.assertEqual(MRTD.passport_class.l_name, record_decoded1.get("last_name"))
                if MRTD.passport_class.m_name == "": 
                    space = ""
                else:
                    space = " "
                self.assertEqual(MRTD.passport_class.f_name+space+MRTD.passport_class.m_name, record_decoded1.get("given_name"))
                self.assertEqual(MRTD.passport_class.pass_num, record_decoded2.get("passport_number"))
                self.assertEqual(MRTD.passport_class.c_code_bot, record_decoded2.get("country_code"))
                self.assertEqual(MRTD.passport_class.birth_date, record_decoded2.get("birth_date"))
                self.assertEqual(MRTD.passport_class.sex, record_decoded2.get("sex"))
                self.assertEqual(MRTD.passport_class.expiration, record_decoded2.get("expiration_date"))
                self.assertEqual(MRTD.passport_class.personal_number, record_decoded2.get("personal_number"))
                idx+=1
            print(f'Total time to complete {i} records with unit tests is : {time.time()-start_time} seconds')

if __name__ == '__main__':
    unittest.main()