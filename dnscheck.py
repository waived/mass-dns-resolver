# -*- coding: utf-8 -*-

import dns.resolver, sys
from urllib.parse import urlparse

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

#generic banner
print('\r\n' * 20 + f'''{b}{c}
     _____ _____ _____ _____   ____  _____ _____    
    |     |  _  |   __|   __| |    \|   | |   __|   
    | | | |     |__   |__   | |  |  | | | |__   |   
   _|_|_|_|__|__|_____|_____| |____/|_|___|_____|_
  | __  |   __|   __|     |  |  |  |  |   __| __  |
  |    -|   __|__   |  |  |  |__|  |  |   __|    -|
  |__|__|_____|_____|_____|_____|\___/|_____|__|__|
''')

try:
    #capture website
    host = input(f'{w}Website:{y} ')
    
    #format host
    host = host.lower()
    
    if not (host.startswith('http://') or host.startswith('https://')):
        host = f'http://{host}'
    
    #get domain name
    try:
        domain = urlparse(host).netloc
    except:    
        sys.exit(f'\r\n{r}Error! Invalid domain/URL.\r\n')
    
    #confirm scan
    input(f'\r\n{w}Ready? Strike <ENTER> to resolve...\r\n')
    
    for server, ip in dns_servers.items():
        try:
            resolver = dns.resolver.Resolver()
            resolver.nameservers = [ip]
            
            answer = resolver.resolve(domain, 'A')
            
            for rdata in answer:
                ip_addresses = [rdata.to_text() for rdata in answer]
            
            print(f'{y}{server}DNS {w}@ {y}{ip}:53 {w}resolved host to: {g}{", ".join(ip_addresses)}')
        except:
            print(f'{y}{server}DNS {w}@ {y}{ip}:53 {r}unable to resolve host!')
        
except KeyboardInterrupt:
    sys.exit(f'{w}\r\nAborted.\r\n')

sys.exit('f\r\n{w}Complete.\r\n')
