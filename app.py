import xml.etree.ElementTree as ET

smsTest = open("smsFull.xml", "r")


# for sms in smsTest.readlines():
#  print(sms)


input = smsTest
sms = ET.fromstring(input)
lst = sms.findall('smss')
print('message count:', len(lst))
for item in lst:
    print('sms'), item.find('address').text

smsTest.close()
