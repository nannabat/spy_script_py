import Inventory_functions
from pprint import pprint
Inventory_list = ['Disks','DNSHostName','Domain','Softwares']
Inventory_list.sort()
return_dict_all_values = {}
Disks_value = Inventory_functions.get_disks_info()
Softwares_value = Inventory_functions.get_softwares_info()
Domain_value = Inventory_functions.get_dna()
DNSHostName_value = Inventory_functions.get_dom()
for value in Inventory_list:
	return_dict_value_var = value + '_value'
	return_dict_all_values{value} = return_dict_value_var
pprint(return_dict_all_values)

