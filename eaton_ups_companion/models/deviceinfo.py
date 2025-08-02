from dataclasses import dataclass
from typing import Dict, Any, List
from . import EcoControl, VoltageRange

@dataclass
class DeviceInfo:
    product: str
    model: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DeviceInfo":
        return cls(
            product=data["product"],
            model=str(data["model"]),

        )