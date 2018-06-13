import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter("Pythia8PtCustomYGun",
    maxEventsToPrint = cms.untracked.int32(5),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(True),

    PGunParameters = cms.PSet(
        MaxPt = cms.double(100.),
        MinPt = cms.double(8.),
        ParticleID = cms.vint32(10551),
        AddAntiParticle = cms.bool(False), 
        MaxY = cms.double(2.4),
        MaxPhi = cms.double(3.14159265359),
        MinY = cms.double(-2.4),
        MinPhi = cms.double(-3.14159265359),
   ),

   PythiaParameters = cms.PSet(
       pythia8CommonSettingsBlock,
       pythia8CP5SettingsBlock,
       processParameters = cms.vstring(
            #'absPDGCode:new = Name antiName spin charge colour m0 mWidth mMin mMax tau0'
            '10551:new = X_b X_b* 1 0 0 10.50000e+00 0.0000000e+00 10.4 10.6 0.0000000e+00',
            '10551:isResonance = false',
            '10551:addChannel = 1 1.0 0 20553 211 -211',
	    '10551:mayDecay = on',
	    '20553:onMode = off',
	    '20553:onIfMatch = 553 gamma',
	    '553:onMode = off',
	    '553:onIfMatch = 13 -13'
       ),
       parameterSets = cms.vstring('pythia8CommonSettings',
                                   'pythia8CP5Settings',
                                   'processParameters'
       )
   )
)

mumugenfilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(541),
    MinPt = cms.untracked.vdouble(3.5, 3.5),
    ParticleID = cms.untracked.int32(443),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    DaughterIDs = cms.untracked.vint32(-13, 13),
    NumberDaughters = cms.untracked.int32(2),
    verbose = cms.untracked.int32(0)
)

bcgenfilter = cms.EDFilter("PythiaDauVFilter",
    MinPt = cms.untracked.vdouble(1.0),
    ParticleID = cms.untracked.int32(541),
    MaxEta = cms.untracked.vdouble(2.5),
    MinEta = cms.untracked.vdouble(-2.5),
    DaughterIDs = cms.untracked.vint32(211),
    NumberDaughters = cms.untracked.int32(1),
    verbose = cms.untracked.int32(0)
)

bc2sgenfilter = cms.EDFilter("PythiaDauVFilter",
    MinPt = cms.untracked.vdouble(0.4, 0.4),
    ParticleID = cms.untracked.int32(100541),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    DaughterIDs = cms.untracked.vint32(-211, 211),
    NumberDaughters = cms.untracked.int32(2),
    verbose = cms.untracked.int32(0)
)

ProductionFilterSequence = cms.Sequence(generator)
