from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    def __init__(self, name, price):
        super().__init__(name, 200, price)
