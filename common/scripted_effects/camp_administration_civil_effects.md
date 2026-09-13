# Civil and colonial administration

Status: implemented owner module; final integration, MCP and probability acceptance belong to the parent.
Acceptance basis: the 2026-09-06 accepted administration implementation and parent assignment for ENG, RAJ, USA, FRA/VIC, ITA and BEL/COG.
The parent explicitly accepted historical host-state cohort membership as an abstraction within the user-authorized design on 2026-09-06.
This abstraction records membership among civilians already present at a host, with no claim of a real state-to-state relocation, no source-state debit and no population creation.

## Public helper map

| Helper | Scope and inputs | Output and side effects | Call sites |
|---|---|---|---|
| `camp_administration_civil_initialize` | Supported country | Idempotent lifetime intake ceiling and counters; publishes tooltip costs; migrates existing infrastructure target and removes routine legacy timers | Parent country initializer, action callbacks, monthly callbacks |
| `camp_administration_civil_prepare_monthly` | Country, before foundation monthly | Once per calendar month: ends invalid authority, closes national occupation contract, releases surviving detainees through foundation reform, opens one qualifying host and admits finite cohorts only if previous monthly policy funding succeeded | `camp_admin_country_prepare_monthly` |
| `camp_administration_civil_monthly` | Country, after foundation maintenance and economic processing | Once per calendar month: shared quote/payment for administration, review and claims; pressure and idea updates | `camp_admin_country_monthly` |
| `camp_administration_civil_action_one` | Country, `action_one_available` | Authorizes appropriate national institution, registers bounded recurring country processing; AI selects development budget; no immediate equipment or PP debit | Parent GUI dispatcher and `camp_admin_civil_authorize_policy_ai` |
| `camp_administration_civil_action_two` | Country, `action_two_available` | Immediate survivor release/reform or dated US property-claims work; paid institutional progress; AI selects priority budget | Parent GUI dispatcher and `camp_admin_civil_review_policy_ai` |
| `camp_administration_civil_open_next_host` | Authorized country, previous paid policy flag | At most one unassigned controlled/subject-controlled eligible host; uses existing registration and foundation initialization; transient `camp_admin_civil_next_host_id` is cleared | Prepare callback |
| `camp_administration_civil_admit_host_cohort` | Eligible operational state with ROOT country | Consumes only `camp_admin_admission_accepted_k` from local remaining membership and national cumulative admission room | Prepare callback's bounded active-state loop |
| `camp_administration_civil_classify_host` | State with ROOT country | Custody/labor role and persistent geographical responsibility labels; USA has custody role and a two-percent economic scale ceiling | Admission helper |
| `camp_administration_civil_authorize_subject_site` | State with immutable existing responsibility | Sets `camp_admin_subject_authority` only for Belgian-administered Congo controlled by Belgian-subject COG or British-administered Raj controlled by British-subject RAJ; resolves responsibility directly without ROOT | Initializer's bounded existing registry and colonial registration before foundation initialization |
| `camp_administration_civil_record_legacy_violence` | Operational state under valid authority | Requests a centrally tuned fraction of surviving detainees as violence; foundation produces actual receipt and all physical accounting | Existing colonial major-harm adapter |
| `camp_administration_civil_migrate_projects` | Country | Transfers one valid pre-existing works target into the foundation economic slot and removes the legacy timer; begins with zero proved paid months | Initializer |
| `camp_administration_civil_cancel_routine_projects` | Country | Removes seven routine timers and their target references without invoking completion outcomes | Migration, review, authority loss and cleanup |
| `camp_administration_civil_cleanup` | Country at terminal lifecycle | Cancels routines and active policy/review/claims flags; clears transient progress and retains cumulative admissions and source-membership records | Parent terminal cleanup |
| `camp_administration_civil_refresh_pressures`, `camp_administration_civil_refresh_ideas` | Country | Actual cohort burden, separate French regional burdens, Raj autonomy pressure, Congo strike penalty and British domestic ideas | Monthly callback; legacy idea refresh delegates the idea helper |
| `camp_administration_civil_finish_review` | Country after required paid months | Terminal review flag, country-specific settlement, Raj autonomy adjustment, concession reform, court result | Monthly callback |
| `camp_administration_civil_quote_policy` | Country | Temporary `camp_admin_quote_support` and `camp_admin_quote_pp`, consumed by `camp_admin_try_pay_project` | Monthly callback |
| `camp_administration_civil_choose_ai_budget` | Country; temporary `camp_admin_control_requested` | Requests the shared `camp_admin_set_budget` command only for unpaused AI; consumes the same quote and PP payment as GUI/decision commands and never refills a monthly allowance | One-time policy authorization/review callbacks |

