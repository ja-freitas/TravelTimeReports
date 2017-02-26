import requests, json

origin = '32.235503,-111.002835'
destination = '32.235930,-110.897526'

response = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&departure_time=now&key=AIzaSyAZEe218wR5BpZMdLHZEpub0Ym8ccP1QNM' % (origin, destination))

if response.status_code == 200:
    print('Response Status is Good! (200)')
else:
    print(status_code)

data = response.json()
print('...')
print(json.dumps(data['routes'][0]['legs'][0]['duration_in_traffic']['text'], indent=4))
