"""
类装饰器实现了 ValidatorMeta 元类的功能
"""

_validators = {}


def register(cls):
    """装饰器：将所有校验器类统一注册起来，方便后续使用"""
    _validators[cls.name] = cls
    return cls


@register
class StringValidator:
    name = 'string'


@register
class IntegerValidator:
    name = 'int'


print(_validators)
