import unittest
from numpy import array, all
from random import randint

from fcm import FCMdata
from fcm import PolyGate, IntervalGate
from fcm.statistics import DPMixture, DPCluster
from numpy.testing.utils import assert_array_equal


class FCMdataTestCase(unittest.TestCase):
    def setUp(self):
        self.pnts = array([[0,1,2],[3,4,5]])
        self.fcm = FCMdata('test_fcm', self.pnts, [('fsc','fsc'),('ssc','ssc'),('fl-1','cd3')], [0,1])
        
    def testChannels(self):
        assert self.fcm.channels[0] == 'fsc', "channel property fails"
        
    def testLen(self):
        assert len(self.fcm) == 2, 'length wrong'
        
    def testShortNames(self):
        assert self.fcm.short_names[2] == 'fl-1', "channel property fails"
        
    def testLongNames(self):
        assert self.fcm.long_names[2] == 'fl-1::cd3', 'long names property fails: %s' % self.fcm.long_names[2]
        assert self.fcm.long_names[0] == 'fsc', 'long names property fails: %s' % self.fcm.long_names[0]
        
    def testGetPnts(self):
        a = randint(0,1)
        b = randint(0,2)
        assert self.fcm.view()[a,b] == self.pnts[a,b], "Data not consistent with initial data"
            
    def testGetChannelByName(self):
        assert self.fcm.get_channel_by_name(['fsc'])[0] == 0, 'incorrect first column'
        assert self.fcm.get_channel_by_name(['fsc'])[1] == 3, 'incorrect first column'
        assert self.fcm.get_channel_by_name(['fl-1'])[0] == 2, 'incorrect last column: %d' % self.fcm.get_channel_by_name(['fl-1'])[0]
        assert self.fcm.get_channel_by_name(['fl-1'])[1] == 5, 'incorrect first column: %d' % self.fcm.get_channel_by_name(['fl-1'])[1]
    def testGetMarkers(self):
        #print self.fcm.markers
        assert self.fcm.markers == [2], 'Marker CD3 not picked up'
    
    def testGetItem(self):
        a = randint(0,1)
        b = randint(0,2)
        assert type(self.fcm[a]) == type(self.pnts[a]), "__getitem__ failed to return array"
        
        assert self.fcm[a,b] == self.pnts[a,b], '__getitem__ returned wrong value'
        assert self.fcm[:,'fsc'][a] == self.pnts[:,0][a], '__getitem__ with multiple strings failed'
        assert self.fcm[:,['fsc','ssc']][a,0] == self.pnts[a,0], '__getitem__ with multiple strings failed'
        assert self.fcm[:,['fsc',1]][a,0] == self.pnts[a,0], '__getitem__ with mixed strings failed'
        
    def testDeligate(self):
        assert self.fcm.mean() == self.pnts.mean(), "deligation of mean failed"
        
