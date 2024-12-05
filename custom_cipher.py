# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
shift_amount = int(input('Enter a number between 1-25: '))

if shift_amount >= 1 and shift_amount <= 25:
    text = ''
    code = 0
    for char in cipher:
        code = ord(char)

        if not char.isalpha():
            text += chr(code)
            continue

        if code >= 65 and code <= 90:
            code += shift_amount
            if code > 90:
                code -= 26
                text += chr(code)
            else:
                text += chr(code)

        elif code >= 97 and code <= 122:
            code += shift_amount
            if code > 122:
                code -= 26
                text += chr(code)
            else:
                text += chr(code)

print(text)
