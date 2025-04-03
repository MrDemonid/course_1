from .magic import Magic
from .bolt import Bolt
from .storm import Storm
from .dust import Dust


class Air(Magic):
    def __init__(self):
        super().__init__("Воздух")
        self.mixtures = {'Water': Storm, 'Fire': Bolt, 'Soil': Dust}
