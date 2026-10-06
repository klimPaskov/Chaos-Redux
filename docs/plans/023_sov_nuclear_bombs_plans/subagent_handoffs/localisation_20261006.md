# Event 023 localisation handoff, 2026-10-06

Disposition: implemented text, with parent gameplay integration and visual validation outstanding.
Acceptance basis: parent bounded assignment and subsequent explicit new-key semantics in this session.
No gameplay files, shared framework, workbook, CSV exports, desktop, game, or commits were changed by this worker.

## Changed files and dynamic text

- `localisation/english/023_soviet_nukes_l_english.yml`
- `localisation/english/023_sov_nuclear_bombs_requirement_flags_l_english.yml`
- `common/scripted_localisation/023_sov_nuclear_bombs_scripted_localisation.txt`
- This handoff.

News 231 names the threatened state and government through `SOV.sov_nuclear_bombs_news_threat_state/country`.
News 232 names the struck state and government through `SOV.sov_nuclear_bombs_news_strike_state/country`.
Parent must capture those normal pointers only when scheduling the corresponding first news, including native and legacy detonation confirmation paths.
`GetSovietNuclearBombsPublicTestPresentation` reads `SOV.sov_nuclear_bombs_news_test_presentation`.
`GetSovietNuclearBombsLastTestPresentation` reads `sov_nuclear_bombs_last_test_presentation`, which parent must capture for each completed public-test receipt and clear for secret tests.
Report 185 describes a confirmed public-test yield, returns the chosen presentation, and displays current Readiness without colours.
Both return plain paragraph text and use the three `sov_nuclear_bombs_closure.presentation_*` constants, with an empty default.
`GetSovietNuclearBombsCommandDevelopmentName` and `GetSovietNuclearBombsCommandDevelopmentDescription` select doctrine-specific decision text from the existing custody variable.
`GetSovietNuclearBombsDoctrineDevelopmentNote` adds a completed-development note to all seven existing posture spirit descriptions.
The parent owns clearing all four development flags on doctrine reform.
Party development uses the confirmed `sov_nuclear_bombs_closure_factor.party_mobile_loss` percentage rather than hardcoded prose.
New maintenance text uses closure constants for duration, Readiness loss, Integrity gain, protection period, and cooldown.
`sov_nuclear_bombs_service_arsenal_tt` shows controlled reactors and the current assembly quote.
Parent must prepare those values in the display scope.

## Prose before and after

- Vagueness: selected government and target in news 231/232 become named government and state.
Retaliation and breakaway news identify commanders, technicians, guards, and the work required.
- Bloat: the stockpile audit, counterintelligence sweep, reform, and limited-strike descriptions keep requirements and consequences with fewer repeated clauses.
- Obvious explanation: redundant Prepare/Choose wording was removed from long test-action names and the active status no longer points players to the event ledger.
- Repetition: stockpile and counterintelligence text no longer restate the same accounting or knowledge result.
- Overcomplication: breakaway command and delivery descriptions name officers, crews, devices, and a route rather than command-formation or delivery-integration stages.
The coercion selector tooltip states the real requirement and the later bomber-range check.
- Style repair: sentence semicolons were replaced with periods throughout the assigned main file.
The stand-down offer and review no longer expose a verification number or its internal counter.
The requirement reads The Soviet atomic stockpile has been registered.
A grammar defect in the populated-target enemy-use flag was repaired.

Existing dynamic values and meaningful requirements were preserved.
The nonce token was deliberately removed from visible prose only, with no script-state change.
No attributed or sourced quotation was edited.
The inherited `chaosx_super_event.108.q` quotation was inspected and verified identical to HEAD, including punctuation. Its attribution was not re-researched, and no quotation wording was altered.

## G1, G2, and G3 evidence

G1: `python .tools/report_colour_audit.py --event 023` returns `total keys with colour: 0` after the initial and presentation/development patches.
The audit traverses report/news descriptions and reachable scripted localisation.
G2 read-only source findings were sent to parent: exposure reports coalesce behind `sov_nuclear_bombs_exposure_report_pending`, cleared by report 107.
Secrecy incidents share `sov_nuclear_bombs_incident_cooldown`.
Major foreign strategic reports use one-time per-stage dispatch.
News 232 has a first-use guard.
Baseline news 230 fired for every public demonstration, news 231 for every ultimatum, and news 233 for later combat uses in both legacy and native confirmation paths.
Those three paths need parent-owned first-news guards to prevent global repeated reports.
The report_seen flags on 101, 102, 106, and authorization reports are receipts, not independent anti-spam gates.
Player-selected operation reports should retain their actual outcome receipts.
G3: assigned prose was read manually and changed where weak.
No sentence semicolons or em dashes remain in the assigned localisation files.
In-world ledger wording remains where it names physical accounting rather than implementation.

