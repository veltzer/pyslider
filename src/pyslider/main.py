"""
main
"""

import sys

import pylogconf.core
from pytconf import config_arg_parse_and_launch, register_endpoint, register_main

from pyslider.static import APP_NAME, DESCRIPTION, VERSION_STR


@register_endpoint(
    configs=[],
    description="Say hello",
)
def hello() -> None:
    print("Hello")


@register_main(
    main_description=DESCRIPTION,
    app_name=APP_NAME,
    version=VERSION_STR,
)
def main():
    pylogconf.core.setup()
    # make sure stdout is line buffered
    sys.stdout.reconfigure(line_buffering=True)
    config_arg_parse_and_launch()


if __name__ == "__main__":
    main()
