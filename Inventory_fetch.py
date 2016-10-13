import Inventory_functions
from pprint import pprint
Inventory_list = ['Disks','DNSHostName','Domain','Softwares']
Inventory_list.sort()
return_dict_all_values = {}
Disks = Inventory_functions.get_disks_info()
Softwares = Inventory_functions.get_softwares_info()
Domain = Inventory_functions.get_dna()
DNSHostName = Inventory_functions.get_dom()
for value in Inventory_list:
	return_dict_all_values{value} = value
pprint(return_dict_all_values)

