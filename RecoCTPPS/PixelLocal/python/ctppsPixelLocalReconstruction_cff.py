import FWCore.ParameterSet.Config as cms

# geometry
from Geometry.VeryForwardGeometry.geometryRP_cfi import *
#from Geometry.VeryForwardGeometry.geometry_CTPPS_alaTotem_RECO_cfi import *

# local clusterizer
from RecoCTPPS.PixelLocal.ctppsPixelClusters_cfi import ctppsPixelClusters

# local rechit producer
from RecoCTPPS.PixelLocal.ctppsPixelRecHits_cfi import ctppsPixelRecHits

# local track producer
from RecoCTPPS.PixelLocal.ctppsPixelLocalTracks_cfi import ctppsPixelLocalTracks

#ctppsPixelTracks = cms.EDProducer('CTPPSPixelLocalTrackProducer',
#  patterFinderAlgorithm = cms.string('testPatternAlgorithm')
#)

from Geometry.VeryForwardGeometryBuilder.ctppsIncludeAlignments_cfi import *
ctppsIncludeAlignments.RealFiles = cms.vstring("Alignment/CTPPS/data/RPixGeometryCorrections.xml")

ctppsPixelLocalReconstruction = cms.Sequence(
    ctppsPixelClusters*ctppsPixelRecHits*ctppsPixelLocalTracks
)
