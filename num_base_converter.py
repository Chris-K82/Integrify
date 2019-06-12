'''
Author: Chris Kraus
Input: A number formatted for the input number's base, the initial base,
and output base. Output: A string representative of a number converted
to the expected output base.
'''
import numpy as np

HEX_NUMS = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
            '6': '6', '7': '7', '8': '8', '9': '9', 'A': 10, 'B': 11, 'C': 12,
            'D': 13, 'E': 14, 'F': 15, '10': 'A', '11': 'B', '12': 'C',
            '13': 'D', '14': 'E', '15': 'F'}
HEX_BIN_NUMS = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
BIN_HEX_NUMS = {'0000': '0', '0001': '1', '0010': '2', '0011': '3',
                '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}    


def get_nums():
    '''
    Retrieves input from the user and validates the input before moving
    forward.
    '''
    original_num = input('Please enter the number you '
                         'would like to convert: ')
    original_num = original_num.replace(' ', '').upper()
    def get_org_base():
        try:
            original_base = int(input('Please enter the base for the '
                                        'number you just entered (i.e. 2 for'
                                        ' binary 16 for hexidecimal): '))
            return original_base
        except ValueError:
            print('\nPlease only enter whole numbers (i.e. Integers).')
            get_org_base()

    def get_out_base():
        try:
            output_base = int(input('Please enter the base '
                                    'for output number: '))
            return output_base
        except ValueError:
            print('\nPlease only enter whole numbers in range 1 - 100.')
            get_out_base()
    return original_num, get_org_base(), get_out_base()


def prepend_zeros(bin_num):
    '''
    Adds 0's to the front of the global num until len(global num) is evenly
    divisible by 4. This prevents errors later when using the dictionaries.
    '''
    if len(bin_num) % 4 != 0:
        return ((4 - (len(bin_num) % 4)) * '0') + bin_num
    return bin_num


def make_readable(bin_num):
    '''
    Places a space after every 4th bit to separate out the binary number to
    make it more human readable.
    '''
    index = 4
    while index < len(bin_num) and index != len(bin_num) - 1:
        bin_num = bin_num[:index] + ' ' + bin_num[index:]
        index += 5
    return bin_num



def conv_to_bin(original_num, original_base):
    '''
    @Params: original num, original base
    Output: A string representing the output num in binary form.
    '''
    bin_num = ''

    if original_base == 2:
        return make_readable(prepend_zeros(original_num))

    elif original_base == 16:
        for i in original_num:
            bin_num += HEX_BIN_NUMS[i]
        return make_readable(prepend_zeros(bin_num))
    else:
        try:
            if original_base != 10:
                original_num = int(conv_all_other_bases(original_num, original_base, 10))

            else:
                original_num = int(original_num)

            while int(original_num / 2) > 0:
                bin_num += str(original_num % 2)
                original_num = int(original_num / 2)
            bin_num += str(original_num % 2)
            bin_num = bin_num[::-1]
            return make_readable(prepend_zeros(bin_num))

        except ValueError:
            print('Oops! Something went wrong. The program expected a number' +
                  f' but instead you entered: {original_num}')
            original_num = input('Please enter the number again formatted properly: ')
            return conv_to_bin(original_num, original_base)


def conv_to_hex(original_num, original_base):
    '''
    @Params: original num, original base
    Output: A string representing the output num in hexidecimal form.
    '''
    hex_num = ''
    try:
        if original_base == 2:
            start_index = 0
            end_index = 4
            while end_index < len(original_num) and end_index != len(original_num):
                hex_num += BIN_HEX_NUMS[original_num[start_index:end_index]]
                start_index = end_index
                end_index += 4
            hex_num += BIN_HEX_NUMS[original_num[start_index:]]
            return hex_num
        elif original_base == 16:
            return original_num
        else:
            if original_base != 10:
                original_num = int(conv_all_other_bases(original_num, original_base, 10))
            else:
                original_num = int(original_num)
            while int(original_num / 16) > 0:
                hex_num += HEX_NUMS[str(original_num % 16)]
                orgn_num = int(original_num / 16)
            hex_num += HEX_NUMS[str(original_num % 16)]
            return hex_num[::-1]
    except ValueError:
        print('Oops! Something went wrong. The program expected a number'
              f' but instead you entered: {original_num}')
        original_num = input('Please enter the number again formatted properly: ')
        return conv_to_hex(original_num, original_base)


def conv_all_other_bases(original_num, original_base, out_base):
    '''
    @Params: original num, original base, output base
    Output: A string representing the output num.
    '''
    try:
        output = ''
        org_base_pow = len(original_num) - 1
        base_10_num = 0
        if original_base == 16:
            for i in original_num:
                base_10_num += int(HEX_NUMS[i])*16**org_base_pow
                org_base_pow -= 1
            if out_base == 10:
                return base_10_num
        else:
            for i in original_num:
                base_10_num += int(i) * original_base ** org_base_pow
                org_base_pow -= 1
            while int(base_10_num / out_base) > 0:
                output += str(base_10_num % out_base)
                base_10_num = int(base_10_num / out_base)
            output += str(base_10_num % out_base)
        return output[::-1]
    except ValueError:
        print('Oops! Something went wrong. The program expected a number'
              f' but instead you entered: {original_num}')
        original_num = input('Please enter the number again formatted properly: ')
        return conv_all_other_bases(original_num, original_base, out_base)


def run_program():
    CONVERT_NUM = True

    while CONVERT_NUM:
        original_num, original_base, out_base = get_nums()
        if out_base == 2:
            print(conv_to_bin(original_num,original_base))
        elif out_base == 16:
            print(conv_to_hex(original_num, original_base))
        else:
            print(conv_all_other_bases(original_num, original_base, out_base))

        while CONVERT_NUM not in ['Y', 'N']:
            CONVERT_NUM = input('Would you like to convert another number? '
                                'Please enter "Y"/"N": ').upper()

        CONVERT_NUM = CONVERT_NUM[0] == 'Y'


run_program()
