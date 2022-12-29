# https://dev.mysql.com/doc/internals/en/capability-flags.html#packet-Protocol::CapabilityFlags
LONG_PASSWORD = 1
FOUND_ROWS = 1 << 1
LONG_FLAG = 1 << 2
CONNECT_WITH_DB = 1 << 3
NO_SCHEMA = 1 << 4
COMPRESS = 1 << 5
ODBC = 1 << 6
LOCAL_FILES = 1 << 7
IGNORE_SPACE = 1 << 8
PROTOCOL_41 = 1 << 9
INTERACTIVE = 1 << 10
SSL = 1 << 11
IGNORE_SIGPIPE = 1 << 12
TRANSACTIONS = 1 << 13
SECURE_CONNECTION = 1 << 15
MULTI_STATEMENTS = 1 << 16
MULTI_RESULTS = 1 << 17
PS_MULTI_RESULTS = 1 << 18
PLUGIN_AUTH = 1 << 19
CONNECT_ATTRS = 1 << 20
PLUGIN_AUTH_LENENC_CLIENT_DATA = 1 << 21
CAPABILITIES = (
    LONG_PASSWORD | LONG_FLAG | PROTOCOL_41 | TRANSACTIONS
    | SECURE_CONNECTION | MULTI_RESULTS
    | PLUGIN_AUTH | PLUGIN_AUTH_LENENC_CLIENT_DATA | CONNECT_ATTRS)

# Not done yet
HANDLE_EXPIRED_PASSWORDS = 1 << 22
SESSION_TRACK = 1 << 23
DEPRECATE_EOF = 1 << 24
