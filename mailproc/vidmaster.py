#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Zoe vidmaster - https://github.com/rmed/zoe-vidmaster
#
# Copyright (c) 2015 Rafael Medina García <rafamedgar@gmail.com>
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('--mail-subject', dest='subject')
parser.add_argument('--msg-sender-alias', dest='sender')
parser.add_argument('--application/octet-stream', dest='script')

if __name__ == '__main__':
    args, unknown = parser.parse_known_args()

    if args.subject != "vidmaster":
        sys.exit(0)

    print("message dst=vidmaster&tag=compose&script=%s&sender=%s" % (
        args.script, args.sender))
