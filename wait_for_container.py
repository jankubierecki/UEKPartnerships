#!/usr/bin/env python3
import sys
import os
import io
from time import sleep

from compose.cli.main import TopLevelCommand, project_from_options
from contextlib import redirect_stdout

print("outside top")


def main():
    print("waiting for containers...", sys.argv[1:])


    print("all containers are ready")


print("outside")

if __name__ == "__main__":
    print("inside 1")
    main()
    print("inside 2")
