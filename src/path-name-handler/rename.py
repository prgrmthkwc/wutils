#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
from argparse import ArgumentParser
from os import listdir
from os.path import join

RE_STARTSWITH_NUMBER = "^([0-9]+)"


def get_max_starts_number_count_in_name(folder):
    """
    Get the max count of the numbers at the beginning of the name.

    Example: if there are three files in a folder: 1.filename-a, 10.filename-b, 112.filename-c ;
    then return 3 (the number count of '112').

    :param folder: the file names  and directory names in the folder to check, just current level.
    :return: 0 if no number at the beginning of the filename, otherwise return the count of the numbers
    """
    num_count = 0
    for f in listdir(folder):
        name = f.strip()
        startswith_nr = re.match(RE_STARTSWITH_NUMBER, name)
        if startswith_nr:
            nr = len(startswith_nr.group(0))
            if nr > num_count:
                num_count = nr

    return num_count


def rename_files_in_dir(folder, replace_space):
    if not os.path.isdir(folder):
        print("Warning: It's not a folder: %s. Do nothing!" % folder)
        return
    nr_count = get_max_starts_number_count_in_name(folder)
    if nr_count == 0 and not replace_space:
        return

    for f in listdir(folder):
        fsrc = join(folder, f)
        name = f.strip()
        startswith_nr = re.match(RE_STARTSWITH_NUMBER, name)
        if startswith_nr:
            nr = len(startswith_nr.group(0))
            if nr < nr_count:  # insert "0"s in the beginning.
                s0_name = '0' * (nr_count - nr) + name
                if replace_space and ' ' in s0_name:
                    s0_name = s0_name.replace(' ', '_')
                print("rename: %s ==> %s" % (fsrc, join(folder, s0_name)))
                os.rename(fsrc, join(folder, s0_name))
            else:
                if replace_space and ' ' in name:
                    name = name.replace(' ', '_')
                    print("rename: %s ==> %s" % (fsrc, join(folder, name)))
                    os.rename(fsrc, join(folder, name))

        else:
            need_rename = len(f) != len(name)  # had stripped the name

            if replace_space and ' ' in name:
                name = name.replace(' ', '_')
                need_rename = True

            if need_rename:
                print("rename: %s ==> %s" % (fsrc, join(folder, name)))
                os.rename(fsrc, join(folder, name))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("folder", help="specify the directory in which all the folder/file names will be renamed, include its sub-directories")
    parser.add_argument('--onlytopdir', help="only walk in the specify directory, NOT go through its sub-directories",
                        default=False, action='store_true')
    parser.add_argument('--space2underline', help="replace the spaces with underlines in folder/file names", default=False, action='store_true')
    # parser.add_argument('--no-space2underline', dest='space2underline', action='store_false')
    # parser.add_argument("-o", "--optional-arg", help="optional argument", dest="opt", default="default")
    # parser.add_argument("n", help="repeat time", type=int)
    # parser.add_argument("-u", "--user-name", dest="user_name")
    args = parser.parse_args()
    folder = args.folder
    if not os.path.isdir(folder):
        print("Error: You must specify a valid folder: %s. Do nothing!" % folder)
        sys.exit(-1)
    replace_space = args.space2underline
    only_walk_topdir = args.onlytopdir

    if only_walk_topdir:
        rename_files_in_dir(folder, replace_space)
    else:
        for (root, _, _) in os.walk(folder, topdown=False):
            rename_files_in_dir(root, replace_space)
