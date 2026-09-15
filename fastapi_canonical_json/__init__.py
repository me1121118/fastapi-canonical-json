import json
import hashlib
from typing import Any
from starlette.responses import JSONResponse

def canonical_json_dumps(obj: Any) -> str:
    """Serialize Python object to deterministic RFC 8785 canonical JSON string."""
    return json.dumps(
        obj,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )

def canonical_json_hash(obj: Any, algorithm: str = "sha256") -> str:
    """Compute cryptographic hash of canonical JSON representation."""
    canonical_bytes = canonical_json_dumps(obj).encode("utf-8")
    h = hashlib.new(algorithm)
    h.update(canonical_bytes)
    return h.hexdigest()

class CanonicalJSONResponse(JSONResponse):
    """Starlette/FastAPI JSON response that outputs RFC 8785 canonical sorted JSON."""

    def render(self, content: Any) -> bytes:
        return canonical_json_dumps(content).encode("utf-8")
