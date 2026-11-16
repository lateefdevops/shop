#!/bin/sh
echo "[build] compiling..."; python3 -m py_compile shop.py || exit 1
echo "[test]  running unit tests..."; python3 test_shop.py
