# Civil and colonial country kits handoff

Disposition: implemented owner module, pending parent integration acceptance and final MCP/probability evidence.
Acceptance basis: the user-authorized administration redesign recorded in `accepted_implementation.md`, the parent's explicit country ownership assignment, and the parent's accepted finite historical host-state membership abstraction.
No Git commit was made, as the parent explicitly requested.

## Files and ownership

New gameplay files:

- `common/script_constants/camp_administration_civil_constants.txt`
- `common/scripted_effects/camp_administration_civil_effects.txt`
- `common/scripted_triggers/camp_administration_civil_triggers.txt`
- `common/scripted_localisation/camp_administration_civil_localisation.txt`
- `common/decisions/camp_administration_civil_decisions.txt`
- `localisation/english/camp_administration_civil_l_english.yml`

Modified existing files:

- `common/scripted_effects/camp_repression_colonial_country_effects.txt`: foundation adapters, routine migration, no independent population-percent loss, no flat output grants, valid Vichy collaboration gates, narrow colonial subject authority and new idea bridge.
- `common/ideas/camp_repression_colonial_country_ideas.txt`: removes flat industry/construction/resource bonuses, preserves political burdens and adds domestic British custody/review and Congo strike ideas.
- `common/decisions/camp_repression_colonial_country_decisions.txt`: retires 37 duplicate routine choices after initialization and preserves six crisis/collaboration/aftermath choices and existing AI weight blocks.

Helper documentation is `common/scripted_effects/camp_administration_civil_effects.md`.
Task evidence is `civil_retired_candidates.json`, `civil_scenarios.py` and `civil_scenario_results.json` in this directory.
No event file, asset, shared hook, GUI, core accounting, registry definition or major-country implementation was created or edited by this owner.

## Exact integration contract

The major-country owner already routes the civil callbacks through the public country wrapper.
The parent must retain the following execution order in its existing bounded registry loop:

1. `camp_administration_civil_initialize` through `camp_admin_country_initialize`.
2. `camp_administration_civil_prepare_monthly` through `camp_admin_country_prepare_monthly`, before the foundation monthly cohort/economy pass.
3. Foundation monthly processing prepares and pays maintenance, support and automatic economic work.
4. `camp_administration_civil_monthly` through `camp_admin_country_monthly`, after foundation budget preparation.

The prepare and monthly callbacks have separate once-per-calendar-month guards using `camp_admin_prepare_month_key`.
The integration owner runs the complete sequence, including preparation and the legacy tail, through hidden recipient-country event `camp_administration_country.1`.
Civil prepare/monthly callbacks require `tag = ROOT` and fail closed without that recipient-country boundary.
The reused legacy registration helpers therefore receive the actual actor ROOT; narrow subject authorization itself derives its actor from immutable state responsibility.
Keep a country registered while `camp_admin_civil_policy_authorized`, `camp_admin_civil_review_active` or `camp_admin_civil_claims_active` remains set, or while the foundation still has civilian replacement work; an empty active custody registry must not stop paid reform work.
Use `camp_administration_civil_cleanup` on terminal national cancellation, after foundation/occupation closure, rather than resetting lifetime cohort variables.
`camp_administration_civil_cancel_routine_projects` is independently callable and removes seven timers without calling their success effects.
Every national civil reform calls `camp_occ_close_country` before `camp_admin_begin_reform`; no state-only GUI reform behavior is changed here.

Country support is `camp_administration_civil_country_supported` for ENG, RAJ, USA, FRA/VIC, ITA and BEL/COG.
The two GUI callbacks are `camp_administration_civil_action_one` and `camp_administration_civil_action_two`, with separate matching `_visible` and `_available` triggers.
The major-country wrappers nest `GetCampAdministrationCivilActionOne` / `GetCampAdministrationCivilActionTwo` and `camp_administration_civil_action_one_tt` / `camp_administration_civil_action_two_tt`.
Action visibility reflects date, government and lifecycle; authorization itself is free, while subsequent months require the exact shared quote/payment contract.
AI budget choices separately request `camp_admin_set_budget` through `camp_administration_civil_choose_ai_budget` and temporary `camp_admin_control_requested`, using the same quote, validation and PP debit as human budget commands.
The requests occur only on explicit authorization/review actions, never as repeated monthly policy changes, and do not refill the current monthly allowance.
Human budget choices remain unchanged.
Development pause prevents further host/intake expansion and AI budget changes; committed administration, review and property claims continue their paid installments.
The two AI decisions invoke exactly these callbacks, so the policy does not depend on human GUI clicks.

