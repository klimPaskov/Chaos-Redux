# Event 014 Evolution III MTTH Contract Cleanup

Date: 2026-08-24

Owner: `event014_evolution3_mtth_contract_cleanup`

Mode: bounded source and contract cleanup. No readiness threshold, gameplay balance, AI weight, event, decision, focus, or localisation source was changed.

## Outcome

The unused `cannibalism_evolution_iii_days` declaration was removed from the Event 014 MTTH source.

Evolution I and Evolution II retain their MTTH timing entries and the existing 21 to 240 day runtime clamp contract.

Evolution III remains governed by `cannibalism_try_schedule_evolution_iii`, which uses convergence entry gates, a warning due date, hard readiness minimums, and convergence recovery rather than an MTTH timing entry.

## Exact files and identifiers

Changed files:

- `common/mtth/014_cannibalism_mtth.txt`: removed the unused `cannibalism_evolution_iii_days` block. The retained MTTH identifiers are `cannibalism_evolution_i_days`, `cannibalism_evolution_ii_days`, `cannibalism_unified_target_decision_weight`, and `cannibalism_wendigo_target_decision_weight`.
- `docs/plans/014_cannibalism_plans/probability_contracts/event014_mtth_mission_contracts.json`: removed the `evolution_iii_declared` MTTH row, updated the Event 014 MTTH source hash and ranges, and recorded the post-cleanup MCP artifact.
- `docs/plans/014_cannibalism_plans/probability_contracts/event014_contract_index.json`: removed the deleted symbol from the source snapshot, changed coverage to Evolution I/II timing contracts plus the Evolution III convergence scheduler, and recorded the post-cleanup MCP artifact.
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_probability_contracts_v1.md`: aligned the contract summary with the current source and distinguished the deterministic Evolution III scheduler from MTTH timing.
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_probability_final_audit_v4.md`: aligned the MTTH section with the retained entries and documented the convergence scheduler as the Evolution III timing surface.
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_evolution3_mtth_contract_cleanup_2026-08-24.md`: this handoff.

Unchanged files:

- `common/scripted_effects/014_cannibalism_effects.txt` remains the runtime owner of convergence scheduling and was not edited. Its concurrent working-tree changes were preserved.
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_probability_audit_2026-08-24.md` remains the dated baseline audit. Its lines 138, 193, and 204 preserve the pre-cleanup contradiction and are historical evidence, not the current contract.

## Before and after contract

| Surface | Before | After |
| --- | --- | --- |
| MTTH declaration | `cannibalism_evolution_iii_days` was declared in `common/mtth/014_cannibalism_mtth.txt` but had no runtime call site. | The unused declaration is absent. |
| Evolution III scheduler | `cannibalism_try_schedule_evolution_iii` already used convergence gates, warning timing, and hard timing constants. | The same convergence scheduler remains authoritative and unchanged. |
| Evolution I and II | MTTH entries were runtime-scheduled with persisted due dates and a 21 to 240 day clamp. | The same entries and contract remain intact. |
| Probability contract | The machine-readable manifest listed a declared Evolution III MTTH row despite its lack of runtime use. | The manifest contains only the runtime Evolution I/II MTTH rows and represents Evolution III as convergence scheduling. |

The accepted reveal specification requires weighted readiness with hard minimums and a warning or counterplay phase. This cleanup removes a contradictory unused timing declaration and does not replace or simplify that design.

## MCP evidence

The pre-cleanup `hoi4.probability_inspect` call used the `event_mean_time_to_happen` adapter against `common/mtth/014_cannibalism_mtth.txt` and returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`. Its baseline artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/83c2d1fe4b97e839f51ef0b89ae33ac62d0af8bf82578a1294088fe71760074b/299b3100181a3374709c9e741bc8221f8efca43074489214dee15970eb8d91e7/probability-inspect-a1950692f970.json`.

The post-cleanup `hoi4.probability_inspect` call used the same adapter and source and returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`, zero candidates, zero required inputs, and zero unresolved inputs. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/03ea4b660ec049a35013107cd3b6775f67d41bf66036808815a2ccab376c20d5/a9bcd81b6be5411cb7eb55713bc42bdb9a15809732fa062e50d0346a0d73df6b/probability-inspect-d7a550b09a98.json`.

The Event 014 decision surface remains classified through `decision_ai_will_do` in the existing probability contract. No decision source changed in this tranche.

No callable `chaosx_ai_probability_auditor` route is exposed in this runtime. The required auditor evidence pass and a same-scenario `hoi4.probability_compare` are therefore unavailable. This patch does not alter a runtime weight or timing score, so no balance comparison is claimed.

## References read

- `AGENTS.md`.
- `.agents/skills/chaos-redux-mtth/SKILL.md`.
- `.agents/skills/chaos-redux-events/SKILL.md`.
- `.agents/skills/chaos-redux-subagents/SKILL.md`.
- `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_7_hannibal_reveal_and_unification.md`.
- `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_3_evolutions_and_spread.md`.
- `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_9_ai_balance_and_integrations.md`.
- `docs/specs/014_cannibalism_specs/matrices/event_map_and_state_machine.md`.
- Offline Paradox wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
- Vanilla documentation `script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, and `modifiers_documentation.md` under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`.
- The requested nested vanilla path `documentation/common/script_constants/documentation.md` is absent in the installed documentation snapshot. Script constant guidance was read from `script_concept_documentation.md`.

## Validation

- The two edited JSON contracts parse successfully with PowerShell `ConvertFrom-Json` and Python's standard JSON parser.
- The retained MTTH identifiers resolve at lines 10, 77, 96, and 127. No runtime source under `common` or `events` references `cannibalism_evolution_iii_days` after the cleanup.
- The post-cleanup probability inspection completed read-only against the current MTTH source and produced the artifact recorded above.
- Hearts of Iron IV was not launched.

## Remaining probability work and limitations

- No exact MTTH timing distribution or campaign probability is certified because the installed adapter reports no directly discovered weighted surface for this source.
- Convergence readiness, host selection, warning counterplay, and scheduler recovery remain source-linked or unresolved for quantitative probability analysis.
- Event 014 decisions continue to require the existing `decision_ai_will_do` adapter contract and typed scenario inputs. Their incomplete candidate and external-input analysis was not changed here.
- If a future owner changes Evolution I/II MTTH factors, decision weights, or convergence timing, rerun `chaosx_ai_probability_auditor` from `hoi4.probability_inspect` and complete a same-scenario `hoi4.probability_compare` when the auditor route is available.

No gameplay simplification was made. The only omitted evidence is the unavailable auditor and compare pass described above.
