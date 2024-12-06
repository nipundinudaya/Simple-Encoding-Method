import base64

base64_data = "#Enter word what you need to encode#"
# 1step convert to the bytes
base64_data_byte = base64_data.encode("utf-8")

# 2step encoding the bytes using Base64
base64_bytes = base64.b64encode(base64_data_byte)

# 3step back to the string convert
base64_string = base64_bytes.decode('utf-8')

#output
print("Original Text:", base64_data)
print("Encoded Text:",base64_string )





