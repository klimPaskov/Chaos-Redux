# Architect source-reading notes

This is an intermediate source synopsis only.
No feature design, implementation, repository research, or external research has begun.
The original 38 assigned variants are fully read in bounded outputs without truncation, covering 55 supplied paths and 629,863 original bytes.
The parent later added both complete 3D owner-skill variants.
All 40 assigned variants are now fully read across 58 supplied paths and 842,833 unique source bytes.
Every duplicate path was verified against the original SHA256 after reading.
Current 3D raw decoded characters [0,48000) are attributed to the documentation curator, with parent acknowledgment.
The architect read the entire old 3D skill and current 3D characters [48000,116222).
The final current 3D chunk was completely replayed after one context-truncated output before it was marked complete.
Both 3D role TOMLs were also independently reread in full for conflict verification, without adding them to the assigned-variant total.

## Authority and scope

The Project Source Protocol requires every supplied text/config/catalog/archive variant to be fully processed before substantive work.
It allows team coverage and hash-verified equivalent copies, but not summaries or previews in place of a complete semantic pass.
The protocol allows a planning package when HOI4 MCP and native custom roles are unavailable, with explicit Subagent and MCP Usage Maps instead of fictional validation claims.
The current user brief controls Event 112 Rise of Cossacks, original catalog 122, Minor Fire-Once, To Be Reworked, chaos level 1, Formables Medium.
The current technical owner skill is preferred over stale role summaries and older variants where the authority is clear.
Acceptance must distinguish explicit user decisions, parent acceptance within authorization, actual implementation, and proposals.
The usual plans and specs locations are docs/plans/<event_id>_<event_slug>_plans/ and docs/specs/<event_id>_<event_slug>_specs/.

## Catalog facts

Both fully read event catalogs have 165 rows and preserve identical problem rows for this task.
ID 112 is Lootboxes with the description of a national wrestling tournament.
ID 122 is Rise of Cossacks with only the premise that Cossacks rise in a random East Slavic state and expand across East Slavia.
Both rows are Unavailable in both supplied exports, with no classification or evolution text for Cossacks.
Formables is cluster 6 in both cluster variants, Minor Repeatable at chaos 3, with listed members 3, 12, 38, 48 and severities High, Severe, High, Medium.
Neither supplied Formables row lists Cossacks.
This is a source identity conflict to preserve for later explicit alignment, not permission to overwrite CSV or reuse an occupied runtime namespace.
The user's current classification overrides the supplied catalog row.
Both catalogs contain several other title/description drifts, so catalog numbers do not prove runtime IDs.

Current versus old event catalog changed IDs are 6, 12, 16, 23, 24, 27, 28, 29, 31, 32, 33, 39, 42, 52, and 70.
Notable catalog changes are Event 23 Playable to To Be Reworked, 27 and 32 Needs Testing to To Be Reworked, 33 and 42 To Be Reworked to Needs Testing, Event 16 cluster 9 removed, Event 29 clusters 7 and 15 removed, Event 31 cluster 16 removed, and 39 and 52 moved from cluster 8 to 20.
Current cluster 16 still lists Event 31, which conflicts with its blank event-side cluster field.
Current Intelligence is cluster 20 rather than 8.
Current Various Anomalies adds Event 42 at Low severity.
Current scenario catalog has 16 entries against 15 old entries, moves Assassin Network from SCN-014 to SCN-019 with changed types and intensity effects, and adds SCN-016 Global Jihad.
Neither scenario catalog contains a Cossack scenario.
The full field-level source delta is catalog_variant_deltas.json.

## Shared script rules

