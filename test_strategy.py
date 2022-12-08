# pylint: disable=too-few-public-methods
"The Strategy Pattern Concept"
from abc import ABCMeta, abstractmethod

class Context():
    "This is the object whose behavior will change"

    @staticmethod
    def request(strategy):
        "The request is handled by the class passed in"
        return strategy()

class IMensaje(metaclass=ABCMeta):
    "A strategy Interface"

    @staticmethod
    @abstractmethod
    def __str__():
        "Implement the __str__ dunder"

class ConcreteStrategyA(IMensaje):
    "A Concrete Strategy Subclass"

    def __str__(self):
        return "I am ConcreteStrategyA"

class ConcreteStrategyB(IMensaje):
    "A Concrete Strategy Subclass"

    def __str__(self):
        return "I am ConcreteStrategyB"

class ConcreteStrategyC(IMensaje):
    "A Concrete Strategy Subclass"

    def __str__(self):
        return "I am ConcreteStrategyC"

# The Client
CONTEXT = Context()

print(CONTEXT.request(ConcreteStrategyA))
print(CONTEXT.request(ConcreteStrategyB))
print(CONTEXT.request(ConcreteStrategyC))