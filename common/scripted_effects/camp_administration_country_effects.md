# Country administration helpers

Status: implemented source; final MCP and integration acceptance are tracked in `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/major_countries_handoff.md`.
Acceptance: the parent's assignment implements the accepted national administration design, including distinct GER/JAP/SOV institutions, finite historical enrollment, and paid civilian conversion.
The parent additionally accepted bounded historical custody envelopes and explicitly identified gameplay project allocations where exact regional counts are unavailable.

## Public contract

| Helper | Scope and caller | Inputs and outputs | Side effects |
|---|---|---|---|
| `camp_admin_country_initialize` | Country, after foundation initialization | No input; initializes major kit once, delegates civil kit | Historical major priority and coercive mandate defaults once; records/program migration; retires ordinary quota missions |
| `camp_admin_country_prepare_monthly` | Country, before foundation monthly | Registry `camp_active_site_states` | Civil prepare, invalid-authority reform, finite major enrollment, routine mission cleanup |
| `camp_admin_country_monthly` | Country, after foundation and occupation monthly | Foundation support/payment state; one actual calendar-month guard | Civil monthly, paid institution/review/archive progress, deterministic AI decisions, display aliases |
| `camp_admin_country_action_1` / `_2` | Country, GUI buttons | Matching `_visible` and `_available` triggers | Authorize/resume or suspend/reform; delegates the two civil callbacks |
| `camp_admin_country_halt` | Country, explicit suspension or terminal lifecycle | No inputs; retains saved program/progress | Stops authorization/review, clears institutional slot; civil cleanup where applicable |
| `camp_admin_country_reform` | Country, national reform | No inputs | Stops institutions and occupation campaign, releases finite survivors through foundation, starts paid civilian conversion, preserves evidence |
| `camp_admin_country_release_registered_prisoners` | Country, retained Soviet release policy | Registry of SOV-responsible operational Gulag states with positive reconciled custody; output `camp_admin_country_last_released_k` | Releases only surviving enrolled people in place and closes intake only after a positive site receipt; the caller preflights every affected site and grants policy relief only after a positive actual total; no army reserve or population creation |
| `camp_admin_country_start_oversight` | Country, native review decisions or deterministic AI | A free institutional slot and affordability checked by callers | Reserves the one slot for six paid months, then reduces national/legacy security authority |
| `camp_admin_country_start_archives` | Country, native aftermath decision or AI | `camp_admin_country_archives_available` | Reserves institution slot for six paid months; completion preserves records and contributes existing evidence pressure |
| `camp_admin_country_apply_institutional_site_mortality` | State, existing guarded `camp_admin_monthly_state` pass | `camp_admin_country_experiment_site_active`, current surviving custody, supported local rate | Requests one measured institutional-cause death receipt through foundation; never modifies research progress or awards |
| `camp_admin_ger_establish_krakow_site` | GER country; human decision or guarded AI monthly call | `camp_admin_ger_krakow_setup_eligible` and enough political power for `global.black_friday_price_genocide_decision_cost_build_concentration` | Debits that Event 026 sale price (25 PP outside a sale) and credits one Political Power sale purchase, registers a base detention site in state 88 once, records responsible authority and `site_established` history, refreshes the interface |
| `camp_admin_country_ai_ger_radical_mandate` / `camp_admin_country_ai_krakow_killing_role` | AI GER country in guarded monthly pass | Nazi wartime context; later site flag, radical mandate, state-88 control and operational detention site | Calls the same paid mandate and selected-role commands used by the GUI; killing conversion and extermination registration are separate from detention setup |

The GUI uses `GetCampAdminCountryAction1Name`, `GetCampAdminCountryAction2Name`, their tooltip functions, and `GetCampAdminInstitutionSummary`.
`camp_admin_research_progress` and `camp_admin_research_target` are read-only display copies of actual institutional progress and target.
Civil review and property-claims progress is copied after civil init/monthly/actions by `camp_admin_country_refresh_civil_institution_display`, and the summary selects civil activity before major-country status.
There are no routine popup events or new worldwide hooks.

## Continuing experiment-site loss

