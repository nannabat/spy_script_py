import Inventory_functions
from pprint import pprint
Inventory_list = ['Disks','DNSHostName','Domain','Softwares']
Inventory_list.sort()
value_set = {}
return_dict_all_values = {}
#Disks = Inventory_functions.get_disks_info()
value_set['Disks'] = Inventory_functions.get_disks_info()
#Softwares = Inventory_functions.get_softwares_info()
value_set['Softwares'] = Inventory_functions.get_softwares_info()
#pprint(Softwares)
#Domain = Inventory_functions.get_dna()
#pprint(Domain)
value_set['Domain'] = Inventory_functions.get_dna()
#DNSHostName = Inventory_functions.get_dom()
#pprint(DNSHostName)
value_set['DNSHostName'] = Inventory_functions.get_dom()
for value in Inventory_list:
        Disks = Inventory_functions.get_disks_info()
	return_dict_all_values[value] = value_set[value]
pprint(return_dict_all_values)

