# Event 006 achievement surface audit — 2026-08-15

## Disposition

The accepted Event 006 achievement matrix is source-covered and remains outside the current completion blockers. All sixteen matrix IDs have one live achievement definition, one completion trigger, one English name, one English description, one player-facing proof tooltip, and one normal icon asset; the corresponding grey and not-eligible icon variants are also present.

The working-tree achievement guard repair is accepted as a narrow source-backed correction. Former-host war, subject, annexation, and remnant-disqualification paths now require `has_independence_wave_living_former_host = yes` before dereferencing `independence_wave_former_host`, and the reconquest achievement requires a living former host. This prevents dead or missing former-host pointers from creating false Event 006 achievement proofs without changing the matrix thresholds.

## Matrix crosswalk

The sixteen rows in `docs/specs/006_independence_wave_specs/matrices/006_achievement_matrix.csv` map one-to-one to the definitions in `common/achievements/chaos_redux_achievements.txt` and the completion triggers in `common/scripted_triggers/006_independence_wave_achievement_triggers.txt`.

The source thresholds match the accepted matrix: ten-year one-state survival, five-year peaceful host settlement, five founding members and five charter pillars, ten members across four regions with 70 cohesion for two years, one-year rescue protection, 85 percent low-intensity scenario survival for five years, three major patrons, five arbitration resolutions, one-state former-host remnant with ten years of peace, 60 percent stability, two civilian factories, and level-two capital infrastructure.

The hidden/visible split matches the matrix. Volga Bulgaria, Assyria, Radical Bloc, and Every Flag Survival are hidden; the other twelve are visible.

## Runtime proof wiring

The proof state is refreshed by Event 006 transactions and narrow engine on-actions in `common/scripted_effects/006_independence_wave_achievement_effects.txt` and `common/on_actions/006_independence_wave_achievement_on_actions.txt`. No daily, weekly, monthly, or world-iteration scan was added.

The achievement effect ledger covers country reset, recognition/capacity state, patron history, peaceful settlement, reconquest capital-loss windows, league founding, cross-regional clocks, rescue protection, radical containment, SCN-008 survival, arbitration, and host-remnant peace. Existing calls from Event 006 effects, decisions, super-event effects, scenario effects, and on-actions were preserved.

The current narrow repair is limited to the living-former-host guard and does not alter central adapters, content attestation, normal/scenario preflight, Join order, package counts, or formable admission.

## Validation boundary

Static source review found no missing or duplicate achievement IDs, trigger IDs, localisation keys, or icon triplets. The achievement subsystem has no exposed HOI4 MCP inspect/render route in the installed server, so no engine-render or live-award claim is made here.

Event 006 remains HOLD/PARTIAL for the broader project boundary: current authority is 40 adapters, 32 content attestations, 29 compatible groups, and 161 unattested selectable rows, with package-local and asset/probability gates still unresolved elsewhere. This audit does not promote any package or claim full Event 006 completion.
