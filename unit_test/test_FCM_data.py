import unittest
from numpy import array
from random import randint

from fcm import FCMdata
from fcm import Gate


class FCMdataTestCase(unittest.TestCase):
    def setUp(self):
        self.pnts = array([[0,1,2],[3,4,5]])
        self.fcm = FCMdata('test_fcm', self.pnts, ['fsc','ssc','cd3'], [0,1])
        
    def testGetPnts(self):
        a = randint(0,1)
        b = randint(0,2)
        assert self.fcm.view()[a,b] == self.pnts[a,b], "Data not consistent with inital data"
            
    def testGetChannelByName(self):
        assert self.fcm.get_channel_by_name(['fsc'])[0] == 0, 'incorrect first column'
        assert self.fcm.get_channel_by_name(['fsc'])[1] == 3, 'incorrect first column'
        
    def testGetMarkers(self):
        #print self.fcm.markers
        assert self.fcm.markers == [2], 'Marker CD3 not picked up'
    
    def testGetItem(self):
        a = randint(0,1)
        b = randint(0,2)
        assert type(self.fcm[a]) == type(self.pnts[a]), "__getitem__ failed to return array"
        assert self.fcm[a,b] == self.pnts[a,b], '__getitem__ returned wrong value'
        assert self.fcm['fsc','ssc'][a,0] == self.pnts[a,0], '__getitem__ with multiple strings failed'
        
#    def testlogicle(self):
#        from numpy.random import normal, lognormal, shuffle
#        from numpy import concatenate
#        from core.fcmtransforms import quantile
#        from pylab import hist, show
#    
#        d1 = normal(0, 50, (50000))
#        d2 = lognormal(8, 1, (50000))
#        d3 = array([concatenate([d1, d2])]).T
# 
#        T = 262144
#        d = 4
#        m = d*log(10)
#        r = quantile(d3[d3<0], 0.05)
#        self.fcm = FCMdata(d3, ['a'])

    def testGate(self):
        verts =  array([[-.1,-.1],[-.1,1.1],[1.1,1.1], [1.1,-.1]])
        cols = [0,1]
        g = Gate(verts, cols)
        self.fcm.gate(g)
        assert self.fcm.view().all() == array([[0,1,2]]).all(), 'gate excluded wrong points'
        
    def testGetAttr(self):
        assert self.fcm.shape == (2,3), '__gettattr__ failed to deligate'
        
if __name__ == '__main__':
    suite1 = unittest.makeSuite(FCSdataTestCase,'test')

    unittest.main()