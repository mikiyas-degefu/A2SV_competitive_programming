# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        is_email = False
        is_phone = False

        if '@' in s:
            is_email = True
        else:
            is_phone = True
        
        if is_email:
            s = s.lower()
            splitted_email = s.split('@')
            hashed_email = splitted_email[0][0] + "*" * 5 + splitted_email[0][-1] + "@" + splitted_email[1]
            return hashed_email

        else:
            cleanend_phone = s.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ','')

            last_ten_digit = cleanend_phone[-10::]
            code = cleanend_phone.replace(last_ten_digit, '')

            last_fout_digit = last_ten_digit[-4::]
            hashed = '***-***-' + last_fout_digit
            pre_code = ''

            if len(code) > 0:
                pre_code = '+' + '*' * len(code) + '-'


            return pre_code + hashed








        



        