from tests.base import get_asset_path

from xstampp_model_parser import parse_hazx_file


def test_parsing_hazx():
    parsed = parse_hazx_file(get_asset_path("ACC_STPA.hazx"))
    print(parsed)