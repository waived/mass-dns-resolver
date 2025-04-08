# -*- coding: utf-8 -*-

import dns.resolver, sys, os
from urllib.parse import urlparse
from tabulate import tabulate

# set colors
b = '\033[1m'  #bright
r = '\033[31m' #red
w = '\033[37m' #white
g = '\033[32m' #green
c = '\033[36m' #cyan
y = '\033[33m' #yellow

dns_servers = {
    "[US] Quad9 ": "9.9.9.9",
    "[US] Google ": "8.8.8.8",
    "[US] Open": "208.67.222.220",
    "[US] WholeSale Internet Inc ": "204.12.225.227",
    "[US] CenturyLink ": "205.171.202.66",
    "[US] NeuStar ": "156.154.70.64",
    "[US] Corporate West Computer Systems ": "66.206.166.2",
    "[CA] Fortinet Inc ": "208.91.112.53",
    "[RU] Sky": "195.46.39.39",
    "[ZA] Liquid Telecommunications Ltd ": "5.11.11.5",
    "[NL] Tele2 Nederland B.V. ": "87.213.100.113",
    "[FR] Online SAS ": "163.172.107.158",
    "[ES] Prioritytelecom Spain S.A. ": "212.230.255.1",
    "[AT] Nemox.net ": "83.137.41.9",
    "[UK] Ancar B Technologies Ltd ": "194.145.240.6",
    "[DE] Verizon Deutschland GmbH ": "194.172.160.4",
    "[MX] Marcatel Com ": "200.56.224.11",
    "[BR] Claro S.A ": "200.248.178.54",
    "[MY] TT Dotcom Sdn Bhd ": "211.25.206.147",
    "[AU] Cloudflare ": "1.1.1.1",
    "[AU] Pacific Internet ": "61.8.0.113",
    "[NZ] Global-Gateway Internet ": "122.56.107.86",
    "[SG] DigitalOcean LLC ": "139.59.219.245",
    "[KR] LG Dacom Corporation ": "164.124.101.2",
    "[CN] Nanjing Xinfeng Information Technologies Inc ": "114.114.115.115",
    "[IN] Kappa Internet Services Private Limited ": "115.178.96.2",
    "[PK] CMPak Limited ": "209.150.154.1",
    "[IE] Daniel Cid ": "185.228.168.9",
    "[BD] SS Online ": "103.80.1.2"
}

# generic banner
os.system('clear')

print(f'''{b}{c}
                                     _____ _____ _____ _____   ____  _____ _____    
                                    |     |  _  |   __|   __| |    \|   | |   __|   
                                    | | | |     |__   |__   | |  |  | | | |__   |   
                                   _|_|_|_|__|__|_____|_____| |____/|_|___|_____|_
                                  | __  |   __|   __|     |  |  |  |  |   __| __  |
                                  |    -|   __|__   |  |  |  |__|  |  |   __|    -|
                                  |__|__|_____|_____|_____|_____|\___/|_____|__|__|
''')

try:
    # Capture website
    host = input(f'{w}Enter Website URL (e.g. example.com):{y} ')

    # Format host
    host = host.lower()

    if not (host.startswith('http://') or host.startswith('https://')):
        host = f'http://{host}'

    # Get domain name
    try:
        domain = urlparse(host).netloc
    except:
        sys.exit(f'\r\n{r}Error! Invalid domain/URL.\r\n')

    # Confirm scan
    input(f'\r\n{w}Ready? Strike <ENTER> to resolve...\r\n')

    # Prepare data for the table
    table_data = []

    for server, ip in dns_servers.items():
        try:
            resolver = dns.resolver.Resolver()
            resolver.nameservers = [ip]

            # Resolve the domain
            answer = resolver.resolve(domain, 'A')

            # Collect all IP addresses
            ip_addresses = [rdata.to_text() for rdata in answer]
            ip_addresses_str = ", ".join(ip_addresses)

            # Add to table data with colors applied
            table_data.append([
                f'{y}{server.ljust(30)}{w}',  # DNS Server in yellow (left-aligned)
                f'{y}{ip.ljust(15)}{w}',      # IP Address in yellow (left-aligned)
                f'{g}Resolved{w}',             # Status in green if resolved
                f'{g}{ip_addresses_str.ljust(40)}{w}'  # Resolved IPs in green (left-aligned)
            ])

        except Exception as e:
            # Add error data to table
            table_data.append([
                f'{y}{server.ljust(30)}{w}',  # DNS Server in yellow (left-aligned)
                f'{y}{ip.ljust(15)}{w}',      # IP Address in yellow (left-aligned)
                f'{r}Unable to Resolve{w}',   # Status in red if unable to resolve
                f'{r}{str(e).ljust(40)}{w}'   # Error message in red (left-aligned)
            ])

    # Print the results as a table with left-alignment and color formatting
    headers = [f'{y}DNS Server{w}', f'{y}IP Address{w}', f'{g}Status{w}', f'{g}Resolved IPs/Error{w}']

    print(tabulate(table_data, headers=headers, tablefmt="pretty", stralign="left"))

except KeyboardInterrupt:
    sys.exit(f'{w}\r\nAborted.\r\n')

sys.exit(f'\r\n{w}Complete.\r\n')
