class Options:
    def __init__(self, telegram_bot_id: str, telegram_bot_apy_key: str, mqtt_server: str, db_filename: str):
        self.telegram_bot_id = telegram_bot_id
        self.telegram_bot_apy_key = telegram_bot_apy_key
        self.mqtt_server = mqtt_server
        self.db_filename = db_filename