#    def testSubSample(self):
#        self.fcm.subsample([2])
#        assert self.fcm.view()[0] == self.pnts[0,2], "subsample failed"
#        assert self.fcm.view()[1] == self.pnts[1,2], "subsample failed"
        
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

    def testPolyGate(self):
        verts =  array([[-.1,-.1],[-.1,1.1],[1.1,1.1], [1.1,-.1]])
        cols = [0,1]
        g = PolyGate(verts, cols)
        self.fcm.gate(g)
        assert all(self.fcm.view() == array([[0,1,2]])), 'gate excluded wrong points'
        self.fcm.visit('root')
        self.fcm.gate(g)
        nodes = self.fcm.tree.nodes.keys()
        assert 'g2' in nodes, 'gating name mangled'
        assert 'g1' in nodes, 'gating name mangled'
        
    def testEmptyPolyGate(self):
        verts =  array([[10,10],[10,11],[11,11], [11,10]])
        cols = [0,1]
        g = PolyGate(verts, cols)
        self.fcm.gate(g)
        assert_array_equal(self.fcm.view(),array([]).reshape((0,3)), 'gated region not empty')

        self.fcm.gate(g)
        assert_array_equal(self.fcm.view(),array([]).reshape((0,3)), 'gated region not empty')

        nodes = self.fcm.tree.nodes.keys()
        assert 'g2' in nodes, 'gating name mangled'
        assert 'g1' in nodes, 'gating name mangled'
        
    def testIntervalGate(self):
        verts =  array([1.5,4.5])
        cols = [0]
        g = IntervalGate(verts, cols)
        self.fcm.gate(g)
        assert_array_equal(self.fcm.view(),array([[3,4,5]]), 'gate excluded wrong points')
        self.fcm.visit('root')
        self.fcm.gate(g)
        nodes = self.fcm.tree.nodes.keys()
        assert 'g2' in nodes, 'gating name mangled'
        assert 'g1' in nodes, 'gating name mangled'

    def testEmptyIntervalGate(self):
        verts =  array([10.5,40.5])
        cols = [0]
        g = IntervalGate(verts, cols)
        self.fcm.gate(g)
        assert_array_equal(self.fcm.view(),array([]).reshape((0,3)), 'gate excluded wrong points')
        self.fcm.gate(g)
        assert_array_equal(self.fcm.view(),array([]).reshape((0,3)), 'gate excluded wrong points')
        nodes = self.fcm.tree.nodes.keys()
        assert 'g2' in nodes, 'gating name mangled'
        assert 'g1' in nodes, 'gating name mangled'

    def testBoundaryEvents(self):
        pnts = array([[0,1,2],[3,4,5],[0,2,5]])
        fcm = FCMdata('test_fcm', pnts, [('fsc','fsc'),('ssc','ssc'),('fl-1','cd3')], [0,1])
        eps = 1e-10
        result = fcm.boundary_events()
    
        assert result['fsc'] - 1 < eps, str(result['fsc'])
        assert result['ssc'] - 2.0/3.0 < eps
        assert result['cd3'] - 1 < eps

    def testChainOp(self):
        verts =  array([[-.1,-.1],[-.1,1.1],[1.1,1.1], [1.1,-.1]])
        cols = [0,1]
        g = PolyGate(verts, cols)
        self.fcm.gate(g).gate(g)
        self.assertTrue( all(self.fcm.view()== array([[0,1,2]])), 'gate excluded wrong points')
        
    def testGetAttr(self):
        assert self.fcm.shape == (2,3), '__gettattr__ failed to deligate'
        
    def testSummary(self):
        tmp =  self.fcm.summary()
        assert tmp.startswith('fsc:') == True, 'Summary failed'
        
    def testPickle(self):
        import pickle
        import StringIO
        buffer = StringIO.StringIO()
        pickle.dump(self.fcm, buffer)
        buffer.seek(0)
        tmp = pickle.load(buffer)
        self.assertTrue(all(self.fcm[:] == tmp[:]))
        for unused in range(3):
            buffer = StringIO.StringIO()
            pickle.dump(tmp, buffer)
            buffer.seek(0)
            tmp = pickle.load(buffer)
        self.assertTrue(all(self.fcm[:] == tmp[:]))
        
    def testCopy(self):
        cpy = self.fcm.copy()
        self.assertFalse(cpy is self.fcm, "copy reproduced the exact same object")
        self.assertTrue(cpy.tree.pprint() == self.fcm.tree.pprint(), "copy failed to reproduce the view tree")
        
        # make sure changes to object self.fcm don't show up on cpy
        verts =  array([[-.1,-.1],[-.1,1.1],[1.1,1.1], [1.1,-.1]])
        cols = [0,1]
        g = PolyGate(verts, cols)
        self.fcm.gate(g)
        self.assertFalse(cpy.tree.pprint() == self.fcm.tree.pprint(), "copy failed to reproduce the view tree")
        
        #make sure tree is actually copied
        cpy = self.fcm.copy()
        self.assertTrue(cpy.tree.pprint() == self.fcm.tree.pprint(), "copy failed to reproduce the view tree")

    def testRandomSubsample(self):
        self.fcm.subsample(1)
        
        self.assertEqual(1,self.fcm.shape[0], 'random subsampling failed')
        self.assertTrue(self.fcm[0] in self.pnts, 'random subsample geneterated non-existant point')

    def testAnomalySubsample(self):
        mu = array([0,1,2])
        sig = array([[1,0,0],[0,1,0],[0,0,1]])
        cluster = DPCluster(1.0, mu, sig)
        mix = DPMixture([cluster])
        self.fcm.subsample(1, 'anomaly', mix)
        
        self.assertEqual(1,self.fcm.shape[0], 'anomaly subsampling failed')
        self.assertTrue(self.fcm[0] in self.pnts, 'anomaly subsample geneterated non-existant point')

    def testBiasSubsample(self):
        neg_mu = array([0,1,2])
        pos_mu = array([3,4,5])
        sig = array([[1,0,0],[0,1,0],[0,0,1]])
        neg_cluster = DPCluster(1.0,neg_mu, sig)
        neg_mix = DPMixture([neg_cluster])
        pos_cluster0 = DPCluster(0.5, neg_mu, sig)
        pos_cluster1 = DPCluster(0.5, pos_mu, sig)
        pos_mix = DPMixture([pos_cluster0, pos_cluster1])
        self.fcm.subsample(1, 'bias', pos=pos_mix, neg=neg_mix)
        
        self.assertEqual(1,self.fcm.shape[0], 'bias subsampling failed')
        self.assertTrue(self.fcm[0] in self.pnts, 'bias subsample geneterated non-existant point')

    def testSubsamplebySlice(self):
        self.fcm.subsample(slice(1))
        self.assertEqual(1,self.fcm.shape[0])
        assert_array_equal(self.pnts[0], self.fcm[0], 'subsample by slice failed')
if __name__ == '__main__':
    suite1 = unittest.makeSuite(FCMdataTestCase,'test')

    unittest.main()
