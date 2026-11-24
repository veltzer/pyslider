# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `src/pyslider/main.py:13` - the only endpoint is a `hello` stub that prints "Hello"; nothing in the package creates PDF slides from markdown as the description (`pyproject.toml:15`, `config/project.lua:2`, `README.md:6`) promises, yet 0.0.1 is published on PyPI. Implement the converter or describe the package honestly as a placeholder.
- `pyproject.toml:25` - classifier `Development Status :: 4 - Beta` for a package with no functionality; use `1 - Planning` until it does something.

## Low

- `src/pyslider/configs.py:9` - `ConfigOutput` (terse/stats/"show projects?"/"print what the project is not") is copied from a project-scanning tool and is used by no endpoint; delete it or replace it with real slide options.
- `pyproject.toml:99` - the dev dependency group repeats `pylogconf` and `pytconf` (`pyproject.toml:100`), which are already runtime dependencies at `pyproject.toml:36`; remove the duplicates.
- `doc/links.txt:1` - points at GitPython documentation and `doc/HOWTO.txt:1` holds a fleet-rebuild snippet, both unrelated to this project, while `doc/DESIGN.txt`, `doc/DONE.txt` and `doc/TODO.txt` are empty; delete the leftovers or fill them with pyslider content.
- `rsconstruct.toml:28` - the ruff and mypy processors (`rsconstruct.toml:32` too) list `config` in `src_dirs`, but `config/` holds only `.lua` files (mypy reports "There are no .py[i] files in directory 'config'"); drop `config` from both lists.
