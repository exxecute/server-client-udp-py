import yaml

class YamlServerConfigAPI():
    def __init__(self, config_path):
        self.ip = 0
        self.port = "0.0.0.0"

        self.parse_config(config_path)

    def get_ip(self):
        return self.ip
    
    def get_port(self):
        return self.port
    
    def parse_config(self, config):
        with open(config, 'r') as file:
            config_dict = yaml.safe_load(file)
        self.ip = config_dict['IP']
        self.port = config_dict['port']