Use shared schema-first script_constants groups for tuning and file-local @ constants only where a native field rejects constant tokens.
Timed days fields that reject constant tokens receive a copied normal or temporary variable.
Do not scope temporary variables.
Preinitialize every temporary output in the caller before a nested scripted helper if it must survive the return.
Use normal scoped variables and flags for durable state, with flags for booleans.
Use short-lived regular event targets for synchronous chains and explicit cleanup for intentionally persistent global targets.
Validate stored country targets with country existence checks because scope_exists is always true on a variable scope.
Use manpower_k, max_manpower_k, max_available_manpower_k, and state_population_k where relevant because plain dynamic manpower values overflow around 2.1 million.
Collection-size comparisons are inclusive.
while_loop_effect and for_loop_effect stop at 1,000 iterations.
Unscoped recurring all-country hooks need explicit user authorization and are not justified by convenience.
Prefer targeted names over meta token pasting when appending one ROOT, PREV, FROM, or THIS scope token to a flag or variable name.
Use documented meta effects or triggers only when static fields need literal injection.
Shared registry helpers must be neutral and used across families.
Event-owned orchestration, selectors, lifecycle, receipts, and private adapters remain with their owner.

## Public dynamic effect contracts

- calculate_economy_scaled_factory_grant is COUNTRY scoped, accepts positive economy_scaled_factory_grant_step, economy_scaled_factory_grant_min, and economy_scaled_factory_grant_cap temporaries, and writes economy_scaled_factory_grant_count without building mutation.
- damage_state_building_dynamic is STATE scoped, reads required dynamic_building_damage_type building token and dynamic_building_damage_amount temporaries without changing them, and dispatches one native damage_building through meta_effect.
  It has no defaults, clamp, rounding, selection, scope change, flag, target, or persistent side effect beyond building damage.
  Native province-building lookup retains the engine's first matching building behavior.
  Current call sites are Acid Rain and Random Terror.
- damage_buildings_in_random_states is COUNTRY scoped and reads buildings_to_damage_per_state, percent_of_states_to_target, damage_modifier, and optional state_population_percent.
  Current documentation restricts selected states to owned and controlled states with a targetable building.
  It computes target count from controlled-state count, rounds, and chooses at least one if any controlled state exists.
  Zero target share defaults to 0.1, zero modifier to 0.25, and a building count below one to 3.
  Its direct optional population branch does not register deaths and the helper currently has no callers.
  Exact-ledger loss callers must use the exact population helper instead.
- get_random_sea_region accepts no input in ANY scope and overwrites global.rand_sea_region from a curated weighted pool.
- clear_special_chaos_country_civilian_effects is COUNTRY scoped, clears mass_panic and removes galaxies_mix if present, and does not create a periodic world caller.
- refresh_world_threat_state reads registered owner global flags and rebuilds global.world_threat_source_count and world_in_threat.
  Current registered sources add sov_nuclear_bombs and random_terror to the older list.
  The nuclear source stops contributing under fallout_transition_active, fallout_active, world_end_final_silence, or world_end_final_silence_completed.
- union_compatible_researched_technologies_from_donor is recipient COUNTRY scoped and needs event_target:technology_union_donor.
  It grants compatible missing donor technology with popups disabled and preserves recipient technologies.
  Flexible and streamlined production are mutually exclusive, as are concentrated and dispersed industry.
  It does not change slots, clear the donor target, or annex the donor.
- call_natural_disaster is the stable COUNTRY gateway into Event 013.
  It accepts owner-documented natural_disaster_call_* inputs and regular targets.
  It returns result, reject reason, sequence ID, primary-job count, skipped-primary count, and resolved target proofs.
  Invalid input queues no work and public request inputs reset after every call.
  Its complete owner contract is not included locally.
- apply_state_population_loss_without_recruitable_manpower_gain is STATE scoped and accepts positive state_population_transaction_loss plus state_population_transaction_contract_supplied = 1.
  It performs one negative state mutation and removes only observed positive owner/controller recruitable-manpower credit up to the request.
  It returns state_population_transaction_reconciled_gain and clears one-shot inputs.
