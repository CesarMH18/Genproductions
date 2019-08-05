# cfg file for chi_b1(3P),chi_b2(3P) -> chi_b1(1P) pion+ pion-. Masses and widths are matched between pythia, evtgen and PDG 2016
#The mass of the chi_b1(3P),chi_b2(3P) are set to 10.5134, 10.5240 GeV (desired resonant masses)

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
            list_forced_decays = cms.vstring('mychib1_3P','mychib2_3P'),       
            operates_on_particles = cms.vint32(10551,555),        
            convertPythiaCodes = cms.untracked.bool(False),
            user_decay_embedded= cms.vstring(
"""
Particle Upsilon 9.4603000 0.00005402
Particle chi_b1  9.8927800 0.00000
Particle chi_b0  10.513400 0.00000
Particle chi_b2  10.524000 0.00000

Alias myUpsilon Upsilon
Alias mychi_b1 chi_b1
Alias mychib1_3P chi_b0
Alias mychib2_3P chi_b2

Decay myUpsilon
1.0   mu+  mu-          PHOTOS  VLL;
Enddecay

Decay mychi_b1
1.0   gamma  myUpsilon  HELAMP 1. 0. 1. 0. -1. 0. -1. 0.;
Enddecay

Decay mychib1_3P
1.0   mychi_b1 pi+ pi-  PHSP;
Enddecay

Decay mychib2_3P
1.0   mychi_b1 pi+ pi-  PHSP;
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
            'Bottomonium:states(3PJ) = 10551,555',   
            'Bottomonium:O(3PJ)[3P0(1)] = 0.085,0.085',
            'Bottomonium:O(3PJ)[3S1(8)] = 0.04,0.04',
            'Bottomonium:gg2bbbar(3PJ)[3PJ(1)]g = on,on',
            'Bottomonium:qg2bbbar(3PJ)[3PJ(1)]q = on,on',
            'Bottomonium:qqbar2bbbar(3PJ)[3PJ(1)]g = on,on',
            'Bottomonium:gg2bbbar(3PJ)[3S1(8)]g = on,on',
            'Bottomonium:qg2bbbar(3PJ)[3S1(8)]q = on,on',
            'Bottomonium:qqbar2bbbar(3PJ)[3S1(8)]g = on,on',
            'PhaseSpace:pTHatMin = 2.',
            '10551:m0 = 10.513400',
	    '555:m0 = 10.524000',        
            '10551:onMode = off'
            '555:onMode = off'
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters'
                                    )
    )
)

# We will filter for chi_b1_3P, and chi_b1, first on the ID, then in the mass, this will constraint the photon daughter

#pwaveIDfilterXb = cms.EDFilter("MCSingleParticleFilter",
#    ParticleID = cms.untracked.vint32(10551),
#    MinPt = cms.untracked.vdouble(0.0),
#    MinEta = cms.untracked.vdouble(-9.),
#    MaxEta = cms.untracked.vdouble(9.),
#    Status = cms.untracked.vint32(2)
#)

pwaveIDfilterchi = cms.EDFilter("MCSingleParticleFilter",
    ParticleID = cms.untracked.vint32(20553),
    MinPt = cms.untracked.vdouble(0.0),
    MinEta = cms.untracked.vdouble(-9.),
    MaxEta = cms.untracked.vdouble(9.),
    Status = cms.untracked.vint32(2)
)

pwaveMassfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(2, 1),
    MinPt = cms.untracked.vdouble(5.0, 0.2),
    MaxEta = cms.untracked.vdouble(2.4, 2.4),
    MinEta = cms.untracked.vdouble(-2.4,-2.4),
    ParticleCharge = cms.untracked.int32(0),
    MinP = cms.untracked.vdouble(0.,0.),
    ParticleID1 = cms.untracked.vint32(553),
    ParticleID2 = cms.untracked.vint32(22),
    MinInvMass = cms.untracked.double(9.88),
    MaxInvMass = cms.untracked.double(9.91)
)

# Next two muon filter are derived from muon reconstruction

muminusfilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(0),
    MinPt = cms.untracked.vdouble(5.0),
    ParticleID = cms.untracked.int32(553),
    ChargeConjugation = cms.untracked.bool(False),
    MinEta = cms.untracked.vdouble(-2.4),
    MaxEta = cms.untracked.vdouble(2.4),
    NumberDaughters = cms.untracked.int32(1),
    DaughterIDs = cms.untracked.vint32(-13)
)

muplusfilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(0),
    MinPt = cms.untracked.vdouble(5.0),
    ParticleID = cms.untracked.int32(553),
    ChargeConjugation = cms.untracked.bool(False),
    MinEta = cms.untracked.vdouble(-2.4),
    MaxEta = cms.untracked.vdouble(2.4),
    NumberDaughters = cms.untracked.int32(1),
    DaughterIDs = cms.untracked.vint32(13)
)

#  two pion filter 

piminusfilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(0),
    MinPt = cms.untracked.vdouble(.5),
    ParticleID = cms.untracked.int32(10551),
    ChargeConjugation = cms.untracked.bool(False),
    MinEta = cms.untracked.vdouble(-2.4),
    MaxEta = cms.untracked.vdouble(2.4),
    NumberDaughters = cms.untracked.int32(1),
    DaughterIDs = cms.untracked.vint32(-211)
)

piplusfilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(0),
    MinPt = cms.untracked.vdouble(.5),
    ParticleID = cms.untracked.int32(10551),
    ChargeConjugation = cms.untracked.bool(False),
    MinEta = cms.untracked.vdouble(-2.4),
    MaxEta = cms.untracked.vdouble(2.4),
    NumberDaughters = cms.untracked.int32(1),
    DaughterIDs = cms.untracked.vint32(211)
)

#ProductionFilterSequence = cms.Sequence(generator*pwaveIDfilterXb*pwaveIDfilterchi*pwaveMassfilter*piminusfilter*piplusfilter*muminusfilter*muplusfilter)
ProductionFilterSequence = cms.Sequence(generator*pwaveIDfilterchi*pwaveMassfilter*piminusfilter*piplusfilter*muminusfilter*muplusfilter)

