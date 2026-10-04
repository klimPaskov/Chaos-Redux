# Soviet famine shortfall localisation handoff, 2026-10-03

Disposition: implemented bounded localisation patch, with MCP display evidence blocked.
Acceptance basis: parent delegation carries the user's 2026-10-03 choice of an explicit response when famine relief lacks resources, with famine and corruption consequences.
The parent authorized conditional wording for the protected active-relief branch.
The parent owns gameplay, sticky unknown-origin pause semantics, integration and the final commit.

## Changed files and ownership

- `localisation/english/camp_repression_country_kits_l_english.yml`: six famine decision, price and mission keys.
- `localisation/english/camp_repression_rework_l_english.yml`: eight famine popup, shortfall and funded consequence keys.
- This handoff.

This shared tree contains other agents' changes.
The key list below identifies this worker's edits, rather than attributing the entire working-tree diff to this task.
No gameplay source, workbook, export CSV, unrelated localisation row or unknown-origin wording was changed by this worker.

## Findings and display changes

Missing key list: none among the 31 unique popup, decision, mission and visible availability keys checked.
Duplicate key list: none for those 31 keys across the current English localisation files.
`soviet_gulag.2.d` and `soviet_gulag.2.shortfall` each resolve once.
Scripted localisation issue list: none found in the scoped famine passages, which do not call a scripted-localisation selector.
The linked Records tooltip calls `GetCampAdminUnknownOriginNote`, whose semantics remain parent-owned and unresolved pending the accepted pause patch.

Before, the warning shortage option claimed there were no trucks or trains even when only support equipment was short.
After, it states that the relief columns cannot be equipped.
Before, both shortfall tooltips promised penalties even when the active relief flag or mission protected an existing effort.
After, penalties are conditional on continuing famine without active relief, and the protected effort is explicitly described as continuing without further penalties.
The critical tooltip retains its additional evidence consequence.

Before, the famine price repeated literal 120, 18 and 180.
After, both ordinary and blocked prices read `camp_rework_equipment_cost.motorized_equipment`, `.trains` and `.support_equipment`, matching the readiness and consumption sources.
Current values remain 120 trucks, 18 trains and 180 support equipment.
The motorized and train icon tokens use the documented names with `GFX_` removed.
The supporting sprite definitions are `interface/chaosx_texticons.gfx:90-99`, installed `interface/texticons.gfx:2563`, and `interface/camp_repression_rework.gfx:78` for the decision icon.
Icon rendering remains unverified because the MCP display route returned no artifact.

Before, mission text required the opaque 'medium threshold'.
After, the decision description, effect tooltip, mission description and success tooltip show the exact target from `camp_rework_threshold.band_medium`, currently famine pressure below 8.
The native decision supplies its separate political power price through `camp_rework_cost.labor_project_pp`.
The relief mission already supplies its deadline natively, so this patch does not repeat that visible duration.
Availability flag labels exist for `sov_famine_relief_active` and `camp_gui_country_action_2_cooldown` in `camp_repression_requirement_flags_l_english.yml:106` and `:19`.
The equipment requirements are concrete native stock checks.

## Prose review

Vagueness: the critical description's claim that the Union Crisis 'absorbs every grievance' becomes anger at Moscow deepening the Union Crisis.
The warning's 'adequate rations' and 'arrest the disaster' become enough food and slowing the famine.
Bloat: the critical passage's long abstract introduction becomes grain seizures, failing transport and forced-labor quotas spreading hunger.
Obvious explanation: 'opening the timed route' becomes the actual relief goal and deadline.
Repetition: material commitments remain in the native price, and the effect tooltip concentrates on quota reductions, mission success and preserved evidence.
Overcomplication: the critical description no longer compares missed quotas with empty districts through an unclear statement about officials.
Style repair: the warning title 'The Grain Reports Diverge' becomes 'Empty Granaries', centering the hunger described in the event.
The crisis option drops 'at any cost', which overstated its fixed equipment price.
The remaining option names and mission failure/cancellation passages are clear and retain their existing meaning.

No sourced or attributed quotation appears in the scoped famine popup/decision/mission passages.
No quotation was edited.
All pre-existing dynamic tokens in changed passages were preserved, and the patch adds integer-formatted constant tokens.
The Records unknown-origin value and its two dynamic totals were preserved by this worker.

## Records syntax and cross-surface notes

