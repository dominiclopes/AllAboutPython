import os

datestr = os.system("date -d -3 day +%Y-%m-%d")
list_of_cves = os.system("mysql -u qa-security nvd -e 'select cve_id from nvd.cves where last_modified > '{}' "
                         "and qas is Null;'|grep -v cve_id".format(datestr))
cves_data = os.system("mysql -u qa-security nvd -e 'select * from nvd.cves where last_modified > '{}' "
                      "and qas is Null;'".format(datestr))

print(list_of_cves)
print("*" * 50)
print(cves_data)