## Coverage and checks

Missing scripted output keys: none.
Duplicate keys in either assigned localisation file: none.
Missing assigned custom getters: none.
Native `GetName` and `GetNameDef` are engine accessors, not absent defined_text helpers.
Existing files retain UTF-8 BOM and one key per line.
Scripted localisation branches use existing or parent-confirmed variable, constant, and flag identifiers.
Popup and tooltip key references in both `events/023_soviet_nukes.txt` and the parent's new `events/023_sov_nuclear_bombs_closure.txt` were checked: no missing keys. The parent must still verify decision, receipt, and mission integration after its full patch lands.

The main Event Details description was left unchanged, so no catalog detail wording handoff is needed from this patch.
The changed active status is a dynamic status suffix rather than catalog description text.
No spreadsheet comparison was made because workbook access was excluded from this assignment.

## Reference and MCP evidence

Read AGENTS.md, events, decisions/missions, and subagents skills.
Offline Localisation wiki Namespaces, lines 531-555, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, confirms scoped variables and target name namespaces.
Path: `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`.
Installed script concept documentation Using a localization object, lines 134-140, revision `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`, confirms chained object property syntax.
Path: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`.
The initial loc_objects context resolved only a title section and was not treated as substantive syntax evidence.
Vanilla precedent: `localisation/english/aat_events_l_english.yml:6` uses `[FROM.GetName]`, and `aat_decisions_l_english.yml:39` uses `[121.owner.GetName]`.
Offline Event modding wiki lines 29, 32, and 149 distinguish recipient ROOT, sender FROM, and major-news broadcasting.
This was read directly when checking successor-news scope and sent to parent.

Connected event inspect and render routes are healthy enough to return partial results.
The live selector requires `{kind: event, eventId: ...}`.
A bounded lint for `chaosx.nr23.163` returned `EVENT_INSPECTED_PARTIAL`, revision `3eacffa45860dba3e66b6bce34d52e3370164de7ff6c0cb291f3206b359173cc`, graph hash `184339ba0021043259f0493c01b90a2ccdf0fea902c3efdae20ff1a23e6cdde6`.
Its aggregate result reported one blocking chain diagnostic and incomplete coverage, so it is not a clean event-lint claim.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/490000321c4d0ef6c90a0c3cd65ff16d380125b5479d2312b59d743620408eb3/88d4c11f0334e796c339cc858a9331352fab6e747d83981d0f93cac92578cea3/event-lint-3eacffa45860.json`.
Options render returned `EVENT_RENDERED_PARTIAL`.
Authoritative JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/91dc39e945f93799963c3c311263fabc9347796f799edc79a467a92362324537/08cd39e4abe355aa0385e0693761d95ad8456eb8a730cf630f8e842c31349467/event-options-3eacffa45860.json`.
Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/595b56f3a7cfd0c3512d69a06401df75ebced09c6d48ef9cbc5d346b80b79d05/b4df17220c04992ff63f56917efdbeeb42144db0934028f391f3e6588f3b4b44/event-options-3eacffa45860-manifest.json`.
The event render is a source-linked chain view, and does not establish parchment popup wrapping or overflow.
The MCP resource listing was empty, so this worker has not read the artifact's full diagnostic payload.
A read-only `hoi4.event_compare` for event 163 did not return within the bounded waiting period. The waiting cell was terminated. No comparison result or comparison coverage is claimed.
No standalone Technology Tree Viewer is exposed in the connected tool inventory.
This is a viewer package gap, not a claim that exposed tech routes are absent or broken.
No technology, focus, or map surface was edited in this bounded assignment.
Shared GUI layout inspection and visual overflow proof remain parent-owned and unverified here.

## Remaining integration and validation limits

