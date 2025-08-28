import sys
print("__name__: ", __name__)
print("__doc__: ", __doc__)
print("__file__: ", __file__)
print("names in this module: ", [n for n in dir() if not n.startswith("_")])
print("argv: ", sys.argv)
if __name__ == "__main__":
    print("Running as a script.")
