# AUTOGENERATED! DO NOT EDIT! File to edit: ../../notebooks/CLI.ipynb.

# %% auto 0
__all__ = ['app']

# %% ../../notebooks/CLI.ipynb 3
from contextlib import contextmanager
import os
import types

import typer

import captn
from captn.cli.token import token
from captn.cli.version import version

from captn.cli import db, ds, api_key, user
from captn.client import _replace_env_var

# %% ../../notebooks/CLI.ipynb 5
app = typer.Typer(help="CLI for interfacing with Capt’n.")

# %% ../../notebooks/CLI.ipynb 7
# token root command

app.command()(token)

# %% ../../notebooks/CLI.ipynb 8
# version root command

app.command()(version)

# %% ../../notebooks/CLI.ipynb 9
# db root command

app.add_typer(db.app, name="db")

# %% ../../notebooks/CLI.ipynb 10
# ds root command

app.add_typer(ds.app, name="ds")

# %% ../../notebooks/CLI.ipynb 11
# api_key root command

app.add_typer(api_key.app, name="api-key")

# %% ../../notebooks/CLI.ipynb 12
# user root command

app.add_typer(user.app, name="user")
