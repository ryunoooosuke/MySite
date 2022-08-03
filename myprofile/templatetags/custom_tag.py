from django import template
# Djangoテンプレートタグライブラリ
register = template.Library()


@register.filter
def multiplication(value_a, value_b):
    """掛け算"""
    calculation_result = value_a * value_b
    return calculation_result
