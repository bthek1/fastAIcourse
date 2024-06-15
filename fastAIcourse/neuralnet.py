# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/021_how-does-a-neural-net-really-work.ipynb.

# %% auto 0
__all__ = ['plot_function']

# %% ../nbs/021_how-does-a-neural-net-really-work.ipynb 7
def plot_function(f, title=None, min=-2.1, max=2.1, color='r', ylim=None):
    import numpy as np, matplotlib.pyplot as plt
    from fastai.basics import torch
    x = torch.linspace(min,max, 100)[:,None]
    if ylim: plt.ylim(ylim)
    plt.rc('figure', dpi=90)
    plt.plot(x, f(x), color)
    if title is not None: plt.title(title)
