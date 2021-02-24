import sys, getopt


class Options:
    def __init__(self, telegram_bot_token: str, mqtt_server: str, db_filename: str):
        self.telegram_bot_token = telegram_bot_token
        self.mqtt_server = mqtt_server
        self.db_filename = db_filename


def __parse() -> Options:
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


options = __parse()
