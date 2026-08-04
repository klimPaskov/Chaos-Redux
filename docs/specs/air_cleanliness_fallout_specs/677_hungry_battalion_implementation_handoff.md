# Hungry Battalion Implementation Handoff

Implement the reviewed Food Compact chain in `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`.

Reserve candidate `677`, events `677` through `683`, transaction `710068`, scheduler route `7168`, and survivor-memory Event Log history `9174`. Keep both Fallout scheduler activation flags unset and preserve the countable release-floor total at `0 of 660`.

Follow the source design in `specs/70_reviewed_archetype_the_hungry_battalion.md` and the visual contract in `677_hungry_battalion_asset_brief.md`.

Implement one human opening, one hidden-AI opening, one human and one hidden-AI delayed result, one human and one hidden-AI callback, and one authenticated cleanup block. Reuse the established Fallout transaction APIs without copying Work for Rations branch content. Add dedicated constants, triggers, effects, dynamic modifiers, localisation, scripted Event Log detail routing, the candidate producer row, the dedicated report asset, sprite registration, proof document, and source-of-truth updates. Do not add a workbook or catalog row.

Final player-facing localisation must be concrete, Food Compact aware, and government aware where the existing scripted localisation supports it. It must not use em dashes, semicolons, generic apocalypse language, staccato prose, process language, or the working matrix label as an unreviewed final title.

The implementation must report any unproven runtime surface. Hearts of Iron IV must not be launched.

## Implementation status

The reviewed tranche is implemented under the final title The Battalion's Bread List.

The static implementation proof is `docs/plans/air_cleanliness_fallout_plans/FALLOUT_HUNGRY_BATTALION_CHAIN_PROOF.md`.

Candidate `FALLOUT-677` is an internal Fallout identity and has no workbook or catalog row.

The dedicated asset package is `docs/assets/677_hungry_battalion/`.

The scheduler activation flags remain unset and the release-floor total remains `0 of 660`. The exact engine-native all-valid-province thermonuclear sweep belongs to the completed consequence core.
