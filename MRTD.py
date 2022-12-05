import json
from Passport import Passport

# Global variable to hold Passport information that is parsed
passport_class = Passport

# Global variable that holds the unparsed passport string
passport_string = []

def scan_MRZ():
    """ This method mimics the hardware device. It pulls information from samples.json"""
    global passport_string
    f = open('samples.json')
    data = json.load(f)
    # This function loads the given sample from the json file
    passport_string = data['givenSample']
    f.close()

def decode_string():
    """ This method parses the strings from the passport """
    # First ensures that the passport class is global and can be used throughout project
    global passport_class

    # Top and bottom strings are seperated into first_string and second_string respectively
    first_string = passport_string[0]
    second_string = passport_string[1]
    # Top portion of the passport can be split with '<' for easier parsing
    # The bottom portion is only split by indexes
    first_string = first_string.split('<')

    # The Passport class is loaded with the parsed information from the two passport strings.
    passport_class = Passport(first_string[0], first_string[1][0:3], first_string[1][3:], first_string[3],
                        first_string[4], second_string[0:9], int(second_string[9]),
                        second_string[10:13], second_string[13:19], int(second_string[19]),
                        second_string[20], second_string[21:27], int(second_string[27]),
                        second_string[28:42],int(second_string[42]), int(second_string[43]))
    passport_class.personal_number = passport_class.personal_number.replace('<','')

    # Function that prints all of the passport information
    # passport_class.print_variables()

def incode_string():
    global passport_string

    # Reformats the top string of the passport from Passport class
    top_string = passport_class.d_type + '<' + passport_class.c_code_top + \
        passport_class.l_name + '<<' + passport_class.f_name + '<' + \
        passport_class.m_name
    
    # Add extra '<' characters so the string is at least 44 characters in length
    while len(top_string) < 44:
        top_string += '<'
    
    # Reformats the bottom string from the passport class.
    idx = 0
    bottom_string = ''
    for value in passport_class.__dict__.values():
        # Ensure the values that are in the top string aren't appended to the 
        # bottom string
        if idx < 5:
            idx+=1
            continue
        # This portion has the same 5 '<' characters - ensures the same passport format
        if idx == 14:
            bottom_string += '<<<<<'
        idx+=1
        # Append the elements that are in the bottom string
        bottom_string += str(value)
    
    # Put the reformatted string back into passport_string.
    # This will most likely be removed in the future, for now
    # it's here just to show that the function works properly
    passport_string = [top_string, bottom_string]

def checksum(check_string):
    """ Performs the checksum function """
    check = 0
    weight = [7,3,1]
    idx = 0
    for char in check_string:
        idx = idx%3
        if char == '<':
            pass
        elif char.isnumeric():
            check+= (int(char) * weight[idx])
        else:
            check += (ord(char) - ord('A') + 10) * weight[idx]
        idx+=1
    check = check%10
    return check

def check_passport():
    print(str(checksum(passport_class.pass_num)) + ':' + str(passport_class.check_pass_num))
    print(str(checksum(passport_class.birth_date)) + ':' + str(passport_class.check_birth_date))
    print(str(checksum(passport_class.expiration)) + ':' + str(passport_class.check_expiration))
    print(str(checksum(passport_class.personal_number)) + ':' + str(passport_class.check_personal_number))

# Driver code
if __name__ == '__main__':
    scan_MRZ()
    print(passport_string)
    decode_string()
    passport_class.print_variables()
    incode_string()
    print(passport_string)
    check_passport()