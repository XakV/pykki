#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path
import typer
import rich
import os
import sys


pykkiai = typer.Typer()

class Pykki:
    """
    A pythonic shout of self knowledge.
    The basic unit of a cheat sheet.
    
    Args:
        self.keybinding (str): An ordered combination of keys, 'CTRL+C' where the '+' indicates 
            CTRL should be held while C is struck, then both are released.
        self.action (str): The response to the keypress sequence. 'Copy highlighted text'.
        self.tags (list): A list of zero or more strings associated with the action.
    """
    def __init__(self):
        self.keybinding = ''
        self.action = ''
        self.tags = []


class Pykkido:
    """
    The Pythonic Way of Keys.

    Args:
        self.config (Path): A path to a config file
        self.metadata (dict): A dict of data about the dojo
        self.dojo (list): A list of Pykki that make up the cheat sheet
    """
    def __init__(self, config, metadata, dojo):
        self.config = Path.home() / '.config' / 'pykki' / self
        self.metadata = {
            'data_path': Path.home() / '.dojo' / self,
            'creation': datetime.date,
            'updated': datetime.date,
        }
        self.dojo = []
        

@pykkiai.command()
def new(waza: Pykkido):
    """
    waza is a group of techniques
    for keybinds, a cheatsheet
    
    Args:
        waza: (Pykkido) a cheatsheet
        
    Returns:
        waza.config
        waza.metadata
        waza.dojo
    """
    pass


@pykkiai.command()
def add(waza: Pykkido, kyo: Pykki):
    """
    Add a new keybind item to a cheatsheet
    """
    pass


@pykkiai.command()
def show(waza: Pykkido, *args):
    """
    Show a set of keybinds
    
    Args:
        waza (Pykkido): a cheatsheet
        
    Optional Args:
        sort (str): A column to sort by
        filter (str): A filter to apply
        
    """
    pass


@pykkiai.command()
def delete(waza: Pykkido, kyo: Pykki):
    """
    Remove a single keybind from a waza/cheatsheet
    
    Args:
        waza (Pykkido): a cheatsheet
        kyo (Pykki): a keybind
    """
    pass


@pykkiai.command()
def purge(waza: Pykkido, *args):
    """
    Delete an entire cheatsheet
    
    Args:
        waza (Pykkido): a cheatsheet
        
    Optional Args:
        force (Bool): defaults Falsey
    """
    pass
