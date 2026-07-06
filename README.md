# example-python

[![coverage badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fdemo.coveragetracker.dev%2Fapi%2Fbadge%2FCoverageTracker%2Fexample-python%2Fcoverage.json)](https://demo.coveragetracker.dev/CoverageTracker/example-python?metric=coverage)
[![complexity badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fdemo.coveragetracker.dev%2Fapi%2Fbadge%2FCoverageTracker%2Fexample-python%2Fcomplexity.json)](https://demo.coveragetracker.dev/CoverageTracker/example-python?metric=complexity)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FCoverageTracker%2Fexample-python.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FCoverageTracker%2Fexample-python?ref=badge_shield)

A small, idiomatic Python text-analysis toolkit used as the Python reference
example for [Coverage Tracker](https://coveragetracker.dev). It exists to
give the Python row in the
[coverage report generation guide](https://coveragetracker.dev/docs/generating-coverage-reports)
a live, working reference, and to populate the
[demo dashboard](https://demo.coveragetracker.dev) with real trend data.

**This is a demo/marketing repo, not a test suite for Coverage Tracker
itself.**

## What's here

- `textkit/` — readability scoring, slug generation, and word-frequency
  helpers, each with real branching logic.
- `tests/` — a [pytest](https://pytest.org) suite with a few deliberately
  uncovered branches, so `branch_coverage < line_coverage` shows up on the
  dashboard.
- `.github/workflows/coverage.yml` — runs tests under
  [coverage.py](https://coverage.readthedocs.io), generates a
  [Radon](https://radon.readthedocs.io) complexity report, then reports both
  to the demo instance via the `coverage-tracker` reporting Action.

## Running locally

```sh
pip install -e ".[dev]"
coverage run -m pytest && coverage lcov -o coverage.lcov   # writes coverage.lcov
radon cc -j textkit > radon.json
```


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FCoverageTracker%2Fexample-python.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FCoverageTracker%2Fexample-python?ref=badge_large)