# Generated from C:\photoCAD\layout1002\.venv_layout1002\Lib\site-packages\AMFpdk_3_5_Cband\technology\layers.csv

from fnpcell.pdk.technology.all import Layer, LayerEnum, Process, ProcessEnum, Purpose, PurposeEnum

class PROCESS(ProcessEnum):
    RIB_WG = Process(10, 'RIB_WG')
    GRAT_WG = Process(11, 'GRAT_WG')
    SLAB_WG = Process(12, 'SLAB_WG')
    PP = Process(20, 'PP')
    PCONT = Process(21, 'PCONT')
    NCONT = Process(22, 'NCONT')
    PIM = Process(23, 'PIM')
    NIM = Process(24, 'NIM')
    IPD = Process(25, 'IPD')
    IND = Process(26, 'IND')
    GeEP = Process(40, 'GeEP')
    NPPGE = Process(41, 'NPPGE')
    VIA1 = Process(100, 'VIA1')
    MT1 = Process(105, 'MT1')
    HTR = Process(115, 'HTR')
    VIA2 = Process(120, 'VIA2')
    MT2 = Process(125, 'MT2')
    PAD = Process(150, 'PAD')
    OX_OPEN = Process(151, 'OX_OPEN')
    DT = Process(160, 'DT')
    EXCL = Process(90, 'EXCL')
    LBL = Process(80, 'LBL')
    MARKER = Process(81, 'MARKER')
    BLACK_FP = Process(97, 'BLACK_FP')

class PURPOSE(PurposeEnum):
    DRW = Purpose(0, 'DRW')
    GEN = Purpose(4, 'GEN')

class LAYER(LayerEnum):
    RIB = Layer(PROCESS.RIB_WG, PURPOSE.DRW, 'RIB WG etch 70nm')
    GRAT = Layer(PROCESS.GRAT_WG, PURPOSE.DRW, 'GC WG etch 60nm')
    SLAB = Layer(PROCESS.SLAB_WG, PURPOSE.DRW, 'SLAB WG etch 90nm')
    PP = Layer(PROCESS.PP, PURPOSE.DRW, 'P+ on SiGe PD ')
    PCONT = Layer(PROCESS.PCONT, PURPOSE.DRW, 'P++ on Si for Ohmic contact/90nm')
    NCONT = Layer(PROCESS.NCONT, PURPOSE.DRW, 'N++ on Si for Ohmic contact/90nm')
    PIM = Layer(PROCESS.PIM, PURPOSE.DRW, 'P for modulator/220nm')
    NIM = Layer(PROCESS.NIM, PURPOSE.DRW, 'N for modulator/220nm')
    IPD = Layer(PROCESS.IPD, PURPOSE.DRW, 'intermediate P doping')
    IND = Layer(PROCESS.IND, PURPOSE.DRW, 'intermediate N doping')
    GeEP = Layer(PROCESS.GeEP, PURPOSE.DRW, 'Germanium epitaxy 500nm')
    NPPGE = Layer(PROCESS.NPPGE, PURPOSE.DRW, 'N++ Ge epi for upper contact')
    VIA1 = Layer(PROCESS.VIA1, PURPOSE.DRW, 'VIA1 to Si/Ge')
    MT1 = Layer(PROCESS.MT1, PURPOSE.DRW, 'Metal 1 750nm')
    HTR = Layer(PROCESS.HTR, PURPOSE.DRW, 'Heater TiN 120nm')
    VIA2 = Layer(PROCESS.VIA2, PURPOSE.DRW, 'VIA2 to HTR & MT1')
    MT2 = Layer(PROCESS.MT2, PURPOSE.DRW, 'Metal 2000nm')
    PAD = Layer(PROCESS.PAD, PURPOSE.DRW, 'Pad Open')
    OX_OPEN = Layer(PROCESS.OX_OPEN, PURPOSE.DRW, 'Oxide open before deep trench')
    DT = Layer(PROCESS.DT, PURPOSE.DRW, 'Deep trench to Si substrate')
    TR = Layer(PROCESS.RIB_WG, PURPOSE.GEN, ' dummy fill for RIB WG')
    TM1 = Layer(PROCESS.MT1, PURPOSE.GEN, ' dummy fill for Metal 1')
    EXCL = Layer(PROCESS.EXCL, PURPOSE.DRW, 'Dummy exclusion')
    LBL = Layer(PROCESS.LBL, PURPOSE.DRW, 'label')
    MARKER = Layer(PROCESS.MARKER, PURPOSE.DRW, 'Text layer, not to print on wafer')
    BLACK_FP = Layer(PROCESS.BLACK_FP, PURPOSE.DRW, 'Design outline(for IP device)')
