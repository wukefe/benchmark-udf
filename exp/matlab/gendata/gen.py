
"""
function [sptprice,strike,rate,divq,volatility,otime,otype,divs,DGrefval] = InputData()
sptprice   = ...
strike     = ...
rate       = ...
divq       = ...
volatility = ...
otime      = ...
otype      = ...
divs       = ...
DGrefval   = ...
end
"""

import time

def genData(lhs, data, col, isChar=False):
    print(('%s = [' % lhs), end = " ")
    if isChar:
        for line in data:
            print(("%d" % (line[col]=='P')), end = " ")
    else:
        for line in data:
            print(("%s" % line[col]), end = " ")
    print('];')

def processData(file_path):
    fp = open(file_path, 'r')
    data = []
    for line in fp:
        data.append(line.strip(' \t\r\n').split(' '))
    fp.close()
    # generate data as follows
    print('function [sptprice,strike,rate,divq,volatility,otime,otype,divs,DGrefval] = InputData()')
    genData('sptprice  ', data, 0)
    genData('strike    ', data, 1)
    genData('rate      ', data, 2)
    genData('divq      ', data, 3)
    genData('volatility', data, 4)
    genData('otime     ', data, 5)
    genData('otype     ', data, 6, True)
    genData('divs      ', data, 7)
    genData('DGrefval  ', data, 8)
    print('end')

if __name__ == '__main__':
    #start = time.time()
    processData('../../../data/in_1M.tbl')
    #print('Elapsed time %.2lf (ms)' % (time.time() - start))


