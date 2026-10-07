# Event 021 probability recovery audit

Date: 2026-10-07.

Disposition: blocked for current probability certification. The bounded read-only recovery and source review are complete, but no current probability or structural MCP artifact returned.

This audit covers the inherited Oct 6 adaptation-weight certification gap for the adaptation decisions and the Event 021 adaptation report options. The parent-described integer-ledger patch is outside the weighted surface and was not audited.

No gameplay, AI, event, decision, trigger, constant, localisation, workbook, or runtime file was changed. The only new files are this handoff and [recovery_evidence.json](event021_probability_recovery_2026-10-07/recovery_evidence.json). No Git command or commit was used. Final review remains with the parent.

## MCP recovery result

The previous audit's event-option probability inspection failed with the exact reported error: tool call failed for hoi4_agent_tools/hoi4.probability_inspect; caused by timed out awaiting tools/call after 600s. It produced no artifact, source revision, source hash, candidate count, or option eligibility result.

I retried hoi4.probability_inspect using the installed route's source object with a path field and one fully qualified option candidate, chaosx.nr21_adaptation.1.a, against events/021_random_civil_war_adaptation_events.txt. The request returned no result during a bounded wait of approximately 122 seconds and was terminated locally. This was not a server-reported timeout. There is no current analysis artifact, source revision, source hash, or analyzer scenario hash from this request.

The one-event hoi4.event_inspect lint request and the one-event hoi4.event_render options request also returned no artifacts during bounded waits of approximately 61 seconds each. Their final MCP outcomes are unobserved. The exact selectors and request bounds are in the evidence JSON.

Because the required current inspection did not return, I did not expand into hoi4.probability_evaluate or hoi4.probability_sweep. There is no current analysisId to render. I did not call hoi4.probability_compare: no immutable, genuine pre-change adaptation source is available, the current decision file hash differs from the prior inspection's candidate-file hash, and the parent-described integer-ledger patch is not a weight change. I did not compare a file to itself. Simulation was not appropriate because no uncertain-input distribution was declared. Sequence analysis was not appropriate because this is not a declared custom weighted pool with cadence and transitions.

## Audited surfaces and current source identity

The source hashes below are SHA-256 hashes of the local bytes read during this recovery. No current MCP source revision was returned.

| Surface | Exact source and identifiers | Current local SHA-256 |
| --- | --- | --- |
| Decision AI willingness | common/decisions/021_random_civil_war_adaptation_decisions.txt: event021_adapt_campaign, event021_mass_mobilization, event021_expose_intervention | 69010B5139D7030F696DDD24AD3D7E7F7354F7504273ACB04D34393797E9CAE3 |
| Event option AI chance | events/021_random_civil_war_adaptation_events.txt: chaosx.nr21_adaptation.1, options .1.a, .1.b, .1.c | 18A224629656E82A18A934F3E692C35B83CDB0FE603496025604AE4E995BBD7F |
| Adaptation eligibility and costs | common/scripted_triggers/021_random_civil_war_adaptation_triggers.txt | D1AE3767FFEED6E9DFDDAB12740B96242B8F1370FDE2FD7B99BF92D0401C00B6 |
| Shared adaptation tuning | common/script_constants/021_random_civil_war_regional_constants.txt | C6377A7DB21FC8CEB68B4C83F72BF8D6DF68FE0875B8B25DA00862B946D68EB8 |
| Rail-target validation | common/scripted_triggers/021_random_civil_war_parent_triggers.txt, event021_secure_rail_mission_target_valid at lines 1186–1194 | 1106FF99BCB031A7EC48EE856AE8F4633B2B041B1E8F08871C4D1DA06A11C8FF |
| Authority-failure helper | The requested basename resolves to common/scripted_triggers/021_random_civil_war_triggers.txt, random_civil_war_authority_is_failing at lines 339–349. The unprefixed path common/scripted_triggers/random_civil_war_triggers.txt is absent. | F8123906ED70709FEE419B6BD0988186474715AF810193AA90960CC8E3AEB170 |
| Authority thresholds | common/script_constants/021_random_civil_war_constants.txt, random_civil_war_authority.collapse_maximum and .failing_maximum at lines 219–220 | EEE6F51D8009B54419221E863FD526FE9D8B8F47FC028C292DE85CC47999908F |
| Inherited audit | docs/plans/021_random_civil_war_plans/subagent_handoffs/2026-10-06_probability_audit.md | 340CD49C92693373C186DB6611347C224D89D9E44CE3B11F71D390501010C798 |
| Inherited fixture matrix | docs/plans/021_random_civil_war_plans/subagent_handoffs/2026-10-06_probability_evidence/scenario_matrix.json | 095DE932C2B15EC4449A90C6484D8BE13089BA1021E43ACAC7CA2192A6392B35 |

