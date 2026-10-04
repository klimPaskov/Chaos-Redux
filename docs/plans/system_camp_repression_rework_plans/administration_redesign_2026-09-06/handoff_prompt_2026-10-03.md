> Disposition: superseded as current navigation by [resume_packet.md](resume_packet.md), reconciled against the current owner integration and famine handoffs on 2026-10-03.
> Preserve this dated prompt as historical evidence, including its earlier failed-agent findings, and do not use its old queued work or terminal-agent status as current implementation instructions.

Continue the existing Chaos Redux camps, forced-labor and repression rework in this workspace:

`C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`

Create or retain an active goal with this full objective: **Complete the Chaos Redux camps, forced-labor, and repression rework plan: add approved bounded package-owned monthly dispatch, finish gameplay and historical/GUI evidence, reconcile audits and documentation, and create a scoped commit only if all required acceptance gates pass.**

The goal is incomplete and uncommitted.
Do not redefine it around the latest small fix, treat archived tests as broad completion proof, or mark it complete while a requirement or required evidence remains missing.
Read the current replacement `AGENTS.md` and applicable repository skills before acting.
The current working tree contains extensive concurrent unrelated changes; preserve them and review ownership by hunk before any commit.

Start by reading these current navigation documents, then verify every relevant claim against the live files rather than relying on this prompt alone:

- `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/accepted_implementation.md`
- `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/resume_packet.md`
- `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/completion.md`
- `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/scoped_diff_review_2026-09-27.md`
- `docs/camp_administration_dispatch.md`
- `docs/camp_institutional_mortality.md`
- `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/soviet_release_integrity_2026-09-27.md`

**Direct user choices confirmed in this session**

- Implement the full accepted plan and keep the goal active until genuinely achieved.
- Keep core Chaos Redux accounting, shared registries, event log/details, settings, diplomacy and super-event frameworks untouched; package adapters may call existing APIs.
- Use the approved bounded hidden event per eligible registered country to reach the same month-guarded recipient even when the Chaos Meter dispatcher is disabled; add no whole-world recurring hook.
- Retain Germany's paid exact-cohort prisoner-transfer decision after administration begins, as one national order selecting the oldest eligible registered living source, with execution-time revalidation and payment only after success.
- On 2026-10-03, grant the Soviet prisoner-release order's national quota/famine/grievance/reform settlement only after its first successful measured release; later paid orders release survivors without repeating that settlement.
- On 2026-10-03, after an unlabelled outside loss makes a host's multiple living origins ambiguous, pause origin-specific actions until a source-labelled receipt restores provenance. Do not use an unknown-origin continuation pool or newest-first/proportional attribution as the chosen policy.
- On 2026-10-03, when Soviet famine relief lacks quoted equipment, offer an explicit no-resource response with famine and corruption penalties. No requisition debt was chosen.

There is a documentation conflict to resolve carefully.
The bottom `User decisions of 2026-10-03` section in `accepted_implementation.md` was found claiming an unknown-origin pool, contrary to the direct pause answer above; that bullet was corrected before this handoff.
The same section also claims approval of zero-survivor pre-administration closure and Riga/Thessaloniki source anchors, but this session has no direct human answer establishing those two choices.
Verify trusted user-message evidence for those claims before treating them as accepted; do not infer approval from a document's status label or another agent's prose.
If trusted evidence is unavailable, retain those two dispositions as unresolved and ask only for the missing decisions.
Do not re-ask the confirmed choices above.

**Most recent implemented Soviet release work**

The reachable native decision is `sov_release_prisoners_for_military_service` in `common/decisions/camp_repression_major_country_decisions.txt`.
Its shared gate `camp_rework_soviet_service_release_ready` and state target are in `common/scripted_triggers/camp_repression_rework_triggers.txt`.
They require one positive reconciled SOV-responsible operating Gulag and reconciled rows at every affected operating Gulag.
The country release helper in `common/scripted_effects/camp_administration_country_effects.txt` releases exact living custody and closes census intake only after a positive site receipt.
The effect in `common/scripted_effects/camp_repression_major_country_effects.txt` returns the native 45-PP quote on zero accepted release and sets `camp_rework_soviet_service_release_policy_enacted` only on the first positive release.
The shared router in `common/scripted_effects/camp_repression_rework_effects.txt` uses the actual numeric `camp_admin_country_last_released_k` receipt to withhold its scripted country-action cooldown on rejection.
The old four-slot Ledger helper is not bound by the current production GUI; do not report it as a reachable consumer without proving a current binding.

