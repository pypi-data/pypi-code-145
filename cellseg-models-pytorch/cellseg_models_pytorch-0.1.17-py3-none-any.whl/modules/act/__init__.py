from torch.nn import (
    CELU,
    ELU,
    GELU,
    GLU,
    SELU,
    Hardshrink,
    Hardsigmoid,
    LeakyReLU,
    PReLU,
    ReLU,
    ReLU6,
    RReLU,
    Sigmoid,
    SiLU,
    Tanh,
    Tanhshrink,
)

from .gated_gelu import GEGLU, ApproximateGELU
from .mish import Mish
from .star_relu import StarReLU
from .swish import Swish

ACT_LOOKUP = {
    "mish": Mish,
    "swish": Swish,
    "relu": ReLU,
    "relu6": ReLU6,
    "rrelu": RReLU,
    "selu": SELU,
    "celu": CELU,
    "gelu": GELU,
    "glu": GLU,
    "tanh": Tanh,
    "sigmoid": Sigmoid,
    "silu": SiLU,
    "prelu": PReLU,
    "leaky-relu": LeakyReLU,
    "elu": ELU,
    "hardshrink": Hardshrink,
    "tanhshrink": Tanhshrink,
    "hardsigmoid": Hardsigmoid,
    "star_relu": StarReLU,
    "geglu": GEGLU,
    "approximate_geglu": ApproximateGELU,
}

__all__ = [
    "Mish",
    "Swish",
    "ReLU",
    "ReLU6",
    "RReLU",
    "SELU",
    "CELU",
    "GELU",
    "GLU",
    "Tanh",
    "Sigmoid",
    "SiLU",
    "PReLU",
    "LeakyReLU",
    "ELU",
    "Hardshrink",
    "Tanhshrink",
    "Hardsigmoid",
    "Activation",
    "ACT_LOOKUP",
    "GEGLU",
    "ApproximateGELU",
]