`camp_admin_country_experiment_site_active` is a state trigger requiring the original responsible authority, current direct or explicitly recognized subject control, reconciled live custody rows, a supported operational site, coercive or radical mandate, and at least Development spending.
The German branch requires state 88, an experiment marker, Nazi Mengele authority, and the 1943-05-30 historical gate. Restricted, limited, full and bypass permission levels select separate centralized monthly fractions.
The Japanese branch requires state 328, the completed Pingfang bureau and experiment markers, active Ishii authority, and no prisoner-experiment shutdown; a Japanese subject may control Kirin only through the site's explicit subject-authority flag.
The site monthly callback first applies custody, labor and any separately authorized killing-center violence causes. It then requests institutional loss from those remaining living detainees, scaled by the paid local support ratio and `camp_admin_institution_mortality` constants.
The foundation measures the actual physical state-population debit, consumes that same amount from custody rows, records one institutional-cause site and original-authority receipt, and makes one shared Deaths projection; a rejected or floor-limited request records no institutional loss.
This consequence can continue after the one-use research bonus because its site authority and maintenance are separate from `camp_admin_institution_slot_active` and the saved six-month research program. Deaths never enter progress, completion, bonus strength or award count.
The Soviet Gulag design and release programs retain their custody and labor causes and do not acquire an experiment mortality cause.
Automatic report calls to `germany_mengele_register_experiment_deaths` are evidence-only delivery and generate no additional physical death, shared Deaths entry or hidden atrocity.
The bounded monthly institutional kernel owns exact finite custody losses; report replay cannot consume survivors or advance programme progress.
See [Germany Mengele report compatibility](germany_mengele_effects.md) for the report helper's zero-receipt and scratch-cleanup contract.
The tuning rates are gameplay fractions and are not historical death estimates. See `docs/camp_institutional_mortality.md` for scenario numbers, provenance and future work.

## German state-88 detention setup

`camp_admin_ger_krakow_setup_context` requires initialized national administration, Nazi German authority at war on or after 1943-05-30, no reform or prior setup, direct control of state 88, and no active/closed camp marker, responsible-authority variable, concentration camp or extermination camp there.
`camp_admin_ger_krakow_setup_eligible` adds the development-budget requirement; the human `camp_admin_ger_establish_krakow_site` decision shows that requirement and a political-power quote, and the effect checks affordability again before debiting the Event 026 sale price of `genocide_decision_cost.build_concentration` (25 PP outside a sale); the decision's custom cost and its texts read the same `global.black_friday_price_genocide_decision_cost_build_concentration`.
The effect sets German responsibility in state 88, ensures the standard concentration-camp level, registers `camp_rework_site_type.detention`, sets country and state once-only flags, and writes `camp_admin_history_kind.site_established` with state 88.
`GetCampAdminHistoryKind` maps that new history kind to `camp_admin_history_site_established`; the player-facing text says “Detention site established.”
The setup grants neither a killing role nor the optional Mengele experiment marker; the separately paid radical mandate and killing-role conversion remain required for the later Łódź occupation-to-custody route.
The AI budget helper recognizes this setup context before the development-budget requirement and can raise spending through `camp_admin_set_budget` when its stock, reserve and policy-hold checks permit.
Within the guarded monthly country callback, AI calls the paid radical-mandate helper, then the detention setup effect, then the paid selected-role helper in that source order; each helper has its own gate, so a failed early mandate attempt can be retried on a later month after the site exists.
This is source implementation evidence, not proof that a natural 1944 scenario reaches the role, support, capacity, control and occupation-row gates or produces an exact engine transfer receipt.
The bounded country callback currently depends on `genocide_monthly_global_pulse` through the monthly Chaos Meter on-action, whose entry guard checks that `settings_chaos_meter_disabled` is absent; this disabled-setting route needs parent resolution before reliable monthly availability can be claimed.

## Internal program map

`camp_admin_country_start_program` receives the required temporary program input, validates that exact programme's historical and authority gates, selects a proven operational enrolled registered state, and saves its id in `camp_admin_institution_state_id`.
The country registry loop uses the current country and `PREV`, never the global pulse's `ROOT`.
Auschwitz is state88 and Pingfang is state328; earlier German institutions do not inherit Mengele's gate.
Japanese transport work selects a Chinese geographic host; Soviet design work selects a Gulag host.
`camp_admin_country_select_program` deterministically chooses the first eligible unfinished program.

