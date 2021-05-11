import sys, getopt
from typing import List


class Options:
    def __init__(self, telegram_bot_token: str, admin_ids: List[int], mqtt_server: str, db_filename: str, is_debug_mode: bool):
        self.telegram_bot_token = telegram_bot_token
        self.admin_ids = admin_ids          # идентификаторы юзеров в телеграме, которые имеют право управлять теплицей
        self.mqtt_server = mqtt_server
        self.db_filename = db_filename
        self.is_debug_mode = is_debug_mode


def __parse() -> Options:
    try:
        longopts = ["bot-token=", "admin-ids=", "mqtt-server=", "db-filename=", "debug-mode="]
        argv = sys.argv[1:]
        opts, args = getopt.getopt(argv, "t:a:m:b:d", longopts)
        args = {}
        for a, v in opts:
            aa = a.replace('--', '')
            args[aa] = v
    except getopt.GetoptError as e:
        sys.exit(2)

    admin_ids = [int(x) for x in args.get("admin-ids", "").split(',')]
    is_debug_mode = bool(args.get("debug-mode", False))

    options = Options(args["bot-token"], admin_ids, args["mqtt-server"], args["db-filename"], is_debug_mode)
    return options


options = __parse()
