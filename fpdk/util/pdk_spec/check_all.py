from types import ModuleType
from typing import Tuple

from . import check_list
from .interfaces import ICheckRule
from .rule import RuleLib


def check_pdk(*, pdk: ModuleType, mode: str = "basic", extend_rules: Tuple[ICheckRule, ...] = tuple()):

    rules = RuleLib()
    rules += check_list.BASIC_RULES  # type: ignore

    if mode == "extend":
        rules += check_list.EXTEND_RULES  # type: ignore

    for rule in extend_rules:
        assert isinstance(rule, ICheckRule), f"param[{extend_rules}] must be ICheckRule"
        rules += rule

    rules.check(pdk)


if __name__ == "__main__":
    # from fpdk.util.standard_check_util.technology.bands import BandsCheckRule
    # extend_rules = (BandsCheckRule(),)
    # import fpdk
    # check_pdk(pdk=fpdk, extend_rules=extend_rules)

    # import fpdk
    # check_pdk(pdk=fpdk)
    # check_pdk(pdk=fpdk, mode="extend")

    import layout01

    check_pdk(pdk=layout01)
