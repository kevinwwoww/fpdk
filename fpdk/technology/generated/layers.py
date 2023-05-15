# Generated from C:\photoCAD\layout1002\fpdk\technology\layers.csv

from fnpcell.pdk.technology.all import Layer, LayerEnum, Process, ProcessEnum, Purpose, PurposeEnum

class PROCESS(ProcessEnum):
    FWG = Process(1, 'Full etch')
    SWG = Process(2, 'Shallow etch')
    NP = Process(20, 'NP, for MOD slab, Ge etc.')
    PP = Process(21, 'PP, for MOD slab, Ge etc.')
    N = Process(23, 'N type light doping')
    P = Process(24, 'P type light doping')
    N2 = Process(25, 'N type light doping 2')
    P2 = Process(26, 'P type light doping 2')
    NPP = Process(27, 'N++ implant')
    PPP = Process(28, 'P++ implant')
    GE = Process(29, 'Ge epitaxy')
    SIL = Process(30, 'Silicide area')
    TIN = Process(31, 'TiN Metal heater')
    CONT = Process(32, 'Contact')
    M1 = Process(33, 'Metal 1')
    VIA1 = Process(34, 'VIA1 on M1 ')
    M2 = Process(35, 'Metal 2')
    VIA2 = Process(36, 'VIA2 on M2 ')
    MT = Process(43, 'Metal Top')
    PASS = Process(50, 'Passivation open window')
    TH_ISO = Process(51, 'Thermal isolation')
    DT = Process(52, 'Deep Trench for edge coupler')
    LABEL = Process(55, 'Label to print on FWG')
    TEXT = Process(56, 'Text, not to print on wafer')
    IOPORT = Process(60, 'Port, for testing')
    PINREC = Process(70, 'Pin rectangle, for LVS, DRC')
    FIBREC = Process(71, 'Fiber rectangle, for LVSS, DRC')
    FIBTGT = Process(72, 'Fiber Target for LVS')
    DEVREC = Process(80, 'Device rectangle, for LVS, DRC')
    PAYLOAD = Process(90, 'Design area')
    M1KO = Process(81, 'Tilling keep-out for M1')
    MTKO = Process(82, 'Tilling keep-out for MT')
    SIKO = Process(83, 'Tiliing keep-out for Silicon')
    FLYLINE = Process(91, 'Fly line')
    ERROR = Process(92, 'Error')

class PURPOSE(PurposeEnum):
    COR = Purpose(1, 'Waveguide core')
    CLD = Purpose(2, 'Waveguide cladding')
    TRE = Purpose(4, 'Waveguide trench')
    HOL = Purpose(5, 'Waveguide hole lattice')
    DRW = Purpose(3, 'Drawing')
    EC = Purpose(11, 'EC')
    GC = Purpose(12, 'GC')
    MT = Purpose(13, 'MT')
    NOTE = Purpose(30, 'Note')
    OREC = Purpose(21, 'Optical')
    EREC = Purpose(22, 'Electrical')
    FWG = Purpose(31, 'Full etch')
    SWG = Purpose(32, 'Shallow etch')
    MWG = Purpose(33, 'Medium etch')
    TEXT = Purpose(41, 'Text')
    MARK = Purpose(35, 'Mark')

