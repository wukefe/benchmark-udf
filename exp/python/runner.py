import time
import numpy
import BlkSchls

def loadData(file_path):
    fp = open(file_path, 'r')
    sptprice = []
    strike = []
    rate = []
    divq = []
    volatility = []
    otime = []
    otype = []
    divs = []
    DGrefval = []
    for line in fp:
        items = line.strip(' \t\r\n').split(' ')
        sptprice.append(float(items[0]))
        strike.append(float(items[1]))
        rate.append(float(items[2]))
        divq.append(float(items[3]))
        volatility.append(float(items[4]))
        otime.append(float(items[5]))
        otype.append(items[6])
        divs.append(float(items[7]))
        DGrefval.append(float(items[8]))
    fp.close()
    return [ numpy.asarray(sptprice)  ,
             numpy.asarray(strike)    ,
             numpy.asarray(rate)      ,
             numpy.asarray(divq)      ,
             numpy.asarray(volatility),
             numpy.asarray(otime)     ,
             numpy.asarray(otype)     ,
             numpy.asarray(divs)      ,
             numpy.asarray(DGrefval)]

def printElapsedTime(elapsed):
    for c,e in enumerate(elapsed):
        print('[%d] %.2lf ms' % (c,e*1000))

def runBlkSchls():
    print('Run black-scholes with numpy!')
    sptprice,strike,rate,_,volatility,otime,otype,_,_ = loadData('../../data/in_1M.tbl')
    elapsed = []
    for x in range(10):
        start = time.time()
        price=BlkSchls.BlkSchls(sptprice, strike, rate, volatility, otime, otype)
        elapsed.append(time.time() - start)
    printElapsedTime(elapsed)
    print('Elapsed time (ms): %2lf (price %lf)' % (1000*numpy.mean(elapsed), numpy.sum(price)))

if __name__ == '__main__':
    runBlkSchls()

