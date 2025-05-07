# Secure Unpickling
#  Danger: pickle can execute arbitrary code if loading untrusted data.
#
#  Safer alternatives:
#
# JSON → for plain data (dict, list, string, number).
#
# marshal → for Python-only, low-level serialization (still not secure for untrusted data).
#
# Custom formats → like Protocol Buffers, MessagePack.