# -*- coding: utf-8 -*-
import os
import subprocess
from optparse import OptionParser


def execute(shell):
    p = subprocess.Popen(shell, shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    return stdout


def lint(ignore):
    for path, dirs, files in os.walk('.'):
        dirs[:] = [dir for dir in dirs if dir not in ignore]
        for file in files:
            if os.path.splitext(file)[1].lower() == '.py':
                file_abs_path = os.path.join(path, file)
                result = execute('pep8 %s' % (file_abs_path))
                if not result:
                    print '%s : pass' % (file_abs_path)
                else:
                    print result


def main():
    parser = OptionParser()
    parser.add_option('--ignore', dest='ignore', default=['venv'],
                      type='string', action='append')
    (options, args) = parser.parse_args()

    assert options.ignore

    lint(options.ignore)


if __name__ == '__main__':
    main()