The first eligible policy is visible without an active site.
Once the policy has received its first monthly payment, `camp_administration_civil_open_next_host` chooses at most one qualifying host per monthly prepare pass through the existing registration helper.
The temporary country pointer is `camp_admin_civil_next_host_id`; it is cleared after the attempt.
`camp_administration_civil_host_state` is the host gate; candidate selection uses controlled eligible geography, never pressure or a population identity selector.
The automatic host gate allows direct control and only the explicit Belgian-subject COG exception in Congo.
The existing-site authorization helper additionally recognizes previously assigned British responsibility in British-subject RAJ; those sites do not enter the British domestic cohort.
Foundation must require `camp_admin_subject_authority` for subject-controlled sites, and validate that current controller remains the immutable responsible country's subject.

## Implemented country behavior

| Country | Institution and transition | Distinct consequences |
|---|---|---|
| Britain | Wartime civilian-government domestic internment from 1940-05-16; tribunal release/review, AI review from August 1940 | British core hosts, custody-only role, domestic review ideas; no Raj or 1950s Kenya population source |
| Raj | British-subject wartime political detention from September 1939; local works and negotiated release; independence terminates colonial custody | Labor burden, accumulating resistance, actual autonomy movement and a funded settlement |
| USA | Democratic wartime incarceration from 1942-02-19 to 1944-12-18; release/court review; property claims from 1948-07-02 | Custody-only role and no productive labor allocation; civil-liberties harm, court pressure and disrupted livelihoods; six paid claims months |
| France/Vichy | February 1939 refugee internment, distinct July 1940 Vichy authority, North African labor, valid late collaboration records, Free French/liberation assistance | Separate regional burdens and roles; existing secondary responsibility records retained; reform uses civilian replacement capacity |
| Italy | Inherited colonial legacy from start, actual wartime sites from June 1940, occupation and forced labor, loss of Italian authority on capture | Libya/East Africa/Balkans geography; subsequent German actions require their own responsible authority and parent German/occupation package |
| Belgium/Congo | Valid Congo concession administration, extraction and transport, labor strikes, negotiated reform | Live supported workforce and actual opportunity determine output; strike halves participating-site scale; funded civilian conversion retains completed infrastructure |

No ordinary monthly event or popup was added.
Legacy crisis choices remain available for extraordinary consequences, including strike suppression/settlement, refugee assistance/suppression, collaboration records and local administration recognition.
The exact retired decision IDs are recorded in `civil_retired_candidates.json` for the probability auditor.

## Population, spending and cleanup

The parent accepted explicit membership among civilians already represented at a historical host as a geographic abstraction.
This does not model physical relocation, debit an originating state, create population, infer detention from unrest, or expose a protected-group selector.
Host declarations survive release, deaths, closure and capture, and each national cumulative admission ceiling can be used only once.
Foundation admission also subtracts occupation membership and validates actual uncommitted civilians and physical capacity.
Only its returned `camp_admin_admission_accepted_k` is consumed from the civil source budget.
Actual legacy violence requests a tuned fraction of surviving detainees through `camp_admin_record_deaths`; the foundation's exact receipt is the sole physical loss path.
No old civilian-population-percent burst remains in the four touched colonial site adapters.

All civil costs and durations reside in `camp_administration_civil_constants.txt`.
Administration costs 10 support equipment and 5 PP per funded month; review costs 15 support and 8 PP for three funded months; claims cost 10 support and 12 PP for six funded months.
There are only two resource types and no separate debit implementation.
The foundation reserve and spending ceiling can pause a program without partial progress.
Economic works use the independent foundation slot and payment rules.
Legacy works migration preserves one valid selected location but credits zero elapsed legacy timer time because that time proves no foundation payment.
That timing difference is explicit; completion never grants an immediate old flat infrastructure reward through the migrated adapter.
Built infrastructure and immutable responsibility records survive reform.

## Historical anchors

