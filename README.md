# fastapi-canonical-json

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://pypi.org/project/fastapi-canonical-json/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

Deterministic RFC 8785 Canonical JSON serializer and response class for FastAPI, webhooks, and cryptographic signatures.

---

## 🚀 Features

- 📜 **RFC 8785 Compliant**: Deterministic key sorting, minimal spacing, UTF-8 normalization.
- 🔐 **Signature Verification**: Perfect for webhook HMAC-SHA256 signatures and blockchain payloads.
- ⚡ **Drop-in FastAPI Response**: Seamless `CanonicalJSONResponse` response class.

---

## 📦 Installation

```bash
pip install fastapi-canonical-json
```

---

## 🛠️ Quickstart

```python
from fastapi import FastAPI
from fastapi_canonical_json import CanonicalJSONResponse, canonical_json_dumps

app = FastAPI()

@app.get("/signed-data", response_class=CanonicalJSONResponse)
def get_signed():
    # Keys will be deterministically sorted with RFC 8785 spacing
    return {"b": 2, "a": 1, "z": [3, 2, 1]}
```

---

## ☕ Support My Studies / Buy Me a Coffee

I am an independent developer and student building open-source developer productivity tools. If this library helped your signature verification and deterministic hashing, please consider supporting my studies:

- ☕ **Buy Me a Coffee:** [ko-fi.com/me1121118](https://ko-fi.com/)
- ⭐ **Star this repository** on GitHub!

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
