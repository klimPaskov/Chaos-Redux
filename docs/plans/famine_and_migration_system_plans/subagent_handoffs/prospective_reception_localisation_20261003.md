# Prospective reception localisation review, 2026-10-03

Disposition: actionable source audit delivered to parent, runtime integration still in progress.
The parent assigned read-only source review of the accepted prospective reception lifecycle and granted ownership of this new handoff only.
No source, existing documentation, workbook, export CSV, gameplay, AI, asset, or Git changes were made by the auditor.
The accepted design clarification was inspected at commit `621df57aa7f1000778c540c220d47911b034aa65`, together with `prospective_reception_lifecycle_plan_20261003.md` and the current integration diff.
The prepared baseline directory contains 28 source files and one baseline record, and was left untouched.
Source is changing concurrently, so findings describe the inspected working copy and require parent reconciliation against final source.

## Recommended parent patches

### Missing native custom-cost keys

Only `migration_cost_open_reception` currently exists across localisation.
The offline Decision modding section at lines 311–329 documents selection of `<custom_cost_text>_blocked` when `custom_cost_trigger` fails and `<custom_cost_text>_tooltip` for hover text.
The six per-resource ready/blocked keys do not replace these engine-selected parent keys.
Add the following in `localisation/english/migration_l_english.yml`:

```text
migration_cost_open_reception_blocked: "$migration_cost_open_reception$"
migration_cost_open_reception_tooltip: "$migration_cost_open_reception$"
```

These aliases retain the same independently coloured resource selectors and do not introduce duplicate payment amounts or extra resource labels.
This is a documented key-coverage issue, not observed native raw-key output.

### Premature agreement, policy precision, and prose repair

Three newly edited descriptions contain sentence semicolons prohibited by the repository prose rules.
The preparation description also says `agreed border state` before the host has accepted the request.
The target tooltip says preparation must improve reception services, but the actual `migration_reception_preparation_can_change_state` predicate also allows a reception-policy change alone.
Its capacity wording should describe the resulting capacity after preparation, rather than imply the missing capacity must already exist before the setup.

Use these exact replacement values, preserving the existing dynamic tokens:

```text
migration_accept_corridor_offer_desc: "Guarantee safe passage from [?humanitarian_corridor_offer_origin_state_id.GetName] through [?humanitarian_corridor_offer_front_state_id.GetName]. Acceptance requires a safe route and enough reception capacity for all requested civilians. People remain at the origin until their transfer succeeds."
migration_open_reception_desc: "Fund shelter, sanitation, and basic medical services in [FROM.GetName]. During an incoming request, this prepares the requested border state. Preparation moves no people and does not open the route. The request must still be accepted."
migration_open_reception_target_tt: "Select a safe state that we own and control, with secure food and usable transport. An incoming request must name this exact state and still be current. Preparation must improve services or change reception policy. For an incoming request, the resulting capacity must cover all requested civilians. An unsuccessful setup returns its payment."
```

Vagueness repaired: `identified civilians` becomes the full requested civilians, and capacity becomes the resulting full-request capacity.
Bloat repaired: the acceptance description combines the meaningful condition with the action instead of repeating an unqualified route-opening claim.
Obvious explanation: no additional redundant passage was found in this bounded diff.
Repetition: no remaining duplicate cost labels or duplicate payment prose were introduced.
Overcomplication repaired: the overloaded preparation requirement sentence is split into complete requirement and failure-consequence sentences.
Style repair: remove all three sentence semicolons and replace premature `agreed` with `requested`.
No quotations are present on these assigned surfaces, and no attributed or sourced quotation was altered.

## Source-confirmed contracts

- `common/scripted_localisation/migration_reception_preparation_cost_scripted_localisation.txt` has three selectors and six literal localisation keys.
Each resource selector compares current holdings against its fresh central cost using `NOT = { holding < constant }`, so equality is ready.
The ready values use the existing yellow normal colour and blocked values use red, with the same resource-specific comparisons as the shared affordability predicate.
- `common/scripted_triggers/migration_reception_preparation_triggers.txt:4` shares inclusive affordability between decision `available`, `custom_cost_trigger`, and the preparation owner.
The predicate includes valid-country context in addition to the three resource comparisons.
The colour selectors appropriately describe resource affordability alone and do not claim that the full target/action is available.
- `common/script_constants/migration_reception_preparation_constants.txt` centralizes 20 political power, 100 support equipment, and 500 fuel.
The preparation effect reads those constants for one payment path and full refund amounts.
The three `migration_reception_preparation_quote_*` normal variables are not used as debit authority.
- `common/scripted_effects/migration_decision_phase_effects.txt:10`–12 projects the three quote amounts from constants in receiver COUNTRY scope at the existing bounded refresh boundary.
Its paired Markdown describes them as display-only amounts.
- `migration_cost_open_reception` prints exactly three icon/amount pairs, no literal resource names and no hidden fourth cost.
The six output keys use integer formatting, which matches these integer costs.
- The support token resolves through `interface/chaosx_texticons.gfx:90` to `GFX_support_equipment_text_icon`.
Installed vanilla `interface/texticons.gfx:123` defines `GFX_fuel_texticon`, and line 262 defines `GFX_pol_power`.
The identical three texticon spellings already appear in `humanitarian_cost_l_english.yml`.
No new asset family or icon token is required.
- The targeted preparation description uses `[FROM.GetName]`, consistent with the decision's state target.
The decision enters `FROM` for `migration_reception_preparation_target_is_valid`, whose owner/control predicate uses the receiving-country `ROOT`.
Accept/reject are untargeted country decisions and resolve requester, origin, and front through their receiver-owned mirror variables.
Those references avoid accidentally using a global scheduler's ambient requester `ROOT` in visible text.
- `GetMigrationPriorityResponse` first selects pending-request text through `migration_pending_reception_issue_is_valid`.
The pending paragraph explains preparation or refusal and conditions acceptance on safety and capacity.
It does not describe arrivals, authorize a route, promise successful movement, or introduce a fourth metric.
- The pending issue predicate requires a valid evacuation offer plus existing phase evidence, repeated incidents, or the exact offered origin amount meeting `category_trapped_people`.
It does not read unrelated large national or origin pressure as a host intake amount.
Its exact-offer validity implementation remains runtime-owner work and was not inferred from the predicate name.
- Preparation, acceptance, and rejection remain three existing controls.
Acceptance is hidden until `humanitarian_corridor_offer_can_be_accepted` passes, while preparation and rejection use the pending request path.
Pending intent is not an arrival or a population credit, and the inspected text does not count movement as death.

