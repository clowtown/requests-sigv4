import sys

from requests_sigv4.sigv4request import Sigv4Request

__all__ = ('Sigv4Request',)
__version__ = '0.1.4'


_ver = sys.version_info
is_py2 = (_ver[0] == 2)
is_py3 = (_ver[0] == 3)

if is_py2:
    import urllib
    urllib.quote_plus = urllib.quote
else:
    from copy import deepcopy
    from urllib.parse import quote, urlencode
    from requests_sigv4.sigv4request import requests
    import requests_aws_sign

    _urlencode = deepcopy(urlencode)

    # patching urlencode in python3 as it has a default
    # quote_via=quote_plus as the default
    def new_urlencode(query, doseq=False, safe='',
                      encoding=None, errors=None, quote_via=None):
        return _urlencode(
            query, doseq, safe, encoding, errors, quote)
    requests.models.urlencode = new_urlencode
    requests_aws_sign.requests_aws_sign.urlencode = new_urlencode
