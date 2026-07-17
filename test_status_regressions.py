from pathlib import Path


CONNECTOR_SOURCE = Path("awswafv2_connector.py").read_text()


def test_failed_ip_updates_return_before_success_summary():
    add_failure = CONNECTOR_SOURCE.index('summary["ip_status"] = AWSWAF_ADD_IP_FAILED')
    delete_failure = CONNECTOR_SOURCE.index('summary["ip_status"] = AWSWAF_DELETE_IP_FAILED')
    add_success = CONNECTOR_SOURCE.index('summary["ip_status"] = AWSWAF_ADD_IP_SUCCESS')
    delete_success = CONNECTOR_SOURCE.index('summary["ip_status"] = AWSWAF_DELETE_IP_SUCCESS')

    assert "return action_result.get_status()" in CONNECTOR_SOURCE[add_failure:add_success]
    assert "return action_result.get_status()" in CONNECTOR_SOURCE[delete_failure:delete_success]


def test_ip_actions_stop_after_validation_or_pagination_errors():
    assert CONNECTOR_SOURCE.count("if ip_set is None:") >= 3
    assert CONNECTOR_SOURCE.count("if action_result.get_status() == phantom.APP_ERROR:") >= 2
