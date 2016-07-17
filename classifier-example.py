#!/bin/python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.join('./decision-tree/'))

import decision_tree as dt
from sklearn.datasets import load_iris

if __name__ == '__main__':
    d = load_iris()

    tree = dt.DecisionTreeClassifier(criterion='entropy', prune='depth', max_depth=3)
    tree.fit(d.data[0:150], d.target[0:150])
    tree.show_tree()

    pred = tree.predict(d.data[100:101])
    print(pred, d.target[100:101])
