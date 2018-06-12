import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *


etafilter = cms.EDFilter("PythiaFilter",
        MaxEta = cms.untracked.double(9999.0),
        MinEta = cms.untracked.double(-9999.0),
        ParticleID = cms.untracked.int32(10551)
)


generator = cms.EDFilter("Pythia8GeneratorFilter",
        pythiaHepMCVerbosity = cms.untracked.bool(False),
        maxEventsToPrint = cms.untracked.int32(3),
        pythiaPylistVerbosity = cms.untracked.int32(1),
        displayPythiaCards = cms.untracked.bool(False),
        comEnergy = cms.double(13000.0),
        PythiaParameters = cms.PSet(
                pythia8CommonSettingsBlock,
                pythia8CP5SettingsBlock,
                pythiaEtab = cms.vstring(
                       'Bottomonium:all=on',
                       '10551:addChannel 1 1.00 100 211 -211 20553',
                       '10551:onMode = off',
                       '10551:onIfMatch 211 -211 20553',
                       '20553:onMode = off',
                       '20553:onIfMatch gamma 553',
                       '553:onMode = off',
                       '553:onIfMatch 13 -13',
                       '10551:m0=10.5',
                       '10551:mWidth =0.00'
),
                parameterSets = cms.vstring(
                        'pythia8CommonSettings',
                        'pythia8CP5Settings',
                        'pythiaEtab',
                )
        )
)


ProductionFilterSequence = cms.Sequence(generator+etafilter)