The parent has converted `camp_admin_records_unknown_origin_note` at `localisation/english/camp_administration_ui_l_english.yml:179` into one physical quoted line with literal `\n\n` paragraph breaks.
The current row matches the documented localisation syntax and retains its two numeric tokens.
The checked localisation files retain UTF-8 BOM and contain no malformed quoted rows under the bounded source check.
No new encoding concern was found.
There is no fresh launch result confirming that the supplied startup error has cleared.
The cycle-one copied `text.log` is older evidence and does not prove current duplicate keys.

The Records prose still describes origin-unknown removals and remaining origin estimates.
It conflicts with the user's accepted sticky pause semantics and is reserved for the parent to align with its gameplay patch.
No inferred source semantics were substituted.
The famine popup, decision and mission wording is aligned with the current shortfall source paths.
The event workbook was not read or edited, so workbook alignment is unverified.
If these passages are mirrored in the catalog, the spreadsheet owner should use the final key-level wording below.
This task supplies no new event-detail or catalog row and changes no achievement or quote surface.

## Source references and evidence limits

The exposed `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read` and `hoi4.source_lookup` routes were checked before use.
Localisation context and Script Constants search calls returned no result during a multi-minute wait and the pending orchestration was terminated.
A bounded source lookup for `sov_emergency_famine_relief` returned no result within 20 seconds.
Direct local sections were read as the permitted reference fallback, without claiming MCP reference coverage.

- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md:65-91`, physical-line syntax and UTF-8 BOM.
- The same page `:184-214`, numeric formatting, and `:221-244`, sprite icon tokens.
- Wiki file SHA-256: `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`.
- Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md:216-244`, Script Constants and scoped-variable access.
- Installed concept file SHA-256: `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`.
- Installed `common/script_constants/documentation.md:1-37`, scope access and schema.
- Installed constants documentation SHA-256: `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`.
- Vanilla precedent: installed `localisation/english/TAOG_decisions_l_english.yml:503`, `SIA_propaganda_campaign_cooldown_tt` uses `[?constant:propaganda.SIA.default_propaganda_campaign_cooldown]`.
- Existing project precedent: `localisation/english/fallout_consolidated_l_english.yml:19` uses an integer-formatted constant in a cost.

Event requests needed `selector = { kind = event, eventId = soviet_gulag.1 }`, rather than the initially attempted selectors.
With that corrected selector, `hoi4.event_inspect` trace and `hoi4.event_render` options returned no result within 20 seconds each.
GUI requests needed a scenario with `id`, and inspection needed windowName and scenario together.
Corrected `hoi4.gui_inspect` and `hoi4.gui_render` requests for `repression_ledger_window`, scenario `soviet_famine_shortfall_records`, 1920x1080 at scale 1, returned no result within 20 seconds.
Therefore no source revision, production render, overflow result, comparison or artifact URI was available.
These delays are an evidence blocker, not proof that the underlying service is absent or broken.
No display defect can be judged or dismissed from these missing renders.
Standalone Technology Tree Viewer availability was checked separately against the callable inventory: there is no exposed standalone viewer route.
That is a package capability gap in this session, and installation or health of any standalone viewer remains unverified.
The exposed technology inspect/render/compare tools are distinct capabilities and no technology surface belongs to this task.

## Meaningful validation and remaining work

Ran `python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/soviet_famine_shortfall_source_tests.py` on the current shared tree: all 15 cases passed.
The source interpreter includes exact stock, each equipment one-unit short, stale funded choices, missing site choices, concurrent duplicate orders, resolved famine, invalid original authority and both protected ongoing-relief cases.
This is mocked source behavior, not engine or live-game evidence.
A scoped key scan found no missing/duplicate definitions among 31 unique referenced keys.
Manual comparison checked the displayed price against the same constants as readiness and payment, and the mission target against its `less_than` condition.

