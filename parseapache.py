
import re
from collections import Counter,OrderedDict
def apache_log_reader():
    myregex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' #fine out the Numeric values from log file consist of IP address

    with open("access.log", "r") as data:       #open the access.log file from directory
        log = data.read()
        my_iplist = re.findall(myregex,log)       #re is use for match other string
        ipcount = Counter(my_iplist)
        ipcount = OrderedDict(sorted(ipcount.items(), key=lambda kv: kv[1], reverse=True)) #lambda take one parameters plus key is use to compare before transform.
        #  OrderedDict:  collection data type

        # print("ipcount..",b)
        for ip, no in ipcount.items():
          print("IP Address from Log file  "  + str(ip) + " " + "Count against IP address "+ str(no))



if __name__ == '__main__':
    apache_log_reader()