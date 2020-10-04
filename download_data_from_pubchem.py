"""Helper script I used to download molecular fingerprints from PubChem.
Takes a lot of time, collected results are saved to pubchem_fingerprints.csv.
"""
import os
import json
import pubchempy as pcp
import pandas as pd
from tqdm import tqdm


def get_compounds_fingerprints(df, cache_dir="temp/train"):
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
        # we'll use this directory to cache downloaded fingerprints

    fingerprints = []
    for i in tqdm(df.index, total=df.shape[0]):
        fingerprint_path = os.path.join(cache_dir, f"fingerprint_{i}.json")
        if os.path.exists(fingerprint_path):
            with open(fingerprint_path) as f:
                data = json.load(f)
            fingerprints.append(data)
            continue
        smiles = df.loc[i, "SMILES"]
        try:
            compounds = pcp.get_compounds(smiles, 'smiles')
            compound = compounds[0]
        except Exception as e:
            print(f"Got error while loading {i} with smiles string {repr(smiles)}, error: {e}")
            continue

        if compound is None:
            print(f"No compound {i} found, skipping molecule {smiles}" )
            continue
        if compound.fingerprint is None:
            print(f"No fingerprint for molecule {i} is found, skipping" )
            with open(fingerprint_path, 'w') as f:
                data = {
                    "SMILES": smiles,
                    "fingerprint": None
                }
                json.dump(data, f)
        else:
            # cactvs_fingerprint contains the same bits as fingerprint property, 
            # the only difference is representation
            with open(fingerprint_path, 'w') as f:
                data = {
                    "SMILES": smiles,
                    "fingerprint": compound.fingerprint
                }
                json.dump(data, f)

    return fingerprints


train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")

train_fingerprints = get_compounds_fingerprints(train, cache_dir="temp/train")
test_fingerprints = get_compounds_fingerprints(test, cache_dir="temp/test")

train_fingerprints = pd.DataFrame(train_fingerprints)
test_fingerprints = pd.DataFrame(test_fingerprints)

df = pd.concat(
    [train_fingerprints, test_fingerprints]).reset_index(drop=True)

df.to_csv("pubchem_fingerprints.csv", index=None)