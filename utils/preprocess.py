'''import pandas as pd

def preprocess_input(df: pd.DataFrame) -> pd.DataFrame:

    rename_cols = {
        "ra": "alpha",
        "dec": "delta",
        "objid": "obj_ID",
        "run": "run_ID",
        "rerun": "rerun_ID",
        "field": "field_ID",
        "specobjid": "spec_obj_ID",
        "plateid": "plate",
        "mjd": "MJD",
        "fiberid": "fiber_ID",
        "camcol": "cam_col",}
    df = df.rename(columns=rename_cols)
    drop_cols = [
        'class', 'obj_ID', 'run_ID', 'rerun_ID', 'field_ID',
        'spec_obj_ID', 'plate', 'MJD', 'fiber_ID', 'g', 'i'
    ]
    return df.drop(columns=drop_cols, errors='ignore')

    #color indexes(Custom features)
    photometric_data = ['u', 'g', 'r', 'i', 'z']
    if all(col in df.columns for col in photometric_data):
        df['u-g'] = df['u'] - df['g']   
        df['g-r'] = df['g'] - df['r']
        df['r-i'] = df['r'] - df['i']
        df['i-z'] = df['i'] - df['z']
    columns_to_drop = ['class','obj_ID','run_ID','rerun_ID','field_ID',
                       'spec_obj_ID','plate','MJD','fiber_ID','g','i']

    df = df.drop(columns=columns_to_drop, errors='ignore')

    required_cols = ['alpha', 'delta', 'u', 'r', 'z', 'redshift', 'u-g', 'g-r', 'r-i', 'i-z']
    for col in required_cols:
        if col not in df.columns:
            df[col] = 0.0

    df = df[[required_cols]]
    return df'''




import pandas as pd

def preprocess_input(df: pd.DataFrame) -> pd.DataFrame:
    # Rename columns to match training
    rename_cols = {
        "ra": "alpha",
        "dec": "delta",
        "objid": "obj_ID",
        "run": "run_ID",
        "rerun": "rerun_ID",
        "field": "field_ID",
        "specobjid": "spec_obj_ID",
        "plateid": "plate",
        "mjd": "MJD",
        "fiberid": "fiber_ID",
        "camcol": "cam_col",
    }
    df = df.rename(columns=rename_cols)

    # Drop irrelevant columns
    drop_cols = ['class', 'obj_ID', 'run_ID', 'rerun_ID', 'field_ID',
                 'spec_obj_ID', 'plate', 'MJD', 'fiber_ID', 'g', 'i']
    df = df.drop(columns=[col for col in drop_cols if col in df.columns], errors='ignore')

    # Feature engineering: color indexes
    photometric_data = ['u', 'g', 'r', 'i', 'z']
    if all(col in df.columns for col in photometric_data):
        df["u-g"] = df["u"] - df["g"]
        df["g-r"] = df["g"] - df["r"]
        df["r-i"] = df["r"] - df["i"]
        df["i-z"] = df["i"] - df["z"]

    # Ensure all required features exist
    required_cols = ['alpha', 'delta', 'u', 'r', 'z', 'cam_col','redshift', 'u-g', 'g-r', 'r-i', 'i-z']
    for col in required_cols:
        if col not in df.columns:
            df[col] = 0  # fill missing columns with 0

    # Keep only required columns and correct order
    df = df[required_cols]

    return df