- Parent gameplay receipt capture, constants, flags, mission/decision wiring, and first-news guards must match the identifiers listed above.
- Successor news 236 names `sov_nuclear_bombs_news_successor_actor` and `sov_nuclear_bombs_news_successor_state`. Parent confirmed these are regular event targets saved inside the successor mission callback and transported to the delayed news. This avoids guessed ROOT or FROM names.
- Event184 keys supplied: `.t`, `.d`, `.absent.d`, `.active.d`, `.unavailable.d`, `.a`.
- Visual fit of popup descriptions and the shared Event Details status is not proven by the chain render.
- MCP comparison remains without a result, and relevant full-artifact diagnostics require parent review.
- No balance weights were edited or audited by this localisation worker.
- No design expansion or simplification was introduced by this patch.

## Changed key wording

### localisation/english/023_soviet_nukes_l_english.yml

- `chaosx.nr23.101.success.d`: The test produced a confirmed atomic yield. Engineers have verified the readings, and the spent device has been removed from the arsenal.\n\nArsenal Readiness: [?sov_nuclear_bombs_last_test_readiness_change|+=0][GetSovietNuclearBombsTestRepeatNote][GetSovietNuclearBombsLastTestPresentation]
- `chaosx.nr23.101.partial.d`: The test produced only a partial atomic yield. The device is spent, and the weak result has shaken confidence in the arsenal, though the engineers learned something from it.\n\nArsenal Readiness: [?sov_nuclear_bombs_last_test_readiness_change|+=0][GetSovietNuclearBombsTestRepeatNote][GetSovietNuclearBombsLastTestPresentation]
- `chaosx.nr23.101.failure.d`: The atomic test produced no yield. The device is spent, and the command board must investigate the failure before another test.\n\nArsenal Readiness: [?sov_nuclear_bombs_last_test_readiness_change|+=0][GetSovietNuclearBombsLastTestPresentation]
- `chaosx.nr23.102.accident.d`: The test accident produced an atomic yield. The blast damaged the test site, and crews are securing the contaminated area as investigators examine how the safeguards failed.[GetSovietNuclearBombsLastTestPresentation]
- `chaosx.nr23.104.d`: The device's conventional explosives detonated during test preparation without producing an atomic yield. Crews are securing contaminated debris and accounting for the dead. The ruined device has been removed from the arsenal.[GetSovietNuclearBombsLastTestPresentation]
- `sov_nuclear_bombs_reinforce_depot_desc`: Send a garrison, engineers and supplies into the selected depot while a Soviet force holds its state. Command Integrity rises by [?constant:sov_nuclear_bombs_breakaway.reinforce_integrity|0], and for [?constant:sov_nuclear_bombs_breakaway.garrison_days|0] days the holder cannot begin technical access there. Work already under way takes [?constant:sov_nuclear_bombs_breakaway.garrison_delay_days|0] days longer. Each depot can be reinforced once.
- `sov_nuclear_bombs_warning_act_tt`: Command Integrity [?constant:sov_nuclear_bombs_false_warning.act_integrity|+=0]. The command moves to the retaliation board under the emergency first-use rules. A target still has to be marked, prepared, certified and finally authorized before anything is released.
- `chaosx.nr23.161.d`: The hotline pause has reached its review date. The command board must confirm that both nuclear powers agreed to suspend release orders and kept their command authorities intact throughout the pause.
- `chaosx.nr23.163.d`: Moscow has suspended its release orders and asks us to do the same. Both sides must keep their command authorities intact throughout the pause. Refusal returns the hotline to crisis footing.
- `chaosx.news.230.d`: A Soviet atomic demonstration has made the arsenal visible to the world. The remote blast proves that Soviet delivery crews can release a working weapon, and every major government is reassessing its air defenses and war plans. [GetSovietNuclearBombsPublicTestPresentation]
- `chaosx.news.231.d`: The Soviet Union has issued an atomic ultimatum to [SOV.sov_nuclear_bombs_news_threat_country.GetNameDef], naming [SOV.sov_nuclear_bombs_news_threat_state.GetName] as its target. Diplomats are seeking a settlement as military staffs prepare for a strike.
- `chaosx.news.232.d`: A Soviet atomic weapon has detonated in [SOV.sov_nuclear_bombs_news_strike_state.GetName], striking [SOV.sov_nuclear_bombs_news_strike_country.GetNameDef]. Fallout spreads beyond the blast zone as casualty lists grow. Foreign governments condemn the attack, and military staffs prepare for retaliation.
- `chaosx.news.233.d`: Nuclear powers are preparing retaliation after a confirmed strike. Commanders must choose between a limited response, keeping weapons in reserve, talks on the emergency hotline, and a wider exchange. Fallout spreads from each blast as people flee the affected cities.
- `chaosx.news.234.d`: A breakaway authority has seized a Soviet nuclear depot. Its guards hold the devices, but technicians must learn to service them, officers must establish release authority, and crews must prepare delivery before the weapons can be used.
- `sov_nuclear_bombs_delivery_force_missing_note`:  (§Rthe delivery force is lost: too few bombers, too little fuel or no air base. Readiness is falling§!)
- `sov_nuclear_bombs_hidden_arsenal_desc`: A secret reserve keeps the arsenal under close political and scientific custody while its delivery network remains limited. Current readiness: [?sov_nuclear_bombs_readiness|0]. Command integrity: [?sov_nuclear_bombs_integrity|0].[GetSovietNuclearBombsDoctrineDevelopmentNote]
- `sov_nuclear_bombs_demonstrative_deterrence_desc`: A confirmed demonstration gives the arsenal public credibility and makes every later test or demand a diplomatic act. Current readiness: [?sov_nuclear_bombs_readiness|0]. Command integrity: [?sov_nuclear_bombs_integrity|0].[GetSovietNuclearBombsDoctrineDevelopmentNote]
- `sov_nuclear_bombs_coercive_posture_desc`: Moscow backs its demands with the atomic arsenal. The threatened government can concede, resist, or seek a foreign guarantee. Current readiness: [?sov_nuclear_bombs_readiness|0]. Command integrity: [?sov_nuclear_bombs_integrity|0].[GetSovietNuclearBombsDoctrineDevelopmentNote]
- `sov_nuclear_bombs_retaliatory_posture_desc`: Survivable command, warning channels, and limited response profiles keep retaliation possible without making every warning a general exchange. Current readiness: [?sov_nuclear_bombs_readiness|0]. Command integrity: [?sov_nuclear_bombs_integrity|0].[GetSovietNuclearBombsDoctrineDevelopmentNote]
- `sov_nuclear_bombs_unrestrained_posture_desc`: The arsenal is prepared for the most dangerous release decisions, but a valid target and a completed authorization remain necessary. Current readiness: [?sov_nuclear_bombs_readiness|0]. Command integrity: [?sov_nuclear_bombs_integrity|0].[GetSovietNuclearBombsDoctrineDevelopmentNote]
- `sov_nuclear_bombs_atomic_moratorium_desc`: The arsenal is sealed under a declared moratorium while the Soviet ledger, custody chain, and any reciprocal stand-down are verified. Current readiness: [?sov_nuclear_bombs_readiness|0]. Command integrity: [?sov_nuclear_bombs_integrity|0].[GetSovietNuclearBombsDoctrineDevelopmentNote]
- `sov_nuclear_bombs_broken_chain_desc`: Command channels and depots no longer agree on who holds the devices, whether a custody crisis is open or command integrity has collapsed. Physical custody does not grant immediate technical or delivery access. The chain holds again once the custody crisis closes and command integrity recovers. Current readiness: [?sov_nuclear_bombs_readiness|0]. Command integrity: [?sov_nuclear_bombs_integrity|0].[GetSovietNuclearBombsDoctrineDevelopmentNote]
- `sov_nuclear_bombs_coercion_target_requirements_tt`: Choose a state held by an independent government other than the Union that has not capitulated. Its controller cannot be a major power. Bomber range is checked when a strike is prepared.
- `sov_nuclear_bombs_breakaway_technical_requirements_tt`: We must hold the selected transferred depot, possess atomic technology and nuclear weapons capability, and have no other project underway.
- `sov_nuclear_bombs_reform_custody_doctrine`: Reform Custody
- `sov_nuclear_bombs_reform_custody_doctrine_desc`: Transfer responsibility for guarding, certifying, and authorizing the arsenal. The transition reduces Readiness and Command Integrity. Custody can be reformed only once.
- `sov_nuclear_bombs_audit_stockpile_desc`: Count every stored device against the arsenal records. The audit settles disputed accounts once every device is accounted for, including weapons spent in bombing raids.
- `sov_nuclear_bombs_counterintelligence_sweep`: Counterintelligence Sweep
- `sov_nuclear_bombs_counterintelligence_sweep_desc`: Send security officers to the reactors, depots, rail yards, and test grounds to arrest informers and close leaks. A completed sweep can dispel foreign suspicion, but cannot erase proof a government already holds. Program security: [GetSovietNuclearBombsSecurityName].
- `sov_nuclear_bombs_prepare_instrumented_proof_test`: Instrumented Proof Test
- `sov_nuclear_bombs_prepare_instrumented_proof_test_desc`: Reserve one assigned device for an instrumented test. Arsenal Readiness changes by [?constant:sov_nuclear_bombs_tuning.test_success_instrumented_readiness|+=0] after a clean result, [?constant:sov_nuclear_bombs_tuning.test_partial_readiness|+=0] after a partial yield and [?constant:sov_nuclear_bombs_tuning.test_failure_readiness|+=0] after a failure. Gains are halved for tests beyond the first [?constant:sov_nuclear_bombs_tuning.test_purpose_count|0] at the current stage. Low Command Integrity increases accident risk. An accident consumes the device and can produce an atomic yield when Integrity is [?constant:sov_nuclear_bombs_tuning.test_accident_catastrophic_integrity_threshold|0] or lower.
- `sov_nuclear_bombs_prepare_concealed_field_test`: Concealed Field Test
- `sov_nuclear_bombs_prepare_concealed_field_test_desc`: Test an assigned device under guard while limiting public exposure. The poorer instruments teach less: Arsenal Readiness changes by [?constant:sov_nuclear_bombs_tuning.test_success_concealed_readiness|+=0] after a clean result, [?constant:sov_nuclear_bombs_tuning.test_partial_readiness|+=0] after a partial yield and [?constant:sov_nuclear_bombs_tuning.test_failure_readiness|+=0] after a failure. Gains are halved for tests beyond the first [?constant:sov_nuclear_bombs_tuning.test_purpose_count|0] at the current stage. Low Command Integrity increases accident risk. An accident consumes the device and can produce an atomic yield when Integrity is [?constant:sov_nuclear_bombs_tuning.test_accident_catastrophic_integrity_threshold|0] or lower.
- `sov_nuclear_bombs_prepare_public_test`: Public Demonstration
- `sov_nuclear_bombs_prepare_public_test_desc`: Prepare an atomic demonstration and choose whether to invite observers, give advance notice, or announce the result afterward. A successful test reveals the arsenal, raises Arsenal Readiness by [?constant:sov_nuclear_bombs_tuning.demonstration_readiness|0], and strengthens Soviet threats. The Readiness gain is halved beyond the first test at the current stage.
- `sov_nuclear_bombs_prepare_limited_strike_desc`: Prepare a military or logistics strike against an eligible nonnuclear target, or the marked state of a nuclear major during the Evolution IV emergency. Release requires technical certification and final authorization. Enforcing a refused demand strengthens later threats. Aborting or redirecting the strike after a public ultimatum weakens them.
- `sov_nuclear_bombs_breakaway_form_command_desc`: Train officers to authenticate orders and command the devices held at our depot.
- `sov_nuclear_bombs_breakaway_integrate_delivery_desc`: Train crews and prepare a delivery route for the devices at our depot. Local technicians and commanders must be ready before the weapons can be used.
- `sov_nuclear_bombs_proof_test_mission_desc`: Technicians and bomber crews are preparing the selected test. The reserved device stays assigned to this operation until the test ends or is cancelled.
- `sov_nuclear_bombs_ultimatum_response_mission_desc`: The threatened government must answer the Soviet demand before the deadline. It can comply, offer a partial settlement, request more time, or refuse.
- `sov_nuclear_bombs_retaliation_window_mission_desc`: A confirmed nuclear crisis gives the command board time to preserve the reserve, limit the profile, open a hotline, or authorize a verified response. A hotline keeps its full negotiating time. An authorized response waits less when command is intact and longer while a warning is unconfirmed or authentication must be restored, and an expanding exchange shortens it.
- `sov_nuclear_bombs.event_details.status.active`: \nStatus: Soviet atomic command is active.
- `023_sov_nuclear_bombs_achievement_eligible_tooltip`: Available to the Soviet Union while its atomic command remains active and nuclear devastation has not ended normal government.
- `023_sov_nuclear_bombs_firebreak_tooltip`: After a confirmed exchange between nuclear majors, verify a reciprocal stand-down involving at least [?constant:sov_nuclear_bombs_achievement.min_nuclear_majors|0] nuclear majors without a violation, before General Exchange or widespread Fallout begins.
- `chaosx.nr23.183.t`: How the World Will See the Test
- `chaosx.nr23.183.d`: The public demonstration is being prepared. Foreign observers can watch the instruments at the test ground, or Moscow can give advance notice without opening the site. The command can also wait until the blast is over to announce what happened.
- `chaosx.nr23.183.a`: Invite observers.
- `chaosx.nr23.183.b`: Give advance notice.
- `chaosx.nr23.183.c`: Announce after the blast.
- `sov_nuclear_bombs_presentation_observers_tt`: A successful test raises Credibility by [?constant:sov_nuclear_bombs_closure.observers_credibility|0] and Command Integrity by [?constant:sov_nuclear_bombs_closure.observers_integrity|0]. Foreign governments are less likely to strengthen air defences or guarantee threatened neighbours.
- `sov_nuclear_bombs_presentation_notice_tt`: A successful test raises Credibility by [?constant:sov_nuclear_bombs_closure.notice_credibility|0]. Advance notice gives threatened neighbours more opportunity to secure foreign guarantees.
- `sov_nuclear_bombs_presentation_afterward_tt`: A successful test raises Credibility by [?constant:sov_nuclear_bombs_closure.afterward_credibility|0]. The unannounced blast makes foreign governments more likely to strengthen their air defences.
- `sov_nuclear_bombs_presentation_observers`: \n\nForeign observers attended the test and watched the instruments.
- `sov_nuclear_bombs_presentation_notice`: \n\nMoscow gave advance notice of the test and kept foreign visitors outside the site.
- `sov_nuclear_bombs_presentation_afterward`: \n\nMoscow gave no advance notice of the test.
- `sov_nuclear_bombs_presentation_none`: `""`
- `chaosx.nr23.184.t`: The Soviet Arsenal Cannot Be Opened
- `chaosx.nr23.184.d`: The Soviet atomic programme cannot be started in the current circumstances.
- `chaosx.nr23.184.absent.d`: No Soviet government holds a state in which the atomic programme can be established.
- `chaosx.nr23.184.active.d`: The Soviet atomic programme is already active, or its opening is awaiting a decision.
- `chaosx.nr23.184.unavailable.d`: The Soviet atomic programme is disabled, or nuclear devastation has ended normal command.
- `chaosx.nr23.184.a`: Understood.
- `sov_nuclear_bombs_develop_command`: [GetSovietNuclearBombsCommandDevelopmentName]
- `sov_nuclear_bombs_develop_command_desc`: [GetSovietNuclearBombsCommandDevelopmentDescription]
- `sov_nuclear_bombs_development_party_name`: Build a Mobile Reserve Command
- `sov_nuclear_bombs_development_military_name`: Add a Second Confirmation Channel
- `sov_nuclear_bombs_development_scientific_name`: Establish a Technical Veto
- `sov_nuclear_bombs_development_dispersed_name`: Build Regional Reserve Commands
- `sov_nuclear_bombs_development_none_name`: Develop Nuclear Command
- `sov_nuclear_bombs_development_party_desc`: Build a mobile command reserve over [?constant:sov_nuclear_bombs_closure.development_days|0] days while the capital is threatened. The reserve reduces the damage to Readiness and Command Integrity from a threat to Moscow to [?constant:sov_nuclear_bombs_closure_factor.party_mobile_loss|%0] of the usual loss.
- `sov_nuclear_bombs_development_military_desc`: Build a second channel for confirming release orders over [?constant:sov_nuclear_bombs_closure.development_days|0] days. Command Integrity rises by [?constant:sov_nuclear_bombs_closure.military_development_integrity|0], and emergency retaliation can then be delegated.
- `sov_nuclear_bombs_development_scientific_desc`: Give scientists a formal veto over strikes on populated centres after [?constant:sov_nuclear_bombs_closure.development_days|0] days of preparation. The veto also lowers accident risk during testing.
- `sov_nuclear_bombs_development_dispersed_desc`: Build regional reserve commands over [?constant:sov_nuclear_bombs_closure.development_days|0] days. With secure storage, these commands can receive delegated retaliation authority and answer an enemy strike even if Moscow falls.
- `sov_nuclear_bombs_development_none_desc`: Choose a custody doctrine before developing its command arrangements.
- `sov_nuclear_bombs_development_requirements_tt`: The custody doctrine must be settled, its command development unfinished, and no other nuclear project underway. A Party mobile command also requires a threat to the capital.
- `sov_nuclear_bombs_command_development_mission`: Command Development
- `sov_nuclear_bombs_command_development_mission_desc`: Guards, technicians, and officers are preparing the command arrangements chosen under our custody doctrine.
- `sov_nuclear_bombs_development_party_note`: \nMobile reserve command reduces the damage to Readiness and Command Integrity from a threat to Moscow.
- `sov_nuclear_bombs_development_military_note`: \nA second confirmation channel allows emergency retaliation authority to be delegated.
- `sov_nuclear_bombs_development_scientific_note`: \nThe scientific command vetoes strikes on populated centres and lowers test accident risk.
- `sov_nuclear_bombs_development_dispersed_note`: \nRegional reserve commands can answer an enemy strike after Moscow falls if storage remains secure.
- `sov_nuclear_bombs_development_none_note`: `""`
- `sov_nuclear_bombs_service_arsenal`: Service the Arsenal
- `sov_nuclear_bombs_service_arsenal_desc`: Service devices held beyond the reactor network's maintenance capacity. Arsenal Readiness changes by [?constant:sov_nuclear_bombs_closure.service_readiness_loss|+=0] immediately. After [?constant:sov_nuclear_bombs_closure.service_days|0] days, Command Integrity rises by [?constant:sov_nuclear_bombs_closure.service_integrity_gain|0] and excess devices cause no maintenance losses for [?constant:sov_nuclear_bombs_closure.service_stabilization_days|0] days. Another service cycle can begin [?constant:sov_nuclear_bombs_closure.service_cooldown_days|0] days after completion.
- `sov_nuclear_bombs_service_requirements_tt`: The usable arsenal must exceed maintenance capacity, with no other nuclear project underway and the previous service cooldown over.
- `sov_nuclear_bombs_service_arsenal_tt`: Controlled production reactors: [?sov_nuclear_bombs_reactor_count|0]. Current assembly batch: [?sov_nuclear_bombs_production_quote|0] devices.
- `sov_nuclear_bombs_service_arsenal_mission`: Arsenal Maintenance
- `sov_nuclear_bombs_service_arsenal_mission_desc`: Technicians are servicing the excess devices. Crews have stood down some weapons for the work, and a completed service cycle restores Command Integrity and protects the arsenal from overload losses.
- `chaosx.news.236.t`: A Breakaway Atomic Arsenal Is Ready
- `chaosx.news.236.d`: [sov_nuclear_bombs_news_successor_actor.GetNameDefCap] has brought the Soviet atomic devices at [sov_nuclear_bombs_news_successor_state.GetName] into service. Local technicians can maintain the weapons, officers can authenticate release orders, and trained crews can deliver them. The arsenal answers to a government outside Moscow's command.
- `chaosx.news.236.a`: Another government holds the bomb.
- `chaosx.nr23.185.t`: The Public Demonstration Succeeds
- `chaosx.nr23.185.d`: The public atomic test has produced a confirmed yield. Engineers have verified the readings, and the spent device has been removed from the arsenal.[GetSovietNuclearBombsLastTestPresentation]\n\nArsenal Readiness: [?sov_nuclear_bombs_readiness|0].
- `chaosx.nr23.185.a`: Read the test result.

