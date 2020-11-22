
import pcbnew

class Layer:
    def __init__(self, id, name, ext, enabled=False):
        self.enabled = enabled
        self.name = name
        self.id = id
        self.ext = ext


class GerberLayer(Layer):
    def __init__(self, id, name, ext, enabled=False):
        Layer.__init__(self, id, name, ext, enabled)
        
class DrillLayer(Layer):
    def __init__(self, id, name, ext, enabled=False):
        Layer.__init__(self, id, name, ext, enabled)

default_layers = [
    GerberLayer(pcbnew.F_Cu     ,'Top Copper', '.gtl', enabled=True),
    GerberLayer(pcbnew.In1_Cu   ,'Inner1 Copper', '.g1', enabled=True),
    GerberLayer(pcbnew.In2_Cu   ,'Inner2 Copper', '.g2', enabled=True),
    GerberLayer(pcbnew.In3_Cu   ,'Inner3 Copper', '.g3', enabled=True),
    GerberLayer(pcbnew.In4_Cu   ,'Inner4 Copper', 'g4', enabled=True),
    GerberLayer(pcbnew.In5_Cu   ,'Inner5 Copper', '.g5', enabled=True),
    GerberLayer(pcbnew.In6_Cu   ,'Inner6 Copper', ''),
    GerberLayer(pcbnew.In7_Cu   ,'Inner7 Copper', ''),
    GerberLayer(pcbnew.In8_Cu   ,'Inner8 Copper', ''),
    GerberLayer(pcbnew.In9_Cu   ,'Inner9 Copper', ''),
    GerberLayer(pcbnew.In10_Cu  ,'Inner10 Copper', ''),
    GerberLayer(pcbnew.In11_Cu  ,'Inner11 Copper', ''),
    GerberLayer(pcbnew.In12_Cu  ,'Inner12 Copper', ''),
    GerberLayer(pcbnew.In13_Cu  ,'Inner13 Copper', ''),
    GerberLayer(pcbnew.In14_Cu  ,'Inner14 Copper', ''),
    GerberLayer(pcbnew.In15_Cu  ,'Inner15 Copper', ''),
    GerberLayer(pcbnew.In16_Cu  ,'Inner16 Copper', ''),
    GerberLayer(pcbnew.In17_Cu  ,'Inner17 Copper', ''),
    GerberLayer(pcbnew.In18_Cu  ,'Inner18 Copper', ''),
    GerberLayer(pcbnew.In19_Cu  ,'Inner19 Copper', ''),
    GerberLayer(pcbnew.In20_Cu  ,'Inner20 Copper', ''),
    GerberLayer(pcbnew.In21_Cu  ,'Inner21 Copper', ''),
    GerberLayer(pcbnew.In22_Cu  ,'Inner22 Copper', ''),
    GerberLayer(pcbnew.In23_Cu  ,'Inner23 Copper', ''),
    GerberLayer(pcbnew.In24_Cu  ,'Inner24 Copper', ''),
    GerberLayer(pcbnew.In25_Cu  ,'Inner25 Copper', ''),
    GerberLayer(pcbnew.In26_Cu  ,'Inner26 Copper', ''),
    GerberLayer(pcbnew.In27_Cu  ,'Inner27 Copper', ''),
    GerberLayer(pcbnew.In28_Cu  ,'Inner28 Copper', ''),
    GerberLayer(pcbnew.In29_Cu  ,'Inner29 Copper', ''),
    GerberLayer(pcbnew.In30_Cu  ,'Inner30 Copper', ''),
    GerberLayer(pcbnew.B_Cu     ,'Back Copper', '.gbl', enabled=True),
    GerberLayer(pcbnew.F_Adhes  ,'Top_Adhesive', ''),
    GerberLayer(pcbnew.B_Adhes  ,'Back_Adhesive', ''),
    GerberLayer(pcbnew.F_Paste  ,'Top Paste', '.gtp', enabled=True),
    GerberLayer(pcbnew.B_Paste  ,'Back Paste', '.gbp', enabled=True),
    GerberLayer(pcbnew.F_SilkS  ,'Top SilkScreen', '.gto', enabled=True),
    GerberLayer(pcbnew.B_SilkS  ,'Back SilkScreen', '.gbo', enabled=True),
    GerberLayer(pcbnew.F_Mask   ,'Top SolderMask', '.gts', enabled=True),
    GerberLayer(pcbnew.B_Mask   ,'Back SolderMask', '.gbs', enabled=True),
    GerberLayer(pcbnew.Edge_Cuts,'Board Edges', '.gko', enabled=True),
    GerberLayer(pcbnew.Margin   ,'Margin', ''),
    GerberLayer(pcbnew.F_CrtYd  ,'Top CourtYard', ''),
    GerberLayer(pcbnew.B_CrtYd  ,'Back CourtYard', ''),
    GerberLayer(pcbnew.F_Fab    ,'Top Fab', ''),
    GerberLayer(pcbnew.B_Fab    ,'Back Fab', ''),
]
