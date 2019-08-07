import requests

SHODAN_API_KEY = str(input('Input your Shodan API key: '))
# host_ip = str(input('Input interesting host IP: '))
host_name = str(input('Input domain name: '))
ip_addr = requests.get('https://api.shodan.io/dns/resolve?hostnames=' + host_name + '&key=' + SHODAN_API_KEY)
response = requests.get('https://api.shodan.io/shodan/host/' + ip_addr.json()[host_name] + '?key=' + SHODAN_API_KEY)

# print(response.json())
print('Country: {}'.format(response.json()['country_name']))
# # print('Hostname: {}'.format(response['hostnames'][0]))
print('Last Update: {}'.format(response.json()['last_update']))
print('Open Ports: {}'.format(response.json()['ports']))
