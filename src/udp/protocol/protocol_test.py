from udp.protocol.protocol import *

REQUEST_CODE = 0x01
REQUEST_SIZE = 3

ANSWER_CODE = 0x01

ANSWER_BYTE_INDEX = 4

class TestProtocol():
    def __init__(self, test_byte):
        self.test_byte = test_byte

        self.answer_test_byte = 0


    def get_request(self):
        request_package = []

        request_package.append(START_BYTE)
        request_package.append(REQUEST_SIZE)
        request_package.append(REQUEST_CODE)
        request_package.append(self.test_byte)
        request_package.append(STOP_BYTE)

        return request_package
    
    def answer_get_test_byte(self, package):
        return package[ANSWER_BYTE_INDEX]