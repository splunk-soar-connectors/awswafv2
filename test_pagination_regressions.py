# Copyright (c) 2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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
