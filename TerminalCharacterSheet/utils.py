import yaml
from pathlib import Path

def _merge_dict(dict1: dict, dict2: dict) -> dict:
    for key, val in dict1.items():
        if type(val) == dict:
            if key in dict2 and type(dict2[key] == dict):
                _merge_dict(dict1[key], dict2[key])
        else:
            if key in dict2:
                dict1[key] = list(dict1[key]) + list(dict2[key])

    for key, val in dict2.items():
        if not key in dict1:
            dict1[key] = val
    return dict1


def _expand_dict_lists(dict_in: dict) -> dict:
    for key, val in dict_in.items():
        if type(val) == dict:
            dict_in[key] = _expand_dict_lists(dict_in[key])
        elif type(val) == list:
            list_to_expand = dict_in[key]
            dict_in[key] = {}

            for element in list_to_expand:
                dict_in[key][element] = get_tooltip(element)
    return dict_in


def get_tooltip(attribute: str, category: str = "general", default: str = None) -> str:
    with open(Path(__file__).parent/"tooltips.yaml") as lookup_file:
        lookup = yaml.safe_load(lookup_file)
    if category != "general":
        raise Exception("Apologies, category argument not implemented")
    return lookup.get(attribute,default)


def combine_features(_dict_list: list[dict]) -> dict:
    for i in range(1, len(_dict_list)):
        _dict_list[0] = _merge_dict(_dict_list[0], _dict_list[i])
    merged_dict = _dict_list[0]
    full_dict = _expand_dict_lists(merged_dict)
    return _dict_list[0]