Blocked meaningful validation: production event/GUI renders, matching visual comparison, actual price/icon display and fresh startup result.
No in-game launch was attempted.
The parent retains integration review, Records semantic alignment, any catalog mirroring, and the shared-tree commit.
There are no gameplay simplifications in this localisation patch.
Completion is limited to the bounded source text patch and handoff, with the display and launch evidence still incomplete.
No additional mechanic plan was written because no new mechanic was designed.
Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`.

## Follow-up read-only acknowledgement review

The parent added six acknowledgement keys and corresponding options after this worker's 13-key patch.
This follow-up changed only the handoff.
All six keys occur exactly once in the English definitions and bind to the matching native event options and shared tooltips.
The expanded source coverage is 31 unique referenced keys, with no missing or duplicate definitions.

The funded options use the full order-ready predicate, and shortfall options require pending positive famine pressure without an active effort as well as an equipment shortage.
The underway predicate checks the active relief flag or mission, and the eased predicate requires famine pressure no greater than zero without ongoing relief.
The popup and acknowledgement predicates are actor-gated to the original Soviet authority.
The four acknowledgement options clear only the relevant popup state variable, except for the crisis-eased option also clearing the stale crisis flag.
They do not debit political power or equipment, change population, grant research, or restart the relief mission.
The current text accurately describes these effects without exposing receipt or predicate identifiers.
The existing price and mission-target constant tokens remain intact.
These six added keys contain no dynamic tokens or sourced quotations requiring preservation.

Resolved wording recommendation: `soviet_gulag.1.famine_eased` says 'The immediate shortage has eased.'
Because the neighboring options discuss equipment shortage, 'shortage' can be read as restored equipment stocks, but this predicate tests famine pressure.
Recommended wording: 'The immediate famine has eased.'
The parent applied 'The immediate famine has eased.' in a subsequent patch, preserving the read-only boundary of this review.
The other five acknowledgement entries are clear and require no style repair.
Both original event descriptions still describe the popup's originating crisis when the acknowledgement reports later relief or resolution.
That is source snapshot text, and the acknowledgements provide the current outcome without inventing a new dynamic event description.

The source test suite ran successfully with its existing 15 cases during this review.
At that moment it did not yet prove the new native availability pools or late crisis-flag cleanup cases, which the parent was adding separately.
MCP visual limits above remain unresolved.
The parent reports successful native task negotiation for the probability auditor, but this subagent holds no live event or GUI job handle to inspect.
No handle was invented and no substitute display evidence was claimed.
Parent-owned new keys for catalog mirroring where applicable follow.

```yaml
soviet_gulag.1.relief_underway: "The relief columns are already moving."
soviet_gulag.2.relief_underway: "Continue the relief already under way."
soviet_gulag.1.famine_eased: "The immediate famine has eased."
soviet_gulag.2.famine_eased: "The famine emergency has passed."
soviet_gulag_relief_underway_tt: "Existing relief continues. No further equipment is committed by this response."
soviet_gulag_famine_eased_tt: "No new relief order is required. Recorded losses and responsibility remain."
```

## Funded ration consequence follow-up

The parent authorized a bounded wording patch for the existing ration redistribution stability consequence.
This worker changed `sov_famine_relief_effect_tt` again and added `soviet_gulag_relief_funded_tt` for the parent to bind in funded event options.
The full worker patch now contains 14 unique localisation keys, with no payment, effect, availability or AI values changed.

The existing effect is `add_stability = constant:camp_rework_soviet.emergency_relief_stability` inside the successful `camp_rework_soviet_relief_order_ready` branch of `camp_repression_major_country_effects.txt:2436-2455`.
The constant at `camp_repression_rework_constants.txt:1332` is `-0.020`, which is a stability change of minus 2 percentage points.
It is a ration redistribution consequence, rather than a fifth spendable payment or a stability affordability threshold.
The ordinary tooltip now states 'Redistributing rations lowers stability' and displays the signed consequence with `[?constant:camp_rework_soviet.emergency_relief_stability|%0]`.
The syntax matches the percentage constant pattern in `localisation/english/006_independence_wave_frontier_l_english.yml:78`.
The existing integer-formatted equipment and mission-target tokens remain intact.
No new sourced quotation or dynamic scope reference was introduced.

The funded native event paths directly call the unhidden helper, which contains the unhidden `add_stability` command.
Their generated native effects therefore have the source needed to expose the stability consequence.
The new event explanation deliberately contains no second numeric stability value, avoiding a duplicate minus-2-percent line alongside that native effect.
The parent owns the `custom_effect_tooltip = soviet_gulag_relief_funded_tt` bindings in the successful order-ready branches of `.1.a` and `.2.a`.
At this worker's binding check, those event calls were still pending parent integration.
Do not place the explanation on an unconditional stale-click path where the actual helper can reject an order.
There is no fresh pixel evidence for native tooltip output or possible duplicate ordinary-tooltip content.
If the ordinary native decision path also draws its generated stability value, its two representations should be reviewed through the production consumer before claiming presentation completion.

The ordinary decision's four quoted payments remain 30 political power from `camp_rework_cost.labor_project_pp` plus 120 trucks, 18 trains and 180 support equipment from the existing equipment constants.
Political power is already the native row price, and the three equipment resources remain in its custom inline price.
No fifth inline item or redundant four-price custom tooltip was added.
The event-funded relief choices do not add a political power payment.

Read installed `documentation/effects_documentation.md:2173-2181` for country-scoped `add_stability`, and offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:1070` for the normalized stability scale.
Installed effects documentation SHA-256: `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Offline Effects page SHA-256: `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.
The previously read offline Localisation section `:194-200` documents integer precision and the `%` formatter multiplying a variable by 100 and appending a percent sign.
The constant therefore renders as `-2%`, and the wording avoids 'reduce by negative 2'.
This is source and documentation evidence, without a claim about actual rendered pixels.

