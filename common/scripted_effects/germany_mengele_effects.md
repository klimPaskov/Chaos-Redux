# Germany Mengele legacy compatibility

This document covers the report and retired foreign-purchase compatibility helpers in `germany_mengele_effects.txt`.
Other package mechanics are documented by their owning event and project documents.

## `germany_mengele_register_experiment_deaths`

Purpose: retain the established entry point used by the automatic report events without submitting an additional casualty transaction.
Scope: country.
Call sites: immediate report blocks in `germany_mengele.10`, `.11`, `.12`, and `.13` in `events/germany_mengele.txt`.
Inputs: none.
Output: temporary `mengele_experiment_deaths = 0`, meaning zero newly accepted deaths from report delivery.
Defaults: the output resets on every call.
Cleanup: the former request scratch values `mengele_autonomy_death_add`, `mengele_facility_death_add`, `mengele_permission_death_add`, and `mengele_permission_hidden_atrocity` reset to zero on every call.
Side effects: temporary writes only.
Report replay leaves physical population, living custody, immutable row provenance, institutional and shared death records, responsibility, hidden atrocity, programme progress, and research awards unchanged.
There is no custody request envelope or persistent event target.

```txt
# Inside an automatic report immediate block.
germany_mengele_register_experiment_deaths = yes
```

The bounded monthly state processor owns continuing harm through `camp_admin_country_apply_institutional_site_mortality` and `camp_admin_record_deaths`.
The actual receipt consumes verified finite living custody, measures physical loss, records the institutional cause and the shared Deaths receipt under the original responsible authority, and advances the known physical-host baseline after the committed receipt.
The country and foundation helper documents define its gates and cleanup contract.
Its historical Germany gate begins on 1943-05-30 and requires actual authority, an operational supported site, appropriate mandate and budget, and active programme proof.
Report flags, stages, condemnation, exposure, and crisis choices remain event-owned.

## Tuning and integration

This compatibility helper adds no tuning constants, timer, hook, row selector, protected-group selector, icon, localisation key, or asset.
The old `germany_mengele_deaths` request tuning is no longer consumed by these four reports.
Monthly institutional rate tuning belongs to `camp_admin_institution_mortality` and the existing country mortality helper.
No death count grants programme progress or research awards.

Acceptance basis: on 2026-10-03 the parent explicitly accepted evidence-only automatic reports under the user-approved single bounded monthly camp processor contract, retiring the duplicate routine casualty burst while retaining the reports and their choices.
Implementation evidence and validation limits are recorded in `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/mengele_exact_custody_adapter_2026-10-03.md`.

Future work: if report text needs historical casualty evidence, the event owner can display already accepted institutional records with a clear reporting window.
Such presentation must never resubmit those records as physical deaths or research progress.

## Retired foreign-subject purchases

Acceptance basis: on 2026-10-03 the parent accepted retirement of `import_subjects_from_japanese_china`, `import_subjects_from_india`, and `import_subjects_from_africa` under the user-approved administration cutover and retirement of duplicate routine purchases.
The existing paid national `germany_transfer_prisoners_to_experiment_site` order through `camp_rework_germany_apply_exact_cohort_transfer` remains the approved exact cohort transfer.
No replacement foreign cohort, shipping route, selector, reward or restoration provider is authorized by this disposition.

The three decisions retain their identifiers, native costs, native re-enable timing and target metadata for save compatibility.
Since the 2026-10-04 agent decision (`docs/plans/system_camp_repression_rework_plans/agent_decisions_2026-10-04.md`, entry 4) they are fully hidden: `allowed`, `visible`, `target_root_trigger` and `available` are `always = no` and `ai_will_do` is zero, so no player or AI can see, target or take them before or after administration starts.
The retirement does not authorize any wider programme or replacement purchase route.

| Retired decision | Native cost and stale refund | Final completion |
|---|---|---|
| `import_subjects_from_japanese_china` | `global.black_friday_price_germany_mengele_decision_import_japanese_china_subjects_cost` | Refund of that charged price only |
| `import_subjects_from_india` | `global.black_friday_price_germany_mengele_decision_import_indian_subjects_cost` | Refund of that charged price only |
| `import_subjects_from_africa` | `global.black_friday_price_germany_mengele_decision_import_african_subjects_cost` | Refund of that charged price only |

The scalar refund body is unreachable while the decisions are hidden and remains only as a trusted native paid-completion callback.
It assumes the engine has charged that decision's native PP price before invoking `complete_effect`.
It creates no source marker, report event, equipment charge, success flag, scripted cooldown, death, benefit or research outcome.
Each additional stale paid callback receives its own matching refund.
Calling a refund body without a native charge is outside this callback contract.
The retained native `days_re_enable` field may still produce a native re-enable delay after a stale completion, and the source fixtures do not prove native cooldown cancellation.

### `germany_mengele_import_subjects_from_from_state` and `_accepted`

Purpose: retain inert compatibility entries for old direct helper calls.
Scope: country.
Input: obsolete temporary `germany_mengele_foreign_subjects_autonomy`.
Output: none.
Cleanup and defaults: both entries set that scratch input to zero on every call.
Persistent side effects: none.
They access no FROM target and issue no payment, refund, death, custody, transfer, report, condemnation, permission, autonomy, progress or reward operation.
Existing historical flags, responsibility and records are preserved.
There is no persistent target or registry cleanup because these helpers own no remaining transaction.

```txt
# A stale direct compatibility call has no gameplay outcome.
germany_mengele_import_subjects_from_from_state = yes
```

The retired decisions no longer call these helpers, and no new production caller is introduced.
The definitions preserve existing identifiers for stale direct references rather than provide a generic free-PP or casualty API.
No constants, icons, assets, localisation keys, periodic hooks or protected-group selectors were added.
Unused foreign-purchase tuning remains package-owned historical source for parent cleanup review.
Evidence and limits are in `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/mengele_foreign_purchase_retirement_2026-10-03/handoff.md`.
