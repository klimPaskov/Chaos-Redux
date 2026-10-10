# Advanced scripted systems and country integration

Read the relevant complete sections before changing shared helpers, country creation or activation, unit-family providers, timed scripted effects, world-threat integration, formables, or 3D entity integration. Small event text or registration edits do not require unrelated sections.

## Owner-side unit-family coverage

When an event or its owning system adds a land sub-unit or equipment-backed special family, declare its consumer disposition before wiring it: standalone provider family, support attachment under an existing provider, or intentionally parent-owned and not independently consumable.

A standalone family must register idempotently from the owner's existing startup path and expose the complete owner-side provider callback contract required by the shared consumer, including eligibility, template or spawn construction, sustainment, equipment-token resolution and publication, presentation, management, derivative setup, public-package removal, and cleanup where those surfaces apply. A support attachment must identify its provider and remain in the same provider-owned transaction or template. A parent-owned disposition must state the engine or consumer constraint and retain its unlock, equipment, sustainment, and cleanup behavior in the parent package.

Wire CXT coverage for every new land sub-unit or concrete equipment type through `docs/testing/chaosx_test_country.md`. Add a modifier-free hidden-idea carrier whose ID names the matching idempotent `_apply` setup effect, bounded startup registration, and tag-scoped daily registration/pending marking under the AGENTS.md CXT contract. Grants, replenishment, and pending-package application after initial setup belong to player-triggered debug decisions; do not add periodic CXT grant hooks.

Before completion, run a full inventory over all installed land sub-unit definitions under `common/units/` and concrete equipment definitions under `common/units/equipment/`, including support definitions, then cross-check provider or parent-owned dispositions, owner registrations, concrete equipment tokens, presentation and localisation tokens, CXT registrations and synchronizers, and duplicate or missing IDs. Every entry must be covered or explicitly blocked with the engine reason.

Do not extend a central consumer-maintained family list, equipment switch, or localisation selector when an owner-side provider contract can supply the data. A missing provider or malformed registry row is a blocking integration failure, not permission to substitute a generic family.

## Handle supporting gameplay systems

An event always needs more than its own script file.

Touch the relevant systems in the same change:

