import re

if __name__ == '__main__':
    # strings = ['asd', 'sdf', 'asdasd', 'itc']
    # for string in strings:
    #     result = re.match("a", string)
    #     print(string, end=' ')
    #     if result:
    #         print(result.group())
    #     else:
    #         print()

    ret = re.match("[a-zA-Z0-9_]{3}", "12a3g45678")
    print(ret.group())

    ret = re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s34455ff66")
    print(ret.group())
