# -*- coding: utf-8 -*-
import random


def test_something():
    print("Test B")
    if random.randint(1, 10) % 2 == 0:
        assert False
    else:
        assert True
