import re
import requests

def ipinfo(ip):
    """Returns a dictionary of information on the ip address."""
    return IpWimia(ip).info

class IpWimia():

    def __init__(self, ip):
        """A class to get information on an ip address using
        whatismyipaddress.com
        
        Parameters
        ----------
        ip : str
            The ip address (V4) for which to get the information,
            e.g. '172.217.13.142'.

        Attributes
        ----------
        info : dict
            A dictionary containing all the information on the ip address.
        
        hostname : str
            The hostname corresponding to the ip address.

        asn : int
            The ASN number corresponding to the ip address.

        isp : str
            The ISP (Internet Service Provider) corresponding to the ip
            address.

        organization : str
            The organization owning the ip address.

        type : str
            The type of ip address.

        continent : str
            The contient of the ip address location.

        country : str
            The country of the ip address location.

        state_region : str
            The state, province or region of the ip address location.

        city : str
            The city of the ip address location.

        latitude : float
            The latitude of the ip address location.

        longitude : float
            The longitude of the ip address location.
        """
        ip_pattern = r'([0-9]{1,3}\.){3}[0-9]{1,3}'
        if re.match(ip_pattern, ip):
            self.ip = ip
        else:
            raise ValueError(f"{ip} is not a valid IP address.")
        self.info = self._get_ip_info()
        self.hostname = self.info.get('Hostname:')
        self.asn = self.info.get('ASN:')
        self.isp = self.info.get('ISP:')
        self.organization = self.info.get('Organization:')
        self.type = self.info.get('Type:')
        self.continent = self.info.get('Continent:')
        self.country = self.info.get('Country:')
        self.state_region = self.info.get('State/Region:')
        self.city = self.info.get('City:')
        self.latitude = self.info.get('Latitude:')
        self.longitude = self.info.get('Longitude:')

    def _get_ip_info(self):
        info = {
            'Hostname:': '',
            'ASN:': '',
            'ISP:': '',
            'Organization:': '',
            'Type:': '',
            'Continent:': '',
            'Country:': '',
            'State/Region:': '',
            'City:': '',
            'Latitude:': '',
            'Longitude:': '',
        }

        lines = self._get_wimia_data()
        for field in info:
            info[field] = self._get_field_data(field, lines)
        
        return info
        

    def _get_wimia_data(self):
        url = f"https://whatismyipaddress.com/ip/{self.ip}"
        resp = requests.get(url)
        page = resp.content.decode()
        lines = page.split('\n')
        return lines

    def _get_field_data(self, field, lines):
        field_pattern = f">{field}"
        for l_num, line in enumerate(lines):
            field_match = re.search(field_pattern, line)
            if field_match is not None:
                if field in ['Latitude:', 'Longitude:']:
                    value_match = re.search('[\-0-9a-zA-Z\.]+',
                                            lines[l_num + 1])
                    return float(value_match[0])
                if field in ['ASN:']:
                    value_match = re.search('td>[0-9]+', line)
                    return int(value_match[0].strip('td>'))
                if field in ['Type:']:
                    value_match = re.search('>[a-zA-Z ]+</a', line)
                    return value_match[0].strip('>').strip('</a')
                else:
                    value_match = re.search('td>[\-0-9a-zA-Z \.]+', line)
                if value_match is not None:
                    return value_match[0].replace('td>', '').strip()
                else:
                    return ''
        return 'Not available'
            