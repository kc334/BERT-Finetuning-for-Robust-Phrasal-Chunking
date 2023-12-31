# count sentences in file that have one word per line and two
# newlines between sentences

# the file can be gzipped but if so it must have the .gz filename
# suffix

# python count.py -i data/input.gz

import sys, argparse, re, gzip, logging

def countSentences(handle):
    contents = re.sub(r'\n\s*\n', r'\n\n', handle.read())
    contents = contents.rstrip()
    return len(contents.split('\n\n'))

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-i", "--inputfile", dest="inputfile", default=None, help="filename in the conll format")
    opts = argparser.parse_args()
    if opts.inputfile is None:
        logging.warning("using standard input")
        print(countSentences(sys.stdin))
    elif opts.inputfile[-3:] == '.gz':
        with gzip.open(opts.inputfile, 'rt') as f:
            print(countSentences(f))
    else:
        with open(opts.inputfile, 'r') as f:
            print(countSentences(f))

