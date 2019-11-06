# cfg file for X(10700) -> Ups(1S)pi+pi-pi0. Masses and widths are matched between pythia, evtgen and PDG 2016

import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    comEnergy = cms.double(13000.0),
    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2014.pdl'),
            list_forced_decays = cms.vstring('myX_b'),
            operates_on_particles = cms.vint32(10551),
            convertPythiaCodes = cms.untracked.bool(False),
            user_decay_embedded= cms.vstring(
"""
Particle chi_b0 10.7000000 0.000000
Particle Upsilon 9.4603000 0.00005402

Alias myX_b chi_b0
Alias myUpsilon Upsilon

Decay myUpsilon
1.0   mu+  mu-          PHOTOS  VLL;
Enddecay

Decay pi0
1.0   gamma  gamma  PHSP;
Enddecay

Decay myX_b
1.0   myUpsilon  pi-   pi+   pi0   PHSP;
Enddecay

End
"""
            )
	),
        parameterSets = cms.vstring('EvtGen130')
    ),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
	pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
            'Bottomonium:states(3PJ) = 10551',
            'Bottomonium:O(3PJ)[3P0(1)] = 0.085',
            'Bottomonium:O(3PJ)[3S1(8)] = 0.04',
            'Bottomonium:gg2bbbar(3PJ)[3PJ(1)]g = on',
            'Bottomonium:qg2bbbar(3PJ)[3PJ(1)]q = on',
            'Bottomonium:qqbar2bbbar(3PJ)[3PJ(1)]g = on',
            'Bottomonium:gg2bbbar(3PJ)[3S1(8)]g = on',
            'Bottomonium:qg2bbbar(3PJ)[3S1(8)]q = on',
            'Bottomonium:qqbar2bbbar(3PJ)[3S1(8)]g = on',
            '10551:m0 = 10.700000',
            '10551:onMode = off'
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters'
                                    )
    )
)

Xbfilter = cms.EDFilter("MCSingleParticleFilter",
    ParticleID = cms.untracked.vint32(10551),
    MinPt = cms.untracked.vdouble(2.0),
    MinEta = cms.untracked.vdouble(-2.4),
    MaxEta = cms.untracked.vdouble(2.4),
    Status = cms.untracked.vint32(2)
)

ups1Sfilter = cms.EDFilter("MCSingleParticleFilter",
    ParticleID = cms.untracked.vint32(553),
    MinPt = cms.untracked.vdouble(0.0),
    MinEta = cms.untracked.vdouble(-2.4),
    MaxEta = cms.untracked.vdouble(2.4),
    Status = cms.untracked.vint32(2)
)

pi0filter = cms.EDFilter("MCSingleParticleFilter",
    ParticleID = cms.untracked.vint32(111),
    MinPt = cms.untracked.vdouble(0.0),
    MinEta = cms.untracked.vdouble(-2.4),
    MaxEta = cms.untracked.vdouble(2.4),
    Status = cms.untracked.vint32(2)
)

# Next two muon filter are derived from muon reconstruction

muonsfilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(10551),
    MinPt = cms.untracked.vdouble(0.0,0.0),
    ParticleID = cms.untracked.int32(553),
    ChargeConjugation = cms.untracked.bool(False),
    MinEta = cms.untracked.vdouble(-2.4,-2.4),
    MaxEta = cms.untracked.vdouble(2.4,2.4),
    NumberDaughters = cms.untracked.int32(2),
    DaughterIDs = cms.untracked.vint32(-13,13)
)

pionsfilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(0),
    MinPt = cms.untracked.vdouble(0.0,0.0),
    ParticleID = cms.untracked.int32(10551),
    ChargeConjugation = cms.untracked.bool(False),
    MinEta = cms.untracked.vdouble(-2.4,-2.4),
    MaxEta = cms.untracked.vdouble(2.4,2.4),
    NumberDaughters = cms.untracked.int32(2),
    DaughterIDs = cms.untracked.vint32(-211,211)
)

photonsfilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(10551),
    MinPt = cms.untracked.vdouble(0.0,0.0),
    ParticleID = cms.untracked.int32(111),
    ChargeConjugation = cms.untracked.bool(False),
    MinEta = cms.untracked.vdouble(-2.4,-2.4),
    MaxEta = cms.untracked.vdouble(2.4,2.4),
    NumberDaughters = cms.untracked.int32(2),
    DaughterIDs = cms.untracked.vint32(22,22)
)

ProductionFilterSequence = cms.Sequence(generator*Xbfilter*pi0filter*ups1Sfilter*photonsfilter*muonsfilter*pionsfilter)
#ProductionFilterSequence = cms.Sequence(generator*upsIDfilter*muonsfilter*pionsfilter)
