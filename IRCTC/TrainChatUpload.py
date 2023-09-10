import requests
# r = requests.post('https://www.irctc.co.in/eticketing/protected/mapps1/trnscheduleenquiry/22912')
# print(r.status_code)
# print(r.json())

r = requests.post('https://www.irctc.co.in/online-charts/api/trainComposition', json={"trainNo": "22912", "jDate": "2023-06-15", "boardingStation": "HWH"})
print(r.status_code)
print(r.json())

# r = requests.post('https://www.irctc.co.in/online-charts/api/coachComposition', json={"boardingStation": "HWH", "cls": "3A","coach": "B2", "jDate": "2023-06-15", "remoteStation": "HWH", "trainNo": "22912", "trainSourceStation": "HWH"})
# print(r.status_code)
# print(r.json())