The prior decision inspection reported source revision 866ba025c5fe9ce020dc5d00d8a585923ac34e42e476a1e9d0135718d2e696c0, analyzer source hash a16e2e3cbf592675fda37dbb40ac08a887bb4531e2f94837bf53bca1245ebb65, and candidate-file hash 8a8f18424060a8dc20e094adbc56b591aaa31b26486efe58a530190db72287f. Its artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3bfc200087f840df646d0a62478e5734ea28856ef67f4abf378e7ac224ea38a3/92ee21bd4f82557313c8245c7ff6b7bc506cd278b400f50e828faf2a4ad6c1ba/probability-inspect-a16e2e3cbf59.json.

That historical inspection discovered the three adaptation decisions and reported poolComplete = false, selectionRule = score_only, raw scores, and no normalized probability. Its required inputs were command power, political power, equipment, and army experience. The current decision-file hash is 69010B..., so the earlier artifact does not certify the current file's eligibility or current source identity. The current source's AI weight expressions match the earlier handoff's listed expressions. That is a source comparison only, not an analyzer-backed delta or confirmation that all other source is unchanged.

The previous handoff's four-scenario evaluate timed out after 600 seconds with no score rows. Its option inspection also timed out after 600 seconds. It reported no current event-option inspection artifact. The event structural request in that handoff was stopped without a result. Those prior absences remain unresolved.

The previous same-source comparison for event021_offer_emergency_settlement is unrelated to the adaptation-weight gap and is not used here. Its scenario hash 29f8925d5cacc89e5fcfed943fa518d3ed068c071770292ed7b010f6583c4a99 and comparison id probability-153ef582240bdf5ff4d2c10f do not identify an adaptation scenario or a genuine before/after weight change.

## Source traces and semantics

The regional constants centralize ai_base = 1, ai_preferred = 3, and ai_urgent = 2 at lines 22–24 of common/script_constants/021_random_civil_war_regional_constants.txt. The traces below record source modifiers only. No total products or scenario scores were calculated by hand.

| Candidate | Source base and modifiers |
| --- | --- |
| event021_adapt_campaign | Base ai_base; ai_urgent when random_civil_war_authority_is_failing is true. |
| event021_mass_mobilization | Base ai_base; ai_preferred when authority is failing; ai_urgent for the opposition side. |
| event021_expose_intervention | Base ai_base; ai_preferred when authority is failing; ai_urgent when the recorded foreign sponsor is major. |
| chaosx.nr21_adaptation.1.a | Base ai_base; one ai_preferred modifier for the government side and a separate ai_preferred modifier for a valid rail mission target. |
| chaosx.nr21_adaptation.1.b | Base ai_base; ai_preferred on mountain terrain; ai_urgent when authority is failing. Its option trigger admits mountain or urban terrain. |
| chaosx.nr21_adaptation.1.c | Base ai_base; one ai_preferred modifier for the opposition side and a separate ai_preferred modifier for the Event 006 adapter-complete flag; ai_urgent on plains terrain. |

ai_will_do and ai_chance are different surfaces. The prior adapter identified the decision surface as score-only, so no decision click probability follows from those weights. The offline AI Modding reference describes most ai_will_do behavior as a random score race with the highest score winning and notes external strategy or define modifiers. The Event Modding reference describes event option ai_chance as proportional sampling over the options eligible when the event fires. No exact conditional option share is certified here because the analyzer did not confirm the candidate pool, trigger-qualified members, or external inputs.

