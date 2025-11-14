#freegsnke headers
from freegsnke import build_machine
from freegsnke import equilibrium_update #update after
from freegsnke.jtor_update import ConstrainPaxisIp #profile object choice
from freegsnke import GSstaticsolver #static nonlinear solver


import numpy as np 
import matplotlib.pyplot as plt

import pickle #data storage or json?

# build machine (MASTU-like)
tokamak = build_machine.tokamak(
    active_coils_path=f"../machine_configs/MAST-U/MAST-U_like_active_coils.pickle",
    passive_coils_path=f"../machine_configs/MAST-U/MAST-U_like_passive_coils.pickle",
    limiter_path=f"../machine_configs/MAST-U/MAST-U_like_limiter.pickle",
    wall_path=f"../machine_configs/MAST-U/MAST-U_like_wall.pickle",
)