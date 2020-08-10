import urllib.request
import simplejson
import numpy
import math
import pdb
def getSharpeRatio( stock, risk_free ):
   link = "https://www.moneycontrol.com/mc/widget/basicchart/get_chart_value?classic=true&sc_did=%s&dur=1yr" % stock
   #from urllib import request
   req = urllib.request.Request(link) #urllib.Request(link)
   from urllib.request import urlopen
   resp = urlopen(req)
   data = resp.read()
   data =  simplejson.loads(data)
   if data['g1'] == None:
      print ( "Unable to fetch data for %s" % stock )
      return 0
   stockReturn  =  (float(data['g1'][-1]['close']) /float(data['g1'][0]['close']) ) -1
   daily_return = [ (float(data['g1'][i+1]['close'])/float(data['g1'][i]['close'])) - 1 for i in range(len(data['g1']) -1 ) ]
   std_dev = numpy.std(daily_return ) * math.sqrt( len(daily_return) )
   sharpeRatio = (stockReturn - risk_free)/std_dev
   print ( "SharpeRatio of %s = %f \n" % ( stock, sharpeRatio) )
   return sharpeRatio
rf = 6.1/100 #assuming risk free rate is 6.1%
for stock in [ "ITC", "RI", "IT" ]: #moneycontrol stock code 
   getSharpeRatio( stock, rf )