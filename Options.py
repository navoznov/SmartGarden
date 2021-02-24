class Options:
    def __init__(self, telegram_bot_token: str, mqtt_server: str, db_filename: str):
        self.telegram_bot_token = telegram_bot_token
        self.mqtt_server = mqtt_server
        self.db_filename = db_filename