class LAYER(LayerEnum):
    FWG_COR = Layer(PROCESS.FWG, PURPOSE.COR, 'Full Etch waveguide core')
    FWG_CLD = Layer(PROCESS.FWG, PURPOSE.CLD, 'Full Etch waveguide cladding')
    FWG_TRE = Layer(PROCESS.FWG, PURPOSE.TRE, 'Full Etch waveguide trench')
    FWG_HOL = Layer(PROCESS.FWG, PURPOSE.HOL, 'Full Etch waveguide hole lattice')
    SWG_COR = Layer(PROCESS.SWG, PURPOSE.COR, 'Shallow Etch waveguide core')
    SWG_CLD = Layer(PROCESS.SWG, PURPOSE.CLD, 'Shallow Etch waveguide cladding')
    SWG_TRE = Layer(PROCESS.SWG, PURPOSE.TRE, 'Shallow Etch waveguide trench')
    SWG_HOL = Layer(PROCESS.SWG, PURPOSE.HOL, 'Shallow Etch waveguide hole lattice')
    NP_DRW = Layer(PROCESS.NP, PURPOSE.DRW, 'NP, for MOD slab, Ge etc.')
    PP_DRW = Layer(PROCESS.PP, PURPOSE.DRW, 'PP, for MOD slab, Ge etc.')
    N_DRW = Layer(PROCESS.N, PURPOSE.DRW, 'N type light doping')
    P_DRW = Layer(PROCESS.P, PURPOSE.DRW, 'P type light doping')
    N2_DRW = Layer(PROCESS.N2, PURPOSE.DRW, 'N2 type light doping 2')
    P2_DRW = Layer(PROCESS.P2, PURPOSE.DRW, 'P2 type light doping 2')
    NPP_DRW = Layer(PROCESS.NPP, PURPOSE.DRW, 'N++ implement')
    PPP_DRW = Layer(PROCESS.PPP, PURPOSE.DRW, 'P++ implement')
    GE_DRW = Layer(PROCESS.GE, PURPOSE.DRW, 'Germanium epitaxy')
    SIL_DRW = Layer(PROCESS.SIL, PURPOSE.DRW, 'Silicide area')
    TIN_DRW = Layer(PROCESS.TIN, PURPOSE.DRW, 'TiN heater')
    CONT_DRW = Layer(PROCESS.CONT, PURPOSE.DRW, 'Contact')
    M1_DRW = Layer(PROCESS.M1, PURPOSE.DRW, 'Metal 1')
    VIA1_DRW = Layer(PROCESS.VIA1, PURPOSE.DRW, 'Via 1 on M1')
    M2_DRW = Layer(PROCESS.M2, PURPOSE.DRW, 'Metal 2')
    VIA2_DRW = Layer(PROCESS.VIA2, PURPOSE.DRW, 'Via 2 on M2')
    MT_DRW = Layer(PROCESS.MT, PURPOSE.DRW, 'Metal Top')
    PASS_EC = Layer(PROCESS.PASS, PURPOSE.EC, 'Passivation, open EC')
    PASS_GC = Layer(PROCESS.PASS, PURPOSE.GC, 'Passivation, open GC')
    PASS_MT = Layer(PROCESS.PASS, PURPOSE.MT, 'Passivation, open MT')
    TH_ISO_DRW = Layer(PROCESS.TH_ISO, PURPOSE.DRW, 'Thermal isolation')
    DT_DRW = Layer(PROCESS.DT, PURPOSE.DRW, 'Deep Trench for edge coupler')
    LABEL_DRW = Layer(PROCESS.LABEL, PURPOSE.DRW, 'Label to print on FWG')
    TEXT_NOTE = Layer(PROCESS.TEXT, PURPOSE.NOTE, 'Text layer, not to print on wafer')
    IOPORT_OREC = Layer(PROCESS.IOPORT, PURPOSE.OREC, 'Optical port, for testing')
    IOPORT_EREC = Layer(PROCESS.IOPORT, PURPOSE.EREC, 'Electrical port, for testing')
    PINREC_NOTE = Layer(PROCESS.PINREC, PURPOSE.NOTE, 'Pin rectangle, for LVS, DRC')
    PINREC_FWG = Layer(PROCESS.PINREC, PURPOSE.FWG, 'Pin rectangle, for LVS, DRC')
    PINREC_SWG = Layer(PROCESS.PINREC, PURPOSE.SWG, 'Pin rectangle, for LVS, DRC')
    PINREC_MWG = Layer(PROCESS.PINREC, PURPOSE.MWG, 'Pin rectangle, for LVS, DRC')
    PINREC_TEXT = Layer(PROCESS.PINREC, PURPOSE.TEXT, 'Pin rectangle, for LVS, DRC')
    FIBREC_NOTE = Layer(PROCESS.FIBREC, PURPOSE.NOTE, 'Fiber rectangle, for LVS, DRC')
    FIBTGT_NOTE = Layer(PROCESS.FIBTGT, PURPOSE.NOTE, 'Fiber Target for LVS')
    DEVREC_NOTE = Layer(PROCESS.DEVREC, PURPOSE.NOTE, 'Device rectangle, for LVS, DRC')
    PAYLOAD_NOTE = Layer(PROCESS.PAYLOAD, PURPOSE.NOTE, 'Design area')
    M1KO_DRW = Layer(PROCESS.M1KO, PURPOSE.DRW, 'Tilling keep-out for M1')
    MTKO_DRW = Layer(PROCESS.MTKO, PURPOSE.DRW, 'Tilling keep-out for MT')
    SIKO_DRW = Layer(PROCESS.SIKO, PURPOSE.DRW, 'Tiliing keep-out for Silicon')
    FLYLINE_MARK = Layer(PROCESS.FLYLINE, PURPOSE.MARK, 'Flyline for insufficient space in AutoLink')
    ERROR_MARK = Layer(PROCESS.ERROR, PURPOSE.MARK, 'Error mark')
