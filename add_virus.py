with open('virus_base.txt','w') as f:
	byte = '\n\t\t# Anythi'
	f.write(byte)
	byte = '\x03\x00\x00\x80\x02\x00\x00\x00\x0f\x00\x00'
	f.write(byte)
f.close()