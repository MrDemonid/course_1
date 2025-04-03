from .magic import Magic
from .lava import Lava
from .mud import Mud
from .dust import Dust


class Soil(Magic):
    def __init__(self):
        super().__init__("Земля")
        self.mixtures = {'Water': Mud, 'Fire': Lava, 'Air': Dust}
