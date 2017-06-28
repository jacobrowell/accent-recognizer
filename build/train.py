import os
import json
import logging
from time import time
from glob import glob
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain2.tools.customxml.networkwriter import NetworkWriter
from pybrain.structure import TanhLayer


def train():
    logging.basicConfig(filename="logfile.log", level=logging.DEBUG)
    accents = ['CH', 'EN', 'IN', 'IR', 'IT', 'JA', 'KO']
    net = buildNetwork(13, 3, 7, hiddenclass=TanhLayer)
    ds = SupervisedDataSet(13, 7)

    logging.info("Started training network")

    try:
        speakers = os.listdir('samples')
        for speaker in speakers:
            samples = glob('samples/{}/part*'.format(speaker))
            for sample in samples:
                s = json.load(open(sample))
                out = [0, 0, 0, 0, 0, 0, 0]
                out[accents.index(s['accent'])] = 1

                for c in s['ceps']:
                    ds.addSample(c, out)

        trainer = BackpropTrainer(net)
        trainer.trainOnDataset(ds, 10000)
        trainer.testOnData(ds, verbose=True)

        NetworkWriter.writeToFile(net, 'models/model-{}.xml'.format(int(time())))
    except Exception as e:
        msg = "Something bad happened: {}".format(e.message)
        print msg
        logging.error(msg)


if __name__ == "main":
    train()