- apply_exact_state_civilian_population_loss is STATE scoped and accepts requested amount, protected minimum, reason, log-deaths switch, target-country pointer, target-valid switch, and one-shot contract proof through the documented state_civilian_population_loss_* temporaries.
  Caller must initialize state_civilian_population_loss_applied and state_civilian_population_loss_result before the call.
  It rounds the floor upward, floors fractional availability, clamps to available whole civilians, measures actual pre/post loss, and returns result 1 only for observed positive loss.
  It optionally registers the measured amount with chaos_deaths_apply_state_pop = 0 and chaos_deaths_record_state_ledger = 1.
  There is one population mutation and no second Deaths debit.
  Logging obeys the Deaths disabled setting except documented fallout states, while the physical transaction remains independent of logging policy.
- remove_support_equipment_from_stockpile, remove_motorized_equipment_from_stockpile, remove_convoys_from_stockpile, remove_trains_from_stockpile, remove_plague_bombs_from_stockpile, and remove_infantry_equipment_from_stockpile accept equipment_stockpile_removal_amount in COUNTRY scope.
  remove_fuel_from_stockpile accepts fuel_stockpile_removal_amount.
  These legacy helpers negate their input in place, have no inferred amount, and do not publish actual-payment receipts.
- cbrn_debit_motorized_stockpile_oldest_first reads a nonnegative whole cbrn_motorized_stock_debit_requested, consumes motorized_equipment_0 before motorized_equipment_1 within actual stock, and publishes completed and remaining counts.
  The caller checks full affordability before debit, rounds the displayed price consistently, records actual completed debit, and blocks operation if anything remains.
  It has no persistent side effects or grant authority.
- chaosx_convert_days_to_date_offset is ANY scoped, reads chaosx_date_days, and writes caller-initialized chaosx_date_offset.
  One hour is 0.00001 date units and one day is 0.00024.
  Whole days convert exactly, fractional days round upward to the next hour, and negative inputs produce past-date offsets.
- chaosx_convert_date_offset_to_days is ANY scoped, reads chaosx_date_offset, and writes caller-initialized chaosx_date_days as whole days rounded up and never below zero.
  Native days fields, scores, and MTTH stay in days.
  Convert only arithmetic with stored encoded dates and never encode a stored date twice.

The current registry also documents chaosx_report_forced_event_failure in chaosx_forced_event_feedback_effects.txt.
It accepts one forced_event_feedback_reason enum through chaosx_forced_event_failure_reason immediately before the call.
Settings must have created the human requester regular event target and request flags through chaosx_begin_manual_event_request.
It records one failure receipt and sends one native text event to the true requester without gameplay, pacing, log, or global changes.
Batch requests share one summary receipt.
It never guesses requester from ROOT or FROM and does nothing for natural firing, expired context, AI, or repeat failure.
The current two-day guard does not uniquely identify overlapping asynchronous requests from the same player.

Other documented owner entries include exact Event 021 front receipts, source-remnant validation and thirty-scalar/seven-pointer/eight-flag synchronous bridge storage, CBRN measured model escrow, CXT setup, Independence Wave ledger, custom/conventional technology APIs, portal raids, clones, alien infantry, the project bridge, universal exact-cost quotations, Black Friday price tables and simple costs, unit-family registry, famine, migration and paid reception, humanitarian cost contracts, asteroid minerals, and Great Depression gateway/region receipts.
The registry explicitly points to their owning files rather than providing complete contracts.
The Event 007 read-only display producer requires caller-initialized quote/valid/affordable outputs and treats an invalid sale quote as unaffordable, not a payable ordinary-price fallback.
Deferred Fury supply settlement uses the actual paid vector, retracts failed delivery, refunds pending payment, and clears the opt-in input on every exit.

## Classifiers

is_desert_state is the sole maintained shared explicit desert registry.
is_special_chaos_country and is_actual_nonhuman_country are distinct hidden classifiers.
Human claimant breakaways and ordinary human hosts are outside the nonhuman classifier.
uses_normal_civilian_systems is the inverse of actual nonhuman treatment.
Only stable owner marker changes that affect shared civilian routing justify classifier edits.
Event stage, evolution, UI, and private lifecycle validation do not belong in the shared classifier registry.
Current trigger docs clarify that pending migration intent does not prove population, reception load, or operational route capacity.

