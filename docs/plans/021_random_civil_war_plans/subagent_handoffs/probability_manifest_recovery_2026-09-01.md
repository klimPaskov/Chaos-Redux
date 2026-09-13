# Event 021 Probability Manifest Recovery

Date: 2026-09-01

## Purpose

The earlier independent target-weight retries could not reproduce the parent result because the exact custom-pool manifest body was never preserved. This parent-side recovery verifies the installed MCP custom-pool expression boundary and records one complete formula-backed probe that later auditors can reproduce.

This is supporting evidence. It is not the required independent full-matrix certificate.

## Installed schema findings

The installed schema is defined in:

- `C:/Users/klimp/AppData/Roaming/npm/node_modules/hoi4-agent-tools/dist/hoi4_agent_tools/schemas/probability.js`
- `C:/Users/klimp/AppData/Roaming/npm/node_modules/hoi4-agent-tools/docs/probability.md`

Custom-pool candidate weights accept numbers or arithmetic expressions using declared `state.*` paths. The arithmetic evaluator supports addition, subtraction, multiplication, division, and parentheses. It does not support `min()` or `max()`. A candidate cap implements the upper clamp. Every referenced state key must be declared in `manifest.state` so initial pool values resolve.

## Exact accepted manifest

```json
{
  "schemaVersion": "1.0",
  "id": "event021_tgt_formula_probe_v3",
  "selection": {
    "mode": "categorical_weighted",
    "cadence": "timer",
    "timerMinDays": 1,
    "timerMaxDays": 1,
    "rounding": "nearest"
  },
  "state": {
    "stable_pressure": 0,
    "stable_authority": 0,
    "stable_route": 0,
    "stable_evidence": 0,
    "stable_fragmentation": 0,
    "stable_occupied": 0,
    "stable_manpower": 0,
    "stable_event006": 0,
    "stable_major": 0,
    "stable_exposure": 0,
    "stable_recent": 0,
    "stable_subject": 0,
    "stable_eligible": false,
    "weak_pressure": 0,
    "weak_authority": 0,
    "weak_route": 0,
    "weak_evidence": 0,
    "weak_fragmentation": 0,
    "weak_occupied": 0,
    "weak_manpower": 0,
    "weak_event006": 0,
    "weak_major": 0,
    "weak_exposure": 0,
    "weak_recent": 0,
    "weak_subject": 0,
    "weak_eligible": false
  },
  "candidates": [
    {
      "id": "stable_minor",
      "category": "country",
      "weight": "10 + state.stable_pressure * 4 + state.stable_authority + state.stable_route + state.stable_evidence * 12 + state.stable_fragmentation + state.stable_occupied + state.stable_manpower + state.stable_event006 + state.stable_major + state.stable_exposure + state.stable_recent + state.stable_subject",
      "cap": 1000,
      "eligibleWhen": "state.stable_eligible == true"
    },
    {
      "id": "weak_minor",
      "category": "country",
      "weight": "10 + state.weak_pressure * 4 + state.weak_authority + state.weak_route + state.weak_evidence * 12 + state.weak_fragmentation + state.weak_occupied + state.weak_manpower + state.weak_event006 + state.weak_major + state.weak_exposure + state.weak_recent + state.weak_subject",
      "cap": 1000,
      "eligibleWhen": "state.weak_eligible == true"
    }
  ],
  "transitions": []
}
```

## Exact accepted scenario

```json
{
  "schemaVersion": "1.0",
  "id": "event021_tgt_probe_scenarios_v3",
  "scenarios": [
    {
      "id": "TGT-01",
      "label": "Stable minor versus unstable minor with valid opposition",
      "state": {
        "stable_pressure": 8,
        "stable_authority": 0,
        "stable_route": 80,
        "stable_evidence": 0,
        "stable_fragmentation": 0,
        "stable_occupied": 0,
        "stable_manpower": 0,
        "stable_event006": 0,
        "stable_major": 0,
        "stable_exposure": 0,
        "stable_recent": 0,
        "stable_subject": 0,
        "stable_eligible": true,
        "weak_pressure": 60,
        "weak_authority": 90,
        "weak_route": 80,
        "weak_evidence": 3,
        "weak_fragmentation": 45,
        "weak_occupied": 70,
        "weak_manpower": 35,
        "weak_event006": 0,
        "weak_major": 0,
        "weak_exposure": 0,
        "weak_recent": 0,
        "weak_subject": 0,
        "weak_eligible": true
      }
    }
  ]
}
```

## MCP result

`hoi4.probability_evaluate` completed with:

- status `ok`
- code `PROBABILITY_ANALYZED`
- analysis `probability-07001ea34f50e09e19322ee7`
- source revision `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`
- source hash `385aecdd805a45e5fd47e1ae45c394d598efea8220661739fba104cbdb232bcb`
- scenario hash `642f4c730dff64583cd284e89d25d60c80360120d124c18f941a16c3e6ffe419`
- zero unresolved items

The authoritative artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bb036b6ba615aa3aa97b5fdb36765d1e1ec311b167c70f2ed7825575b15c2c64/e72f0d694aaba8822fa44ec14b581cfa09f6c009d5568f2cd86fa16a3fe53f7e/probability-07001ea34f50e09e19322ee7.json`.

The probe demonstrates a reproducible formula-backed manifest route. It does not certify TGT-01 through TGT-10 or any other Event 021 family by itself.
