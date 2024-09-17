"""Defines custom types and type aliases for the fire_py package."""

from __future__ import annotations

from typing import Literal, Required, TypedDict

Reference = TypedDict("Reference", {"$ref": str})


class Base(TypedDict, total=False):
    """Base class for property types with an optional description."""

    description: str


class Numeric[T](Base):
    """Base class for numeric property types with minimum and maximum values."""

    minimum: T
    maximum: T
    monetary: bool


class Integer(Numeric[int]):
    """Represents an integer property with optional monetary attribute."""

    type: Required[Literal["integer"]]
    monetary: bool


class Number(Numeric[float]):
    """Represents a number property."""

    type: Required[Literal["number"]]


class Boolean(Base):
    """Represents a boolean property."""

    type: Required[Literal["boolean"]]

class String(Base):
    """Represents a string property with an optional enumeration of allowed values."""

    type: Required[Literal["string"]]
    enum: list[str]


class Date(String):
    """Represents a date property."""

    format: Required[Literal["date"]]


class DateTime(String):
    """Represents a date-time property."""

    format: Required[Literal["date-time"]]


class Array(Base):
    """Represents an array property with a list of items."""

    type: Required[Literal["array"]]
    items: Property | Reference
    minItems: int
    uniqueItems: bool



class Object(Base):
    """Represents an object property with properties and required fields."""

    title: str
    type: Required[Literal["object"]]
    properties: dict[str, Property | Reference]
    required: list[str]
    additionalProperties: bool


Property = (
    String
    | Integer
    | Number
    | Boolean
    | DateTime
    | Array
    | Object
)
