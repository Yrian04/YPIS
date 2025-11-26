from toylang.types import *


class Operator:
    def __init__(
        self,
        name: str,
        *in_types: Type_, 
        out_type: Type_
    ) -> None:
        self.name = name
        self.in_params = in_types
        self.out_param = out_type
    
    def apply(self, in_args: list[Type_]) -> Type_:
        if len(in_args) > len(self.in_params):
            raise ValueError(
                f'Too many args for operator {self.name}. '
                f'It needs {len(self.in_params)}, '
                f'but {len(in_args)} were given.'
            )
        if len(in_args) < len(self.in_params):
            raise ValueError(
                f'Too less args for operator {self.name}. '
                f'It needs {len(self.in_params)}, '
                f'but {len(in_args)} were given.'
            )
        for in_arg, in_param in zip(in_args, self.in_params):
            if in_param is not any_ and in_arg is not in_param:
                raise ValueError(
                    f'operator {self.name} needs {in_param}, '
                    f'but {in_arg} were given.'
                )
        return self.out_param


class ArithmeticsOperator(Operator):
    def __init__(self, name: str, arity: int, toy_type: Type_) -> None:
        super().__init__(name, *([toy_type]*arity), out_type=toy_type)


union = ArithmeticsOperator('union', 2, set_)
intersection = ArithmeticsOperator('intersection', 2, set_)
difference = ArithmeticsOperator('difference', 2, set_)
product = ArithmeticsOperator('product', 2, set_)

and_ = ArithmeticsOperator('and', 2 , bool_)
or_ = ArithmeticsOperator('and', 2 , bool_)
not_ = ArithmeticsOperator('not', 1, bool_)

in_ = Operator('in', any_, set_, out_type=bool_)
not_in_ = Operator('not in', any_, set_, out_type=bool_)

eq_ = Operator('eq', any_, any_, out_type=bool_)
ne_ = Operator('ne', any_, any_, out_type=bool_)
gt_ = Operator('gt', set_, set_, out_type=bool_)
lt_ = Operator('lt', set_, set_, out_type=bool_)
ge_ = Operator('ge', set_, set_, out_type=bool_)
le_ = Operator('le', set_, set_, out_type=bool_)
