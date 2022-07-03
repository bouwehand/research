import numpy as np
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt


def candlestick(df, x):
    fig = go.Figure(
        data=[go.Candlestick(
            x=x,
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close'])
        ])

    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.show()


def brownian_motion_values(n: int, dt: int) -> list:
    """
    :param n: total number of results
    :param dt: delta time as difined in seconds so 3600 for an hour
    :return:
    """
    dif = np.sqrt(dt) * np.random.normal(size=(n - 1))
    return np.cumsum(dif)


def reduce_time_frame(lst: list, n):
    result = {
        "open": [],
        "close": [],
        "high": [],
        "low": []
    }
    for i in range(0, len(lst), n):
        tmp = lst[i:i + n]
        result["open"].append(tmp[0])
        result["close"].append(tmp[-1])
        result["high"].append(max(tmp))
        result["low"].append(min(tmp))

    return result


def create_axis_x(bars: int, interval: int, start: int):
    total = start + (bars * interval)
    return np.linspace(start, total, bars + 1, dtype=int)


