#cfg file for X_b -> Chib(1P) pion+ pion-. Masses and widths are matched between pythia, evtgen and PDG 2016
#The mass of the chi_b0(1P) is set to 10.5 GeV (desired resonant mass)

import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *


generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(3),
    comEnergy = cms.double(13000.0),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
	pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
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
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters',
                                    )
    )
)

ProductionFilterSequence = cms.Sequence(generator)
