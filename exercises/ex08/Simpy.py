"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730470448"


class Simpy:
    values: list[float]

    def __init__(self, lists: list[float]):
        self.values = lists

    def __str__(self) -> str:
        return f"Simpy({str(self.values)})"

    def fill(self, value: float, num: int):
        self.values = list()
        i: int = 0
        while i < num:
            self.values.append(value)
            i += 1
    
    def sum(self) -> float:
        i: int = 0
        j: float = 0.0
        while i < len(self.values):
            j += self.values[i]
            i += 1
        return j
    
    def arange(self, start: float, stop: float, step: float = 1.0):
        i: float = start
        if(stop > 0):
            while i < stop:
                self.values.append(i)
                i += step
        elif(stop < 0):
            while i > stop:
                self.values.append(i)
                i += step
    
    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        sum: list[float] = list()
        i: int = 0
        if isinstance(rhs, Simpy):
            while i < len(self.values):
                sum.append(self.values[i] + rhs.values[i])
                i += 1
        elif isinstance(rhs, float):
            while i < len(self.values):
                sum.append(self.values[i] + rhs)
                i += 1        
        return Simpy(sum)

    # TODO: Your constructor and methods will go here.