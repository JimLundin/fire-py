"""Defines custom types and type aliases for the fire_py package."""

from __future__ import annotations

from typing import Literal, TypedDict

Reference = TypedDict("Reference", {"$ref": str})


class BaseProperty(TypedDict, total=False):
    description: str


class StringProperty(BaseProperty):
    type: Literal["string"]
    enum: list[str]


class NumericProperty[T](BaseProperty):
    type: Literal["number"]
    minimum: T
    maximum: T
    monetary: bool


class IntegerProperty(NumericProperty[int]):
    type: Literal["integer"]
    monetary: bool


class NumberProperty(NumericProperty[float]):
    type: Literal["number"]


class BooleanProperty(BaseProperty):
    type: Literal["boolean"]


class DateProperty(BaseProperty):
    type: Literal["string"]
    format: Literal["date"]


class DateTimeProperty(BaseProperty):
    type: Literal["string"]
    format: Literal["date-time"]


class ArrayProperty(BaseProperty):
    type: Literal["array"]
    items: list[Property]
    minItems: int


class ObjectProperty(BaseProperty):
    type: Literal["object"]
    properties: dict[str, Property]
    required: list[str]
    additionalProperties: bool


Property = (
    StringProperty
    | IntegerProperty
    | NumberProperty
    | BooleanProperty
    | DateTimeProperty
    | ArrayProperty
    | ObjectProperty
)