## Native raids

Country preflight is actor scope and FROM is target country when applicable.
Physical state/province filters must remain actor-neutral unless binding is documented.
A state target filter may have state ROOT.
Both actor_effects and victim_effects inside success_levels begin in RAID_INSTANCE scope.
Enter var:actor_country, var:victim_country, or var:target_state explicitly.
ROOT remains the raid instance after nesting.
A helper needing country ROOT uses an immediate hidden actor country_event and saved regular actor/victim/state targets.
Temporary variables do not cross that event boundary.
Use disjoint exact-one markers or fixed event IDs instead of one shared pending scalar for concurrent raids.
Native essential_equipment and command_power own native preparation costs.
Do not debit them a second time, invent refunds, or promise outcomes before exact resolution revalidation.
Visible, available, and launchable are separate gates.
The persistence of an already prepared instance after visible closes is explicitly an open runtime question.

## State ledgers

One transfer owner performs physical population movement.
Origin debit, route-death slice, destination credit, reception accounting, and outcome projections are separate values.
Validate explicit request, route, actor, states, and floor proof before mutation.
Measure origin and destination deltas and require actual debit minus route deaths minus measured credit to equal zero before acceptance.
Use sparse aligned registries with monotonic IDs, preserved origin/provenance, explicit statuses, exact-one resolution, symmetric append/update/removal, and bounded active processors.
Indexes are not identity.
Reception load belongs both to destination state and receiving country, while capacity belongs to receiving country.
Both ledgers update symmetrically once per accepted amount and both must cover a debit.
Integration and resettlement outcomes do not create people.
Custody at a shared site can require closure/release receipts even when the action's own marker does not name that custody.
Mapmode projections are written at transaction time in state scope, not rebuilt by scanning global arrays.
Mapmode bottom/top layers, documented FROM state scope, endpoint markers, and borders can represent roles.
There is no generic route-arrow geometry.
Exact receipts and capacity are owner/controller information, with qualitative public text.

## GUI and localisation

Current GUI requires an accepted reference before source construction, native image-to-element mapping, iterative renders, matched final source/scenario evidence, and real dynamic controls.
Default is one primary and up to two supporting values, with four visible values as the hard maximum.
Default primary actions are three to five, with six as the hard maximum, and usually one to three missions or target controls.
Costs use no more than four spendable resource types with correct icons and shared action validation/payment/effect/AI paths.
Budget rules cannot be evaded through empty or duplicate tabs.
Expected scenario coverage includes coherent phases, long real text, empty/crowded lists, exact bounds, targets, enabled/disabled/hover/selected states, and declared resolution/UI scales.
1920 by 1080 at scale 1 is the default baseline.
No separate GUI comparison tool is documented.
comparisonScenario is not an old-source snapshot.
gui_rewrite is optional and a transaction failure does not veto direct application of an already authorized edit.
Visible render defects remain blockers and cannot be excused as renderer discrepancies.
Unknown visibility or enablement and dashed amber hit areas do not prove campaign state.
State-piece selection must survive loss of qualification as an unresolved selected piece.
Requiredness does not suppress a declared visibility hook.
Localisation uses UTF-8 BOM, no :0 key suffix, and no direct formatting characters in scripted localisation.
Player-visible flag requirements need meaningful localisation or hidden implementation checks with custom tooltips.
The prose auditor preserves source quotations and dynamic tokens, removes vague or generic prose, and forbids em dashes or sentence semicolons in authored game text.

## Evidence and ownership

