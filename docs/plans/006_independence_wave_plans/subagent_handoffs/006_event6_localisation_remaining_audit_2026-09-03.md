# Event 006 remaining localisation audit

## Result and ownership

Two source-safe decision descriptions were rewritten in `localisation/english/006_independence_wave_decisions_l_english.yml`.
No gameplay, costs, affordability predicates, palette strings, visibility gates, scripted localisation, GUI layout, events, ideas, or spreadsheet files were changed.
No files were staged or committed.
Other agents' existing edits were preserved.
This is a bounded localisation patch and actionable remaining-issue handoff, not completion proof for all 8,817 Event 006 strings or every linked visual surface.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
No skills were created or updated.
References consulted include the required offline core wiki pages, Localisation, Decision modding, Event modding, Interface modding, Scripted GUI modding, installed vanilla localisation formatter/object documentation, and the custom-cost decision precedent in vanilla `common/decisions/AFG.txt` around line 1733.

## Changed keys and consumers

### `independence_wave_accept_arms_mission_desc`

Consumer: `independence_wave_accept_arms_mission` in `common/decisions/006_independence_wave_decisions.txt`.

Before: "Receive real equipment from a sponsor with adequate stocks. The shipment strengthens security and records an arms channel in the patron ledger."

After: "Receive rifles and support equipment from a sponsor with adequate stocks. The shipment strengthens security and increases the sponsor's influence."

Source proof: the decision's removal effect sends `infantry_equipment` and `support_equipment`, sets the arms patron channel, adds standard patron influence, and raises security.
The rewrite replaces the internal bookkeeping description with the actual foreign-influence consequence.
No amounts or payment conditions were changed.

### `independence_wave_call_charter_expulsion_vote_desc`

Consumer: `independence_wave_call_charter_expulsion_vote` in `common/decisions/006_independence_wave_decisions.txt`.

Before: "The recognized League leader may put [FROM.owner.GetNameDef] before the anti-puppetry charter for a documented breach: [FROM.owner.GetIndependenceWaveExpulsionGroundName]. At least [?constant:independence_wave_decision_gate.charter_expulsion_member_minimum|0] members must remain in the ledger. The vote takes time, fractures confidence, and removes the member from the League if it passes."

After: "Call a League vote to expel [FROM.owner.GetNameDef] for breaching the anti-puppetry charter: [FROM.owner.GetIndependenceWaveExpulsionGroundName]. Only the recognized League leader may call the vote, and the League must have at least [?constant:independence_wave_decision_gate.charter_expulsion_member_minimum|0] members. The vote weakens confidence in the League and removes the member if it passes."

Source proof: `is_independence_wave_charter_expulsion_authority` in `common/scripted_triggers/006_independence_wave_decision_triggers.txt` checks the current leader, membership, anti-puppetry charter, and current global member count inclusively against the named constant.
The prior wording could imply a post-expulsion minimum because it said members must "remain".
The rewrite describes the existing pre-vote condition, retains the charter, and leaves the dynamic target, ground, and minimum tokens intact.
The eight `GetIndependenceWaveExpulsionGroundName` branches were inspected and remain unchanged.

## Prose-quality summary

- Vagueness: "real equipment" now identifies rifles and support equipment, and "put ... before the charter" now states the expulsion action.
- Bloat: the arms-channel bookkeeping phrase was replaced with its player-facing consequence.
- Obvious explanation: "The vote takes time" was removed because the decision already carries its timer.
- Repetition: no broad repetition rewrite was performed.
- Overcomplication: "members must remain in the ledger" became the actual League membership requirement.
- Style-rule repair: internal ledger language was removed from these two passages, with no em dashes, semicolons, staged contrasts, or fragment chains introduced.

No sourced or attributed quotation occurs in either changed passage.
No quotation-bearing super-event surface was edited or validated.
All dynamic tokens in the changed passages were preserved verbatim.
Dynamic localisation added or fixed: none.

## Key and source audit

- Missing keys: no missing explicit `name`, `desc`, `title`, `text`, `tooltip`, `custom_effect_tooltip`, or `custom_cost_text` token references were found in the scoped Event 006 decision, category, idea, and event files when compared with the English localisation inventory.
- Duplicate keys: none found among the 8,817 keys in `localisation/english/006_independence_wave*.yml`.
- Malformed and indented keys: none found in the scoped localisation files by a full-line key/value check, including escaped quotes and trailing whitespace.
- Scripted localisation: no unresolved `GetIndependenceWave*` calls were found against the registered definitions in `common/scripted_localisation`.
- File encoding concerns: none found in the scoped localisation files, and the edited file retains its UTF-8 BOM.
- Cross-surface mismatch repaired: arms-mission prose now explains the existing influence gain, and the expulsion prose describes the current-member gate instead of implying a remaining-member gate.
- These inventories do not establish that every implicit key, every runtime scope, or all 8,817 prose passages have received a full individual semantic review.

## Remaining cost and wording issues

### DM-35: `independence_wave_balance_patrons`

Files: `common/decisions/006_independence_wave_decisions.txt`, `localisation/english/006_independence_wave_decisions_l_english.yml`.
Keys: `independence_wave_cost_patron_balance`, `independence_wave_cost_patron_balance_blocked`, and the tooltip alias.

The current cost text prints both Start and Later rows and repeats command power in the Later row.
The first completion pays `independence_wave_decision_pay_diplomatic_standard`.
A later completion also pays `independence_wave_decision_pay_administration_light`.
Both `available` and `custom_cost_trigger` test the diplomatic cost plus a separate light command-power threshold, rather than the sum of both command-power payments.
This can approve a country that can afford each component separately but cannot afford their combined payment.
The same later branch uses strict `>` checks for light command power and manpower.
This was escalated to the parent while preserving the repaired cost palettes and all gameplay.

