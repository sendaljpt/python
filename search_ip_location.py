import ipinfo
import time
access_token = 'PUT YOUR TOKEN'
handler = ipinfo.getHandler(access_token)
data = open("list_ip.txt", "r")
write_file = open("scan_result.txt", "w")
print("Starting scan bro....")
list_res = []
for x in data:
    try:
        ip_address = x.strip('\n')
        print("Scanning : {}".format(x))
        details = handler.getDetails(ip_address)
        item = {
            "ip": str(ip_address),
            "city": details.city,
            "region": details.region,
            "country": details.country
        }
        list_res.append(item)
    except:
        continue

write_file.write(str(list_res))
write_file.close()
print("Done :)")