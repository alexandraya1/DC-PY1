from pprint import pprint
dict_bin = [{'bin': bin(i), 'dec': i, 'oct': oct(i), 'hex': hex(i)} for i in range(16)]
pprint(dict_bin)
