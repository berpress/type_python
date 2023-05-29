from pydantic import BaseModel, Extra, ValidationError


class Model(BaseModel):
    v: str

    class Config:
        max_anystr_length = 10
        error_msg_templates = {
            'value_error.any_str.max_length': 'max_length:{limit_value}',
        }


try:
    Model(v='x' * 20)
except ValidationError as e:
    print(e)
    """
    1 validation error for Model
    v
      max_length:10 (type=value_error.any_str.max_length; limit_value=10)
    """


class ModelA(BaseModel, extra=Extra.forbid):
    a: str


model_dict = {'a': 'foo', 'b': 'bar'}

try:
    ModelA(**model_dict)
except ValidationError as e:
    print(e)
    """
    1 validation error for Model
    b
      extra fields not permitted (type=value_error.extra)
    """
