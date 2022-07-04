"""
Collection of research functions
"""
import pandas as pd
import numpy as np


def difference_returns(s: pd.Series, delta_time: int):
    """
    calculate the difference in returns of a price series
    """
    s = s.copy()
    return s.diff() / np.sqrt(delta_time)


def empirical_rule_quartiles(s: pd.Series) -> list:
    """
    Show the four quartiles of the normal distribution
    """
    s = s.copy()

    mu = s.mean()
    std = s.std()
    r1 = s.loc[s.gt(mu - std) & s.lt(mu + std)]
    r2 = s.loc[s.gt(mu - std * 2) & s.lt(mu + std * 2)]
    r3 = s.loc[s.gt(mu - std * 3) & s.lt(mu + std * 3)]
    r4 = s.loc[s.gt(mu - std * 4) & s.lt(mu + std * 4)]

    q1 = round(len(r1) / len(s), 2)
    q2 = round(len(r2) / len(s), 2)
    q3 = round(len(r3) / len(s), 2)
    q4 = len(r4) / len(s)
    return [q1, q2, q3, q4]


def empirical_rule(s: pd.Series) -> bool:
    """
    Tells if a distribution is normal
    """
    q = empirical_rule_quartiles(s)
    return q[0] >= 0.68 and q[1] >= 0.95 and q[2] >= 0.99
