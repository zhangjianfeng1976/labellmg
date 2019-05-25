#!/usr/bin/env python

import argparse


HELP_BLURB = (
    "To see help text, you can run:\n"
    "\n"
    "  labelImg --help\n"
)

USAGE = (
    "labelImg [arguments]\n"
    "%s" % HELP_BLURB
)

def parse_args(args):
    parser = argparse.ArgumentParser(description='labelImg app',
                                     formatter_class=argparse.RawTextHelpFormatter, usage=USAGE)
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' +
                        __version__, help='Get current %(prog)s version')
    parser.add_argument("--verbose", help="increase output verbosity")
    parser.add_argument("--predefine", help="pre-define label files")
    parser.add_argument("--image", help="the path of an image")
    return parse_args

