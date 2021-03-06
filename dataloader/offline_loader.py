from random import randint
import numpy as np
from os import system

from .loader import Loader

class OfflineLoader(Loader):
  def __init__(self, data, batch_size):
    # map each label to the index of all that label's images
    self.map_label_indices = {label: np.flatnonzero(data.table['category_id'] == label).tolist() for label in data.table['category_id']}

    super().__init__(data, batch_size, "Offline Triplets Loader")

  def getSet(self, index):
    # set anchor to next image in data table
    anchor_class_id = self.data.set[index][1]
    neg_class_id = anchor_class_id
    # select different class for negative example
    while (anchor_class_id == neg_class_id):
      neg_class_id = np.random.choice(self.data.table['category_id'], 1, replace=False)[0]
    assert anchor_class_id != neg_class_id, "Negative example must be of a different class than anchor."

    # randomly select a positive and a negative image
    pos_idx = np.random.choice(self.map_label_indices[anchor_class_id], 1, replace=False)[0]
    neg_idx = np.random.choice(self.map_label_indices[neg_class_id], 1, replace=False)[0]

    # return [images], [labels]
    anchor_img, anchor_label, anchor_file = self.data.set[index]
    pos_img, pos_label, pos_file = self.data.set[pos_idx]
    neg_img, neg_label, neg_file = self.data.set[neg_idx]
    return [anchor_img, pos_img, neg_img], [anchor_label, pos_label, neg_label], [anchor_file, pos_file, neg_file]
