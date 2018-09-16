import hashlib
def md5(arg):
	return hashlib.md5(arg.encode("utf-8")).hexdigest()
machine = 'B8AAA-EEC64-DEAE3-0789A'
machine = machine.replace('-','')
login = '1111111111111111111111111'
subject = 'PhotoshopCS4'
input = machine + '&' + login + '&' + subject

secret1 = md5(input)[0:20].upper()
secret2 = md5(secret1).upper()

output = secret2[:5]+'-'+ secret2[5:10]+'-'+ secret2[10:15]+'-'+ secret2[15:20]
print(output)
