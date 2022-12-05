class Passport:
    def __init__(self, d_type=None, c_code_top=None, l_name=None, f_name=None, m_name=None, 
    pass_num=None, check_pass_num=None, c_code_bot=None, birth_date=None, check_birth_date=None, 
    sex=None, expiration=None, check_expiration=None, personal_number=None, check_personal_number=None,
    final_check=None):
        self.d_type = d_type
        self.c_code_top = c_code_top
        self.l_name = l_name
        self.f_name = f_name
        self.m_name = m_name
        self.pass_num = pass_num
        self.check_pass_num = check_pass_num
        self.c_code_bot = c_code_bot
        self.birth_date = birth_date
        self.check_birth_date = check_birth_date
        self.sex = sex
        self.expiration = expiration
        self.check_expiration = check_expiration
        self.personal_number = personal_number
        self.check_personal_number = check_personal_number
        self.final_check = final_check
    
    def print_variables(self):
        for attribute, value in self.__dict__.items():
            print(attribute + ": " + str(value))