| Program | Earliest phase and additional gate | Category | One-use bonus |
|---|---|---|---|
| Camp Inspectorate administration | 1936, Nazi regime | industry | 50% |
| WVHA industrial coordination | March1942, Nazi regime at war | industry | 100% |
| Auschwitz medical administration | 30May1943, Nazi regime, German-controlled operational Auschwitz, permitted existing program | support_tech | 50% |
| Japanese occupation transport | 7July1937, war, Chinese geographic operating institution | industry | 75% |
| Central Army administration | 1939, review authorized | support_tech | 50% |
| Pingfang records | 1939, operating named institution, no shutdown | support_tech | 50% |
| Soviet detained design bureaux | 1939, communist authority | engineers_tech | 75% |
| Soviet wartime industry | 22June1941, war | industry | 100% |
| Soviet engineer release | After1January1944, review authorized | engineers_tech | 50% |

Program work requires a coercive mandate, development spending, at least 75% local support, and payment of 12 support equipment plus 5 PP for each advancing month.
The six-month target takes twelve paid months if contested authority halves progress throughout.
The source never reads deaths to determine progress or research strength.
`camp_admin_country_award_program` checks a stable per-program completion flag and rejects an award while any bonus in the same technology category is held.
It then calls foundation's shared award receipt; only accepted receipts add the fixed-name bonus with `uses = 1`.
Foundation limits accepted awards to two per actual calendar year and50–100% strength.
A fully progressed program waiting for category availability or the annual limit does not pay again.
The development-pause control prevents automatic selection of a new program but does not cancel an already funded commitment.
The Soviet release program records a technical-personnel subset of at most 0.5 thousand surviving detainees, then completes its positive finite release through `camp_admin_release_detainees` before requesting its survivor-derived award.
It preserves the camp's other prisoners and does not create military manpower.
`camp_admin_country_prepare_ai_budget` runs only for AI, respects development pause, and holds each successful policy change for three calendar months.
It forecasts actual registered custody/civilian maintenance and requires three months of maintenance plus economic/institutional commitments above the support reserve before raising maintenance spending to development.
It lowers spending only when stock cannot cover one maintenance month plus the reserve, after the policy hold.
Both changes call the shared paid `camp_admin_set_budget` command and never grant equipment or extra spending allowance.
Human choices are untouched, and native authority decisions do not bypass the shared national-priority control.
These bonuses represent abstract administration, industrial design and later use of records; they are not claims that abusive experiments produced reliable scientific benefits.
No biological procedure, weapon-development method or research slot is introduced.

## Finite enrollment

`camp_admin_country_prepare_census` selects a country/group envelope and calls `camp_admin_country_apportion_census = { GROUP = ... }`.
The literal group selects a matching state host predicate and persistent state/national cumulative enrollment receipts.
The national envelope is divided across currently eligible existing registered hosts rather than assigned in full to every camp.
`camp_admin_country_admit_census_host` bounds the request by the host share less prior enrollment, the national remaining allowance, actual state population less existing custody/occupation/civilian cohorts, and foundation's physical capacity/floor/population-share checks.
All quantities ending `_k` are thousands.
Admission changes membership only, not physical population.
Only the accepted foundation receipt increments `camp_admin_country_census_<group>_enrolled_k`, aggregate state `camp_admin_country_census_enrolled_k`, national `camp_admin_country_cumulative_<group>_k`, and aggregate `camp_admin_country_cumulative_intake_k`.
Those cumulative receipts survive death, release and capture, so the same enrollment allowance cannot repeatedly refill losses.
For the German camp stock snapshots, the dated ceiling is compared with cumulative accepted enrollment before assigning any new share; falling live stock alone never reopens that date's intake.
Full survivor release closes the affected host's automatic census intake, while the Soviet partial engineer release leaves other registered survivors in custody.
Protected forced-transfer membership is not used as a census source; the existing verified transfer path remains separate.

German camp headcount anchors and the later civilian forced-labor envelope are separate groups with distinct host roles.
The ordinary German camp census excludes an operating killing role, so it cannot automatically refill a killing center or consume capacity intended for a measured transfer.
Before a detention site is converted, it can still receive ordinary finite census intake; conversion therefore does not promise a particular amount of later free capacity.
German concentration-camp labor is represented separately from extermination-site roles; Soviet penal labor is separate from institutional abuse; Japanese industrial/railway cohorts exclude experiment sites.
Historical state labor-role defaults are assigned once, so later player role changes survive every monthly census pass.
Pingfang's small lifetime institutional envelope never represents all Japanese occupation losses.
Wider occupation membership belongs to `camp_occ_*`, which must exclude actual detainees; census enrollment excludes `camp_occ_remaining_k` in return.