All six weighted candidates have explicit bases and conditional modifiers in the named files. The tuning numbers are centralized. The separate ai_preferred conditions on options .1.a and .1.c can both be true in the same state, so stacking and rank sensitivity should be checked by the analyzer. No dominance, starvation, or rank reversal is established by this source observation.

## Scenario and candidate-pool completeness

The inherited matrix is EVENT021_ADAPTATION_GOV_RAIL_CLAIMANT_PLAINS_FAILING_MOUNTAIN_EVENT006_PLAINS_2026_10_06. It submitted actor CXT, flat state values and flags, plus a ROOT binding with the same flat state. The matrix records submitted inputs, not values accepted by an analyzer. The current recovery did not submit these scenarios and received no analyzer scenario hash.

| Scenario | Inherited fixture and relevant source gates | Completeness and classification |
| --- | --- | --- |
| GOV_RAIL | Government, Evolution II, active crisis, war, priority-front action used, authority 0, 30 army experience, 100 command power, 100 political power, 3,000 infantry equipment, 500 support equipment, plains. The fixture also sets event021_rail_spine_secured. Option .1.a only receives its rail preference when random_civil_war_rail_mission_state exists, is owned and controlled by ROOT, belongs to ROOT's opening-core-state array, and has a supply node or sufficient infrastructure. The fixture flag does not establish those target and map facts. | External factors incomplete. The event's event021_adaptation_report_pending trigger is not in the matrix. No current score or option result. Unresolved. |
| CLAIMANT_PLAINS | Opposition, Evolution II, active crisis, war, arsenal action used, authority 0, the same declared resource values, plains. Option .1.c has opposition and plains modifiers if the event fires. The mass-mobilization decision additionally requires event021_campaign_adapted and a total-chaos or world-collapse stage flag, neither of which appears in this fixture. | Event firing, response-slot state, and analyzer input acceptance are unresolved. The inherited flags do not establish the extra decision gates. No current score or option result. Unresolved. |
| FAILING_MOUNTAIN | Government, Evolution II, active crisis, war, capital action used, authority 15, the same declared resource values, mountain. The source authority helper requires the variable to be above 14 and at or below 39, if the scenario value is accepted. Option .1.b passes its source terrain trigger on mountain. The exposure decision needs random_civil_war_foreign_intervention_active plus a live random_civil_war_foreign_sponsor_scope, active commitment, and unexpired commitment date. The matrix's random_civil_war_foreign_intervention flag does not establish those conditions. | Terrain and supplied authority are relevant, but event-pending, phase, target, sponsor scope, and live-date gates are unverified. No current score or option result. Unresolved. |
| EVENT006_PLAINS | Opposition, Evolution II, active crisis, war, priority-front action used, Event 006 adapter-complete flag, authority 15, the same declared resource values, plains. Option .1.c has the opposition and Event 006 modifiers if the event fires. Option .1.b is excluded by its source mountain-or-urban trigger on plains. | The event-pending marker and all analyzer acceptance remain unknown. No current score or option result. Unresolved. |

The event source contains three local options. Analyzer-confirmed option-pool completeness is unknown because neither the previous inspection nor this retry returned. The adaptation decision file contains three local candidates. The previous decision inspection also found 18 candidates in the older Event 021 decision file and reported an incomplete pool. The combined decision-category pool was never certified. This recovery deliberately did not repeat four scenarios across those 18 decisions.

External-factor completeness is insufficient for every inherited fixture. Unverified inputs include the event-pending flag, the response slot and phase helpers, terminal locks, resource representation as interpreted by the adapter, the rail target pointer and opening-core array, the sponsor scope and commitment timer, and any external AI strategy factors. The decision adapter's historical list of required inputs is not a current acceptance result.

## Validity, dominance, repetition, and risk

