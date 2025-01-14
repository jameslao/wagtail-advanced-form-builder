#!/usr/bin/env python3
from __future__ import absolute_import, unicode_literals

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "build_test.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
