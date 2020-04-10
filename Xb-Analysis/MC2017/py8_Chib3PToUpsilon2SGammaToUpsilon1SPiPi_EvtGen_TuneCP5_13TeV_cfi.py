# cfg file for Chi_{b1,b2}(3P) -> Upsilon(2S) gamma,  we are neglecting Chi_b0. Masses and widths are matched between pythia, evtgen and PDG 2016
# a mass separation between Chi_b1 and Chi_b2 is assumed to be 10.4 MeV  
#
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
            list_forced_decays = cms.vstring('mychi_b1','mychi_b2'),        # will force one at the time
            operates_on_particles = cms.vint32(20553,555),                  # we care just about our signal particles
            convertPythiaCodes = cms.untracked.bool(False),
            user_decay_embedded= cms.vstring(
"""
Particle Upsilon(2S) 10.02326 0.00003198
Particle Upsilon  9.4603000   0.00005402
Particle chi_b1 10.513400 0.00000
Particle chi_b2 10.524000 0.00000

Alias myUps_2s Upsilon(2S)
Alias myUps_1s   Upsilon
Alias mychi_b1 chi_b1
Alias mychi_b2 chi_b2

Decay myUps_1s
1.0   mu+  mu-          PHOTOS  VLL;
Enddecay

Decay myUps_2s
1.0   myUps_1s pi+ pi-  PHSP;
Enddecay

Decay mychi_b1
1.0   gamma  myUps_2s  HELAMP 1. 0. 1. 0. -1. 0. -1. 0.;
Enddecay

Decay mychi_b2
1.0   gamma  myUps_2s  PHSP;
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
            'Bottomonium:states(3PJ) = 20553,555',
            'Bottomonium:O(3PJ)[3P0(1)] = 0.085,0.085',
            'Bottomonium:O(3PJ)[3S1(8)] = 0.04,0.04',
            'Bottomonium:gg2bbbar(3PJ)[3PJ(1)]g = on,on',
            'Bottomonium:qg2bbbar(3PJ)[3PJ(1)]q = on,on',
            'Bottomonium:qqbar2bbbar(3PJ)[3PJ(1)]g = on,on',
            'Bottomonium:gg2bbbar(3PJ)[3S1(8)]g = on,on',
            'Bottomonium:qg2bbbar(3PJ)[3S1(8)]q = on,on',
            'Bottomonium:qqbar2bbbar(3PJ)[3S1(8)]g = on,on',
            'PhaseSpace:pTHatMin = 2.',
            '20553:m0 = 10.513400',
            '555:m0 = 10.524000',
            '20553:onMode = off',
            '555:onMode = off'
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters'
                                    )
    )
)

# We will filter for chi_b1, and chi_b2, first on the ID, then in the mass, this will constraint the photon daughter

pwaveIDfilter = cms.EDFilter("MCSingleParticleFilter",
    ParticleID = cms.untracked.vint32(20553,555),
    MinPt = cms.untracked.vdouble(0.0, 0.0),
    MinEta = cms.untracked.vdouble(-9., -9.),
    MaxEta = cms.untracked.vdouble(9., 9.),
    Status = cms.untracked.vint32(2, 2)
)

pwaveMassfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(2, 1),
    MinPt = cms.untracked.vdouble(3., 0.2),
    MaxEta = cms.untracked.vdouble(9., 9.),
    MinEta = cms.untracked.vdouble(-9., -9.),
    ParticleCharge = cms.untracked.int32(0),
    MinP = cms.untracked.vdouble(0.,0.),
    ParticleID1 = cms.untracked.vint32(100553),
    ParticleID2 = cms.untracked.vint32(22),
    MinInvMass = cms.untracked.double(10.50),
    MaxInvMass = cms.untracked.double(10.53),
)

dimuonIDfilter = cms.EDFilter("MCSingleParticleFilter",
    ParticleID = cms.untracked.vint32(100553),
    MinPt = cms.untracked.vdouble(2.0),
    MinEta = cms.untracked.vdouble(-3.4),
    MaxEta = cms.untracked.vdouble(3.4),
    Status = cms.untracked.vint32(2)
)

# Next two muon filter are derived from muon reconstruction

muminusfilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(100553),
    MinPt = cms.untracked.vdouble(0.5),
    ParticleID = cms.untracked.int32(553),
    ChargeConjugation = cms.untracked.bool(False),
    MinEta = cms.untracked.vdouble(-3.4),
    MaxEta = cms.untracked.vdouble(3.4),
    NumberDaughters = cms.untracked.int32(1),
    DaughterIDs = cms.untracked.vint32(-13)
)

muplusfilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(100553),
    MinPt = cms.untracked.vdouble(0.5),
    ParticleID = cms.untracked.int32(553),
    ChargeConjugation = cms.untracked.bool(False),
    MinEta = cms.untracked.vdouble(-3.4),
    MaxEta = cms.untracked.vdouble(3.4),
    NumberDaughters = cms.untracked.int32(1),
    DaughterIDs = cms.untracked.vint32(13)
)

ProductionFilterSequence = cms.Sequence(generator*pwaveIDfilter*pwaveMassfilter*dimuonIDfilter*muminusfilter*muplusfilter)
