"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730470448"


class Simpy:
    values: list[float]

    def __init__(self, lists: list[float]):
        """A constructor for the class"""
        self.values = lists

    def __str__(self) -> str:
        """Converts the contents of Simpy to a string"""
        return f"Simpy({str(self.values)})"

    def fill(self, value: float, num: int):
        """Fills an empty string with a specified float and certain number of time."""
        self.values = list()
        i: int = 0
        while i < num:
            self.values.append(value)
            i += 1
    
    def sum(self) -> float:
        """Adds the contents of the input list."""
        i: int = 0
        j: float = 0.0
        while i < len(self.values):
            j += self.values[i]
            i += 1
        return j
    
    def arange(self, start: float, stop: float, step: float = 1.0):
        """Generates a list with a specified start, stop and step!"""
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
        """An overloaded constructor for the + operator!"""
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

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """An overloaded constructor for the ** operator!"""
        result: list[float] = list()
        i: int = 0
        if isinstance(rhs, Simpy):
            while i < len(self.values):
                result.append(self.values[i] ** rhs.values[i])
                i += 1
        elif isinstance(rhs, float):
            while i < len(self.values):
                result.append(self.values[i] ** rhs)
                i += 1
        return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """An overloaded constructor for the == operator!"""
        result: list[bool] = list()
        i: int = 0
        if isinstance(rhs, Simpy):
            while i < len(self.values):
                if(self.values[i] == rhs.values[i]):
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        elif isinstance(rhs, float):
            while i < len(self.values):
                if(self.values[i] == rhs):
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """An overloaded constructor for the > operator!"""
        result: list[bool] = list()
        i: int = 0
        if isinstance(rhs, Simpy):
            while i < len(self.values):
                if(self.values[i] > rhs.values[i]):
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        elif isinstance(rhs, float):
            while i < len(self.values):
                if(self.values[i] > rhs):
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """An overloaded constructor for the subscription operator!"""
        result: list[float] = list()
        i: int = 0
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            while i < len(self.values):
                if(rhs[i]):
                    result.append(self.values[i])
                i += 1
        return Simpy(result)