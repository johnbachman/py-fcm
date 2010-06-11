# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.39
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_cdp', [dirname(__file__)])
        except ImportError:
            import _cdp
            return _cdp
        if fp is not None:
            try:
                _mod = imp.load_module('_cdp', fp, pathname, description)
            finally:
                fp.close()
                return _mod
    _cdp = swig_import_helper()
    del swig_import_helper
else:
    import _cdp
del version_info
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def mvnpdf(*args):
  return _cdp.mvnpdf(*args)
mvnpdf = _cdp.mvnpdf
class cdpcluster:
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cdpcluster, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cdpcluster, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _cdp.new_cdpcluster(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cdp.delete_cdpcluster
    __del__ = lambda self : None;
    def makeResult(self): return _cdp.cdpcluster_makeResult(self)
    def run(self): return _cdp.cdpcluster_run(self)
    def step(self): return _cdp.cdpcluster_step(self)
    def stepburn(self): return _cdp.cdpcluster_stepburn(self)
    def setseed(self, *args): return _cdp.cdpcluster_setseed(self, *args)
    def setT(self, *args): return _cdp.cdpcluster_setT(self, *args)
    def setJ(self, *args): return _cdp.cdpcluster_setJ(self, *args)
    def setBurnin(self, *args): return _cdp.cdpcluster_setBurnin(self, *args)
    def setIter(self, *args): return _cdp.cdpcluster_setIter(self, *args)
    def setVerbose(self, *args): return _cdp.cdpcluster_setVerbose(self, *args)
    def getBurnin(self): return _cdp.cdpcluster_getBurnin(self)
    def getIter(self): return _cdp.cdpcluster_getIter(self)
    def getn(self): return _cdp.cdpcluster_getn(self)
    def getd(self): return _cdp.cdpcluster_getd(self)
    def getclustN(self): return _cdp.cdpcluster_getclustN(self)
    def getT(self): return _cdp.cdpcluster_getT(self)
    def getJ(self): return _cdp.cdpcluster_getJ(self)
    def setlambda0(self, *args): return _cdp.cdpcluster_setlambda0(self, *args)
    def getlambda0(self): return _cdp.cdpcluster_getlambda0(self)
    def setphi0(self, *args): return _cdp.cdpcluster_setphi0(self, *args)
    def getphi0(self): return _cdp.cdpcluster_getphi0(self)
    def setnu0(self, *args): return _cdp.cdpcluster_setnu0(self, *args)
    def getnu0(self): return _cdp.cdpcluster_getnu0(self)
    def setgamma(self, *args): return _cdp.cdpcluster_setgamma(self, *args)
    def getgamma(self): return _cdp.cdpcluster_getgamma(self)
    def setnu(self, *args): return _cdp.cdpcluster_setnu(self, *args)
    def getnu(self): return _cdp.cdpcluster_getnu(self)
    def sete0(self, *args): return _cdp.cdpcluster_sete0(self, *args)
    def gete0(self): return _cdp.cdpcluster_gete0(self)
    def setf0(self, *args): return _cdp.cdpcluster_setf0(self, *args)
    def getf0(self): return _cdp.cdpcluster_getf0(self)
    def setee(self, *args): return _cdp.cdpcluster_setee(self, *args)
    def getee(self): return _cdp.cdpcluster_getee(self)
    def setff(self, *args): return _cdp.cdpcluster_setff(self, *args)
    def getff(self): return _cdp.cdpcluster_getff(self)
    def getMu(self, *args): return _cdp.cdpcluster_getMu(self, *args)
    def getm(self, *args): return _cdp.cdpcluster_getm(self, *args)
    def getSigma(self, *args): return _cdp.cdpcluster_getSigma(self, *args)
    def getPhi(self, *args): return _cdp.cdpcluster_getPhi(self, *args)
    def getp(self, *args): return _cdp.cdpcluster_getp(self, *args)
    def setgpunchunksize(self, *args): return _cdp.cdpcluster_setgpunchunksize(self, *args)
    def getgpunchunksize(self): return _cdp.cdpcluster_getgpunchunksize(self)
    def setdevice(self, *args): return _cdp.cdpcluster_setdevice(self, *args)
    def getdevice(self): return _cdp.cdpcluster_getdevice(self)
    def getnumberdevices(self): return _cdp.cdpcluster_getnumberdevices(self)
    def setnumberdevices(self, *args): return _cdp.cdpcluster_setnumberdevices(self, *args)
    def samplem(self, *args): return _cdp.cdpcluster_samplem(self, *args)
    def samplePhi(self, *args): return _cdp.cdpcluster_samplePhi(self, *args)
    def samplew(self, *args): return _cdp.cdpcluster_samplew(self, *args)
    def sampleq(self, *args): return _cdp.cdpcluster_sampleq(self, *args)
    def samplealpha0(self, *args): return _cdp.cdpcluster_samplealpha0(self, *args)
    def samplemu(self, *args): return _cdp.cdpcluster_samplemu(self, *args)
    def sampleSigma(self, *args): return _cdp.cdpcluster_sampleSigma(self, *args)
    def samplek(self, *args): return _cdp.cdpcluster_samplek(self, *args)
    def samplep(self, *args): return _cdp.cdpcluster_samplep(self, *args)
    def samplealpha(self, *args): return _cdp.cdpcluster_samplealpha(self, *args)
    def loadMu(self, *args): return _cdp.cdpcluster_loadMu(self, *args)
    def loadm(self, *args): return _cdp.cdpcluster_loadm(self, *args)
    def loadp(self, *args): return _cdp.cdpcluster_loadp(self, *args)
    def loadpV(self, *args): return _cdp.cdpcluster_loadpV(self, *args)
    def loadSigma(self, *args): return _cdp.cdpcluster_loadSigma(self, *args)
    def loadPhi(self, *args): return _cdp.cdpcluster_loadPhi(self, *args)
    def loadW(self, *args): return _cdp.cdpcluster_loadW(self, *args)
    def loadK(self, *args): return _cdp.cdpcluster_loadK(self, *args)
    def loadq(self, *args): return _cdp.cdpcluster_loadq(self, *args)
    def loadqV(self, *args): return _cdp.cdpcluster_loadqV(self, *args)
    def loadalpha(self, *args): return _cdp.cdpcluster_loadalpha(self, *args)
    def printModel(self): return _cdp.cdpcluster_printModel(self)
cdpcluster_swigregister = _cdp.cdpcluster_swigregister
cdpcluster_swigregister(cdpcluster)



