#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import getopt
from options import Options


class OptionsParser:
    @staticmethod
    def parse():
        try:
            longopts = ["bot-id=", "bot-key=", "mqtt-server=", "db-filename="]
            argv = sys.argv[1:]
            opts, args = getopt.getopt(argv, "i:k:u:t:d", longopts)
            args = {}
            for a, v in opts:
                aa = a.replace('--', '')
                args[aa] = v
        except getopt.GetoptError as e:
            sys.exit(2)

        options = Options(args["bot-id"], args["bot-key"], args["mqtt-server"], args["db-filename"])
        return options
