# IW-047 Mari El shared focus hooks handoff — 2026-08-14

## Scope and ownership

This bounded patch wires the five IW-047 Mari El (MEL) package helpers into the existing `independence_wave_focus_tree` framework. It owns only the shared focus call sites and this handoff. It does not create a bespoke MEL focus tree, new package root, central attestation or admission path, Join/dispatcher change, localisation, icon, AI, decision, or event content.

## Changed file and identifiers

Changed file:

- `common/national_focus/006_independence_wave_focus.txt`

Every call uses the exact guard `original_tag = MEL` together with `is_independence_wave_mari_package = yes`:

| Shared focus anchor | MEL helper effect | Source line |
| --- | --- | ---: |
| `independence_wave_prepare_capital_administration` | `independence_wave_mel_focus_convene_forest_congress` | 119 |
| `independence_wave_inventory_the_state` | `independence_wave_mel_focus_secure_mari_communities` | 165 |
| `independence_wave_bind_the_first_oath` | `independence_wave_mel_focus_integrate_woodland_guards` | 192 |
| `independence_wave_define_former_host_policy` | `independence_wave_mel_focus_settle_former_host_ledgers` | 1424 |
| `independence_wave_recognize_fellow_new_states` | `independence_wave_mel_focus_open_volga_finnic_corridor` | 1695 |

The helper definitions are present in the country-core-owned `common/scripted_effects/006_independence_wave_mari_package_effects.txt`; the package guard is defined in `common/scripted_triggers/006_independence_wave_mari_package_triggers.txt`.

## Route behavior before and after

| Full-framework focus | Before | After |
| --- | --- | --- |
| `independence_wave_prepare_capital_administration` | No MEL package call. | An active MEL package invokes `independence_wave_mel_focus_convene_forest_congress`. |
| `independence_wave_inventory_the_state` | No MEL package call. | An active MEL package invokes `independence_wave_mel_focus_secure_mari_communities`. |
| `independence_wave_bind_the_first_oath` | No MEL package call. | An active MEL package invokes `independence_wave_mel_focus_integrate_woodland_guards`. |
| `independence_wave_define_former_host_policy` | No MEL package call. | An active MEL package invokes `independence_wave_mel_focus_settle_former_host_ledgers`. |
| `independence_wave_recognize_fellow_new_states` | No MEL package call. | An active MEL package invokes `independence_wave_mel_focus_open_volga_finnic_corridor`. |

The shared focus prerequisites, availability gates, layout geometry, mutual exclusions, AI weights, localisation keys, icon references, and generic rewards are unchanged.

## Required source review

The offline National focus modding, Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding wiki snapshots were consulted. The vanilla `effects_documentation.md`, `triggers_documentation.md`, and `script_concept_documentation.md` were consulted with vanilla national-focus examples. The hook syntax follows the existing IW-038/IW-040/IW-044/IW-045 guarded `if` calls inside `completion_reward.hidden_effect` blocks.

## MCP evidence

The required post-change `hoi4.focus_inspect` completed successfully for `independence_wave_focus_tree` in workspace `mod_chaos_redux_ea3b2d67c2c0`:

- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c727dc1549b9f881bc9fe6c4716a2117599642634b30f943b954cc8b12c3b1ab/c88094db95caeed927947bb389d232a08b6fea88aac50e4b7ff0bb8275a8f3c3/focus-inspect.4e98d2e2917c614b.json`
- Graph: 184 focuses, 196 connectors, zero connector crossings, zero focus-node intersections, layout hash `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`.
- The tree retained six source diagnostics (including pre-existing layout warnings); the MCP validation summary reports 14 blocking diagnostics from generic continuous-focus icon references and existing layout/reference findings, outside this five-call patch. No MEL helper reference remained unresolved in the inspect result.

The required post-change `hoi4.focus_render` completed successfully:

- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6c95b6d7fe0b98c27b9c2f47455dbf4ccc4a13568ac2c53c537dc1c0dd7098c1/0942ca3436a43afdb93f2b032fe843d8bdc9694bbd8d7e627bff0e79092103dc/independence_wave_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/02a33b6e26cd319131d46e708aa7260478638f337d0a28a6efe1f823d448af30/f3eaa1dc26e4e571e5928630cf3863a63660294ee676f0a69c0221307ab4d973/independence_wave_focus_tree.focus.svg`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5bb3cd0b4a39dddc24a09383d180449702f4b75ff825bb6d769e01aa28049c87/0beda4afd1342172ab4313e77847e07636f09f14c4777aee4919932f1e8ea85f/independence_wave_focus_tree.focus.json`

The unchanged layout hash and connector/node metrics confirm that no geometry rewrite was needed. `hoi4.focus_rewrite` was not used.

## Validation limits and follow-up

Static checks found each MEL helper exactly once in the shared focus source and exactly five occurrences of the combined MEL guard. `git diff --check` reported no whitespace error for the focus file. No AI/probability surface changed, so no probability audit was needed for this narrow hook patch.

The MCP report retains generic continuous-focus icon errors and pre-existing layout warnings. No live HOI4 launch, save/load, or in-game focus completion was performed; those checks belong to the user/runtime validation boundary. No localisation keys or icon IDs changed, so no localisation or asset validation was required.

No simplification or fallback was used. Central admission/Join remains outside this handoff and must stay fail-closed unless separately attested by the parent.
