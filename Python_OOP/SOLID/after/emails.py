from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        ...


class MyML(IContent):
    def format(self):
        return f'<myML> {self.text} </myML>'


class Div(IContent):
    def format(self):
        return f'<div> {self.text} </div>'


class IProtocol(ABC):
    @staticmethod
    @abstractmethod
    def format(name):
        ...


class IM(IProtocol):
    @staticmethod
    def format(name):
        return f"I'm {name}"


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        ...

    @abstractmethod
    def set_receiver(self, receiver):
        ...

    @abstractmethod
    def set_content(self, content):
        ...


class Email(IEmail):
    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = ""

    def set_sender(self, sender):
        self.__sender = protocol.format(sender)

    def set_receiver(self, receiver):
        self.__receiver = protocol.format(receiver)

    def set_content(self, *contents):
        for content in contents:
            self.__content += f"{content.format()}\n"

    def __repr__(self):
        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"


protocol = IM()
first_email = Email(protocol)
first_email.set_sender('qmal')
first_email.set_receiver('james')
first_content = MyML('Hello, there!')
second_content = Div('This is an important email!')
first_email.set_content(first_content, second_content)
print(first_email)
