import shodan



SHODAN_API_KEY = str(input('Input your Shodan API key: '))
api = shodan.Shodan(SHODAN_API_KEY)
host_ip = str(input('Input interesting host IP: '))
try:
    results: object = api.host(host_ip)
    available_ports = api.services()

    print('Country: {}'.format(results['country_name']))
    print('Hostname: {}'.format(results['hostnames'][0]))
    print('Last Update: {}'.format(results['last_update']))
    print('Open Ports: {}'.format(results['ports']))
    for port in range(len(results['ports'])):
        current_port = str(results['ports'][port])
        print('Ports Services: {}'.format(available_ports[current_port]))
except shodan.APIError as e:
    print('Error: {}'.format(e))


