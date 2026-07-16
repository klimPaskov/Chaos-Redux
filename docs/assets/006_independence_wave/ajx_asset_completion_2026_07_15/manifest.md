# Event 006 IW-010 Saar focus asset manifest

Date: `2026-07-15`
Event: `006_independence_wave`
Package: `IW-010` Saar (`AJX`)
Source mode: official built-in ImageGen

This package contains only the distinct Municipal Neutral Commission focus
icon. The previously authored custom advisor dossier icons were withdrawn and
deleted at the user's direction. Saar's gameplay advisor offices do not carry
custom Event 006 portrait sprites.

## Asset

| Stable stem | Target | Sprite | Runtime DDS |
| --- | ---: | --- | --- |
| `goal_independence_wave_ajx_neutral_commission` | `94x86` | `GFX_goal_independence_wave_ajx_neutral_commission` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_ajx_neutral_commission.dds` |

The matching shine handle is
`GFX_goal_independence_wave_ajx_neutral_commission_shine`. The base and shine
sprites are registered in `interface/006_independence_wave.gfx` and the base
sprite is consumed by `independence_wave_ajx_appoint_neutral_commission_focus`.

## Evidence

- exact prompt: `prompts/ajx_asset_prompts.md`;
- raw ImageGen master:
  `source_png/imagegen_raw/goal_independence_wave_ajx_neutral_commission_imagegen_raw.png`;
- alpha-processed master:
  `source_png/alpha_processed/goal_independence_wave_ajx_neutral_commission_alpha_master.png`;
- processed PNG:
  `processed_png/focus/goal_independence_wave_ajx_neutral_commission.png`;
- processing metadata:
  `metadata/focus/goal_independence_wave_ajx_neutral_commission.json`;
- package DDS mirror:
  `final_dds/focus/goal_independence_wave_ajx_neutral_commission.dds`;
- decoded DDS:
  `decoded_png/focus/goal_independence_wave_ajx_neutral_commission.png`;
- visual comparison:
  `contact_sheets/focus/goal_independence_wave_ajx_neutral_commission_comparison.png`;
- complete retained-file inventory: `checksums.sha256`.

The runtime DDS is one-level `94x86` BGRA with alpha and is byte-identical to
the package mirror. Its SHA-256 is
`06063478a0d1a4e0cd562e1230f31cfa46eeb718814f11bcb83e86b6c059b613`.

## Simplifications, omissions, fallbacks, and blockers

- Custom advisor icons are intentionally absent by explicit user direction.
- The focus icon has no fallback, placeholder, or missing evidence.
- No remaining asset blocker exists within this focus-only package.
