import sys

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.supervised.trainers import BackpropTrainer

net = buildNetwork(32, 128, 1)
ds = SupervisedDataSet(32, 1)

for line in sys.stdin:
    tokens = line.strip().split()
    inputs = map(float, tokens[1:-1])
    output = (float(tokens[-1]),)
    ds.addSample(inputs, output)

trainer = BackpropTrainer(net, ds)
trainer.trainUntilConvergence()

NetworkWriter.writeToFile(net, sys.argv[1])
