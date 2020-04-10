#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re;

def main():
    re_tel = re.compile( "^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$");
    with open("./file.txt", "r") as f:
        line = f.readline();
        while line:
            print(re_tel.match(line));
            line = f.readline();

if __name__ == "__main__":
    main();
