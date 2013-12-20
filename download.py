#!/usr/bin/python
import urllib2

for i in range(1, 8356):
  response = urllib2.urlopen('http://ndb.nal.usda.gov/ndb/foods/show/{}?format=Abridged&reportfmt=csv'.format(i))
  f = open('data/{}'.format(i), 'w')
  f.write(response.read())
  f.close()

