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
        ParticleID = cms.vint32(100541),
        AddAntiParticle = cms.bool(False), 
        MaxY = cms.double(2.4),
        MaxPhi = cms.double(3.14159265359),
        MinY = cms.double(-2.4),
        MinPhi = cms.double(-3.14159265359),
        TFunction_string = cms.string('x*((1.+1./(3.357-2.)*x*x/2.085)^(-3.357))'),  #This if J/psi pT
   ),

   PythiaParameters = cms.PSet(
       pythia8CommonSettingsBlock,
       pythia8CP5SettingsBlock,
       processParameters = cms.vstring(
            #'absPDGCode:new = Name antiName spin charge colour m0 mWidth mMin mMax tau0'
            '100541:new = B_c(2S)+ B_c(2S)- 1 3 0 6.8670000e+00 0.0050000e+00 6.817 6.917 0.0000000e+00',
            '100541:isResonance = false',
            '100541:addChannel = 1 1.0 0 541 211 -211',
	    '100541:mayDecay = on',
	    '541:onMode = off',
	    '541:onIfMatch = 443 211',
	    '443:onMode = off',
	    '443:onIfMatch = 13 -13'
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

ProductionFilterSequence = cms.Sequence(generator*bc2sgenfilter*bcgenfilter*mumugenfilter)
