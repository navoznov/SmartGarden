import sys
import getopt
import Options


class OptionsParser:
    @staticmethod
    def parse():
        try:
            longopts = ["bot-id=", "bot-key=", "mqtt-server=", "db-filename="]
            argv = sys.argv[1:]
            opts, args = getopt.getopt(argv, "i:k:u:t:d", longopts)
            d = {}
            for a, v in opts:
                aa = a.replace('--', '')
                d[aa] = v
        except getopt.GetoptError as e:
            sys.exit(2)

        options = new Options(d["bot-id"], d["bot-key"], d["mqtt-server"], d["db-filename"])
        return options