The exact shared inputs are `camp_admin_admission_requested_k`, `camp_admin_admission_source_k`, `camp_admin_admission_proven`, `camp_admin_quote_support`, `camp_admin_quote_pp`, `camp_admin_death_requested_k`, `camp_admin_death_cause` and `camp_admin_death_contract`.
Shared outputs are `camp_admin_admission_accepted_k`, `camp_admin_payment_accepted` and `camp_admin_death_actual_k`.
The foundation validates physical civilians, occupation membership exclusion, capacity, protected stockpile reserves, budget availability, responsibility and current authority.
No civil helper modifies the shared Deaths core or directly changes civilian population.

## Controls and presentation

`camp_administration_civil_country_supported` is the country routing trigger.
`camp_administration_civil_action_one_visible` and `camp_administration_civil_action_two_visible` hide future dates and invalid governments.
Matching `_available` triggers additionally require an unoccupied institutional slot.
Authorization is a policy choice rather than an upfront purchase; monthly work proceeds only after the shared payment accepts the quoted costs.
Human budgets are retained; AI requests a development ceiling for administration and a priority ceiling for review through the shared paid budget command.
Unaffordable requests leave the budget unchanged, and an already selected budget causes no second payment.
No monthly callback repeats or oscillates those policy choices.
Development pause prevents additional civil hosts/intake and AI budget changes; already committed administration, review and claims installments continue using their existing shared monthly envelope.

Scripted names are `GetCampAdministrationCivilActionOne` and `GetCampAdministrationCivilActionTwo`.
Tooltips are `camp_administration_civil_action_one_tt` and `camp_administration_civil_action_two_tt`.
Country explanation selectors are `GetCampAdministrationCivilAuthorityText` and `GetCampAdministrationCivilReviewText`.
Costs are cached from script constants by the initializer and displayed only in tooltips.
The module creates no routine events or popups.

## Country distinctions

British domestic internment requires wartime civilian government from 1940-05-16 and uses directly controlled British core locations.
It never admits Raj civilians into the British domestic cohort.
Tribunal review releases surviving internees and uses civilian employment conversion.
AI tribunal review opens from August 1940, rather than retaining mass internment until the end of the war.

Raj political detention requires British subject status, wartime authority and a British civilian government from September 1939.
Its local works role, accumulating autonomy resistance, actual autonomy movement and negotiated settlement remain separate from British domestic internment.
Indian independence terminates colonial custody authority.

US incarceration requires democratic wartime government from 1942-02-19 until 1944-12-18.
Custody provides no industrial labor allocation.
Civil-liberties pressure, court challenges and disrupted livelihoods persist through their respective stages.
Court review releases survivors; property claims require democratic government from 1948-07-02, prior incarceration or outstanding claims, and six funded months.
The 1948 claims abstraction is not the 1988 redress program.

French refugee internment is a pre-Vichy institution from February 1939, with the Vichy authority branch gated separately from July 1940.
North African labor uses a distinct state role and pressure total.
Vichy collaboration records retain the existing second-responsible-country mechanism and require fascist Germany after July 1942.
Free France and restored democratic government cannot continue Vichy authority.
Release and refugee assistance use the foundation's real civilian-employment replacement.

Italy retains an inherited colonial-legacy flag from the 1936 start but does not activate the wartime institution before 1940-06-10.
Wartime mainland, Libyan, East African and occupied Balkan hosts remain geographical branches.
German seizure invalidates current Italian control; the original Italian records are not reassigned to Germany.
Later German persecution is handled through the parent capture/occupation and German country package, with German responsibility for its own subsequent actions.

Belgian/Congolese concession administration uses only the Congo geographical pool and valid Belgian authority or a Belgian-subject Congo.
Current detainees, support, local extraction opportunity and transport determine economic contribution.
Accumulated labor burden creates an actual strike penalty that halves the participating site's economic scale.
Negotiated review releases survivors, funds civilian employment and settles the concession dispute; completed transport infrastructure remains.

## Central tuning and source membership

