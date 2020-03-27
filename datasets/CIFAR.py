from datasets.data import Data

class CIFAR(Data):
    def __init__(self):
        CIFAR_dir = '/student/rolwesg/Data/CIFAR10/'
        CIFAR_img_size = 256
        self.name = "CIFAR"
        super().__init__(CIFAR_dir, CIFAR_img_size)
