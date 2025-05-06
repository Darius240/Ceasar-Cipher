import sys

def shift_letter(letter, key):
    return chr(((ord(letter) - ord('A') + key) % 26) + ord('A'))

def format_output(text):
    blocks = [text[i:i+5] for i in range(0, len(text), 5)]
    lines = [''.join(blocks[i:i+10]) for i in range(0, len(blocks), 10)]
    return '\n'.join([' '.join(line[j:j+5] for j in range(0, len(line), 5)) for line in lines])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit()

    key = int(sys.argv[1]) % 26
    input_text = ""

    for line in sys.stdin:
        input_text += line.strip().upper()

    only_letters = ''.join([c for c in input_text if c.isalpha()])
    encoded = ''.join([shift_letter(c, key) for c in only_letters])
    print(format_output(encoded))

