# -*- coding: utf-8 -*-

import numpy as np
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain2.tools.customxml.networkwriter import NetworkWriter
from pybrain2.tools.customxml.networkreader import NetworkReader
from pybrain.structure import TanhLayer
import json
from time import time


class NNClassifier:

    def __init__(self, model):
        self.net = NetworkReader.readFrom(model)
        self.accents = [
            "CH",
            "EN",
            "IN",
            "IR",
            "IT",
            "JA",
            "KO",
        ]

    def train(self):
        samples = open("models/samples.json", "r")
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

    def classify(self, cache_file):
        x = []
        ceps = np.load(cache_file)
        num_ceps = len(ceps)
        x.append(np.mean(ceps[int(num_ceps / 10):int(num_ceps * 9 / 10)], axis=0))
        vx = np.array(x)

        result = self.net.activate(vx[0].tolist()).tolist()
        prob = max(result)
        accent = self.accents[result.index(prob)]

        print accent, prob
        return accent, prob
