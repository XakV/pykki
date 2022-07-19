#!/usr/bin/env python3
from pathlib import Path
from unicodedata import name
import typer
import rich
import configparser
import os
import sys


class pykki:
    '''
    A pythonic shout of self knowledge
    '''
    def __init__(self):
        self.keybinding = ''
        self.action = ''
        self.tags = []


class pykkido:
    '''
    The Pythonic Way of Keys.
    '''
    def __init__(self):
        self.name = name
        self.ref_path = Path.home() / '.config' / 'pykki' / self.name
        self.metadata = {}
        self.entry = pykki
        self.kido = []
        

    def delete_all(self, ref_path):
        self.ref_path.unlink()

    def delete_ki(self, entry):
        self.remove()