## Pending integration condition

At the inspected snapshot, `humanitarian_corridor_submit_offer` writes the receiver mirror and calls `migration_register_active_country`, but its host mirror block at lines 329–338 has no immediate `migration_refresh_decision_phase_from_country` call.
The runtime architect is still implementing this boundary, so this is a precise pending dependency rather than a completed-feature defect.
Before a newly eligible receiver's first preparation row renders, the owner must execute that receiver's existing phase refresh so all three normal quote variables contain the central amounts.
Otherwise a fresh receiver can reach a cost row whose resource readiness comparisons are correct but whose uninitialized displayed normal variables show zero.
The same refresh boundary must preserve the accepted threshold and exact-generation evidence.
No new periodic hook, quote-on-render mutation, or quote-based payment should be introduced to resolve this dependency.

## Required audit lists

Missing keys: `migration_cost_open_reception_blocked`, `migration_cost_open_reception_tooltip`.
Duplicate keys: none found in the bounded migration YML.
Scripted-localisation issue list: no missing six resource output keys or getter-name mismatch found, but the native parent blocked/hover keys above need coverage.
Dynamic text opportunities: existing target/actor tokens are appropriate, and pending priority does not need another metric.
Cross-surface mismatches: service-only target wording conflicts with the allowed policy-only change, and `agreed` conflicts with pre-acceptance request status.
Final wording for mirror consumers is provided above.
Encoding concerns: none identified in the bounded migration YML source check.
Sourced quotation preservation: no quote-bearing assigned surface, no quotation changes.
Workbook handoff: none, because this shared system has no new event row.
Unresolved wording decisions: parent application of the exact recommended key/prose patches remains pending at handoff creation.

## References and evidence limits

Skills applied: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
AGENTS.md was read before the bounded work.

Local references read:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md:1`–45, acting COUNTRY scope, targeted FROM scope, and controlled-state targeting.
SHA-256: `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019`.
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:307`–329, custom-cost parent, blocked, and hover localisation keys.
SHA-256: `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162`.
- Earlier same-agent localisation review read the offline Localisation scripted-text ordering section and installed vanilla `00_scripted_localisation.txt` precedent.
Those references justify the first passing priority branch and literal output-key structure, not native display execution.

The accepted plan already records corrected reference-context and decision-inspection requests timing out after 600 seconds without artifacts, and probability route worker failures.
The parent's explicit task is a bounded source-only localisation review, so no heavy duplicate MCP request or GUI render was attempted.
No GUI layout changed, and no production wrapping, overflow, colour rendering, engine execution, AI balance, or physical-transfer result is claimed.
No useful new artifact URI was returned to retain.

Meaningful checks: compared all three readiness conditions against shared inclusive affordability, traced constant-backed quotes/payment/refunds, verified target/receiver scope references, resolved existing icon definitions, inspected six selector output keys and native custom-cost suffix coverage, and manually read the changed priority/decision/requirement prose.
Runtime helper bodies and initial quote scheduling are still under owner integration and require final parent review.
No game was launched, no logs were read, and no source tests or workbook changes were made.
No gameplay simplification was made by this auditor.

## Parent patch disposition, 2026-10-03

Disposition: implemented in source by parent, with final native evidence still separate.
The parent applied all three recommended wording replacements and added the Open Reception blocked and hover parent aliases.
The auditor verified those exact descriptions and existing alias keys after application.
The parent introduced `migration_project_reception_preparation_cost_quote` as a shared COUNTRY helper called by the existing active-country registration and phase provider.
Calls at `migration_core_effects.txt:564` and `migration_decision_phase_effects.txt:16` address the previously recorded first-display quote dependency in source.
The parent's hidden completion effect and meaningful custom effect tooltip remain parent-owned changes.
The subsequent append-only closure for the other cost-family suffix keys is recorded in `humanitarian_cost_parent_key_closure_20261003.md`.
This disposition supersedes the earlier pending key/prose/quote items without claiming runtime display or engine execution.
