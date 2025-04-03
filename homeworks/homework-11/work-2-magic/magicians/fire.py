from .magic import Magic
from .steam import Steam
from .bolt import Bolt
from .lava import Lava


class Fire(Magic):
    def __init__(self):
        super().__init__("Огонь")
        self.mixtures = {'Water': Steam, 'Air': Bolt, 'Soil': Lava}