## Tuning and lifecycle

The canonical country tuning is `common/script_constants/camp_administration_country_constants.txt`: progress, quote amounts, support requirement, authority accumulation/review relief, technical-personnel cohort, program enum, and historical/project envelopes.
Concentrating authority reduces immediate institutional contention by 10, then increases security control by 4 per authorized month; economic sponsorship accumulates contention by 1 during active work.
Historical gates are explicit dates because they express chronology rather than numerical balance.
No persistent global event target is introduced.
Immutable responsible-country pointers and the registered state array are supplied by foundation/integration.
Named subject authorization is granted only to the accepted Japanese institution under the current MAN-to-JAP subject relationship; this does not authorize arbitrary subject camp control.
Capture or invalid authority prevents further work; a saved program may resume only if its full historical and operational gate is valid again.
Reform retains death/evidence totals and infrastructure while replacing the economic dependence through foundation's paid civilian slot.
The former flat Soviet25000 manpower grant is removed because release in place does not create additional military manpower.

## Existing surfaces and migration

The major-country ideas no longer add flat research speed, building speed or factory-efficiency gain on top of derived administration output.
Only the three camp-specific research-speed entries were removed from `germany_mengele_ideas.txt`; unrelated clone and weapon-system fields are outside this ownership.
The eight ordinary allocation/guard/record decisions are hidden and unavailable after foundation initialization; their AI weight literals are unchanged.
The six ordinary GER/JAP/SOV missions are removed after the foundation initialization flag is set. Their six `cancel_effect` blocks refuse to apply legacy outcomes after initialization even if the engine invokes them on `remove_mission`. The cleanup helper clears German project markers and Japan's bureau-active marker directly, then recalculates country values once when a mission was present; it does not apply the old German overstretch/evidence penalties or Soviet quota/famine relief as a migration side effect. Their legacy activations are disabled after initialization.
Distinct construction, review, crisis, evacuation, shutdown, records and reform decisions remain available under their existing phase gates.
The five legacy major-country instant percentage casualty calls are replaced by site initialization so finite monthly cause accounting owns physical losses.
Existing exceptional crisis events remain; normal paid administration is silent.

## Icons and future work

Native decisions reuse `GFX_decision_germany_ss_camp_administration`, `GFX_decision_japan_army_medical_review`, `GFX_decision_sov_gulag_expansion`, and `GFX_decision_sov_gulag_dismantlement` from `interface/camp_repression_rework.gfx` and existing `gfx/interface/camp_repression/icons/` DDS files.
The state-88 setup decision specifically reuses the existing `GFX_decision_germany_ss_camp_administration` definition and `gfx/interface/camp_repression/icons/GFX_decision_germany_ss_camp_administration.dds`; no new icon or image was produced for it, and no new art provenance is claimed.
No new portrait, art, sprite or event image is required by these helpers.
Potential future work is a separately accepted set of additional named industrial hosts with documented geography and independent cohort provenance.
Such additions must preserve the finite national receipts, funding, institutional slot and attribution rules rather than add demographic selectors or casualty-driven rewards.

## Engine helper inputs

`camp_admin_country_start_program = yes` requires temporary `camp_admin_start_program_input` to be initialized immediately before the call from the exact `constant:camp_admin_country_program.<program>` value.
It reads that input once into the existing persistent program variable before selecting a host.
Institutional work only advances after a full monthly payment while the authority, location, support and matching technology-bonus slot remain valid.
An active category bonus or the two-award calendar-year ceiling pauses further charges.
A measured engineer release awaiting its award is retried without another funded month or release, including after a year boundary.
`camp_admin_country_award_program_<program> = yes` has one explicit variant for each of the nine program rows above.
Each variant retains its original completion flag, bonus name, technology category, bonus constant, award validation, engineer-release handling and slot cleanup.
`camp_admin_country_apportion_census_<group>` and `camp_admin_country_admit_census_host_<group>` use explicit `ger_camps`, `ger_labor`, `sov_camps`, `jap_industry`, `jap_pingfang` and `jap_railway` suffixes.
Their country and state scopes, stock/lifetime inputs, host predicates, cumulative receipts, physical admission proof and PREV attribution remain identical to the documented census contract.
All explicit census variants take `= yes` and retain their existing input and cleanup contracts.

