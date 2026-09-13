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
| `camp_admin_country_release_registered_prisoners` | Country, retained Soviet release policy | Registry of operational Gulag states; output `camp_admin_country_last_released_k` | Releases only surviving enrolled people in place; no army reserve or population creation |
| `camp_admin_country_start_oversight` | Country, native review decisions or deterministic AI | A free institutional slot and affordability checked by callers | Reserves the one slot for six paid months, then reduces national/legacy security authority |
| `camp_admin_country_start_archives` | Country, native aftermath decision or AI | `camp_admin_country_archives_available` | Reserves institution slot for six paid months; completion preserves records and contributes existing evidence pressure |

The GUI uses `GetCampAdminCountryAction1Name`, `GetCampAdminCountryAction2Name`, their tooltip functions, and `GetCampAdminInstitutionSummary`.
`camp_admin_research_progress` and `camp_admin_research_target` are read-only display copies of actual institutional progress and target.
Civil review and property-claims progress is copied after civil init/monthly/actions by `camp_admin_country_refresh_civil_institution_display`, and the summary selects civil activity before major-country status.
There are no routine popup events or new worldwide hooks.

## Internal program map

`camp_admin_country_start_program` receives a literal `PROGRAM` constant, selects an operational enrolled registered state, and saves its id in `camp_admin_institution_state_id`.
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
The Soviet release program records a technical-personnel subset of at most 0.5 thousand surviving detainees, then releases only the accepted finite receipt through `camp_admin_release_detainees`.
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
Protected forced-transfer membership is not used as a census source; the existing verified transfer path remains separate.

German camp headcount anchors and the later civilian forced-labor envelope are separate groups with distinct host roles.
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
Ordinary Soviet quota/famine-cycle missions are removed without executing their timeout/completion effects, and their legacy activations are disabled after initialization.
Distinct construction, review, crisis, evacuation, shutdown, records and reform decisions remain available under their existing phase gates.
The five legacy major-country instant percentage casualty calls are replaced by site initialization so finite monthly cause accounting owns physical losses.
Existing exceptional crisis events remain; normal paid administration is silent.

## Icons and future work

Native decisions reuse `GFX_decision_germany_ss_camp_administration`, `GFX_decision_japan_army_medical_review`, `GFX_decision_sov_gulag_expansion`, and `GFX_decision_sov_gulag_dismantlement` from `interface/camp_repression_rework.gfx` and existing `gfx/interface/camp_repression/icons/` DDS files.
No new portrait, art, sprite or event image is required by these helpers.
Potential future work is a separately accepted set of additional named industrial hosts with documented geography and independent cohort provenance.
Such additions must preserve the finite national receipts, funding, institutional slot and attribution rules rather than add demographic selectors or casualty-driven rewards.
