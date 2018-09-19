'''
Write a function called sed that takes as arguments a pattern string,
a replacement string, and two filenames; it should read the first file
and write the contents into the second file (creating it if necessary).
If the pattern string appears anywhere in the file, it should be
replaced with the replacement string.

If an error occurs while opening, reading, writing or closing files,
your program should catch the exception, print an error message,
and exit.
Solution: http://thinkpython2.com/code/sed.py.


Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''
from __future__ import print_function, division


def sed(p_string, r_string, source, dest):
    """Reads a source file and writes the destination file.

    In each line, replaces pattern with replace.

    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    fin = open(source, 'r')
    fout = open(dest, 'w')

    for line in fin:
        line = line.replace(p_string, re_string)
        fout.write(line)

    fin.close()
    fout.close()


def main():
    p_string = 'pattern'
    r_string = 'replace'
    source = 'sed_tester.txt'
    dest = source + '.replaced'
    sed(p_string, r_string, source, dest)


if __name__ == '__main__':
    main()
