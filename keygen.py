import rsa
import stdio
import sys


# Entry point.
def main():
    # Accept lo (int) and hi (int) as command-line arguments
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])

    # get a as tuple using available function
    a = rsa.keygen(lo, hi)

    # write standard output
    stdio.writeln(str(a[0]) + ' ' + str(a[1]) + ' ' + str(a[2]))


if __name__ == '__main__':
    main()