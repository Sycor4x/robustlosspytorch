#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
  name="robust_loss_pytorch",
  packages=find_packages(),
  version="0.0.2",
  package_data={
    "robust_loss_pytorch": ["data/*.npz", "data/*.mat"]
  }
)
