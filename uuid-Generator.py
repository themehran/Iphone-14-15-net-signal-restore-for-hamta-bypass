import uuid
unique_id = uuid.uuid4()
unique_id_str = unique_id.hex
print("UUID:",unique_id)
print("UUID HEX:", (unique_id_str))
print("UUID FOR Identifier:", "com.apple.cellular."+(unique_id_str))
