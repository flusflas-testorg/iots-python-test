from dataclasses import dataclass, field
from typing import List, overload

from .category import _CategoriesMethod
from .obj import APIObject
from .thing import _ThingsMethod


@dataclass
class Space(APIObject, _CategoriesMethod, _ThingsMethod):
    name: str

    def _build_partial_path(self):
        return f"/spaces/{self.name}"


@dataclass
class Spaces(APIObject):
    spaces: List[Space] = field(default_factory=list)

    def _build_partial_path(self):
        return f"/spaces"


class _SpacesMethod:
    """
    This class declares and implements the `spaces()` method.
    """
    @overload
    def spaces(self, name: str) -> Space:
        ...

    @overload
    def spaces(self) -> Spaces:
        ...

    def spaces(self, name: str = None):
        if name is None:
            return Spaces()._child_of(self)
        else:
            return Space(name)._child_of(self)
