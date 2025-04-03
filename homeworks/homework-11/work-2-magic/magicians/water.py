from .magic import Magic
from .steam import Steam
from .storm import Storm
from .mud import Mud


class Water(Magic):
    def __init__(self):
        super().__init__("Вода")
        self.mixtures = {'Fire': Steam, 'Air': Storm, 'Soil': Mud}
