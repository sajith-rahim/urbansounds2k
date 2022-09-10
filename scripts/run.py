def extract_csv():
    import pandas as pd

    df = pd.read_csv("UrbanSound8K.csv", header="infer")
    df.head(5)

    grouped = df[df["fold"].isin([1, 2, 3, 4, 5, 6])].groupby('classID')

    new_df = pd.DataFrame([], columns=df.columns)
    _count = 200
    for key, values in grouped:
        new_df = pd.concat([new_df, grouped.get_group(key)[:_count]], 0)

    new_df.head()
    print(new_df['classID'].value_counts())
    new_df.to_csv("urbansounds2k.csv")


def move_files(by='class'):
    import pandas as pd
    import os
    import shutil

    df = pd.read_csv("urbansounds2k.csv", header="infer")
    # df.head(5)
    _by = by if by is not None else 'class'  # 'fold'
    curr_dir = os.getcwd()

    for index, row in df.iterrows():

        _directory = 'urbansounds2k'
        if not os.path.exists(os.path.join(curr_dir, _directory, str(row[_by]))):
            os.makedirs(os.path.join(curr_dir, _directory, str(row[_by])))

        _src = os.path.join(curr_dir, 'fold' + str(row['fold']), row['slice_file_name'])
        # _dest = os.path.join(curr_dir, _directory, str(row['fold']), row['slice_file_name'])
        _dest = os.path.join(curr_dir, _directory, str(row[_by]), row['slice_file_name'])

        # check if file exist in destination
        if not os.path.exists(_dest):
            try:
                print(f"Copying: {_src}")
                shutil.copy(_src, _dest)
            except Exception:
                print(f"Failed to copy: {_src}")


if __name__ == "__main__":

    print("invoking..", end="\n")
    extract_csv()
    move_files()
