import rsa
import stdio
import sys


# Entry point.
def main():
    # take n (int) and d (int) as command-line arguments
    n = int(sys.argv[1])
    d = int(sys.argv[2])

    # Get the number of bits per character(width)
    width = rsa.bitLength(n)

    # get message from standard input
    message = ''
    while not stdio.isEmpty():
        message += stdio.readString()

    # get j as floored division of length of message by width
    j = len(message) // width

    # in a loop compute for decrypting and writing the message
    for i in range(j):
        s = message[(i * width):(i * width) + width]
        y = rsa.bin2dec(s)  # set y to decimal representation of s
        z = rsa.decrypt(y, n, d)  # decrypt y
        stdio.write(chr(z))  # write the message


if __name__ == '__main__':
    main()