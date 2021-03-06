#!/usr/bin/python3

import subprocess
import sys


def main():
    gclient_cmd = ('cd third_party/gn '
                   '&& python build/gen.py')

    try:
        rc = subprocess.call(gclient_cmd, shell=True)
    except OSError:
        print('could not run "%s" via shell' % gclient_cmd)
        sys.exit(1)

    if rc:
        print('failed command: "%s"' % gclient_cmd)
        sys.exit(1)

    print('fetched gn dependencies')

if __name__ == '__main__':
    main()
