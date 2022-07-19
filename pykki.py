#!/usr/bin/env python3
from pathlib import Path
from unicodedata import name
import typer
import rich
import configparser
import os
import sys


class TUI_Cheat:
    def __init__(self):
        self.name = name
        self.ref_path = Path.home() / '.config' / 'pykki' / self.name
        self.tags = []
        self.src_url = src_url


def 
