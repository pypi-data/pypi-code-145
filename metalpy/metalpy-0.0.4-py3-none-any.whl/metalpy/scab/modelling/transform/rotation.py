import numpy as np
from scipy.spatial.transform import Rotation as R

from metalpy.utils.dhash import dhash
from .transform import Transform


class Rotation(Transform):
    def __init__(self, y, a, b, degrees=True, seq='xyz'):
        super().__init__()
        self.params = (y, a, b, degrees, seq)
        self.rot = R.from_euler(seq, [y, a, b], degrees=degrees).as_matrix()
        self.irot = R.from_euler(seq[::-1], [-b, -a, -y], degrees=degrees).as_matrix()

    def transform(self, mesh):
        return np.asarray(mesh).dot(self.rot)

    def inverse_transform(self, mesh):
        return np.asarray(mesh).dot(self.irot)

    def clone(self):
        return Rotation(*self.params)

    def __dhash__(self):
        return dhash(*self.params[:-1], self.params[-1])
