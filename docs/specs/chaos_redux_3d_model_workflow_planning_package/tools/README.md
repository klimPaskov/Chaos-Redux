# Planning Utilities

## `estimate_meshy_credits.py`

Uses the 2026-07-22 API pricing snapshot to estimate a job. It does not call Meshy and is not authoritative billing data. The reviewed pricing table did not publish a UV unwrap price, so UV unwrap estimates require `--uv-unwrap-unit-cost` from a live source.

Examples:

```bash
python estimate_meshy_credits.py --model smart_topology --textured --rig --animations 3
python estimate_meshy_credits.py --model meshy7 --textured --generation-attempts 2 --remesh 1 --animations 3 --retry-reserve-percent 20 --json
```

## `hash_artifacts.py`

Creates a sorted SHA256 inventory for an artifact directory.

```bash
python hash_artifacts.py docs/assets/014_cannibalism/models_3d/cannibal_raider --output artifact_hashes.json
```
