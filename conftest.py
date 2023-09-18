from checks import checkout
import pytest
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    print({data['folderin']})
    print({data['folderout']})
    return checkout(f"mkdir -p {data['folderin']} {data['folderout']} {data['folderext']}", '')

@pytest.fixture()
def make_files():
    return checkout(f"cd {data['folderin']}; touch file1 file2", '')
