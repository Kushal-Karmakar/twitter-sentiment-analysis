import os

class InitConfig():
    def __init__(self):
        self.config_file = self.get_file_path()

    def get_file_path(self):
        cwd = os.getcwd()
        config_file = "app\config\.env"
        config_file_path = os.path.join(cwd, config_file)
        return config_file_path


