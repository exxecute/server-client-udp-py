BYTE_C0 = 0xc0
BYTE_DB = 0xdb
BYTE_CE = 0xce

CODE_FIRST_BYTE = 0xdb

CODE_C0_SECOND_BYTE = 0xdc
CODE_DB_SECOND_BYTE = 0xdd
CODE_CE_SECOND_BYTE = 0xde

C0_CODE = [CODE_FIRST_BYTE, CODE_C0_SECOND_BYTE]
DB_CODE = [CODE_FIRST_BYTE, CODE_DB_SECOND_BYTE]
CE_CODE = [CODE_FIRST_BYTE, CODE_CE_SECOND_BYTE]

FIRST_BYTE = 0
SECOND_BYTE = 1
NEXT_BYTE = 1

WITHOUT_START_BYTE = 1
WITHOUT_STOP_BYTE = -1

class SlipProtocolApi():
    def code_package(self, package):
        coded_package = []
        coded_package.append(BYTE_C0)

        for byte in package[WITHOUT_START_BYTE : WITHOUT_STOP_BYTE]:
            if byte == BYTE_C0:
                for code_byte in C0_CODE:
                    coded_package.append(code_byte)

            elif byte == BYTE_DB:
                for code_byte in DB_CODE:
                    coded_package.append(code_byte)

            elif byte == BYTE_CE:
                for code_byte in CE_CODE:
                    coded_package.append(code_byte)

            else:
                coded_package.append(byte)

        coded_package.append(BYTE_CE)

        return coded_package

    def decode_package(self, package):
        decoded_package = []
        decoded_package.append(BYTE_C0)

        byte_index = WITHOUT_START_BYTE
        while byte_index != len(package[: WITHOUT_STOP_BYTE]):
            if (package[byte_index] == C0_CODE[FIRST_BYTE]) and (package[byte_index + NEXT_BYTE] == C0_CODE[SECOND_BYTE]):
                decoded_package.append(BYTE_C0)
                byte_index += NEXT_BYTE
            
            elif (package[byte_index] == DB_CODE[FIRST_BYTE]) and (package[byte_index + NEXT_BYTE] == DB_CODE[SECOND_BYTE]):
                decoded_package.append(BYTE_DB)
                byte_index += NEXT_BYTE
            
            elif (package[byte_index] == CE_CODE[FIRST_BYTE]) and (package[byte_index + NEXT_BYTE] == CE_CODE[SECOND_BYTE]):
                decoded_package.append(BYTE_CE)
                byte_index += NEXT_BYTE

            else:
                decoded_package.append(package[byte_index])

            byte_index+= NEXT_BYTE

        decoded_package.append(BYTE_CE)

        return decoded_package