British internment and release records are anchored in the [UK National Archives internees guide](https://www.nationalarchives.gov.uk/help-with-your-research/research-guides/internees/), its [Arandora Star account and release records](https://www.nationalarchives.gov.uk/explore-the-collection/stories/the-loss-of-ss-arandora-star/) and [Kindertransport education collection](https://www.nationalarchives.gov.uk/education/resources/kindertransport/).
The represented British ceiling of 27,000 uses the approximate German/Austrian internment scale in the [Imperial War Museums Second World War Galleries text](https://www.iwm.org.uk/sites/default/files/files/2023-10/second_world_war_galleries_large_print.pdf); it is not asserted to include every category of British internee.

US authorization and the approximate 120,000 national incarceration scale follow the [National Archives Executive Order 9066 collection](https://www.archives.gov/milestone-documents/executive-order-9066).
Court review uses the [National Archives court records guide](https://www.archives.gov/research/aapi/ww2/courts).
The July 2, 1948 property-claims boundary follows the [National Archives Japanese American genealogy guide](https://www.archives.gov/research/aapi/ww2/genealogy); the later [NPS Civil Liberties Act account](https://www.nps.gov/miin/learn/historyculture/civil-liberties-act.htm) keeps the 1988 redress program distinct.

Raj detention, wartime political conflict and autonomy consequences follow the [National Archives Indian independence collection](https://www.nationalarchives.gov.uk/education/resources/indian-independence/), [Gandhi meeting ban documents](https://www.nationalarchives.gov.uk/education/resources/indian-independence/gandhi-meeting-ban/) and [Cripps/Nehru/Gandhi records](https://www.nationalarchives.gov.uk/education/resources/indian-independence/cripps-nehru-gandhi/).
These sources establish the political context; they do not substantiate the module's exact 60,000 national tuning ceiling.

The French transitions and geographic distinctions follow USHMM's [Gurs account](https://encyclopedia.ushmm.org/content/en/article/gurs) and [labor and internment camps in North Africa](https://encyclopedia.ushmm.org/content/en/article/labor-and-internment-camps-in-north-africa).
Italian wartime and later German authority distinctions follow USHMM's [Italy account](https://encyclopedia.ushmm.org/content/en/article/italy), [Axis invasion of Yugoslavia](https://encyclopedia.ushmm.org/content/en/article/axis-invasion-of-yugoslavia), and the North Africa source's separate account of Giado.
Those sources support institutional/geographic separation; source counts from different institutions are not added together into a false national total.

Wartime Belgian colonial authority and economic commitment follow the Belgian State Archives/CegeSoma [Albert De Vleeschauwer account](https://www.cegesoma.be/en/albert-de-vleeschauwer) and [Battle of Saio historical account](https://www.belgiumwwii.be/belgique-en-guerre/articles/bataille-de-saio-la.html).
The strike and concession mechanisms preserve the existing country kit; the exact 40,000 represented labor-cohort ceiling is a finite tuning bound, not a verified wartime national incarceration census.

## Validation and remaining completion requirements

`civil_scenarios.py` evaluates selected actual current script branches with a restricted interpreter and explicit native fixtures.
The final owner run passed 26 scenarios against the updated foundation and shared budget command.
Its companion JSON records date/regime gates, French authority distinctions, US claims timing, twelve monthly finite admissions without population creation, capture, subject-control restrictions, actual survivor release/idempotence, national lifetime intake exhaustion, terminal mission cancellation and protected-reserve/shared-payment scenarios.
This is source-driven scenario evidence, not an engine simulation or a complete twelve-month national economy/GUI playthrough.
The additional contract cases verify paid/unaffordable AI budget changes, unchanged human choices, unchanged paused budgets, no second debit for an identical budget, no allowance replenishment, rejection of a wrong monthly ROOT, continued committed review/claims during development pause and blocked expansion during that pause.
GUI refresh and history presentation calls are explicit fixtures in these command tests; the actual command quote, eligibility, PP debit and budget assignment are evaluated from current source.
The owned colonial monthly bridge remains bypassed after civil initialization; the four site adapters contain no direct population-percent or independent death accounting path, and the sole civil violence adapter calls the foundation receipt helper.
An AST comparison against the preserved baseline found the existing `ai_will_do` subtrees unchanged across 62 legacy decision/mission definitions and confirmed all 37 retirement gates.
All civil/foundation helper references used by the owned files resolve, and every civil scripted-localisation selector resolves to a supplied localisation key.

The initial exact event MCP request was `hoi4_event_inspect` with mode `scan`, selector path `common/scripted_effects/camp_repression_colonial_country_effects.txt`, `maxNodes: 40`, `maxDepth: 1`; it timed out after 180 seconds.
The initial GUI inspection lacked required `scenario` and returned a validation error; a corrected `repression_ledger_window` request was stopped when the parent took exclusive ownership of the serialized MCP queue.
No substitute source check is claimed as GUI/event engine evidence.
Parent-owned GUI inspect/render/compare and final decision-probability compare remain required.
The probability owner has the preserved legacy baseline plus an absent-file baseline for the two new civil AI decisions; existing AI weights were not retuned.
The parent authorized retiring the 37 duplicate candidates after baseline preservation and attempted inspection, while retaining the mandatory same-scenario final comparison requirement.

The parent must review current wrapper routing, registry retention after all detainees are released, narrow foundation subject authorization, final French collaboration attribution and the major German post-capture branch.
Live-game validation belongs to the user; this worker did not launch the game.

## Simplifications, omissions and blockers

- Raj, French, Italian and Congo national intake ceilings remain conservative represented-cohort tuning bounds, not fully sourced national historical calibrations.
- Host-state membership is an explicitly parent-accepted geographic abstraction; exact historical relocation and originating-region population debits are not implemented by this module.
- French collaboration retains responsibility records but adds no physical inter-state deportation route; that would require a separate accepted transfer contract.
- Later German persecution is a parent German/occupation integration requirement, rather than a civil helper reassigning Italian responsibility.
- Migrated legacy timers retain their selected target but not unproved paid-month credit.
- Required final MCP/probability evidence and integrated national economic scenario acceptance are pending; owner source checks do not prove these surfaces complete.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`.
No skill was created or changed by this owner.
Existing idea pictures and vanilla `generic_political_discourse` are reused; no new image asset is required.
