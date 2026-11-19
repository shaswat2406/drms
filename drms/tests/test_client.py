import pytest

import drms
from drms.config import ServerConfig


def test_client_init_defaults():
    c = drms.Client()
    assert isinstance(c._server, ServerConfig)
    assert c._server.name.lower() == "jsoc"
    assert c.email is None


@pytest.mark.parametrize("server_name", ["jsoc", "kis"])
def test_client_registered_servers(server_name):
    c = drms.Client(server_name)
    assert isinstance(c._server, ServerConfig)
    assert c._server.name.lower() == server_name
    assert c.email is None


def test_client_custom_config():
    cfg = ServerConfig(name="TEST")
    c = drms.Client(cfg)
    assert isinstance(c._server, ServerConfig)
    assert c._server.name == "TEST"


def test_repr():
    assert repr(drms.Client()) == "<Client: JSOC>"
    assert repr(drms.Client("kis")) == "<Client: KIS>"


def test_export_request_status_no_requestid():
    mock_client = MagicMock()
    req = drms.ExportRequest({"status": 2}, client=mock_client)
    assert req._status == 2
    assert req.status == 2
    mock_client._json.exp_status.assert_not_called()
