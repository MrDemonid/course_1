import argparse


parser = argparse.ArgumentParser(description='Sample')
parser.add_argument('-x', action='store_const', const=42)
parser.add_argument('-y', action='store_true')
parser.add_argument('-z', action='append')
parser.add_argument('-i', action='append_const', const=int, dest='types')
parser.add_argument('-f', action='append_const', const=float, dest='types')
parser.add_argument('-s', action='append_const', const=str, dest='types')

# args = parser.parse_args()
args = parser.parse_args("-x -y -z 42 -z 73 -i -f -s".split())

print(args)

# Namespace(x=42, y=True, z=['42', '73'], types=[<class 'int'>, <class 'float'>, <class 'str'>])
