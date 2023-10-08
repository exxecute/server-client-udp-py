import yaml

class YamlServerConfigAPI():
    def __init__(self, config_path):
        self.ip = 0
        self.port_reading = 0
        self.port_writing = 0

        self.parse_config(config_path)

    def get_ip(self):
        return self.ip
    
    def get_port_reading(self):
        return self.port_reading
    
    def get_port_writing(self):
        return self.port_writing
    
    def parse_config(self, config):
        with open(config, 'r') as file:
            config_dict = yaml.safe_load(file)
        self.ip = config_dict['IP']
        self.port_reading = config_dict['port_reading']
        self.port_writing = config_dict['port_writing']