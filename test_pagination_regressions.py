from pathlib import Path


CONNECTOR_SOURCE = Path("awswafv2_connector.py").read_text()
CONSTANTS_SOURCE = Path("awswafv2_consts.py").read_text()


def test_waf_pagination_has_hard_page_and_item_limits():
    assert "AWSWAF_MAX_PAGINATION_PAGES = 1000" in CONSTANTS_SOURCE
    assert "AWSWAF_MAX_PAGINATION_ITEMS = 100000" in CONSTANTS_SOURCE
    assert "page_count >= AWSWAF_MAX_PAGINATION_PAGES" in CONNECTOR_SOURCE
    assert "len(set_list) >= AWSWAF_MAX_PAGINATION_ITEMS" in CONNECTOR_SOURCE


def test_waf_pagination_rejects_repeated_markers():
    assert "next_marker in seen_markers" in CONNECTOR_SOURCE
    assert "returned a repeated pagination marker" in CONNECTOR_SOURCE