- decisions and categories if the event creates player tools, responses, or for example containment mechanics
- ideas or dynamic modifiers if the event creates persistent gameplay state
- AI strategies or templates if the event changes how AI should respond
- special-country exclusions if the event touches broad civilian, political, migration, or ideology systems
- Chaos Meter hooks when the event owns Chaos-changing outcomes
- shared country classification when the event creates or manages chaos countries, as required under [Event-created country setup and audit](#event-created-country-setup-and-audit)
- and much more

Keep the complete bodies of `is_special_chaos_country`, `is_actual_nonhuman_country`, and `uses_normal_civilian_systems` inside `hidden_trigger`. Player-facing callers that need to explain eligibility must provide a concise custom tooltip instead of exposing the classifiers' tags, flags, or provider triggers.

If you add a new reusable dynamic scripted effect (an effect that could be generalized for all events), document it in `common/scripted_effects/chaosx_dynamic_effects.md` in the same change.

### Helper output lifetime

Temporary variables first created inside a scripted effect or trigger may disappear after return, while caller-preinitialized storage retains the helper's modifications (`paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, Variable types, line 440).

- Before each helper call, ensure every temporary scalar and temporary-array output consumed afterwards has caller-owned storage, including calls inside `if.limit` and scripted-localisation `text.trigger`. Initialize new output storage without resetting existing input or cursor values.
- Apply this at every nested call boundary: each caller initializes the outputs it consumes, and outer callers also initialize forwarded outputs needed after return.
- Public helper API docs must list caller-owned output storage and its required initial values.
- Actual-source tests must model conservative call-frame cleanup by discarding temporary scalars and arrays first created in the returning helper, retaining modifications to caller-preinitialized storage, and keeping scoped regular saved state separate from temporary storage instead of using one flat global temporary dictionary.

When a source audit or fixture cannot model this call-frame lifetime, report it as unmodelled and separately check caller preinitialization before consuming helper outputs.
For shared dispatchers, locate the matching authorization gate and recursively inspect its body and invoked helpers for actual dispatch and accounting, including package-specific nested branches.
A flat block-shape assertion or literal marker match does not establish that execution coverage.



When queue processing stops before the end, preserve the unvisited suffix and every unacknowledged receipt rather than clearing the whole queue and rebuilding only visited rows.
This includes the documented 1,000-iteration ceiling for `while_loop_effect` and `for_loop_effect`; do not infer the same ceiling for foreach loops.
Process a bounded batch by popping each selected row before recovery and appending unresolved rows behind the unvisited suffix, without adding a world scan.
Clear a receipt only after its matching recovery is acknowledged.
Actual-source fixtures must enforce the native loop ceiling and verify more than 1,000 queued rows across repeated invocations, unresolved-row rotation, and receipt preservation.

#### Retiring unused helpers

- Before deleting a scripted effect, trigger, or `defined_text`, search every placeholder constructor (`[ID]`-style `meta_effect`/`meta_trigger` text, `@` token pasting, `[EXTENSION_EFFECT]_apply`) and the GUI, `.gfx`, localisation, and docs for the name; a zero token count alone does not prove the code is dead.
- Delete the comment header attached directly above the removed block, or it will describe the next definition.
- After each removal pass, rescan for helpers, localisation keys, and script-constant keys whose only consumer was the removed code, and repeat until nothing new appears.
- Repository files can mix CRLF and LF line endings; edit them line by line with their own endings instead of splitting on one newline style.

#### Isolate foreach break state

Use this rule when a helper iterates records or scopes, especially nested receipt settlement and recovery.
Both `for_each_loop` and `for_each_scope_loop` default to the unscoped temporary variable `break`, so an inherited nonzero value can truncate traversal.
Give every loop a private helper-owned break temporary, reset it to `0` immediately before every invocation, and explicitly bind `break = <that_temp>`.
Use distinct names for inner and outer loops and any nested helpers that can execute together, because changing scope does not isolate temporary variables.
Repairing an inner loop does not protect its enclosing loop, and one reset at helper entry does not protect repeated inner invocations.

Tiny generic example, with valid country scopes in `participants` and each participant's records in `receipt_ids`:

```text
set_temp_variable = { settlement_participants_break = 0 }
for_each_scope_loop = {
	array = participants
	break = settlement_participants_break
	set_temp_variable = { settlement_receipts_break = 0 }
	for_each_loop = {
		array = receipt_ids
		value = settlement_receipt_id
		index = settlement_receipt_index
		break = settlement_receipts_break
		# Validate and settle this exact receipt here.
	}
}
```

Keep pending, unvisited, and unacknowledged receipts until their exact settlement is complete.
Clear only acknowledged receipts and retain unfinished work across an interrupted or deliberately bounded pass.
Do not remove array elements during `for_each_loop` traversal.

Test the actual source with inherited `break = 1` and two objects for each iterable kind, then two outer participants with two receipts each, asserting complete visitation and exactly one settlement per eligible receipt.
Also seed each private break temporary with `1` before calling the helper, repeat the call, and exercise an intentional early exit or unresolved receipt to verify reset and retention.
Keep a conservative test with more than 1,000 objects and repeated invocations, but do not impose an undocumented foreach ceiling in the fixture or claim that test proves an engine limit.
The documented 1,000-iteration bound explicitly applies to `while_loop_effect` and `for_loop_effect`, while the cited foreach sections state no such ceiling.

Sources:

- Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, lines 4279-4295 (`for_each_loop`) and 4296-4311 (`for_each_scope_loop`), explicitly define the default temporary break variable and nonzero termination.
- Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md`, lines 440-442 (temporary lifetime and unscoped storage), 1216-1217 (foreach rules), and 1222-1256 (foreach examples).
- The same offline file, lines 1219-1220 and footnote at 1828, explicitly documents the default 1,000 bound for `while_loop_effect` and `for_loop_effect` through `NDefines.NGame.MAX_EFFECT_ITERATION`.

#### Deterministic max-score selection

For deterministic max-score selectors, track explicit first-valid-candidate presence and accept that first candidate regardless of its score.
A numeric best-score sentinel must not reject an otherwise valid negative score.
After the first candidate, retain the exact score comparison and existing ID tie-break without changing weights or eligibility.


### Native special-project output overrides

Do not assume duplicate native project IDs safely replace or partially merge definitions across filenames.
For approved vanilla project output changes, use a complete replacement at the same relative vanilla file path unless the relevant engine merge behavior is proven.
Repeating full definitions in a distinct mod filename can duplicate enable-equipment or module list entries.

- Check installed native documentation, current vanilla source, and every existing mod owner of the file and project IDs before editing.
- Retain original tuning, availability, rewards, and file-scoped constants, including other projects in the replaced file, while adding only approved owned output hooks.
- Record vanilla source paths and SHA-256 hashes, then remove only the owned hooks from a comparison copy and verify exact remaining content against those sources.
- Check effective source-ID uniqueness after same-path masking, including other mod files that still declare the IDs.

Source equality establishes preservation only, and must not be described as engine validation.

### Event-created country setup and audit

If the event creates or manages non-standard countries, account for that in shared classification triggers. Any event-created or event-managed chaos country must be registered in `is_special_chaos_country` in `common/scripted_triggers/chaosx_dynamic_triggers.txt` and documented in `common/scripted_triggers/chaosx_dynamic_triggers.md`. If that chaos country is actually nonhuman rather than merely unusual, supernatural, extremist, or scenario-specific, also register it in `is_actual_nonhuman_country` and update the same documentation. Do not create event-specific duplicate classifiers such as `is_<event>_chaos_enemy`, `is_<event>_special_country`, or per-event nonhuman triggers when the shared triggers can express the category. Events interact with each other, so systems that usually affect normal countries, such as black plague, mass panic, civilian migration, or ideology spread, should exclude zombie, alien, and other nonhuman countries through the shared triggers instead of one-off checks.

When an event can create a normal tag that may also already exist from vanilla, another mod, or prior campaign state, track whether the event actually created it before loading a runtime focus tree. A good pattern is to set a country flag immediately after `release = TAG` and have the focus-tree loader check that flag before `load_focus_tree`. Existing tags with their own meaningful trees should get crisis ideas, decisions, events, or additive branch integration, not a blind replacement tree.

Before registering any new country, cosmetic, formable, or route tag, audit it against vanilla, Chaos Redux, every installed Workshop mod, and other local mods. Do not add a duplicate new country for a national identity that already exists in vanilla: reuse the vanilla tag, preserve the living country and its meaningful content, and add only safely gated Event content. If a proposed new tag conflicts anywhere in the installed set, remap it and update every script, history, localisation, asset, manifest, scenario, documentation, and catalog reference together. Apply any event-specific suffix convention only after the collision-free tag is locked.

When auditing event-created country packages, verify the whole playable-country surface, not only the release effect. Check country files, custom-tag history files, additive startup grants for existing countries, generated startup scientists when needed, tag registration, base localisation, ideology-specific cosmetic localisation (`TAG_democratic`, `TAG_communism`, `TAG_fascism`, `TAG_neutrality` plus `_DEF` and `_ADJ`), flags, decision/focus/idea icons, focus loading, AI strategy, docs, and manifests together. For existing-country variants, verify the event-created flag is set only on the release path and every `load_focus_tree` path is gated by that flag. Do not copy vanilla country, state, or unit history only to add Chaos Redux technologies, equipment, facilities, traits, or other additive setup. Put that setup in `common/scripted_effects/chaosx_startup_history_effects.txt` and call it from `on_startup`. Static named characters requiring persistent script tokens must be recruited in history. Do not use runtime `recruit_character` or attempt a character-scope transfer of an unrecruited identity. For dated identities, a bounded `history/general` recruitment pool on a dedicated dormant holder is valid; the holder must have no owned states or gameplay route and must not reuse an event-owned playable holder or test harness. Check date eligibility and original ownership before transferring from the original owner's country scope with `set_nationality = { target_country = <destination> character = <static_token> }`. Preserve availability dates, roles, identity flags, and retirement gates. Use `generate_scientist_character` only when a generated unnamed identity without a persistent character token is intended; never silently replace approved static identities with generated substitutes. Keep results from the user's game separate from code review; their absence does not prevent finishing the implementation.

Every registered country tag, including stateless dormant or internal history holders, needs valid default and ideology flag lookup coverage in `gfx/flags/` (`82x52`), `gfx/flags/medium/` (`41x26`), and `gfx/flags/small/` (`10x7`) because native flag consumers remain active without territory or a playable route.
Use the existing `chaos-redux-event-assets` workflow for this minimum native consumer package, with asset authorization limited to that package and intentionally shared institutional designs across aliases documented in the manifest.
Validate actual 32-bit uncompressed bottom-left TGA headers and decoded orientation against installed and repository examples, correcting flag files directly without UI or dynamic-routing workarounds.

### Country activation and ROOT

Stored state pointers refer to persistent map objects, so do not use COUNTRY-only `exists = yes` inside a STATE scope.
Validate the intended state with an appropriate documented native STATE predicate or registered state marker such as `has_state_flag`, together with its expected state ID using the documented identity semantics.
`scope_exists` is always true for variable scopes and does not validate the stored pointer.
Retain `exists = yes` checks in actual COUNTRY scopes, including a state's owner, controller, or stored country pointer.

Entering another country scope does not rebind ROOT.
Capture and annex callbacks retain their native ROOT: `on_annex` has the winner as ROOT and the annexed country as FROM, while `on_state_control_changed` has the new controller as ROOT, the old controller as FROM, and the changed state as FROM.FROM.
Trace each callback-to-helper scope chain before changing a receipt read.
When a country helper enters its exact source-state pointer, PREV there is the calling project owner, so read that owner's receipt through PREV rather than the callback's ROOT.
Within a state's stored-owner or holder country scope, return explicitly to the state through PREV for state flags.
PREV depends on the actual nesting, and ROOT remains valid wherever the contract explicitly requires it.

In a participant-country iterator reached from a country event, `ROOT` remains that event's original recipient across participant-country and state scope changes.
For targeted decisions, verify the actual callback's `ROOT`/`FROM` contract against installed documentation and a native precedent rather than assuming the owner's country-event contract: in the standard targeted-decision context, `ROOT` is the country taking the decision and `FROM` is its target country or state.
Capture the intended current participant with regular `save_event_target_as = participant` in that participant's country scope before entering state scope, then use `event_target:participant` for helper payer, victim, and target-country inputs and participant receipt or idempotence flags.
Using an unrelated `ROOT` can misattribute deaths and receipts even when the correct state was selected; retain `ROOT` wherever the documented callback or helper contract requires it.

For synchronous country transactions that can launch nested helper work, `ROOT` remains the original sender, temporary loop indexes are unscoped, and regular event-target names are shared throughout the effect chain.
Nested transaction setup can overwrite both indexes and named targets, so a regular event target alone is not a frozen transaction input.
Before any helper that can launch nested work, capture the proven source and origin pointers, actor/episode/receipt identity, and outer row indexes into recipient-owned normal private input fields.
At durable context commit, read those frozen fields and validate real object existence plus exact actor, episode, and receipt identity, rather than trusting overwritten aliases or `scope_exists` on a variable scope.
Restore outer row indexes only from that frozen frame, and clear the private fields on every success or rejection return while preserving the public immediate outputs.

Require matching actor/state nonce mirrors and exact source-state identity before closing a receipt or applying its accounting.
Use actor-owned persistent state pointers for asynchronous local projects and revalidate site identity and current holder at resolution.
Cleanup for a nonexistent or dead actor must not clear another living actor's global selection.
Partition recorded-owner and physical-holder accounting by the state disposition so each amount is debited and credited once even when both pointers identify the same country.
Review matching and stale nonces, distinct and identical owner/holder identities, repeated closure, and dead-actor cleanup along the exact source call chains.

When setup helpers require the recipient country as ROOT, invoke them from a hidden triggered-only country event received by that country; regular event targets carry through events fired by the originating effect chain.
Apply this ROOT contract to country scopes entered by `for_each_scope_loop` or debug dispatch as well.
Country-owned helpers need an explicit actor input contract or a generation-bound `country_event` relay rooted in the actual recipient.
Revalidate the saved recipient and generation before dispatching the helper, and cover direct actor entry and foreign-root debug/iterator entry separately.
Give a dormant tag owned land and a valid capital before entering capital-based setup or spawning units; use runtime meta construction when its TAG scope must be deferred until activation.
For a player-transfer bootstrap, queue the delayed recipient event before `change_tag_from` and make player transfer the final effect in that country block, so receiver scheduling does not reuse an invalidated country scope.
Inject file-scoped duration constants as meta arguments when generating a new script buffer, rather than leaving an unresolved `@` token inside generated text.
State transfers preserve stored variables, so a dedicated sandbox fixture must assign its intended responsible-country pointer before registration when it replaces an inherited site; ordinary historical responsibility should remain intact.

History grants can run before the recipient has a capital or other countries are initialized.
Keep their local grants and records, but queue capital-dependent scoring and diplomatic refreshes until country activation rather than dropping gameplay outputs.
Guard capital entry with an owned-state capital check; entering `capital_scope` to test whether it exists can itself raise an invalid-target error.

An exposed database array may include its reserved default object alongside real content.
Before excluding an entry, verify the array's registration order, the database's default-object initialization, and the consuming effect or trigger's validity check against installed documentation or other direct engine evidence.
Exclude only the confirmed reserved slot; do not guess that a numeric value or token is invalid, and preserve dynamic coverage of every real entry.
Keep read-only engine inspection distinct from executed runtime validation.

When additive tag-specific hooks can each request a full registry synchronization, coalesce their requests behind one pending recipient event instead of repeating the full consumer pass inside each hook.
Track scheduled delivery separately from pending work when an immediate refresh can consume that work before the queued event fires; this avoids scheduling duplicate receivers for a later request.
Set the scheduling flag before enqueueing, clear scheduling and pending-work flags before dispatch, and retain an immediate apply path for explicit setup or refresh.
Verify registration convergence, repeated requests, and refresh while a request is pending; preserve every registry consumer and package repair hook.

When bounded controller-country callbacks service a STATE-owned mechanic, keep each independent review or growth date persistently on that state and gate advancement on elapsed time.
Controller changes must preserve those dates so cycling controllers or receiving duplicate callbacks cannot accelerate the same mechanic's cadence.
Callback count is not elapsed time.

When a terminal record stops maintenance but an achievement or outcome still needs elapsed-time verification, schedule a one-time callback in the record owner's scope guarded by a persistent due date and a pending receipt consumed before verification.
Preserve the original due date across narrow controller changes, rescheduling only the remaining delay when delivery needs repair.
Revalidate the exact record and eligible actor tag under the existing identity contract, preserving any actor-specific invalidation.
Check early, duplicate, transferred, and stale-actor deliveries without adding a periodic world scan.

Compare a temporary paid benefit's duration with the recurring consequence cadence and state whether the intended rule samples current status or credits elapsed coverage, because activation and expiry can both fall between pulses.
When elapsed coverage is promised, preserve exact successful activation and expiry or earlier invalidation times instead of relying only on the current flag.
Aggregate the union of valid service intervals once against the existing consequence window, retain past valid service after expiry or control changes, and prune history only after its covered portion has been consumed.
Do not silently shorten the cadence or invent coefficients to compensate for missed service.
Validate expiry before the first pulse, intervals crossing window boundaries, overlapping activations, duplicate callbacks, and control transfer or other invalidation.

## Duration fields and constants

Use `script_constants` for shared tuning, but remember that some duration fields reject both `constant:` and variable tokens.

Before adding or extending `script_constants`, read the installed `common/script_constants/documentation.md` and `documentation/script_concept_documentation.md` (Script Constants), then inspect the existing group.
Every new group must begin with `schema` matching its key and data kinds (`int`, `fixed_point`, or a documented complex schema); new keys in an existing group inherit and must satisfy that schema.
A basic brace parse does not validate schema correctness.

**Variable arithmetic evidence:** Distinguish getter, modifier, normal variable and script constant representations, read installed `documentation\script_concept_documentation.md:184-215` and offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:425-434`, and record precision conflicts rather than inferring a universal normal variable maximum from mathExpr fixed point, modifier-only three-decimal precision or deprecated raw-manpower getter overflow near 2.1 million.
Audit actual source operations with a conservative bounded fixed-point model, explicit rounding/truncation assumptions and independent integer-floor boundary and count-type cases; a later division or clamp does not prove intermediate safety, and passing unbounded Python arithmetic does not prove engine behavior.
Never turn an unsupported numeric maximum into an eligibility gate or no-payment policy, or silently cap actual history.
For integer receipt validation, prefer modulo by one on scratch storage using documented `modulo_temp_variable` (installed `documentation\triggers_documentation.md:6442-6454` and `documentation\effects_documentation.md:4986-4998`) without rounding the receipt or adding maximum/count caps; use ratio quotient/remainder or rational scaled coefficients only when proven equivalent under the stated arithmetic assumptions.
Keep script constant category IDs unique across files so helpers with different schemas cannot redeclare the same category.

Known sensitive fields:

- `set_country_flag = { days = ... }`
- `set_global_flag = { days = ... }`
- any other timed field that throws `Malformed token` for either `constant:category.key` or a variable token

Fields in the list above are the ones that reject variable tokens as well, so they take a file-scoped `@NAME = literal` constant in the same script file passed as `days = @NAME`. Keep the value mirrored with the matching `common/script_constants/` tuning entry, and update both in the same change.

For any other duration field that rejects `constant:category.key`, assign the constant to a normal or temporary variable first and pass that variable to `days =`. A `meta_effect` must be used when the field accepts neither form.

Scripted effects and scripted triggers do not expand `$PARAMETER$` placeholders or accept named argument blocks as a parameter API in HOI4.
Pass inputs through documented variables or tokens and invoke the helper with `= yes`.
For literal-only fields, use `[PARAMETER]` inside `meta_effect` or `meta_trigger` `text` with a matching replacement declared on that meta block; consult installed documentation and a vanilla precedent before relying on a substitution.

Meta replacements are captured while the `text` is built, before its effects execute, so compute a delay or amount before invoking the meta block that consumes it.
If that computation belongs behind a dynamic meta guard, call a small owner helper after the computation inside the guarded text, and let that helper build the literal-consuming meta block.
Preserve eligibility, exactly one random draw, due-record ordering, and duplicate checks; do not move RNG ahead of the guard to resolve capture timing.
Verify dynamic support for the specific effect field against installed documentation, the offline wiki, and vanilla; a `country_event` variable-delay precedent does not establish `state_event` support.

## World threat framework

If an event or mechanic creates an existential external threat that should push other systems toward cooperation, integrate it with the shared world-threat framework instead of inventing a new one-off flag.

Current shared state:

- aggregate flag: `world_in_threat`
- source-count variable: `global.world_threat_source_count`
- per-source flags named `world_threat_source_<source>`; the registered list lives in `refresh_world_threat_state` and `docs/systems/world_threat_mechanic.md`
- per-source read triggers live in `common/scripted_triggers/chaosx_world_threat_triggers.txt`

Implementation pattern:

1. create or reuse a threat-specific source flag
2. write a threat-specific refresh effect that sets or clears that source flag from real gameplay conditions
3. update `refresh_world_threat_state` in `common/scripted_effects/chaosx_dynamic_effects.txt`
4. expose reusable scripted triggers if other systems should read the new source directly
5. document the threat source in the mechanic doc

Do not create a parallel global "cooperation crisis" or "threat active" flag for a single event chain. Everything should fold back into `world_in_threat`. The exact purpose of that flag is not yet planned.

## Formable nations as event surfaces

When an event can create or empower countries, consider whether it should create formable nation routes. A formable can be a major event payoff, a late-game ambition, a hidden branch, a rare evolution reward, a country package route, or a post-crisis consolidation goal.

Event implementation must keep formables aligned across:

- event flags and route flags
- decision category visibility
- focus unlocks
- scripted triggers for state control
- scripted effects for formation
- cosmetic tags and country names
- flags and portraits
- AI strategy
- achievements
- super-events where the formation changes world order
- cleanup after tag switch, annexation, puppet transfer, civil war, or route failure

Use scripted helpers for formation effects. Do not duplicate formation logic in events, decisions, focuses, scripted GUI buttons, and achievements. The decision can pay the cost and validate requirements, while a shared helper performs the identity change and logs the result.

Hidden formables should still have implementation coverage. They need reveal events, hidden flags, visibility triggers, localisation, assets, AI rules, and cleanup.

When exact state control is the formation proof, use the manifest-driven state-puzzle workflow under `.agents/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/`. Keep the generated state pieces, shared territory helper, formation decision, AI path, and every in-scope decision category synchronized. Complete the companion `category_attachment_audit.md` and list every category that exposes the formable, including shared or phase-specific categories.

When an event declares the strict `all_formable_categories` attachment policy, every in-scope formable category must set `scripted_gui = <generated_state_puzzle_gui_id>` and point to the generated `context_type = decision_category` block for its manifest. A category picture, text-only description, or separate status GUI does not satisfy this rule. A missing or mismatched category row is an incomplete formable surface and must remain a blocker in the handoff.

## 3D model and entity integration

When an event creates or changes a 3D unit or building, treat the model as a runtime contract across the event, unit or building definition, entity, `.asset`, `.gfx`, materials, textures, actions, and live map consumer.

The event implementation must use the `chaos-redux-3d-model-pipeline` handoff instead of trying to produce geometry or animations inside event work. The model handoff must include the exact runtime identifiers, processed texture paths, `.mesh`/`.anim` paths, action names, scale crosswalk, provider and Blender evidence, and reimport proof.

For a spawned unit, validate that `create_unit` is executed in a country or other supported scope, that the unit template and sub-unit are registered, that every emitted `unit_<id>_icon_small` text icon exists when required, and that movement uses a real exported action rather than a static substitute.

For a building or map entity, validate that the building has an entity, the entity key resolves in the `.gfx`/`.asset` chain, the province belongs to the specified state, the building command has the correct argument count, and the test province is visible at the intended zoom without an existing building hiding it.

For map-entity allocation, distinguish typed country/state scope references from documented plain numeric IDs, and do not assume `THIS.id` is a displayed state number or country ordinal.
Host fixtures must preserve that distinction and reject undocumented pointer arithmetic instead of seeding scope references with ordinary integers.
Allocate entity IDs from a proven numeric getter or an existing verified literal map ledger, then audit uniqueness and collisions against every existing and proof allocation because `create_entity` replaces an entity with the same ID.
Preserve scope pointers separately for identity and durable target links.
Source/model and collision checks do not prove native playback or save/restore entity identity, and do not establish that every native arithmetic conversion is impossible.

The main event agent owns the gameplay and runtime source wiring, final runtime copy synchronization, province/state placement, and review of live-consumer and in-game evidence supplied by the user. The user performs live-consumer and in-game validation. The 3D worker owns the bounded model package and must not claim event or in-game completion.
