# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/91_Nbdev.ipynb.

# %% auto 0
__all__ = ['prepare', 'gacp']

# %% ../nbs/91_Nbdev.ipynb 4
def prepare():
    "Export, test, and clean notebooks, and render README if needed"
    import nbdev.test, nbdev.clean, nbdev.quarto
    
    nbdev.quarto.nbdev_export.__wrapped__()
    print(f'nbdev_export finshed')
    nbdev.test.nbdev_test.__wrapped__(
        n_workers = 8,  # Number of workers
        timing = True,  # Time each notebook to see which are slow
    )
    print(f'nbdev_test finshed')
    nbdev.clean.nbdev_clean.__wrapped__()
    print(f'nbdev_clean finshed')
    nbdev.quarto.refresh_quarto_yml()
    print(f'refresh_quarto_yml finshed')
    nbdev.quarto.nbdev_readme.__wrapped__(chk_time=True)
    print(f'nbdev_readme finshed')

# %% ../nbs/91_Nbdev.ipynb 7
def gacp(
    comment:str="update"
):
    import subprocess
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", comment])
    subprocess.run(["git", "push"])
