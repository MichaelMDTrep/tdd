#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Michael Trepanier"


import sys


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--data_dir', help='directory to save data to', type=str, default='glue_data')
    parser.add_argument('--tasks', help='tasks to download data for as a comma separated string',
                        type=str, default='all')
    return


def main(args):
    """Implementation of echo"""
    # your code here
    return


if __name__ == '__main__':
    main(sys.argv[1:])
