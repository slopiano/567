import unittest
import json
from unittest.mock import Mock
import MRTD
from MRTD import scan_MRZ, decode_string, incode_string, checksum

class TestForErrors(unittest.TestCase):
    def test_scan_MRZ(self):
        json = Mock()
        json.load.return_value = ["P<GBRTHATCHER<<HILLARY<<<<<<<<<<<<<<<<<<<<<<","8656069044GBR6608073M1601013668035532<<<<<84"]
        scan_MRZ()
        passport_string = ["P<GBRTHATCHER<<HILLARY<<<<<<<<<<<<<<<<<<<<<<","8656069044GBR6608073M1601013668035532<<<<<84"]
        assert passport_string == ["P<GBRTHATCHER<<HILLARY<<<<<<<<<<<<<<<<<<<<<<","8656069044GBR6608073M1601013668035532<<<<<84"]

    def test_decode_string(self):
        MRTD.passport_string = ["P<GBRTHATCHER<<HILLARY<<<<<<<<<<<<<<<<<<<<<<","8656069044GBR6608073M1601013668035532<<<<<84"]
        decode_string()
        assert MRTD.passport_class.d_type == "P"
        assert MRTD.passport_class.c_code_top == "GBR"
        assert MRTD.passport_class.l_name == "THATCHER"
        assert MRTD.passport_class.f_name == "HILLARY"
        assert MRTD.passport_class.m_name == ""
        assert MRTD.passport_class.pass_num == "865606904"
        assert MRTD.passport_class.check_pass_num == 4
        assert MRTD.passport_class.c_code_bot == "GBR"
        assert MRTD.passport_class.birth_date == "660807"
        assert MRTD.passport_class.check_birth_date == 3
        assert MRTD.passport_class.expiration == "160101"
        assert MRTD.passport_class.check_expiration == 3
        assert MRTD.passport_class.personal_number == "668035532"
        assert MRTD.passport_class.final_check == 4

    def test_incode_string(self):
        MRTD.passport_class.d_type == "P"
        MRTD.passport_class.c_code_top == "GBR"
        MRTD.passport_class.l_name == "THATCHER"
        MRTD.passport_class.f_name == "HILLARY"
        MRTD.passport_class.m_name == ""
        MRTD.passport_class.pass_num == "865606904"
        MRTD.passport_class.check_pass_num == 4
        MRTD.passport_class.c_code_bot == "GBR"
        MRTD.passport_class.birth_date == "660807"
        MRTD.passport_class.check_birth_date == 3
        MRTD.passport_class.expiration == "160101"
        MRTD.passport_class.check_expiration == 3
        MRTD.passport_class.personal_number == "668035532"
        MRTD.passport_class.final_check == 4
        incode_string()
        assert MRTD.passport_string == ["P<GBRTHATCHER<<HILLARY<<<<<<<<<<<<<<<<<<<<<<","8656069044GBR6608073M1601013668035532<<<<<84"]

    def test_checksum(self):
        assert checksum("255346242") == 1
        assert checksum("4N89D0ED") == 4
        assert checksum("23OI40KJDN239") == 8
        assert checksum("98JHVD972490KJBHSAKJNL9874359876BKJHV") == 8

if __name__ == '__main__':
    unittest.main()