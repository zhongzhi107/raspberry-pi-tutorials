# encoding: utf-8

from util import bin2dec

a = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0]

values = []
for i in range(0, 5):
  values.append(int(bin2dec(''.join(str(i) for i in a[i*8:(i+1)*8]))))

print len(a) > 1000 and 0 or 1

if values[4] == sum(values[0:3]):
  print 'OK\ntemperature: %d°C, humidity: %d%%'%(values[2], values[0])
else:
  print 'Fail'
