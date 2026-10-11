#!/usr/bin/env python3
"""Fetch CNN's UNDOCUMENTED Fear & Greed graph data and save latest values.

Do not rely on this as a stable/public/licensed developer API. To protect the
user from false market data, abort on bad responses rather than fabricate scores.
"""
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

ENDPOINT = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata"
DEST = Path(__file__).resolve().parents[1] / "data" / "latest.json"


def get_data():
    req = Request(
        ENDPOINT,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "Referer": "https://www.cnn.com/markets/fear-and-greed",
            "Origin": "https://www.cnn.com",
            "Accept": "application/json, text/plain, */*",
        },
    )
    with urlopen(req, timeout=25) as response:
        data = json.load(response)
    raw = data.get("fear_and_greed")
    if not isinstance(raw, dict):
        raise ValueError("CNN response missing 'fear_and_greed'; check upstream schema")
    score = raw.get("score")
    if not isinstance(score, (int, float)) or isinstance(score, bool) or not (0 <= score <= 100):
        raise ValueError("CNN score missing or outside 0–100")
    out = {
        "score": score,
        "rating": raw.get("rating"),
        "timestamp": raw.get("timestamp"),
        "previous_close": raw.get("previous_close"),
        "previous_1_week": raw.get("previous_1_week"),
        "previous_1_month": raw.get("previous_1_month"),
        "previous_1_year": raw.get("previous_1_year"),
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "source": "CNN Fear & Greed Index (unofficial endpoint)",
    }
    return out


if __name__ == "__main__":
    data = get_data()  # raises rather than overwriting good data with null
    DEST.parent.mkdir(parents=True, exist_ok=True)
    tmp = DEST.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(DEST)
    print(f"Saved score={data['score']:.2f}, CNN timestamp={data['timestamp']}")