## Provenance boundaries and completed engineer receipts

The accepted 2026-10-03 pause policy is enforced through the common physical-host observer.
Programme work uses only the saved selected site: uncertainty in either its custody or co-located occupation rows blocks start, paid progress and final grant.
An unrelated uncertain occupation-only host does not block a proven selected-site programme, but it blocks national reform through `camp_admin_country_sites_ready_for_reform`, which inspects the complete bounded custody/occupation union.
Suspension through `camp_admin_country_halt` remains reachable without proving survivor release.
Fresh capacity/host observation runs before monthly institution work and final dispatch; each award variant repeats current selected-site authority, support, programme identity, completion, category and annual-limit checks.
Direct wrong-programme, incomplete or unavailable calls grant nothing.
No death total contributes to completion.

| Helper | Scope, inputs and defaults | Outputs, side effects and callers |
|---|---|---|
| `camp_admin_country_start_input_valid` | Country; required temporary `camp_admin_start_program_input` enum, no implicit default | Read-only exact programme/phase/regime validation; `camp_admin_country_start_program` consumes the input and rejects an occupied slot or pending engineer receipt |
| `camp_admin_country_program_site_ready` | State; PREV is the selecting country | Read-only authority, operational and reconciled-host proof; requires living custody or that same country's identity-valid completed engineer receipt; selection and current saved-site validation |
| `camp_admin_country_has_proven_program_site` | Country; bounded existing active-site array | Read-only existence gate for programme availability |
| `camp_admin_country_program_completion_ready` | Country; existing saved programme/site/progress | Read-only active slot, fresh valid site, support, mandate, budget, category availability, completed target and annual ceiling; all award variants and deferred receipt retry |
| `camp_admin_country_engineer_receipt_identity_valid` | Country; pending flag and six saved receipt fields | Read-only positive release, original authority, exact programme/state/progress/target identity; final award and zero-held post-release selected-site proof |
| `camp_admin_country_clear_engineer_pending_receipt` | Country; no inputs/defaults | Clears pending flag and six receipt fields, retains historical `camp_admin_country_last_engineers_released_k`; accepted engineer award, gated national reform and intentional oversight abandonment |

Only a positive actual foundation release sets `camp_admin_country_engineer_release_pending` and its `camp_admin_country_engineer_receipt_k`, `_state_id`, `_authority`, `_program`, `_progress` and `_target` fields.
Zero/rejected release creates no receipt, award, completion flag or award-count increment.
The pending receipt can survive category contention, the annual ceiling or capture until the same programme and site again satisfy the final gate; it cannot select another host, clear provenance uncertainty, create population or authorize another release/payment.
Accepted award consumes the pending receipt while retaining the historical release total.
Starting oversight deliberately abandons the saved programme and clears its pending receipt before changing programme/state; this grants no further release, payment or bonus.
Parent-owned terminal lifecycle must call the clear helper when deliberately abandoning a programme; it must preserve separate custody/occupation uncertainty and history.

```txt
# Country scope; choose only a currently open exact programme.
set_temp_variable = { camp_admin_start_program_input = constant:camp_admin_country_program.sov_engineer_release }
camp_admin_country_start_program = yes
# Existing monthly processing and finish dispatcher observe the saved site.
camp_admin_country_tick_institution = yes
```

Source scenarios and inspection limits are recorded in `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_country_civil_integration_2026-10-03.md`.
No new tuning constants, weighted values, icons or event targets are introduced by these gates.

## Authorization quote boundary

`camp_admin_country_can_commit` and `camp_admin_country_archives_available` read `political_power` and `num_equipment@support_equipment` with inclusive `check_variable` comparisons against their existing monthly/archive constants.
Exact quoted PP and support therefore permit authorization; a shortfall in either independently blocks it.
Authorization makes no immediate payment.
The monthly owner still performs the actual shared quote/payment checks against protected reserves and the remaining budget; these availability predicates do not promise that a later payment will succeed.
The bounded source cases exercise the actual predicates and action/start effects for exact funds, one-unit shortages and a missing resource separately.
