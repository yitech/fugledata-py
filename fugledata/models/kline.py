# coding: utf-8

"""
    standard public schema

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 12.2.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Kline(BaseModel):
    """
    Kline
    """ # noqa: E501
    id: StrictInt = Field(description="Note: This is a Primary Key.<pk/>")
    symbol: Annotated[str, Field(strict=True, max_length=255)]
    dt: date
    open: Union[StrictFloat, StrictInt]
    high: Union[StrictFloat, StrictInt]
    low: Union[StrictFloat, StrictInt]
    close: Union[StrictFloat, StrictInt]
    volume: StrictInt
    __properties: ClassVar[List[str]] = ["id", "symbol", "dt", "open", "high", "low", "close", "volume"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Kline from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Kline from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "symbol": obj.get("symbol"),
            "dt": obj.get("dt"),
            "open": obj.get("open"),
            "high": obj.get("high"),
            "low": obj.get("low"),
            "close": obj.get("close"),
            "volume": obj.get("volume")
        })
        return _obj

