from enum import Enum

CODE_ANSWER = 0x80

class ProtocolCode(Enum):
    PROTOCOL_TEST_REQ = 0x01
    PROTOCOL_FILE_REQ = 0x02

    PROTOCOL_TEST_ASW = PROTOCOL_TEST_REQ + CODE_ANSWER
    PROTOCOL_FILE_ASW = PROTOCOL_FILE_REQ + CODE_ANSWER

PROTOCOL_CODE_INDEX = 4
PROTOCOL_PACKAGE_SIZE_INDEX = 5

class Protocol():
    def __init__(self, code_request, code_answer, size_request, size_answer):
        self.code_request = code_request
        self.size_request = size_request

        self.code_answer = code_answer
        self.size_request = size_answer

    def validate_recieved_package(self, __package, __code):
        return __code == __package[4] # mb here validate size