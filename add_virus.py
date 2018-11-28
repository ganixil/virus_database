with open('virus_base.txt','ab') as f:
	byte = b'\n\t\t# Anythi'
	f.write(byte)
	byte = b'\x03\x00\x00\x80\x02\x00\x00\x00\x0f\x00\x00'

	f.write(byte)

f.close()