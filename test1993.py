import pprint
import iso8583
from iso8583.specs import v1993 as spec

try:
    while True:
        bytestring = input("\nPlease enter 12xx hexstring:")
        encoded_raw = bytes.fromhex(bytestring)
        decoded, encoded = iso8583.decode(encoded_raw, spec)
        #pprint.pp(encoded)
        pprint.pp(decoded)
except EOFError:
    exit
