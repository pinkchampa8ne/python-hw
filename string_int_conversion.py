#write one program to do what str() function does and another to do what int() function does
#useful to know: 254 // 10 = 25 and 254 % 10 = 4
#to reverse a string use my_string[::-1] or str(reversed(my_string)) 

def str_to_int(my_input):
    if type(my_input) == str:
        allowable_char = ['0','1','2','3','4','5','6','7','8','9']
        corresponding_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        new_num = 0
        reverse_string = my_input[::-1]
        for char in range(len(reverse_string)):
            if reverse_string[char] not in allowable_char:
                raise ValueError('Cannot convert alphabet to integer.')
            else:
                for index in range(len(allowable_char)):
                    if reverse_string[char] == allowable_char[index]:
                        new_num = corresponding_num[index] * (10 ** char) + new_num
        print(new_num)
            
str_to_int(25.4)
str_to_int('254')
#str_to_int('Hello')

def float_to_int(my_input):
    if type(my_input) == float:
        allowable_char = ['0','1','2','3','4','5','6','7','8','9']
        test_str = str(my_input)
        new_str = ''
        for char in range(len(test_str)):
            if test_str[char] not in allowable_char:
                break
            else:
                new_str = new_str + test_str[char]
    str_to_int(new_str)    

float_to_int(25.4)

def int_to_str(my_input, mult = 1, remainder = 0, length = 1):
    if type(my_input) == int:
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        corresp_char = ['0','1','2','3','4','5','6','7','8','9']
        test_input = my_input
        while test_input > 10:
            remainder = remainder + ((test_input % 10) * mult)
            test_input = test_input // 10 
            mult = mult * 10
            length = length + 1
        new_str = ''
        for index in range(len(nums)):
            if test_input == nums[index]:
                new_str = new_str + corresp_char[index]
        if mult > 10 and remainder < 10:
            new_str = new_str + '0'
        if remainder < 10:
            for index in range(len(nums)):
                if remainder == nums[index]:
                    new_str = new_str + corresp_char[index]
        print(new_str, end='') #not really one new string like this
        if remainder > 10:
            int_to_str(my_input = remainder)
    print() #skips a line?

int_to_str(542)
int_to_str(868)
#int_to_str(104539837) # ??? doesn't work w 10 at start
int_to_str(100338474575)
int_to_str(847567639)

#hw - fix int_to_str; change any print statements within function to return
