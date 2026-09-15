import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi_canonical_json import CanonicalJSONResponse, canonical_json_dumps, canonical_json_hash

def test_canonical_json_dumps():
    data1 = {"b": 2, "a": 1}
    data2 = {"a": 1, "b": 2}
    assert canonical_json_dumps(data1) == '{"a":1,"b":2}'
    assert canonical_json_dumps(data1) == canonical_json_dumps(data2)
    assert canonical_json_hash(data1) == canonical_json_hash(data2)

def test_canonical_response():
    app = FastAPI()

    @app.get("/data", response_class=CanonicalJSONResponse)
    def get_data():
        return {"z": 10, "m": 5, "a": 1}

    client = TestClient(app)
    res = client.get("/data")
    assert res.status_code == 200
    assert res.content == b'{"a":1,"m":5,"z":10}'
