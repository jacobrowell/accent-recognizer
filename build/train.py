from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain2.tools.customxml.networkwriter import NetworkWriter
from pybrain.structure import TanhLayer
import json
from time import time

samples = open("samples.json", "r")
accents = json.load(samples)

net = buildNetwork(13, 3, 7, hiddenclass=TanhLayer)

ds = SupervisedDataSet(13, 7)

for accent in accents:
    samples = accents[accent]["samples"]
    out = accents[accent]["out"]

    for sample in samples:
        ds.addSample(sample, out)

trainer = BackpropTrainer(net)
trainer.trainOnDataset(ds, 10000)
trainer.testOnData(ds, verbose=True)

NetworkWriter.writeToFile(net, 'models/model-{}.xml'.format(int(time())))