The first/repeat description uses `GetSovServiceReleaseConsequence` in `common/scripted_localisation/camp_administration_country_localisation.txt` and keys in `localisation/english/camp_repression_country_kits_l_english.yml`.
The repeat branch is first and the first-settlement branch is an unconditional fallback.
The old compatibility label `camp_ledger_action_sov_military_release` was corrected to `Release Prisoners` in `localisation/english/camp_repression_rework_l_english.yml`.
The row requirement now says that all affected sites need complete, consistent custody records.
The one-time design was recorded in `accepted_implementation.md` and promoted into the Soviet prisoner-release subsection of `docs/specs/system_camp_repression_rework_specs/specs/system_camp_repression_rework_spec_part_3_germany_japan_soviet_deepening.md`.

`soviet_release_integrity_source_tests.py` currently passes five parsed-production scenarios, with results in `soviet_release_integrity_source_results.json`.
They cover a bad second site with refund/no relief/no intake closure/no scripted cooldown, 15,000 survivors across two valid sites for one 45-PP debit, headroom exhausted at execution, a one-person first settlement, and a later new-site one-person release for another 45 PP with zero repeated national policy delta.
These use mocked engine primitives and native payment; they do not prove a live click, refund ordering or the native 150-day `days_re_enable` timer.
The foundation and major-country suites last passed 34 and 15 scenarios.

The one-time localisation audit completed with no semantic/key/encoding defect in the new branches; its two wording recommendations were applied.
The final one-time decision audit and Soviet probability comparison did not complete: their agents ended with `workspace routing discovery timed out`.
Restart only the necessary bounded audits and save their handoffs to files so evidence survives the session transition.
The frozen pre-row-gate decision file is `ai_evidence/sov_release_decisions_before_row_gate_2026-09-27.txt`, SHA-256 `3EF974763A83E937FD5068B890BE0EE09EE9F454AE9E0895434CBE06FA515782`.
The weight remains `constant:camp_rework_ai_weight.soviet_relief`; direct decision inspection reported raw willingness 40 and native cost 45, with array eligibility unresolved.
Use the same named scenario set and candidate pool for a matched compare; do not call a decision score an AI click probability.

**Urgent current-source famine finding at handoff**

The latest read unexpectedly found much of the no-resource famine implementation already present in the shared worktree; do not duplicate it.
`events/soviet_gulag.txt` has equipment-gated `.1.a`/`.2.a`, a warning shortfall option `.1.c`, and a crisis shortfall option currently named `soviet_gulag.2.d`.
The shared `camp_rework_soviet_relief_resources_ready` trigger exists near line 2380 of `camp_repression_rework_triggers.txt` and accepts exact quoted motorized, train and support stock.
The native relief decision uses it in custom-cost and availability gates.
`camp_rework_soviet_relief_mobilization_failed` exists in the major-country effect file.
This work is unverified and its proposal document is stale.

Fix this concrete collision first: `localisation/english/camp_repression_rework_l_english.yml` contains `soviet_gulag.2.d` twice, once for the event description near line 542 and once for the new shortfall option near line 546.
The event currently uses that same key for both `desc` and option `name`.
Give the new option a unique stable key such as `soviet_gulag.2.shortfall` and update its event name/localisation together, preserving the original event description key.
Then verify the entire accepted famine contract: final affordability recheck before equipment debit, one payment, exact-stock acceptance, one-unit-short rejection, a visible no-resource option even with no valid site target, no duplicate mission or penalty, no population/research reward, first/critical penalty differences, meaningful tooltips and candidate-pool AI evidence.
The relief helper itself still appeared to call `camp_rework_consume_labor_project_resources` unconditionally, so trace all reachable callers and the dispatcher rather than assuming option-time gates suffice.
Update the accepted proposal, event documentation/catalog only where player-facing facts are actually represented, and run scoped event, decision, localisation and probability audits.

**Next large implementation tranche**

