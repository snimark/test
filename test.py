#!/usr/bin/env python

import sys
import argparse

init_test = __import__("__init__", {})

parser = argparse.ArgumentParser(description="process some integers.")

parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')



def output_args(args):
    print "provided args: %s" % args

if __name__ == "__main__":
    #args = sys.argv[1:]
    #init_test.init_testing(args)
    #output_args(args)

    args = parser.parse_args()
    print args.accumulate(args.integers)


