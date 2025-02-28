import pprint
import iso8583
from iso8583.specs import default as spec, field48private, postilionprivate

try:
    while True:
        bytestring = input("\nPlease enter 01xx/02xx/06xx hexstring:")
        encoded_raw = bytes.fromhex(bytestring)
        decoded, encoded = iso8583.decode(encoded_raw, spec, field48private, postilionprivate)
        #pprint.pp(encoded)
        pprint.pp(decoded)
        iso8583.pp(decoded, spec, field127spec=postilionprivate, line_width=120)
except EOFError:
    exit

