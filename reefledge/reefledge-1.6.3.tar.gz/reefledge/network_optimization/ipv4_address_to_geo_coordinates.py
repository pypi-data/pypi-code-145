from typing_extensions import TypeAlias
from typing import Tuple, Optional as Opt, Dict, cast, List
import warnings

import requests
from requests.exceptions import SSLError

Pair: TypeAlias = Tuple[float, float]


def ipv4_address_to_geo_coordinates(ipv4_address: Opt[str] = None) -> Pair:
    data = _get_data_in_json_format(ipv4_address)
    geo_coordinates = _extract_geo_coordinates(data)

    return geo_coordinates


def _get_data_in_json_format(ipv4_address: Opt[str]) -> Dict[str, str]:
    url: str = __assemble_url(ipv4_address)

    try:
        response = requests.get(url)
    except SSLError:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            response = requests.get(url, verify=False)

    return cast(Dict[str, str], response.json())

def __assemble_url(ipv4_address: Opt[str]) -> str:
    url: str = 'https://ipinfo.io/'

    if ipv4_address is not None:
        url += f"{ipv4_address}/"

    url += 'json'
    return url


def _extract_geo_coordinates(data: Dict[str, str]) -> Pair:
    _geo_coordinates: List[str] = data['loc'].split(',')
    assert len(_geo_coordinates) == 2

    geo_coordinates = cast(
        Pair,
        tuple([float(c) for c in _geo_coordinates])
    )

    return geo_coordinates