The mass-mobilization source currently gates the decision through affordability, a prior campaign-adapted flag, the high-chaos or world-collapse stage, response-slot state, and an unused-action flag. Its current gate has no command-power requirement. The exposure decision is limited to the government side with live intervention and affordability gates. The campaign adaptation decision requires its stage, war, response-slot, affordability, and lifecycle gates. These are source findings, not proof that the MCP adapter accepted them.

Option .1.b has a terrain trigger that excludes plains. Its positive base weight must not be interpreted as an available plains candidate. The rail and sponsor preference modifiers depend on state or country scope data that the inherited matrix does not supply. Whether the corresponding action effects safely handle invalid targets was not established by this bounded source set.

The campaign adaptation, mass mobilization, and exposure decisions each have lifecycle flags that limit repeat use. This supports a source-level repetition safeguard. The event is triggered-only and requires event021_adaptation_report_pending. No sequence or repeated-campaign analysis was run, and the effect-side consumption of that pending receipt was not re-audited here. Snowball, starvation, excessive repetition, exploit risk, and campaign-level dominance remain unresolved.

No analyzer result proves a positive-weight impossible choice, an unavailable decision being selected, a rank reversal, starvation, dominance, or a snowball. No source-only balance claim is made. There is no supported numerical weight adjustment recommendation.

## Reference review

The referenced offline pages were read locally for this recovery. The inherited Oct 6 MCP reference-context results supplied the same source revisions listed below. The current local SHA-256 values match those revision hashes for the decision, event, and installed decision documentation.

| Reference | Read section | Revision or local SHA-256 |
| --- | --- | --- |
| paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md | AI section, lines 357–374 | 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162 |
| paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md | Options, lines 151–179 | 96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d |
| paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md | MTTH and AI selection distinction, lines 26–36 | Local SHA-256 917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818. No MCP reference revision was available in the inherited handoff. |
| C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md | Country decision visibility and availability, lines 1–46 | 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019 |

The installed Markdown documentation search found no ai_will_do or ai_chance scoring entry. The installed decision documentation does distinguish visible and available checks. The offline wiki sections supply the score-race versus proportional-option-sampling distinction. The inherited handoff records that its targeted hoi4.reference_search did not return and that no hoi4.reference_read artifact was captured. This recovery read the exact local sections directly and does not claim a new MCP reference read.

## Recommended follow-up

1. Keep the current weights unchanged until a current analyzer inspection and named scenario evaluation return. This audit does not select balance targets.
2. After MCP responsiveness changes, restart with the same exact event source path and a single fully qualified option candidate. Expand the event option pool only after successful inspection, and include all three local event options before claiming a normalized conditional share.
3. Evaluate only the relevant named scenarios one at a time. Preserve GOV_RAIL, CLAIMANT_PLAINS, FAILING_MOUNTAIN, and EVENT006_PLAINS when their declared state is source-valid. Obtain rail-state, sponsor-scope, and phase bindings from an actual accepted fixture. Do not add invented scenario fields or flags.
4. Keep decision AI results as willingness scores. If a category-wide rank claim is needed, first establish the complete relevant candidate pool and external strategy factors. Do not repeat the old four-by-eighteen matrix.
5. Use hoi4.probability_compare only if an immutable genuine pre-change adaptation source and the identical named scenarios become available. The current audit has no such baseline.

## Explicit gaps

- Current probability inspection did not return within the bounded recovery window, so all current score and probability conclusions are unresolved.
- Current structural event inspection and options rendering did not return artifacts.
- No current source revision, MCP source hash, analyzer scenario hash, comparison id, or rendered URI exists for this recovery.
- No probability_evaluate, probability_sweep, probability_compare, probability render, simulation, sequence, vanilla runtime, or live campaign result is claimed.
- No MTTH, random-list, custom weighted-pool, GUI-linked, focus, research, doctrine, or technology surface was identified in the exact named source set, so those analyses were skipped as out of scope.
- No gameplay fix or balance target is recommended without analyzer evidence.

Skills consulted: chaos-redux-subagents, chaos-redux-events, chaos-redux-event-planning, and chaos-redux-decisions-missions. The audit prompt at .codex/agents/chaosx_ai_probability_auditor.toml was also read.
