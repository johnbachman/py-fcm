/* cdp.cpp
 * @author Quanli Wang, quanli@stat.duke.edu
 */
#pragma once

#if  defined(PYWRAP)
#include "cdpresult.h"
#include "cdpbase.h"
using namespace std;
#endif

class Model;
class CDP:public CDPBase
{
 public:
  CDP();
  ~CDP(void);
  void InitMCMCSteps(Model& model);
  void LoadData(Model& model);
  void LoadInits(Model& model,CDPResult& result, MTRand& mt);

  void CheckSpecialCases(Model& model, CDPResult& result);

  bool SimulateFromPrior2(CDPResult& result, MTRand& mt, int isEM);
  bool clusterIterate_one(CDPResult& result, MTRand& mt);
  bool iterate(CDPResult& result, MTRand& mt);

  void partition(int* W, vector<vector<int> >& w1d);
  
  void UpdateKJ(int* K,vector<int>& w1d, vector<int>& KJ);
	
	void ComponentRelabel(CDPResult& result);
  
  // turn off/off individual sampling steps
  bool mcsamplem;
  bool mcsamplePhi;
  bool mcsamplew;
  bool mcsampleq;
  bool mcsamplealpha0;

  bool mcsamplemu;
  bool mcsampleSigma;
  bool mcsamplek;
  bool mcsamplep;
  bool mcsamplealpha;	
  bool mcsampleEta;
	
  bool mcRelabel;

 private:
  static bool LoadFileData(string FileName, Matrix& A, int rows, int columns);
  static bool LoadFileData(string FileName, double*** A, int rows, int columns);
  static bool LoadFileData(string FileName, double& A);
#if defined(CDP_TBB)
  static bool LoadFileData(string FileName, concurrent_vector<RowVector>& A, int rows, int columns);
  static bool LoadFileData(string FileName, concurrent_vector<SymmetricMatrix>& A, int rows, int columns);
#else
  static bool LoadFileData(string FileName, vector<RowVector>& A, int rows, int columns);
  static bool LoadFileData(string FileName, vector<SymmetricMatrix>& A, int rows, int columns);
#endif
  static bool LoadFileData(string FileName, int* A, int columns);
  static bool LoadFileData(string FileName, RowVector& A, int columns);
};