from random import choice


def string_encr(text, code):
    string = []
    simbols = ' 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    text_index = 0
    for index in range(len(text) * code):
        if index % code == 0 and text_index < len(text):
            string.append(text[text_index])
            text_index += 1
        else:
            string.append(choice(simbols))
    string = ''.join(string)
    return string


def string_desc(text, code):
    result = []
    for i in range(len(text)):
        if i % code == 0:
            result.append(text[i])
    result = ''.join(result)
    return result


if __name__ == '__main__':
    text = 'I have not failed. I just found 10,000 options that did not work. - Thomas Edison'
    code = 15
    string_encr = string_encr(text, code)
    print('String encr: ', string_encr)
    string_desc = string_desc(string_encr, code)
    print(string_desc)
