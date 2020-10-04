My baseline solution for AICROWD's Learning to smell competition.

## TL;DR

I use precomputed fingerprints from PubChem database, which are collected at `pubchem_fingerprints.csv` file. The script `download_data_from_pubchem.py` can be used for downloading them (might be slow, because it downloads data from remote server).

# HOWTO run and reproduce

1. Download files from competition and save them to `data` directory.
2. File `pubchem_fingerprints.csv` is already precomputed - it is output from `python download_data_from_pubchem.py` run.
3. You can run `baseline_solution.ipynb` with jupyter notebook.
