# -*- coding: utf-8 -*-
"""
    Github Api Tests
    ~~~~~~~~~~~~~~

    Tests the Github API to scan for score application.

    :copyright: (c) 2016 Christophe Graniczny
    :license: MIT, see LICENSE for more details.
"""
import pytest
from gitmojithis import GithubRepo

def test_returns():
    stats = GithubRepo().scan('bullshit_repo')
    assert stats.exists() == False
