My baseline solution for [AICROWD's Learning to smell competition](https://www.aicrowd.com/challenges/learning-to-smell).

## TL;DR

I use precomputed fingerprints from PubChem database, which are collected at `pubchem_fingerprints.csv` file. The script `download_data_from_pubchem.py` can be used for downloading them (might be slow, because it downloads data from remote server).

# HOWTO run and reproduce

1. Download files from competition and save them to `data` directory.
2. File `pubchem_fingerprints.csv` is already precomputed - it is output from `python download_data_from_pubchem.py` run.
3. You can run `baseline_solution.ipynb` with jupyter notebook.

You can also read [my Medium post](https://medium.com/@latticetower/aicrowd-learning-to-smell-challenge-right-fingerprint-is-all-you-need-4d45e2afb869?source=friends_link&sk=74aa8b448f2d5d19e31ee32901151e37) about this solution both with some ideas what to do next.
