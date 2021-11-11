# Contributing

## Documentation

### Conda environment for documentation

Install miniconda first.

```bash
conda env create -f environment.yml
conda activate docs
```

### Generating documentation

Install Sphinx and plugins:
```bash
pip install sphinx autodoc recommonmark sphinx-rtd-theme
```

Generate HTML:
```bash
cd docs && make html
```

Run HTTP server:
```bash
cd docs/_build/html && python -m http.server 8000
```

Don't forget to change the version in `docs/conf.py` before generating.
```python
release = "<VERSION>"
```

Generated documentation will be in `docs/_build/html`.

### Uploading to GitHub Pages

Documentation for GitHub Pages is placed in following branch
[`gh-pages`](https://github.com/IntelPython/numba-dppy/tree/gh-pages).

Folders:
- `dev` folder contains current documentation for default branch.
- `0.12.0` folder and other similar folders contain documentation for releases.
- `latest` folder is a link to the latest release folder.

Copy generated documentation into corresponding folder and create pull request
to `gh-pages` branch.
