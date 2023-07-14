from abc import ABC, abstractmethod


class BaseWorker(ABC):
    @staticmethod
    @abstractmethod
    def work():
        ...


class Worker(BaseWorker):
    @staticmethod
    def work():
        print("I'm working!!")


class SuperWorker(BaseWorker):
    @staticmethod
    def work():
        print("I work very hard!!!")


class BestWorker(BaseWorker):
    @staticmethod
    def work():
        print("I'm working 24/7!!!!")


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, BaseWorker):
            raise AssertionError(f'`worker` must be an instance of type - one of the subclasses of {BaseWorker}')

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


manager = Manager()

worker = Worker()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
manager.set_worker(super_worker)
manager.manage()

best_worker = BestWorker()
manager.set_worker(best_worker)
manager.manage()