The current source suite now passes 17 cases, including each event's resolved-famine acknowledgement with no false crisis presentation or payment.
The parent also added the immediate zero-pressure guard and corrected the eased label noted above.
A definition scan checks the new funded tooltip key once, alongside the previous 31 scoped keys.
The key is not considered wired until the parent adds and reviews its event calls.
Existing launch, MCP production rendering, ordinary duplicate-display and catalog limitations remain explicit.

```yaml
soviet_gulag_relief_funded_tt: "Funding relief redistributes rations and lowers stability. Grain extraction and forced-labor quotas ease as relief begins."
```

## Final worker-changed keys and wording

`localisation/english/camp_repression_country_kits_l_english.yml`

```yaml
sov_emergency_famine_relief_desc: "Divert trains, trucks, and support equipment to the hungry districts and reduce grain extraction and forced-labor quotas. Relief succeeds when famine pressure falls below §Y[?constant:camp_rework_threshold.band_medium|0]§!."
sov_emergency_famine_relief_cost: "£motorized_equipment_text_icon §Y[?constant:camp_rework_equipment_cost.motorized_equipment|0]§!  £train_texticon §Y[?constant:camp_rework_equipment_cost.trains|0]§!  £support_equipment_text_icon §Y[?constant:camp_rework_equipment_cost.support_equipment|0]§!"
sov_emergency_famine_relief_cost_blocked: "£motorized_equipment_text_icon §R[?constant:camp_rework_equipment_cost.motorized_equipment|0]§!  £train_texticon §R[?constant:camp_rework_equipment_cost.trains|0]§!  £support_equipment_text_icon §R[?constant:camp_rework_equipment_cost.support_equipment|0]§!"
sov_famine_relief_effect_tt: "Reduces grain extraction and forced-labor quotas and begins the relief effort. Redistributing rations lowers stability (?R[?constant:camp_rework_soviet.emergency_relief_stability|%0]?!). Lower famine pressure below ?Y[?constant:camp_rework_threshold.band_medium|0]?! before the relief mandate expires. Evidence of the deaths remains."
sov_emergency_famine_relief_mission_desc: "Relief columns are moving into the hungry districts. Reduce famine pressure below §Y[?constant:camp_rework_threshold.band_medium|0]§! before their mandate expires."
sov_emergency_famine_relief_mission_success: "Famine pressure falls below §Y[?constant:camp_rework_threshold.band_medium|0]§! during the relief effort."
```

`localisation/english/camp_repression_rework_l_english.yml`

```yaml
soviet_gulag.1.t: "Empty Granaries"
soviet_gulag.1.d: "Grain quotas have emptied district reserves, and families are abandoning their settlements. Prison laborers arrive at their work sites without enough food. Emergency relief could slow the famine. Concealing the deaths would keep the quotas in force and deepen the hunger."
soviet_gulag.1.c: "We cannot equip the relief columns."
soviet_gulag.2.d: "Grain seizures, failing transport, and forced-labor quotas have spread famine across the Soviet borderlands. Districts bearing the heaviest demands are losing people to hunger. Anger at Moscow is deepening the Union Crisis."
soviet_gulag.2.a: "Send emergency relief."
soviet_gulag_relief_shortfall_tt: "If famine persists without an active relief effort, the shortage increases famine pressure and administrative corruption. Relief already under way continues without further penalties."
soviet_gulag_relief_crisis_shortfall_tt: "If famine persists without an active relief effort, the shortage increases famine pressure, administrative corruption, and evidence of the losses. Relief already under way continues without further penalties."
```

