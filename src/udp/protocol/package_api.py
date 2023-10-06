START_PACKAGE_COMBINATION = [0x00, 0x11, 0x22, 0x33]
STOP_PACKAGE_COMBINATION = [0xcc, 0xdd, 0xee, 0xff]


class PackageAPI():
    def __init__(self):
        self.start_byte = 0
        self.stop_byte = 0

    def get_package(self, __buffer, __buffer_size):
        _is_package = False
        for _byte in range(__buffer_size):
            if(_is_package):
                if(__buffer[_byte : len(STOP_PACKAGE_COMBINATION) + _byte] == STOP_PACKAGE_COMBINATION):
                    self.stop_byte = _byte + len(STOP_PACKAGE_COMBINATION)
                    break
            else:
                if(__buffer[_byte : len(START_PACKAGE_COMBINATION) + _byte] == START_PACKAGE_COMBINATION):
                    self.start_byte = _byte
                    _is_package = True

        return __buffer[self.start_byte : self.stop_byte]