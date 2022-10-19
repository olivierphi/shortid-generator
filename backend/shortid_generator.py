from datetime import datetime, timezone
import hashids

ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ1234567890"  # I and O removed to avoid confusion with 1 and 0

_ORIGIN = int(datetime.fromisoformat("2022-10-01").timestamp())
_Hasher = hashids.Hashids(alphabet=ALPHABET)


def get_shortid() -> str:
    now = int(datetime.now(tz=timezone.utc).timestamp())
    now_short = now - _ORIGIN
    return _Hasher.encode(now_short)
