# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_Deployment.ipynb.

# %% auto 0
__all__ = ['learn']

# %% ../nbs/01_Deployment.ipynb 25
#|eval: false
learn = vision_learner(dls, resnet18, metrics=error_rate)
learn.fine_tune(5)
