from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    def __init__(self, name, price):
        super().__init__(name, 250, price)
