# wutils

## src/path-name-handler/rename.py

Some files named with names in the format which starts with *numbers* to show their order: 

```
1-readable-string.txt, 2-readable.txt, ..., 9-readable.txt, 10-readable.txt, 11-readable.txt, ...
```

But when sort them by file name in File Manager, it lists with ugly order, such as:

```
1-readable-string.txt, 10-readable.txt, 11-readable.txt, 2-readable.txt, ...
```

To solve this, I wrote the `rename.py` util by adding '0'(s) at the beginning of the file names. Eg.

```
01-readable-string.txt, 02-readable.txt, ..., 09-readable.txt, 10-readable.txt, 11-readable.txt, ...
or 
001-readable-string.txt, 002-readable.txt, ..., 009-readable.txt, 010-readable.txt, 011-readable.txt, ..., 100.txt
or
0001-readable.txt, ..., 1000.txt, ...
```

usage:

```shell
src/path-name-handler/rename.py /path/to/folder/which/you/wanna/fck
```
This command will walk through all the sub directories and rename all the folder names and file names.

If you just want it works in the current folder, use the option `--onlytopdir`; 
If you want to replace ' ' with '_' in the names too, use `--space2underline` please. 

```shell
src/path-name-handler/rename.py --space2underline /path/to/folder/

src/path-name-handler/rename.py --onlytopdir /path/to/folder/

src/path-name-handler/rename.py --onlytopdir  --space2underline /path/to/folder/
```