The current subagent routing requires context-complete no-inheritance tasks, strict event-owned GUI limits, parent integration, and honest completion reports.
The probability auditor is read-only and separates exact, bounded, sampled, score-only, and unresolved evidence.
Every weighted patch needs immutable before-source bytes, SHA256 and exact saved scenarios, then owner patch and mandatory probability_compare.
A current file compared to itself does not replace missing baseline evidence.
MTTH value evaluation is not automatically a probability or cumulative timing distribution.
The debug-playtest skill is explicit-invocation-only and has not been invoked here.
Ordinary agents do not launch HOI4 or ask for logs.
Save inspection reads supplied HOI4txt saves only, preserves them, records date/version, and supports exact before/after, savecheck, observer tallies, and footprint evidence.
One save proves only that save.
These checks supplement required MCP analysis rather than replacing it.
The catalog workbook is the only editable source, and CSV is export-only.
XLSX changes preserve actual package features, formulas, literal strings, concurrent hashes, and reopen comparisons before replacement.
The catalog exporter regenerates all three CSV files after successful workbook changes.
No workbook or CSV edit is authorized in this reading task.
Shared Git commits require an isolated index, reviewed owned hunks, HEAD compare-and-swap, precise real-index reconciliation, and preservation of other staged work.

## Source conflicts already established

1. The user assigns runtime Event 112, but both supplied catalogs call 112 Lootboxes and put Rise of Cossacks at 122.
2. Older AGENTS allowed recurring CXT synchronization and optional weekly maintenance, while current AGENTS permits only registration/pending markers in fallback hooks and reserves grants and replenishment for player debug decisions.
3. Older AGENTS required broad offline pages before opening any file, while the current protocol puts complete supplied-source reading first and current AGENTS uses relevant cited offline/installed sections before engine-facing edits.
4. Old shared damage defaults were sparse and controlled-state-only, while current docs give owned-and-controlled selection and exact zero/default rules.
5. Old exact population docs did not explain caller-owned output storage or measured-return/logging details, which are mandatory in current documentation.
6. Current config invokes HOI4 MCP through npx.cmd with --yes --prefer-online hoi4-agent-tools@latest, while some current prose still says hoi4-agent-tools.cmd.
   Actual connected process identity and live schema must settle capabilities later.
7. Current GUI owner skill and worker say rewrite is optional, while current config and completion-role summary still list rewrite in mandatory evidence.
   The detailed GUI owner contract controls this point.
8. Current TOML variants mostly change model declarations, while ownership prose remains materially identical.
9. The current detailed 3D owner skill and current role body require a separately generated item-free body, separate item geometry tasks, a Meshy rig for eligible bipeds, and receipt-verified provider actions.
   The older owner skill and the current role description retain a firearm-specific direct-to-Blender rig/action route that is superseded by those detailed current rules.
10. The current 3D owner skill requires actual live Blender authoring for missing bones, weights, and keys and prohibits repository-synthesized authoring routes.
    Current role prose still mentions verified adapter authoring operations, while the detailed current owner skill restricts unattended adapter work to processing, ingestion, export, reimport, and read-only evidence.
11. The older 3D skill uses ordinary uncompressed DDS conversion and larger default model texture budgets.
    The current 3D owner skill instead requires the dedicated compressed BC1/BC3 full-mip route, with 512 as the default and evidence for any 1024 exception.
12. Older 3D routing describes automatic recovery while credits permit.
    Current detailed role routing requires explicit locked generation attempt allowances, with no repeated paid rig or action attempt under the ordinary fallback.

## Complete 3D source requirements

### Current route and ownership

