from src import ebx_checklist

obj_Checklist = ebx_checklist.Options()

lst_Hosts = [{'IP': '15.128.89.74', 'DC': u'asia-dc'}, {'IP': '15.128.89.75', 'DC': u'asia-dc'}, {'IP': '15.128.89.76', 'DC': u'asia-dc'},
             {'IP': '15.128.89.77', 'DC': u'asia-dc'}, {'IP': '15.128.89.78', 'DC': u'asia-dc'}, {'IP': '15.128.89.79', 'DC': u'asia-dc'},
             {'IP': '15.128.89.80', 'DC': u'asia-dc'}, {'IP': '15.128.89.81', 'DC': u'asia-dc'}, {'IP': '15.128.89.88', 'DC': u'asia-dc'},
             {'IP': '15.128.89.89', 'DC': u'asia-dc'}, {'IP': '15.128.89.90', 'DC': u'asia-dc'}, {'IP': '15.128.89.91', 'DC': u'asia-dc'},
             {'IP': '15.128.89.92', 'DC': u'asia-dc'}, {'IP': '15.128.89.93', 'DC': u'asia-dc'}, {'IP': '15.128.89.94', 'DC': u'asia-dc'},
             {'IP': '15.128.89.95', 'DC': u'asia-dc'}, {'IP': '15.128.89.96', 'DC': u'asia-dc'}, {'IP': '15.128.89.97', 'DC': u'asia-dc'},
             {'IP': '15.128.89.98', 'DC': u'asia-dc'}, {'IP': '15.128.89.99', 'DC': u'asia-dc'}, {'IP': '15.128.89.100', 'DC': u'asia-dc'},
             {'IP': '15.128.89.101', 'DC': u'asia-dc'}, {'IP': '15.128.89.102', 'DC': u'asia-dc'}, {'IP': '15.128.89.103', 'DC': u'asia-dc'},
             {'IP': '15.130.89.74', 'DC': u'eu-dc'}, {'IP': '15.130.89.75', 'DC': u'eu-dc'}, {'IP': '15.130.89.76', 'DC': u'eu-dc'},
             {'IP': '15.130.89.77', 'DC': u'eu-dc'}, {'IP': '15.130.89.78', 'DC': u'eu-dc'}, {'IP': '15.130.89.79', 'DC': u'eu-dc'},
             {'IP': '15.130.89.80', 'DC': u'eu-dc'}, {'IP': '15.130.89.81', 'DC': u'eu-dc'}, {'IP': '15.130.89.82', 'DC': u'eu-dc'},
             {'IP': '15.130.89.83', 'DC': u'eu-dc'}, {'IP': '15.130.89.84', 'DC': u'eu-dc'}, {'IP': '15.130.89.85', 'DC': u'eu-dc'},
             {'IP': '15.130.89.92', 'DC': u'eu-dc'}, {'IP': '15.130.89.93', 'DC': u'eu-dc'}, {'IP': '15.130.89.94', 'DC': u'eu-dc'},
             {'IP': '15.130.89.95', 'DC': u'eu-dc'}, {'IP': '15.130.89.96', 'DC': u'eu-dc'}, {'IP': '15.130.89.97', 'DC': u'eu-dc'},
             {'IP': '15.130.89.98', 'DC': u'eu-dc'}, {'IP': '15.130.89.99', 'DC': u'eu-dc'}, {'IP': '15.130.89.100', 'DC': u'eu-dc'},
             {'IP': '15.130.89.101', 'DC': u'eu-dc'}, {'IP': '15.130.89.102', 'DC': u'eu-dc'}, {'IP': '15.130.89.103', 'DC': u'eu-dc'},
             {'IP': '15.135.51.19', 'DC': u'america-dc'}, {'IP': '15.135.51.20', 'DC': u'america-dc'}, {'IP': '15.135.51.21', 'DC': u'america-dc'},
             {'IP': '15.135.51.22', 'DC': u'america-dc'}, {'IP': '15.135.51.23', 'DC': u'america-dc'}, {'IP': '15.135.51.24', 'DC': u'america-dc'},
             {'IP': '15.135.187.74', 'DC': u'america-dc'}, {'IP': '15.135.187.75', 'DC': u'america-dc'}, {'IP': '15.135.187.76', 'DC': u'america-dc'},
             {'IP': '15.135.187.77', 'DC': u'america-dc'}, {'IP': '15.135.187.78', 'DC': u'america-dc'}, {'IP': '15.135.187.79', 'DC': u'america-dc'},
             {'IP': '15.135.187.86', 'DC': u'america-dc'}, {'IP': '15.135.187.87', 'DC': u'america-dc'}, {'IP': '15.135.187.88', 'DC': u'america-dc'},
             {'IP': '15.135.187.89', 'DC': u'america-dc'}, {'IP': '15.135.187.90', 'DC': u'america-dc'}, {'IP': '15.135.187.91', 'DC': u'america-dc'},
             {'IP': '15.135.187.92', 'DC': u'america-dc'}, {'IP': '15.135.187.93', 'DC': u'america-dc'}, {'IP': '15.135.187.94', 'DC': u'america-dc'},
             {'IP': '15.135.187.95', 'DC': u'america-dc'}, {'IP': '15.135.187.96', 'DC': u'america-dc'}, {'IP': '15.135.187.97', 'DC': u'america-dc'}]

