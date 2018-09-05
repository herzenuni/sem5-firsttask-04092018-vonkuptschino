nums = { 0:'null', 1:'eins', 2:'zwei', 3:'drei', 4:'fier', 5:'fünf', 6:'sechs', 7:'sieben', 8:'acht', 9:'neun' }

def inputChecker(func):
    def inner(data):
        data = (str(data)).split()
        try:
            data[0] = int(data[0])
        except (IndexError, ValueError):
            return 'First argument is not an integer'
        if data[0] not in nums.keys():
            return 'First argument is not a digit from 0 to 9'
        if len(data) == 2:
            if data[1] not in ['bin', 'oct', 'hex']:
                return 'conversion is not correct'
        if len(data) > 2:
            return 'that was too much'
        return func(data)
    return inner

@inputChecker #decor!!!1
def converter(data):
    if len(data) == 1:
        return nums[data[0]]
    if len(data) == 2:
        number = int(data[0])
        conversion = data[1]
        if conversion == 'bin':
            return bin(number)
        if conversion == 'oct':
            return oct(number)
        if conversion == 'hex':
            return hex(number)

def test_converter():
    assert converter(7) == 'sieben'
    assert converter(';') == 'First argument is not an integer'
    assert converter('-4') == 'First argument is not a digit from 0 to 9'
    assert converter('4 44') == 'conversion is not correct'
    assert converter('1 2 3') == 'that was too much'
    assert converter('44 oct 4') == 'First argument is not a digit from 0 to 9'

if __name__ == '__main__':
    test_converter()
    
    data = input('Input \'digit\' or \'digit conversion\' using space key: ')
    print(converter(data))