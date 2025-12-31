MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..',  'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....', 'I': '..',   'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',   'N': '-.',   'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',  'S': '...',  'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',  'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----','1': '.----','2': '..---','3': '...--','4': '....-',
    '5': '.....','6': '-....','7': '--...','8': '---..','9': '----.',
    ' ': '/'   # / == space
}

def alpha_to_morse(message):
    l = []
    for _ in message:
        _ = _.upper()
        l.append(MORSE_CODE[_])
    return "".join(l)

def morse_to_alpha(message):
   pass
ch = input("Morse to Alpha (1) | Alpha to Morse (2) : ")
if ch.upper() == "2":
    message = input("Enter message : ")
    print(alpha_to_morse(message))
elif ch.upper() == "1":
    message = input("Enter message : ")
    print(morse_to_alpha(message))