The current detailed owner skill is the controlling route for later model planning.
Every equipped body is generated without held items and with empty neutral hands.
Each firearm, melee weapon, tool, shield, staff, banner, instrument, or carried item has an independent Meshy 7 geometry task from exactly one item-only image.
Each body task likewise receives exactly one approved body-only input.
Existing equipped units are regenerated even when the existing armed geometry appears complete.
Clearly articulated bipedal anatomy can be provider eligible without being human.
A usable eligible body receives at most one Meshy rig attempt and one provider attempt per required action.
Provider rig, skin weights, and transferred actions retain exact task IDs, immutable sources, and receipt-verified ingestion lineage.
Unsupported anatomy or the first unusable rig or action result routes to live Blender repair or authoring without another ordinary paid attempt.
Polling or downloading the same task does not consume a new attempt, but regenerating or rerigging cannot reset a failed attempt allowance.
The final body and all items must be assembled before action acceptance.
Empty-hand action acceptance followed by late item parenting is expressly insufficient.
Grip, support-hand, stock, shoulder, retention, aim axis, muzzle position, recoil, discharge, and recovery are reviewed on the assembled model at the relevant frames.
Each firing state has distinct timing, locator, particle/light, licensed sound, and synchronization rows.
A deliberately non_firing equipped unit retains its equipment and records zero firing-state, effect, and sound requirements.

The worker owns the bounded model source package, rig, materials, actions, exports, evidence, legally sourced sound package, and bespoke counter handoff.
The parent owns active runtime copies, .asset, entity, .gfx, gameplay, and general sound wiring.
The user performs live-game validation.
A worker package marked complete does not make the runtime feature complete.
Every requested requirement uses complete, needs_user_review, blocked, or canceled with exact reason and evidence.
There is no fallback completion status.

### Source, preparation, and paid-operation gates

Model input is selected modern designed artwork with defensible provenance and terms.
Permitted source families include game concept, production, tabletop, miniature, fantasy, horror, and professional design art.
Archival, museum, historical, ethnographic, archaeological, reenactment, and documentary imagery is excluded from this model-input route.
This restriction is specific to the model pipeline and does not redefine the separate grounded portrait or documentary event-art routes.
Copyrighted artwork can use the reference_only_user_authorized route only with authorization for the actual source and no incompatible explicit restriction.
NoAI and no-derivative restrictions remain disqualifying.
The source-free fallback requires documented failed source search and its separate approval gate.
Native ImageGen prepares a source-informed, substantially original, fully colored model-ready derivative with the declared period, identity, proportions, materials, and non-anime style.
Preparation may remove equipped items, restore obscured body parts, and normalize the pose to useful A/T geometry.
Excluded item identities and reconstruction references remain in evidence.
Source photos, comparison boards, and QA views never become extra provider inputs.
Native alpha is preserved for transparent consumers and local background removal is a documented fallback only.
Original source and prepared input remain non-shipping evidence.

Before provider discovery, balance checks, or Meshy calls, the process must have a nonblank MESHY_API_KEY.
Existing Blender-only repair skips the Meshy key and provider gate.
Actual locked server, Meshy 7 identifier, operation schemas, versions, paid flags, required arguments, wrapper identities, Blender build, and io_pdx_mesh checksums are verified before production.
Live balance is checked for every paid tranche.
Planned calls are authorized by the accepted job, while recovery uses recorded paid_generation_attempts_per_pilot and retry_paid_calls limits.
Missing or incompatible capabilities remain blocked and are not replaced with invented operations or silent provider downgrades.

### Actual authoring versus adapter processing

Unattended adapter operations run separate factory-startup Blender workers for processing, inspection, export, and reimport.
Live Blender Lab is the actual authoring route for missing geometry, rigs, weights, and skeletal keys when needed.
The current skill prohibits repository routines that synthesize bones, assign procedural skins, or generate the required action keys.
The old author_humanoid_rig, author_humanoid_actions, and related synthetic authoring routes are not current authoring authority.
prepare_candidate rejects rig-binding payloads and cannot turn mesh processing into skeleton creation.
Receipt-verified import_animation_action, import_bvh_animation_action, and retime_animation_action operations ingest or mechanically retime real source animation.
They do not establish that the ingested action passes its semantic and contact review.
Weight sanitization may remove invalid or zero entries, retain the strongest permitted influences, and normalize them.
It must fail on a genuinely unweighted deforming vertex rather than pinning it to the root or inventing deformation.
Quaternion continuity cleanup can negate equivalent existing quaternion keys and handles but cannot create replacement animation keys.

### Geometry, scale, and material rules

