'''
using while loop controlled by flag
'''

#
def get_starting_number():
    '''
    ask for input until user response if any integer 1 or greater.\n
    returns integer equivalent of value user entered.
    '''
    stay_on_this = True
    while stay_on_this:
        user_raw = input('How many bottles of beer of the wall? ')
        user_str_prep = str(user_raw)
        user_str = user_str_prep.strip()
        if user_str.isnumeric() and user_str != '0':
            stay_on_this = False
        else:
            stay_on_this = True
    user = int(user_str)
    return user

def sing(initial):
    '''
    takes argument specifying how many bottles to start with.\n
    outputs lyrics to the song, starting from passed num of bottles.
    '''

    x = initial
    another_one = True

    while another_one:
        if x > 2:
            print(f'{x} bottles of beer on the wall, {x} bottles of beer.')
            print(f'Take one down, pass it around, {x-1} bottles of beer on the wall.')
            print('')
            x = x - 1
        elif x == 2:
            print(f'{x} bottles of beer on the wall, {x} bottles of beer.')
            print(f'Take one down, pass it around, {x-1} bottle of beer on the wall.')
            print('')
            x = x - 1
        else:
            print(f'{x} bottle of beer on the wall, {x} bottle of beer.')
            print('Take it down, pass it around, no more bottles of beer on the wall!')
            x = x - 1
            another_one = False
