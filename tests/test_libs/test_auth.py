import os
import mock
import boto3
from obs.libs import auth
from obs.libs import config
from cloudianapi.client import CloudianAPIClient
from requests_aws4auth import AWS4Auth
from obs.libs import auth as auth_lib


def fake_config():
    pass


def fake_session(**kwargs):
    session = mock.Mock()
    session.resource.return_value = "s3_resource"
    return session


def test_resource(monkeypatch):
    monkeypatch.setattr(config, "load_config_file", fake_config)
    monkeypatch.setattr(boto3, "Session", fake_session)
    monkeypatch.setattr(auth_lib, "get_endpoint", lambda: None)
    assert auth.resource() == "s3_resource"
