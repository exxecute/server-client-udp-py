from udp.protocol.protocol import ProtocolCode, Protocol

REQUEST_SIZE = 1
ANSWER_SIZE = 1
TEST_BYTE_INDEX = 7

class ProtocolTest(Protocol):
    def __init__(self):
        super().__init__(self, 
                         code_request= ProtocolCode.PROTOCOL_TEST_REQ,
                         size_request= REQUEST_SIZE,
                         code_answer= ProtocolCode.PROTOCOL_TEST_ASW,
                         size_answer= ANSWER_SIZE)
        print("test protocol")
        self.test_byte = 0

    # def process_package(self, __package):
    #     # if self.validate_recieved_package(__package, self.code_answer):
    #     print(__package[TEST_BYTE_INDEX])