Scale comes from an actual installed vanilla mesh and its active entity runtime scale, with collision-only geometry excluded from the measured source height.
Source height and effective runtime height are separate measurements.
Apply the calibrated runtime scale once.
The static facility example has source height 3.4697628021 and scale 0.6, producing runtime height 2.0818576813.
Its maximum XY footprint is 4 meters and a uniformly fitted mesh or an explicit rejection is required.
Those documented calibration values are not permission to assume a cavalry or rider scale.
Retain immutable provider geometry and edit working copies.
Audit holes, degenerates, loose components, nonmanifold edges, duplicate geometry, negative scale, weights, topology, material slots, and actual decoded export streams.
The engine ceiling is 65,535 vertices and triangle indices per export stream, while the conservative processing target is 24,000.
Static and skeletal exporters must partition real geometry safely and bind every active stream.
Topology reports across split streams distinguish per-stream limits from combined logical-object topology.
An ambiguous topology finding is evidence for review rather than automatic permission to damage geometry.

The current model texture pipeline is .tools/3d_pipeline/textures/cli.py.
Diffuse uses BC1 and normal/specular use BC3 with complete mip chains.
The default size is 512 and must never upscale smaller inputs.
Any 1024 exception requires a measured consumer or size justification.
A preexisting large atlas does not automatically qualify.
UV occupancy masks, registered source hashes, staged masks, final source identity, and an evidence-backed gutter accompany compression.
The default gutter is 12 pixels within the documented 8 to 16 range.
PDX specular green is strength, blue is metalness, and alpha is one minus roughness.
Scalar-channel resize must not treat material alpha as premultiplied opacity.
For an unproven packed normal handedness, preserve occupied green and alpha, mirror green to red, clear blue, and repair only flat padding.
Do not flip a normal channel merely to improve an unverified preview.
A Blender preview graph that interprets material alpha as opacity needs an explicit graph correction and separate evidence.

### Animation, sound, and counter acceptance

Every requested semantic action needs real articulated motion and source lineage.
Static poses, whole-rig transforms, static aliases, or renaming one role as another fail acceptance.
Firing roles require aim, discharge, recoil, and recovery.
Death roles require articulated collapse, impact, and settling.
Root policy, FPS, range, loop behavior, contact groups, deformation, action source, export, and proposed runtime binding are recorded per action.
Foot evidence measures actual support geometry and sole contact rather than ankle height or guessed quarter phases.
Ground contact review uses the documented positive clearance and tolerance with scale context.
Delivered .anim bytes undergo pose-delta, spike, drift, seam, stride, contact, and semantic-role review.
Skeleton changes invalidate downstream action and export approvals.

Custom unit audio must come from legally usable recordings with actual source pages, licensing, original downloads, hashes, and documented mechanical transformations.
No synthesized, generated, agent-recorded, placeholder, or unlicensed final audio is accepted.
The shared audio mastering entry point is .tools/3d_pipeline/audio/master.py, with inspect, audit-tree, and batch roles and an explicit allowlist.
Outputs use PCM16 mono at 44.1 kHz.
The documented target categories are shot peak at -3 dBFS, step peak at -6 dBFS, and loop loudness at -20 LUFS with -1 dBTP.
Unsupported voice or selection roles cannot be relabeled to fit a mastering category.
Long super-event audio remains audit-only under this model helper.
Selection, acknowledgement, movement, idle, engine, attack, impact, special-action, and death roles are derived from exact consumer precedents.
Infantry selection wiring is tag-scoped rather than an invented per-subunit voice surface.

Every custom unit counter surface requires original art based on the exact installed vanilla definition, DDS, canvas, frames, tokens, border, alpha, and sampled green colors.
The matching skill-local family guides the icon artist handoff.
Copied or renamed vanilla counters, arbitrary green, generic placeholders, or uninspected reference claims do not satisfy the counter requirement.

### Export, runtime evidence, and synchronization

