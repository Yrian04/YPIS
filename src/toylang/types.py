from __future__ import annotations
from typing import NewType


class Type_:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def __str__(self) -> str:
        return self.name
    
NoneType_ = NewType('NoneType_', Type_)
AnyType_ = NewType('AnyType_', Type_)
ElementType_ = NewType('ElementType_', Type_)
SetType_ = NewType('SetType_', Type_)
BoolType_ = NewType('BoolType_', Type_)
UnknownType_ = NewType('UnknownType_', Type_)

none_ = NoneType_(Type_('none'))
any_ = AnyType_(Type_('any'))
unknown_ = UnknownType_(Type_('unknown'))
element_ = ElementType_(Type_('element'))
set_ = SetType_(Type_('set'))
bool_ = BoolType_(Type_('bool'))


class FuncType_(Type_):
    def __init__(self, in_params: list[Type_], out_params: list[Type_]) -> None:
        super().__init__('func')
        self.in_params = in_params
        self.out_params = out_params

    @property
    def name(self) -> str:
        return (
            f'{', '.join(t.name for t in self.in_params)} -> '
            f'{self._name}'
            f' -> {', '.join(t.name for t in self.out_params)}'
        )
    
    def apply(self, in_args: list[Type_]) -> list[Type_]:
        if len(in_args) > len(self.in_params):
            raise ValueError(
                f'Too many args for func. It needs {len(self.in_params)}, '
                f'but {len(in_args)} were given.'
            )
        if len(in_args) < len(self.in_params):
            raise ValueError(
                f'Too less args for func. It needs {len(self.in_params)}, '
                f'but {len(in_args)} were given.'
            )
        for in_arg, in_param in zip(in_args, self.in_params):
            if in_param is not any_ and in_arg is not in_param:
                raise  ValueError(
                    f'Func needs {in_param}, but {in_arg} were given.'
                )
        return self.out_params.copy()
