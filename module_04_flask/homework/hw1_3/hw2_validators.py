"""
Довольно неудобно использовать встроенный валидатор NumberRange для ограничения числа по его длине.
Создадим свой для поля phone. Создайте валидатор обоими способами.
Валидатор должен принимать на вход параметры min и max — минимальная и максимальная длина,
а также опциональный параметр message (см. рекомендации к предыдущему заданию).
"""
from typing import Optional
import math
from flask_wtf import FlaskForm
from wtforms import Field, ValidationError


def number_length(min: int, max: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        data = field.data
        if (data is not None
                and not math.isnan(data)
                and (min is None or data >= min)
                and (max is None or data <= max)
        ):
            return

        if max is None:
            message = field.gettext("Number must be at least %(min)s.")

        elif min is None:
            message = field.gettext("Number must be at most %(max)s.")

        else:
            message = field.gettext("Number must be between %(min)s and %(max)s.")

        raise ValidationError(message % dict(min=min, max=max))
    return _number_length


class NumberLength:
    def __init__(self, min: int, max: int, message: Optional[str] = None):
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        data = field.data
        if (data is not None
                and not math.isnan(data)
                and (self.min is None or data >= self.min)
                and (self.max is None or data <= self.max)
        ):
            return

        if self.message is not None:
            message = self.message
        elif self.max is None:
            message = field.gettext("Number must be at least %(min)s.")

        elif self.min is None:
            message = field.gettext("Number must be at most %(max)s.")

        else:
            message = field.gettext("Number must be between %(min)s and %(max)s.")

        raise ValidationError(message % dict(min=self.min, max=self.max))
