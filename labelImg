#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys
CURRENT_FILE_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(CURRENT_FILE_DIR, 'src'))
sys.path.insert(0, os.path.join(CURRENT_FILE_DIR, 'src', 'labelImg'))

from labelImg.app import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
