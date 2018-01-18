import httplib2

if __name__ == '__main__':
   httplib2.debuglevel     = 0
   h = httplib2.Http()
   http = h.HTTPConnection("http://127.0.0.1/vias", 5000)

   response, content = http.request("GET")
   print (http.getresponse().read())
  
