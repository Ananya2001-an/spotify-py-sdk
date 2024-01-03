import pytest
from spotify_py_sdk.endpoints.endpoints_base import EndpointsBase


def test_params_for_omits_none():
    result = EndpointsBase.params_for({"ids": None})

    assert result == ""


def test_params_for_correctly_encodes_string():
    result = EndpointsBase.params_for({"ids": "abc"})

    assert result == "?ids=abc"


def test_params_for_correctly_encodes_list():
    result = EndpointsBase.params_for({"ids": ["abc", "abc"]})

    assert result == "?ids=abc%2Cabc"


def test_params_for_correctly_encodes_bool():
    result = EndpointsBase.params_for({"ids": False})

    assert result == "?ids=false"


def test_params_for_correctly_encodes_0():
    result = EndpointsBase.params_for({"ids": 0})

    assert result == "?ids=0"


def test_params_for_correctly_encodes_non_zero_value():
    result = EndpointsBase.params_for({"ids": 20})

    assert result == "?ids=20"


