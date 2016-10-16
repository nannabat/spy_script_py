import Inventory_functions
from pprint import pprint
<<<<<<< HEAD
Inventory_list = ['Disks','DNSHostName','Domain','ReportDateTime','Manufacturer','Model','NumberOfLogicalProcessors','NumberOfProcessors','Softwares']
=======
Inventory_list = ['Disks','SystemFamily','DNSHostName','Domain','ReportDateTime','Manufacturer','Model','NumberOfLogicalProcessors','NumberOfProcessors','Softwares']
>>>>>>> be0a083baadbbfa1af6141971ea191eef1a1e0f1
Inventory_list.sort()
value_set = {}
return_dict_all_values = {}

value_set['Disks'] = Inventory_functions.get_disks_info()
value_set['Softwares'] = Inventory_functions.get_softwares_info()
value_set['ReportDateTime'] = Inventory_functions.get_tm()
value_set['Domain'] = Inventory_functions.get_dna()
value_set['Manufacturer'] = Inventory_functions.get_mani()
value_set['Model'] = Inventory_functions.get_mod()
value_set['NumberOfLogicalProcessors'] = Inventory_functions.get_proc1()
value_set['NumberOfProcessors'] = Inventory_functions.get_proc2()
<<<<<<< HEAD

=======
value_set['SystemFamily'] = Inventory_functions.get_fami()
>>>>>>> be0a083baadbbfa1af6141971ea191eef1a1e0f1
value_set['DNSHostName'] = Inventory_functions.get_dom()
for value in Inventory_list:
        Disks = Inventory_functions.get_disks_info()
	return_dict_all_values[value] = value_set[value]
pprint(return_dict_all_values)