### localisation/english/023_sov_nuclear_bombs_requirement_flags_l_english.yml

- `sov_nuclear_bombs_coercion_settlement_open`: A nuclear ultimatum is being settled
- `sov_nuclear_bombs_confirmed_enemy_populated_nuclear_use`: The enemy has used a nuclear weapon on a populated target
- `sov_nuclear_bombs_ledger_active`: The Soviet atomic stockpile has been registered
- `sov_nuclear_bombs_site_technical_denial`: Technicians have barred this site from nuclear operations
- `sov_nuclear_bombs_mobile_reserve_command`: A mobile reserve command is ready
- `sov_nuclear_bombs_second_confirmation_channel`: A second confirmation channel is ready
- `sov_nuclear_bombs_technical_veto`: Scientists hold a formal veto over strikes on populated centres
- `sov_nuclear_bombs_regional_reserve_commands`: Regional reserve commands are ready


## Parent correction

The parent verified normal-variable localisation scopes against offline Data structures lines 492?496 and installed AAT localisation lines 399?415.
News 231/232 normal state/country pointers use the mandatory question-mark prefix.
The earlier unprefixed `SOV.variable.GetName` wording claim was incorrect for these custom variables and is superseded by this source correction.
The successor?s regular event targets retain the ordinary namespace form.
