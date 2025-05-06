import json
import os

import pytest

from src.save import JSONFileHandler


def test1(json_file_handler):
    q = json_file_handler
    q.write_to_file([{"стул": 9, "стол": 11}, {'винни пук': 22}])
    program_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    absolute_json_file_path = os.path.join(program_dir, "vac.json")
    with open(absolute_json_file_path, "r", encoding="utf-8") as f:
        e = json.load(f)
    assert len(e) == 2

def test2(json_file_handler):
    q = json_file_handler
    assert q.all_data == [{"стул": 9, "стол": 11}, {'винни пук': 22}]


def test3():
    q = JSONFileHandler("uohoh")
    assert q.all_data == []

def test4():
    program_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    absolute_json_file_path = os.path.join(program_dir, "vac.json")
    q = JSONFileHandler(absolute_json_file_path)
    with pytest.raises(Exception):
        q.write_to_file([{(1, [], []): 0}])