All civil tuning lives in `common/script_constants/camp_administration_civil_constants.txt`.
Standard monthly administration costs 10 support equipment and 5 PP; review costs 15 support and 8 PP for three funded months; claims cost 10 support and 12 PP for six funded months.
Foundation maintenance, protected reserves and remaining budget are checked before any such payment.
An exhausted budget pauses progress without granting partial success.
The institution slot remains occupied during review or claims and is released on completion or terminal cancellation.

The national admission ceilings are 27,000 British internees, 60,000 Raj detainees, 120,000 US incarcerated civilians, 30,000 French detainees, 10,000 Italian detainees and 40,000 Congo labor detainees.
These are conservative finite gameplay cohort ceilings, not asserted national census totals, fatality totals or historical quotas.
The approximate US incarceration scale is anchored to the documented national total; the British ceiling uses the Imperial War Museums' approximately 27,000 German and Austrian internees as a represented cohort scale.
The other ceilings are tuning bounds for represented host membership and require further calibration if exact national historical counts are demanded.
Each host has at most 10,000 declared members and accepts at most 2,000 per funded month, further reduced by foundation physical and capacity checks.
The nation cannot re-use admission capacity after release or deaths.
The location cannot replenish declared membership after closure, reopening or capture.
Names of protected populations are not exposed as player selectors.

## Migration, event targets and cleanup

The immutable state source-membership flag and remaining quantity survive all terminal paths.
Country admission totals are initialized once and never reset by cleanup.
The temporary candidate host pointer is always cleared after the registration attempt.
No global event target is added.
The entire monthly callback chain must run in the recipient-country `camp_administration_country.1` event supplied by the integration owner, so ROOT is the administering country rather than the global pulse host.
Both civil monthly callbacks fail closed when the current country differs from ROOT.
This boundary also makes the reused legacy `camp_rework_colonial_register_current_state` and `camp_rework_register_active_site` ROOT contract valid for automatic registration.
The existing state responsibility variable and foundation immutable country pointer retain attribution.
The foundation's actor event target is chain-scoped and used only through its public APIs.

Routine legacy decisions retire after `camp_admin_civil_initialized`; the exact 37 candidate IDs are in the task's `civil_retired_candidates.json`.
Six crisis/collaboration/aftermath choices remain, and legacy AI weight values are unchanged.
The old monthly colonial bridge is bypassed after initialization so it cannot re-open routine missions or overwrite the new monthly burden calculation.
Legacy country ideas retain social/political burdens but no flat industry, construction or resource bonuses.
Old minor-project completion places a works project into the paid foundation slot instead of granting an instant infrastructure level.
The migration preserves a valid selected infrastructure target, but elapsed legacy timer time grants no unproved paid foundation progress.
That deliberate migration rule is recorded here as an implementation difference rather than disguised as identical timing.

## References and validation limits

Required offline references consulted: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Scripted GUI modding and Interface modding.
Vanilla references consulted: `documentation/script_concept_documentation.md` Script Constants; `common/script_constants/documentation.md`; effects documentation for variables, autonomy, mission removal, state buildings and event targets; triggers documentation for control, subjects and event targets; `common/scripted_effects/ENG_scripted_effects.txt` autonomy adjustment precedent; and `common/scripted_localisation/00_scripted_localisation.txt` native `localization_key` spelling.
The existing shared dynamic-effect registry was checked; this module uses owner-specific foundation APIs rather than adding a shared helper without unrelated consumers.

Historical anchors are documented in the task handoff.
The task's `civil_scenarios.py` evaluates actual current source for selected date, government, finite-membership, reserves, payment, cancellation and release scenarios.
It is a restricted script interpreter with explicit native fixtures, not HOI4 runtime evidence.
The initial narrow event MCP inspection timed out after 180 seconds.
Parent-owned GUI MCP and the probability auditor's final same-scenario compare remain completion requirements.

## Assets and future work

New British ideas reuse `uk_imperial_detention_administration`; the Congo strike idea reuses `bel_congo_extraction_pressure`.
Those picture families already exist in the colonial idea/GFX package.
AI-only decisions use vanilla `generic_political_discourse`; no new raster asset or sprite registration is required.
Future calibration can replace the conservative Raj, French, Italian and Congo cohort ceilings with sourced institution-by-institution membership bounds and site-specific mortality evidence without changing the admission or physical loss contract.
Exact state-to-state relocation remains outside this accepted host-membership abstraction.