lst_OptionDCs = [d['DC'] for d in {v['DC']:v for v in lst_Hosts}.values()]
print("\033c")

###################################################################################################################################

lst_DataCentersCheck = obj_Checklist.get_OptionList('DC to restart', 5, 20, 20, lst_OptionDCs, ClearLine=True, Options_Index=-1)

lst_indexes = [index for index in range(len(lst_DataCentersCheck)) if lst_DataCentersCheck[index] == 1]
lst_DataCentersFilter = [lst_OptionDCs[i] for i in lst_indexes]

lst_OptionHosts = [d['DC'] + ' - ' + d['IP'] for d in lst_Hosts if d['DC'] in lst_DataCentersFilter]

lst_HostsCheck = obj_Checklist.get_CheckList('Hosts to restart', 5, 120, 20, lst_OptionHosts, ClearLine=False, Options_sets=[])
   
lst_tmp_hosts = [d['IP'] for d in lst_Hosts if d['DC'] in lst_DataCentersFilter]
lst_indexes = [index for index in range(len(lst_HostsCheck)) if lst_HostsCheck[index] == 1]
lst_DataCentersFilter = [lst_tmp_hosts[i] for i in lst_indexes]

for host in lst_DataCentersFilter:
    print(host)
    

###################################################################################################################################

lst_DataCentersCheck = obj_Checklist.get_CheckList('DC to restart', 5, 20, 20, lst_OptionDCs, ClearLine=True, Options_sets=[])

if lst_DataCentersCheck == -1:
    print('Canceled 1')
else:    
    lst_indexes = [index for index in range(len(lst_DataCentersCheck)) if lst_DataCentersCheck[index] == 1]
    lst_DataCentersFilter = [lst_OptionDCs[i] for i in lst_indexes]

    lst_OptionHosts = [d['DC'] + ' - ' + d['IP'] for d in lst_Hosts if d['DC'] in lst_DataCentersFilter]

    lst_HostsCheck = obj_Checklist.get_CheckList('Hosts to restart', 5, 120, 20, lst_OptionHosts, ClearLine=False, Options_sets=[])
    if lst_HostsCheck == -1:
        print('Canceled 2')
    else:    
        lst_tmp_hosts = [d['IP'] for d in lst_Hosts if d['DC'] in lst_DataCentersFilter]
        lst_indexes = [index for index in range(len(lst_HostsCheck)) if lst_HostsCheck[index] == 1]
        lst_DataCentersFilter = [lst_tmp_hosts[i] for i in lst_indexes]

        for host in lst_DataCentersFilter:
            print(host)
   