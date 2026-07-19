# Event 016 Kruger State focus parent-review handoff

Date: 2026-07-19

Owner: root implementation review

Status: gameplay structure and layout reviewed; asset production and mapped audits remain open.

## Reviewed files

- `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt`
- `common/scripted_triggers/016_brilliant_scientist_focus_triggers.txt`
- `common/scripted_effects/016_brilliant_scientist_focus_effects.txt`
- `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt`
- `interface/016_brilliant_scientist_kruger_state_focus.gfx`
- `localisation/english/016_brilliant_scientist_focus_l_english.yml`

## Parent corrections

- Replaced the unsupported `add_army_experience` effect with the documented `army_experience` effect.
- Preserved every original OR/AND focus gate while moving large cross-lane requirements into explicit `available` checks. The offline National Focus Modding reference confirms that entries in one prerequisite block are OR and separate prerequisite blocks are AND.
- Re-authored the 100-focus coordinates into founding, economy, conventional security, political identity, foreign policy, six project-force, temporal, exotic, integration, and terminal modules.
- Removed the seven-route all-to-all mutual-exclusion mesh only after verifying that every route requires `brilliant_scientist_kruger_focus_identity_is_open` and every route-forming effect atomically sets `brilliant_scientist_sovereign_identity_locked`. A custom player-facing trigger tooltip now explains the permanent route lock.
- Kept Paleogenetics, Xenobiological Synthesis, portal, temporal, alien-arms, and biological military packages causally separate. No focus grants project history, spawns free project units, or bypasses paid force decisions.

## Render evidence

The HOI4 focus inspector and rasterizer both completed after storage recovery.

- Focus count: 100.
- Resolved titles: 100.
- Connector crossings: 0.
- Connector-through-node intersections: 0.
- Long connectors: 0.
- Same-row spacing violations: 0.
- Remaining Event 016 focus diagnostics: 100 missing registered icon textures.
- Latest reviewed raster SHA-256: `f4fec021baea316797b744f539b9a2049a5905b32d9a55ade858cd520d180a02`.

The raster uses placeholder cards until each registered DDS exists. It is layout acceptance evidence, not asset acceptance evidence.

## Open work

- Finish and visually review all 100 independently generated focus icons, their processed PNGs, runtime DDS files, prompt records, contact sheets, and manifest statuses.
- Re-run focus inspection with final icons decoded.
- Audit all 15 route AI plans against the final decision/event consumers and disabled-evolution behavior.
- Run the mapped focus-tree auditor after the improvement-loop addendum is resolved.

No fallback, substitute icon, or completion claim is authorized by this handoff.