Recommended owner fix: establish one current-stage payment and inclusive affordability predicate, then use a current-stage compact row with a single combined command-power amount.
A text-only claim that the combined payment is already enforced would be incorrect.

### DM-01: `independence_wave_secure_provisional_capital_desc`

The phrase "required force-tier garrison" exposes an internal classification without stating the actual required garrison.
The static "30-to-75-day" range agrees with the current base timer and fragile/viable adjustments, but it is less useful than the country's current mission duration.
Source: `independence_wave_start_provisional_capital_mission` in `common/scripted_effects/006_independence_wave_decision_effects.txt` and `independence_wave_secure_provisional_capital_garrison_satisfied` in the decision triggers.
Dynamic opportunity: publish the existing current garrison requirement through a read-only localisation selector, and rely on the actual mission timer or expose its configured duration without changing mechanics.
No requirement or duration was removed to make this sentence shorter.

### Form03 follow-up prose

`independence_wave_form03_ratify_confederal_charter_desc` still uses "both public values", "genuine federal language scope", and "stored values".
These are mechanically opaque labels that need a connected Form03 owner review to name the actual public measures and language requirement accurately.
This finding is queued rather than presented as acceptable prose.

## Strict pre-event surface

The active-country classifier requires `independence_wave_active_origin`, the Event 006 `liberation_origin`, and absence of `independence_wave_origin_ended`.
The stricter player-surface classifier additionally excludes Event 021 preparation/completion receipts.
The inspected founding, government, recognition, security, host-relations, patron, network, and League category gates use these active or player-surface predicates.
The existing post-release and patron-pressure spirit wording describes an active country's state rather than an advance prediction.
No visibility or lifecycle code was modified.
This source review does not certify all idea writers or all category visibility scenarios.

## MCP evidence and blockers

Event namespace scan and options render used `chaosx.nr6`.
Both returned focused partial analysis with zero indexed helpers and explicitly deferred workspace-wide helper projections and lifecycle passes.
They are not full lifecycle or popup-text overflow proof.

- Scan: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94400f6e3bb784b4de7fef5eeef75d6b2576c44630a28917df16af715e703cf5/f913983eae13d2a906a10dcb235e1ff54033ed3e9fbeabb274161d5e1defd6d8/event-scan-65f53c2f4a09.json`
- Options render data: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da7ad73b3ebb1534478f0dc69997e0f3208ba1e240635501263a0264263fb82a/db57a2b322cd9742ff80d85e21d62041b69f21bbe2d370c7c05f96a2539ca070/event-options-65f53c2f4a09.json`
- Comparison attempt using the returned revision failed with `EVENT_REVISION_NOT_CACHED: Requested event graph revision is not cached`.
No event source changed in this patch.

The attached `independence_wave_status_window` was inspected and rendered at 1920×1080, UI scale 1, normal state.
The minimal input `{ id: event6_localisation_audit_pre_event, country: { tag: ENG } }` was expanded by the service to `event6_localisation_audit_pre_event-generated-1` with synthetic values.
Despite the scenario name, this is not a faithful pre-event visibility test.

- GUI inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/072c1612197422ad02407e874285ec796ca88ac791ee5c286dc89e5b5f2f922a/55926eb7612be79385e749d89b7acfaffc2b2f03ad720c3784262c63f2ecfb1c/gui-inspect.df5bebbd63e8218f.json`
- Visually reviewed cropped production PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/019d7636b6d51b5cc7a2887b9f2d835e1c7afb95ef2a41a897788942d53a55ca/888b5e8d14641dc2b6548fc0344e597fed51ecb0a1d61d09956840ba8882529b/independence_wave_status_window-cropped.png`

The production render visibly stacks multiple explanatory texts at the bottom right, approximately x280–665 and y449–480 in the cropped image.
The five `independence_wave_status_{government,recognition,security,league,ambitions}_panel` elements all occupy x280/y444 in `interface/006_independence_wave.gui`.
This visible overlap is a blocker requiring the GUI owner to repair and re-render the actual mutually exclusive tab states.
It is not dismissed as a renderer difference, and prose shortening is not an adequate substitute for the layout/state repair.
The parent received the image URI and finding.

The inspector also reports missing static fallback resolution for the recognition, dependency, League-charter, and formable animated sprites.
Those asset warnings and the incomplete state matrix require the GUI owner, not this text-only patch, to resolve.
The first 98,304-byte image read was transport-truncated.
The image was recovered through 52 smaller byte-range reads, validating base64 characters, each offset and decoded length, and the PNG signature before visual display.

## Validation and omitted work

Meaningful completed checks: exact arms shipment/influence consumer match, pre-vote membership predicate match, all expulsion-ground selector branches, scoped explicit-key and scripted-localiser inventories, pre-event classifier/category source review, focused event MCP, and one production status-window render with a recorded visual defect.
No gameplay simplification was introduced.
Full cost-family reconciliation, all Form03 semantics, all category/formable GUI states, focus/map/technology consumers, event-popup overflow, implicit idea/category keys, and every prose passage remain outside the completed proof in this bounded pass.
The linked status-window work has not received the required owner rewrite and post-change visual comparison.
The two edited descriptions were not rendered inside the game's native decision tooltip consumer, so tooltip wrapping remains unverified.
No game was launched and no live testing was requested.

Parent follow-up: review the two-key patch, assign the DM-35 summed-affordability repair, fold the DM-01/Form03 wording opportunities into their owning work, and carry the status-panel visual blocker into the current GUI pass.