Decode the actual delivered mesh bytes and compare object names, meshsettings indexes, textures, and active runtime mappings.
Active meshsettings texture bindings can override stale embedded filenames.
Use the selected active consumer and actual stream names rather than infer material binding from filenames.
The runtime reimport helper snapshots the exact installed mesh and bound texture hashes, checks the adapter mesh SHA256, and records the saved proof checkpoint hash.
An empty preview_views array proves geometry and skeleton import only.
It does not prove rendered materials, deformation, action playback, or in-game acceptance.
promote_accepted_reimport needs the complete hash-bound receipt, immutable source blend/mesh/animation hashes, exactly one rig, 1 to 512 exact meshes, and a new sibling checkpoint.
Its approval is metadata-only and preserves geometry, materials, weights, bones, actions, and scale through save and reopen.

Static buildings require a dedicated type=province spawn pool, a matching building_<spawn_point> entity, and matching .gfx scale/shader, object, texture, building, and spawn definitions.
Different meshes cannot share one spawn point.
Direct gameplay building rendering supplies one explicit spawn position for every possible rendered level.
A hidden provincial anchor is reserved for a deliberately single visual and requires explicit conversion, dismantlement, annexation, and deletion cleanup.
Do not use vanilla special_project_facility_spawn for a custom map building.
Keep automatic nudging unless full buildings.txt coverage is maintained.
Any generated map override preserves all vanilla rows and adds complete custom coverage.

Select and lock final source geometry, textures, and actions before copying runtime files.
Every copy records source and destination paths, both hashes, actor/tool, time, and provenance, then verifies destination hashes.
Filename equality alone cannot select a provider candidate or prove that the active runtime texture is current.
The parent may perform read-only decoding and binding review without reopening production.
Source export, native checkpoint import, rendered review, and user live-consumer evidence remain distinct acceptance records.

### Additional 3D supporting references absent from the supplied roots

Later production requires the true dependency locks, meshy_tool_schema.lock.json, blender_hoi4_adapter.json, profile/calibration files, actual wrapper implementations, and live exposed schemas.
The detailed current skill also requires references/unit_rebuild_workflow.md and the named review tools for new or rebuilt bipeds.
Named helper implementations include review_cli.py, provider_intake.py, lab_actions.py, pdx_textures.py, export_package.py, textures/cli.py, audio/master.py, and runtime/reimport_runtime.py.
The exact installed vanilla mesh, entity, material, animation, sound, counter, and building consumers are also required.
These files and runtime services were not supplied and have not been inspected or invoked here.

## Referenced supporting sources not supplied in these roots

No gameplay .txt helper bodies, offline paradox_wiki pages, installed-game documentation, workbook bytes, or current runtime registrations are present in the supplied text inventories inspected here.
Later exact implementation evidence requires common/scripted_effects/chaosx_dynamic_effects.txt, common/scripted_triggers/chaosx_dynamic_triggers.txt, common/mtth/chaosx_mtth_variables.txt, common/script_constants/chaosx_date_units_constants.txt, docs/testing/chaosx_test_country.md, and the named owner API files before their contracts are consumed.
The universal cost framework needs docs/systems/universal_cost_modifier.md plus common/scripted_triggers/chaosx_universal_cost_exact_triggers.md and its implementing sources.
Native raids need installed common/raids/_documentation.md and exact vanilla raid/effect/trigger precedents.
GUI needs installed common/scripted_guis/_documentation.md, exact linked source and vanilla UI consumers, plus the separately named references/visual-review.md if that file exists.
All exact engine fields require the offline and installed effects, triggers, scopes, data structures, script constants, dynamic variables, scripted localisation, and relevant country/unit/focus docs.
Spreadsheet work additionally needs docs/spreadsheets/README.md, the true XLSX bytes, and the XLSX skill's references/catalog.md and references/preservation.md.
The save inspector implementation and generic autonomous-debug skill are referenced but absent from these supplied text roots.
These are later supporting-source limitations, not missing supplied-source variants.
