#ifndef HLTEcalPixelIsolTrackFilter_h
#define HLTEcalPixelIsolTrackFilter_h

#include "HLTrigger/HLTcore/interface/HLTFilter.h"
#include "DataFormats/HcalIsolatedTrack/interface/IsolatedPixelTrackCandidate.h"

/*
 This filter is an improvement in the HLT_IsoTrack for HB(HE) trigger paths
 by complementing the HLTPixelIsolTrackFilter with information from
 ECAL to remove non-MIP candidates. 
 */

class HLTEcalPixelIsolTrackFilter : public HLTFilter {  
 public:
  explicit HLTEcalPixelIsolTrackFilter(const edm::ParameterSet&);
  ~HLTEcalPixelIsolTrackFilter();
  virtual bool hltFilter(edm::Event&, const edm::EventSetup&, trigger::TriggerFilterObjectWithRefs & filterproduct) const override;
  
 private:
  edm::EDGetTokenT<reco::IsolatedPixelTrackCandidateCollection> candTok;
  edm::InputTag candTag_; 
  double maxEnergyIn_;
  double maxEnergyOut_;
  int nMaxTrackCandidates_;
  bool dropMultiL2Event_;
};

#endif 
