"""Multi-1D/Multi-2D/Multi-3D automaic control."""

import os 
import shutil
import subprocess
import re
import warnings
import skopt
from enum import Enum
import struct

VERSION = '0.1.0'