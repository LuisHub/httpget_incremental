import urllib2
import sys
import getopt
import os
import pycurl
import random

# cadena enviada por el GET. Se concatenan los parametros en cada peticion
CADENA = ''

# Numero de peticiones GET a enviar
NUMGET = 0

if len(sys.argv) < 3:
        print "Usage get_incremental.py <URL> <num_requests>\n"
        sys.exit(0)
  
URL= sys.argv[1] + '?'
NUMGET = sys.argv[2]
c = pycurl.Curl()

# Opcion para pasar peticiones a traves de proxy (Burp, ZAP, ...)
c.setopt(c.PROXY, '127.0.0.1:8080')

# Opciones de Curl (no hace falta tocar)
c.setopt(pycurl.WRITEFUNCTION, lambda x: None)
c.setopt(pycurl.SSL_VERIFYPEER, 0)
c.setopt(pycurl.SSL_VERIFYHOST, 0)
c.setopt(pycurl.USERAGENT, 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:8.0) Gecko/20100101 Firefox/8.0')
c.setopt(pycurl.HTTPHEADER, ["Proxy-Connection:"])

random.seed()

for i in range (1,int(NUMGET)+1):
	if i != 1:
		CADENA +='&'
	CADENA += 'id' + str(i) + '=' + str(random.randint(0000,9999))
	print "Req:" + str(i) + ": " + URL+CADENA
	c.setopt(c.URL, URL+CADENA)
        c.perform()
# FIN