Implement the accepted mixed-origin pause policy from `occupation/origin_ambiguity_audit_2026-09-27.md`.
The design-only architect failed before returning a handoff; `origin_ambiguity_containment_architecture_2026-10-03.md` must not be assumed to exist or be complete.
Use `chaos-redux-state-ledgers` and a bounded `chaosx_scripted_system_architect` pass before patching.
Inspect `camp_occ_reconcile_external_population`, custody `camp_admin_refresh_capacity`, all exact transfer and row-death gates, source/destination authority, rollback and cleanup.
An outside loss may be visible in shared Deaths while hidden by net population growth; shared core receipts lack origin labels.
Create package-owned sticky host ambiguity, pause every action that would fabricate a specific original-cohort claim, preserve aggregate observations without another physical debit/Deaths entry, and define a verified restoration receipt rather than clearing the flag on an unrelated new transfer.
Keep reform/release/capture/annexation behavior finite and honest, and show current uncertainty in Records.
Exercise mixed A/B origins with an unlabelled loss, growth-masked loss, custody loss below headroom, one-origin control, exact transfer then destination death, failed inverse and terminal cleanup.

**Other evidence and limits to preserve**

- The existing 900×540 native window is `repression_ledger_window` with Administration, Locations and Records, separate native controls and contextual actions. Use its current source and archived exact scenarios for further edits.
- Four postqualified 900×540 design references are in `references/postqualified_2026-09-27/`; parent visually inspected them and the handoff records vanilla/Chaos MCP inputs and native mapping. The original references preceded populated vanilla capture, so the requested original reference-before-edit chronology was missed and cannot be repaired retroactively.
- The country timer, current GUI matrices, institutional Records renders, vanilla reference renders, reference reads and partial domain results are indexed from `resume_packet.md` and `completion.md`.
- Monthly Auschwitz/Pingfang institutional losses have 23 source scenarios. German full-permission and Pingfang 12-month examples measured 234 and 292 institutional deaths from a declared 10,000 opening cohort, with separate custody losses; rates are gameplay tuning, not archival estimates.
- The legacy Mengele burst's shared death target was corrected from `OWNER` to German event `ROOT`, with a POL-owned/GER-controlled state-88 source test. It still lacks an exact living custody-origin bind, so full cohort nonoverlap remains unresolved.
- Broader historical Holocaust and China benchmarks remain partial by controller, geography, transport/rescue and cause. Do not tune a quota toward six million or merge Pingfang institutional losses into the five-state China occupation result.
- Event/technology helper coverage, native timer scheduling, dynamic tooltip pixels, clicks, save persistence and exact live receipts remain unproved. No usable current save is available, and AGENTS.md forbids agent-run HOI4 testing or requesting logs. Report the limits without instructing the user to run a test.
- Installed direct MCP last reported 3.6.0, while connected route schemas sometimes differed and rejected `controls`. Reverify current health, version, tool schema and task negotiation; do not assume the version still matches. Successful reference wrappers are archived under the Soviet release MCP directories. `omittedSources` must be resolved before claiming source coverage.
- Event-option `.10` current-source conditional probabilities were evaluated under a complete declared local pool; decision/mission results remain score-only where documented. A separate render lookup sometimes returned `PROBABILITY_ANALYSIS_NOT_CACHED` despite evaluation artifacts being emitted.
- The workbook audit found no catalog row for the Soviet prisoner-release decision; no workbook/export edit was made for it. The Event 22 catalog mismatch belongs to a separately unimplemented rewrite and must not be silently rewritten as this package.
- Core dirty changes in `chaosx_on_actions_chaos_meter.txt` and `chaos_meter_effects.txt` belong to other Event 42/23 work and must be excluded from the camps commit. The Soviet-collapse UWR aftermath file is mixed and needs precise package-hunk staging.
- A duplicate diagnostic image directory `mcp/after/gui351_current_matrix/` remains because automatic approval review rejected recursive removal as blocked by policy; exclude it from the scoped commit and do not bypass that rejection.

Useful current source checks, run from the mod root after relevant changes:

```text
python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/soviet_release_integrity_source_tests.py
python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/institutional_mortality_source_tests.py
python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/foundation_source_tests.py
python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/major_countries_source_tests.py
python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/dispatch_source_tests.py
```

Do the remaining implementation and audits, reconcile the accepted spec and current docs, review a package-only diff, and use `chaos-redux-shared-git-commit` for the scoped commit only after the complete plan and all required acceptance evidence are genuinely finished.
Keep the goal incomplete and report each remaining requirement honestly if an input or supported route blocks it.
The handoff session has no live shell process or agent still doing gameplay work; the architecture/probability/one-time decision agents are terminal errors, and the localisation/reference/catalog agents are completed.
