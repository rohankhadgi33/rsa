import rsa
import stdio
import sys


# Entry point.
def main():
    # get n and e as CLI
    n = int(sys.argv[1])
    e = int(sys.argv[2])

    # Get the number of bits per character(width)
    width = rsa.bitLength(n)

    # get message from standard input
    message = ''
    while not stdio.isEmpty():
        message += stdio.readLine()
        message += '\n'

    # in a loop compute for encrypting and writing the message
    for i in range(len(message)):
        z = message[i: i + 1]  # take separate characters from string
        x = ord(z)  # turn z into an integer x
        y = rsa.encrypt(x, n, e)  # encrypt y
        w = rsa.dec2bin(y, width)  # change decimal to binary
        stdio.write(w)  # write the message
    stdio.writeln()  # write an empty line


if __name__ == '__main__':
    main()