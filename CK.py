import os, sys

try:

    __import__("cheek")cheek.ud()

except Exception as e:

    exit(str(e))
