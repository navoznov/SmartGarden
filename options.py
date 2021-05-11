import sys, getopt


class Options:
    def __init__(self, telegram_bot_token: str, mqtt_server: str, db_filename: str, is_debug_mode: bool):
        self.telegram_bot_token = telegram_bot_token
        self.mqtt_server = mqtt_server
        self.db_filename = db_filename
        self.is_debug_mode = is_debug_mode


def __parse() -> Options:
    try:
        longopts = ["bot-token=", "mqtt-server=", "db-filename=", "debug-mode="]
        argv = sys.argv[1:]
        opts, args = getopt.getopt(argv, "t:m:b:d", longopts)
        args = {}
        for a, v in opts:
            aa = a.replace('--', '')
            args[aa] = v
    except getopt.GetoptError as e:
        sys.exit(2)

    options = Options(args["bot-token"], args["mqtt-server"], args["db-filename"], bool(args.get("debug-mode", False)))
    return options


options = __parse()
