#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import getopt
from options import Options


class OptionsParser:
    @staticmethod
    def parse():
        try:
            longopts = ["bot-token=", "mqtt-server=", "db-filename="]
            argv = sys.argv[1:]
            opts, args = getopt.getopt(argv, "t:m:d", longopts)
            args = {}
            for a, v in opts:
                aa = a.replace('--', '')
                args[aa] = v
        except getopt.GetoptError as e:
            sys.exit(2)

        options = Options(args["bot-token"], args["mqtt-server"], args["db-filename"])
        return options