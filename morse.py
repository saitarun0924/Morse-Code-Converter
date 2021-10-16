MORSE_CODE = { "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", "&": ".-...", "@": ".--.-.", ":": "---...", ",": "--..--", ".": ".-.-.-", "'": ".----.", '"': ".-..-.", "?": "..--..", "/": "-..-.", "=": "-...-", "+": ".-.-.", "-": "-....-", "(": "-.--.", ")": "-.--.-", "!": "-.-.--"}

def encrypt(msg):
    cipher = ""
    for letter in msg:
        if letter != " ":
            cipher += MORSE_CODE[letter] + " "
        else:
            cipher += "/ "
    return cipher[:-1]


def decrypt(msg):
    decipher = ""
    letters = msg.split(" ")
    for letter in letters:
        if letter != "/":
            decipher += list(MORSE_CODE.keys())[
                list(MORSE_CODE.values()).index(letter)
            ]
        else:
            decipher += " "

    return decipher


print("1. Encrypt the Text")
print("2. Decrypt the Text")
mode = int(input("Enter the mode : "))

if(mode==1):
  msg = input("Enter your message: ")
  result = encrypt(msg.upper())
  print(result)

elif(mode==2):
  msg = input("Enter your message: ")
  result = decrypt(msg)
  print(result)

else:
  print("Invalid Input")