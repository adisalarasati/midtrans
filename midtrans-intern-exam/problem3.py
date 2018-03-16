import string

validchars = string.digits
phone = input("Phone Number\t\t: ")
type(phone)
normalized = ''.join(c for c in phone if c in validchars)
if normalized[0] == '0':
    p = normalized.replace("0", "62", 1)
else:
    p = normalized
print("Normalized Phone Number\t:", p)
