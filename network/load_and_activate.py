import sys

from pybrain.tools.xml.networkreader import NetworkReader

net = NetworkReader.readFrom(sys.argv[1])

for line in sys.stdin:
    tokens = line.strip().split()
    fname = tokens[0]
    inputs = tokens[1:-1]
    output = tokens[-1]
    print fname, net.activate(inputs), 'vs', output