# Event028 presentation capabilities, 2026-10-03

## Authority and disposition

This is the complete inline research handoff from chaosx_scripted_system_architect.
Research started on 2026-10-03 and the final citation review continued into 2026-10-04, Europe/Kiev.
The parent request authorizes read-only engine-capability research and this one new Markdown file.
No gameplay, GFX, GUI, localisation, installed-game file, asset, index, or commit was changed by this worker, and Hearts of Iron IV was not launched.
The shared tree continued changing during research.
The last observed HEAD before drafting was b60528470e00464641edf2e99f591e1599d33a8a, and the runtime source bytes cited below remained SHA-256 377003CD7FA7337BD60B95BEA4F22886D133595C842369B314AAD015BC1DCC8B.
A HEAD or an MCP workspace revision is not interchangeable with a physical file SHA-256.

Acceptance basis is the parent's explicit presentation-only request and the supplied accepted Part 2 trajectory, Part 3 nonnuclear separation, and Part 9 map-visual requirements.
The following helper names and consumer bindings are proposals for the parent, not implemented source or independently approved design changes.
F06 and F18 remain unresolved as completion findings.

Skills applied: .agents\skills\chaos-redux-events\SKILL.md, .agents\skills\chaos-redux-subagents\SKILL.md, .agents\skills\chaos-redux-event-assets\SKILL.md, and .agents\skills\chaos-redux-super-events\SKILL.md.
The skills kept the shared super-event/history framework parent-owned and separated graphical source linkage from native acceptance.
No skill was created or modified.
No probability-bearing helper or weight was designed or changed, so this research does not claim a probability audit.

## Capability findings

| Requirement | Supported finding | Disposition and proof limit |
| --- | --- | --- |
| Presentation-only placement on the map | Installed create_entity creates a graphical entity, with province/state/coordinate placement and an optional stored handle. | Native scripting API exists. It is a different API from nuclear detonation. This research has not executed it. |
| Existing ordinary blast art | Installed nuke_entity has attack animation, nuclear-sized particles, light, and sound. Vanilla raid presentation independently uses entity = "nuke_entity", animation = "attack". | Source-backed existing consumer and graphics package. No new mesh or artwork is required. |
| Existing large blast art | Installed nuke_big_entity uses nuke_big_mesh, larger blast particles, flash, and sound. | Existing large visual candidate. An explicit thermonuclear_bomb to nuke_big_entity mapping was not found in the inspected script definitions. That engine mapping and visual equivalence remain unobserved. |
| Activation of placed blast | Installed set_entity_animation accepts id and animation. attack is the existing entity state and mesh-local animation ID. | Exact command exists. Whether this effect enters the entity state and fires its particle/light/sound events is not explicitly documented. No installed scripted call site for this combination was found. Playback acceptance remains unresolved. |
| Zero nuclear effects | The proposed graphical route contains no launch_nuke, raid execution, nuclear effects, damage, or nuclear callback invocation. | Strong source separation. Native statistics, achievements, callbacks, damage, and save/MP behavior were not measured. No zero-consequence runtime claim is made. |
| Durable intended-country identity and geography | Current code stores country ID/pointer, state ID/pointer, capital status, transaction and timing context. | Existing representation is sufficient for identity and geographic lock, not for frozen display. |
| Durable ruling ideology context | current_party_ideology_group can be copied to a normal global variable. Vanilla and Chaos Redux both do this. | Supported narrow snapshot, independently of a later country existence check. |
| Durable arbitrary current display name | Current GetName is a localisation getter. No documented/exemplar-backed arbitrary string storage effect or current-name localisation-key getter was found. | Blocked separately. Neither an ordinary variable nor an event target is a string snapshot. |
| Durable current flag/cosmetic context | GetFlag is a live getter. has_cosmetic_tag checks a supplied literal. No generic current cosmetic-tag/flag-texture getter or flag snapshot API was found. | Blocked separately. Saving ideology alone does not capture cosmetics, flag lookup overrides, or the current texture. |

The conclusion is not that all engine versions categorically lack a string facility.
The precise result is that the current installed documentation and inspected source precedents do not establish one that meets this feature's arbitrary-country snapshot contract.

## F18: current detonation calls

The current source is common\scripted_effects\028_asteroid_incoming_runtime_effects.txt.
Its main-center block at lines 1219 to 1230 is:

~~~txt
CONTROLLER = {
	set_global_flag = asteroid_incoming_visual_strike_active
	launch_nuke = {
		state = PREV
		controller = THIS
		use_nuke = no
		nuke_type = thermonuclear_bomb
	}
	clr_global_flag = asteroid_incoming_visual_strike_active
}
~~~

The fragment-center block at lines 1272 to 1281 uses the same pattern with nuke_type = nuclear_bomb.
In that nested block THIS is the current controller and PREV is the affected state.
Neither the attacker scope nor the stockpile setting makes the command presentation-only.

Installed effects_documentation.md lines 4745 to 4761, freshly read through MCP, declares COUNTRY scope and no supported targets:

~~~txt
launch_nuke = {
	provinve = 42
	state = 42
	controller = GER
	use_nuke = yes
	nuke_type = nuclear_bomb
}
~~~

The misspelling provinve above is in the installed documentation itself.
The offline wiki's Effects line 1517 specifies province, not provinve, and says the effect nukes the selected province.
The installed comment for use_nuke says only that it consumes a nuke when specified.
There is no documented visual_only, damage = no, stats = no, or callback-disable parameter.
The command is therefore unsuitable for the parent's nonnuclear presentation boundary regardless of use_nuke = no.

The checked project precedent common\scripted_effects\023_sov_nuclear_bombs_runtime_effects.txt describes launch_nuke as detonation.
The current Event023 on_nuke_drop wrapper at common\on_actions\023_sov_nuclear_bombs_on_actions.txt:91 checks the asteroid global guard.
Such a script guard affects only the guarded scripted consumer and its execution timing.
It does not prove that native damage, statistics, achievements, or a later callback are suppressed.
The fragment visual follows the asteroid's measured transaction, so any native detonation damage is outside that receipt.
No extra executed casualty, achievement, or condemnation is fabricated by this report.

## Installed graphical command registry

The following are generated installed effect-documentation entries, not invented spawn_entity or play_gfx syntax.

| Command | Scope/targets | Exact documented fields and behavior |
| --- | --- | --- |
| create_entity | any / any | entity names a GFX entity. Optional id addresses it later and replaces an existing entity with that ID. Optional var stores its ID. x and y position it. province or state places it at that object's coordinate. Combining a coordinate with province/state shifts that coordinate. z shifts height. rotation is radians. scale scales it. min_zoom controls the zoom threshold. visible names a scripted trigger evaluated in player-country scope. |
| set_entity_animation | any / any | id = 123, animation = "shoot_lasers". The section prose incorrectly says rotation, but the section name, command, and field are animation. |
| destroy_entity | any / any | destroy_entity = 123 deletes the addressed graphical entity. |
| meta_effect | any / THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL | text is compiled and executed after named replacements. Installed example uses COUNTRY = "GER", POW = 42, and debug = no. |

Exact line spans are create_entity:3046 to 3068, destroy_entity:3528 to 3537, meta_effect:4833 to 4851, and set_entity_animation:6826 to 6837.
The offline Effects page corroborates create_entity/destroy_entity/set_entity_animation at lines 366 to 372 and gives examples at 496 to 512 and 564 to 570.
No inspected entry promises automatic destruction after a one-shot animation.
No inspected entry promises that arbitrary variable tokens or constant: values are accepted by every positional or ID field.
Emit literal numeric parameters through meta_effect rather than extending the parser contract by assumption.

## Existing vanilla entity and particle chain

C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx\entities\nuke.asset lines 1 to 25:

~~~txt
entity = {
	name = "nuke_entity"
	pdxmesh = "nuke_mesh"
	state = { name = "attack" animation = attack looping = no
		event = { time = 0.5 particle = "nuke_particle" keep_particle = yes sound = { soundeffect = "nuke" } }
		event = { node = nuke time = 0.5 particle = "nuke_top_particle" keep_particle = yes light = nuke_light }
	}
	scale = 0.5
}
entity = {
	name = "nuke_big_entity"
	pdxmesh = "nuke_big_mesh"
	state = { name = "attack" animation = attack looping = no
		event = { time = 0 light = nuke_big_light sound = { soundeffect = "nuke_big_light_flash" } }
		event = { time = 0.5 particle = "nuke_big_particle" keep_particle = yes sound = { soundeffect = "nuke_big_explosion_and_fire" } }
		event = { time = 4 node = nuke time = 0.5 particle = "nuke_big_top_particle" keep_particle = yes light = nuke_flash }
	}
	scale = 0.7
}
~~~

These entity event blocks contain graphics and sound fields, with no Clausewitz gameplay effect body.
That supports a graphical-consumer separation inference, not an observed native-behavior result.
The big top event contains time twice in the installed source.
Its effective timing must not be guessed.
nuke_flash is referenced here, but the bounded installed gfx\entities and gfx\particles text scan found no declaration for it.
nuke_light and nuke_big_light are declared in gfx\entities\map_lights.asset at lines 100 and 228.
The unlocated nuke_flash symbol is a source-resolution limitation, not proof that the engine fails to render the entire effect.

gfx\entities\nuke.gfx lines 3 to 15 registers:

~~~txt
pdxmesh = {
	name = "nuke_mesh"
	file = "gfx/models/nuke.mesh"
	animation = { id = "attack" type = "nuke_animation" }
	scale = 1.0
}
pdxmesh = {
	name = "nuke_big_mesh"
	file = "gfx/models/nuke.mesh"
	animation = { id = "attack" type = "nuke_animation" }
	scale = 1.0
}
~~~

gfx\models\animations_test.asset lines 6 to 9 registers nuke_animation with file = "nuke_attack.anim".
gfx\entities\particles.gfx:664 to 685 registers nuke_particle to nuke_file, nuke_top_particle to nuke_top_file, nuke_big_particle to nuke_big_file, and nuke_big_top_particle to nuke_big_top_file, each at scale 1.
Those types are defined by the four existing gfx\particles\environment\nuke*.asset files.
For example, the ordinary shockwave source size is 200 at nuke.asset:40 and the large source size is 300 at nuke_big.asset:40.
Entity scales are separately 0.5 and 0.7.
Those numbers are source values, not a measured on-screen size ratio or a calibration instruction to multiply scale again.

The linked sound definitions were found in sound\sound.asset:964 to 969 and sound\soundeffects.asset:1156 to 1170 for the large blast.
The ordinary entity already references the existing nuke sound.
This is map-presentation audio, independent of Event028's musical super-event cue.

Vanilla common\raids\air_raids.txt:979 to 982 independently uses:

~~~txt
visual_effect = {
	entity = "nuke_entity"
	animation = "attack"
}
~~~

This is a raid-definition consumer block, not a free effect callable inside Event028.
Do not paste visual_effect into an event or launch a raid to obtain the presentation.
The precedent verifies the entity/attack pairing, not create_entity playback or nuclear-free raid execution.

No custom project thermonuclear entity override was found in the inspected gfx\entities definitions.
Current project thermonuclear presentation call sites use launch_nuke with thermonuclear_bomb.
That call-site precedent cannot prove a separate pure-VFX helper already exists.

## Narrow graphical consumer plan

Proposed parent-owned helpers are asteroid_incoming_emit_main_visual, asteroid_incoming_emit_fragment_visual, and asteroid_incoming_clear_visual.
The main and fragment helpers have STATE scope, use a validated land-province anchor belonging to the already selected state, and store one graphical handle on that state.
Their inputs are the anchor province, transaction identity, and any explicitly validated render settings.
Their output is the graphical entity handle and a presentation receipt.
Their only intended external side effects are the entity, particles, lights, and existing map sound.
They must not change nuclear records, state damage, population, Deaths, Chaos, diplomacy, fallout, countries, units, or controllers.
Call sites are the two presentation blocks in asteroid_incoming_apply_state_profile.
There is no reason to place this owner-specific orchestration in the neutral chaosx_dynamic_effects registry.

The following is a documented-command candidate, not executed or validated gameplay code.
It omits a manually chosen ID using the documented var handle facility, and emits province and the later handle as literal numbers.
The caller must initialize the numeric province input in its own frame and validate actual membership first.

~~~txt
# STATE scope. The input is a verified province in this exact state.
meta_effect = {
	text = {
		create_entity = {
			entity = nuke_big_entity
			province = [PROVINCE_ID]
			var = asteroid_incoming_visual_entity_id
		}
	}
	PROVINCE_ID = "[?asteroid_incoming_visual_province_id|.0]"
}
meta_effect = {
	text = {
		set_entity_animation = {
			id = [ENTITY_ID]
			animation = "attack"
		}
	}
	ENTITY_ID = "[?asteroid_incoming_visual_entity_id|.0]"
}
~~~

The fragment consumer changes only the entity literal to nuke_entity.
No numeric scale override is chosen here, and no bomb type is passed.
The documentation supports storage of the handle through var, but this worker found no installed scripted auto-handle blast precedent.
Actual handle storage, state-event activation, default visibility/placement, and lifecycle must remain unresolved until native evidence exists.
The native set_entity_animation entry does not explicitly say whether particle/light/sound state events run.
Do not claim its mere availability settles playback.

An additional source-backed activation mechanism exists at the entity-definition level: default_state = "attack".
Installed gfx\entities\particle_entities.asset:162 to 180 uses it with a one-shot attack state and particle/sound events.
Installed gfx\entities\buildings.asset:800 to 803 separately verifies the clone/name syntax.
Those precedents do not prove that a clone override or a newly registered default-state alias preserves every blast behavior.
No alias was written, no new asset was produced, and no engine file was altered.
A parent implementation may investigate an owner-specific registration reusing the exact existing mesh/particle package if needed, but this report does not substitute such an unvalidated registration for the accepted existing visual.

### Placement, IDs, cleanup, and fragment sequencing

The current Air Winter source at common\scripted_effects\fallout_consolidated_effects.txt:8094 to 8098 records a prior live issue with state placement and seven-digit IDs producing invalid parameters and entities at map origin.
That is project-recorded evidence, not a reproduction by this worker.
Its current helper at 8241 to 8259 emits province placement and literal numeric ID/position fields through meta_effect.
Its destroy helper at 8184 to 8188 emits literal destroy_entity.
The approved Kaiserreich reference 00_ambient_object_effects.txt:1 to 40 also uses create_entity with explicit coordinates and small numeric IDs.
Neither precedent executes the nuke entity's attack state.

Do not copy Air Winter's IDs.
Its current reserved bands are ground 3000, primary particles 5000, secondary particles 7000, vegetation 9000, and hydrology 11000, with state IDs added.
The native documentation says an existing matching ID is replaced.
If the parent selects deterministic IDs instead of the optional native handle, it must audit all consumers and prove collision-free allocation.
There is no documented native ID-size limit in the inspected create_entity section.

A cleanup candidate, entered in the same state that owns the recorded handle, is:

~~~txt
meta_effect = {
	text = { destroy_entity = [ENTITY_ID] }
	ENTITY_ID = "[?asteroid_incoming_visual_entity_id|.0]"
}
clear_variable = asteroid_incoming_visual_entity_id
~~~

The source documentation does not establish when attached keep_particle effects finish or whether destruction preserves or kills them.
Immediate destruction could erase the required visual.
A country_event hours/days delay is game time, while entity event time/particle life are presentation time.
Their relationship at pause and different game speeds is not established by these sources.
Cleanup timing, replay behavior, and the required short main-then-fragment sequence therefore remain native acceptance gaps.
No new periodic world iterator, dummy unit/country, nuclear ledger reset, suppression race, delayed punishment, or weaker visual is proposed.

The bounded map lookup examined state 64 and province 6521 as a reference pair.
Installed history\states\64-Brandenburg.txt:57 to 58 places 6521 in state 64.
This is a placement specimen, not the locked Event028 target and not universal province coverage.
Every real selected main/fragment state needs its own validated anchor.
The fixed state must never be redirected to another state merely to obtain a visible effect.

## F06: identity snapshots and exact scope contract

Current acceptance at runtime:540 to 555 saves the following:

~~~txt
event_target:asteroid_incoming_candidate_country = {
	save_global_event_target_as = asteroid_incoming_locked_country
}
event_target:asteroid_incoming_candidate_state = {
	save_global_event_target_as = asteroid_incoming_locked_state
	save_global_event_target_as = asteroid_incoming_original_target_state
	set_variable = { global.asteroid_incoming_target_state_id = THIS.id }
}
event_target:asteroid_incoming_candidate_country = {
	set_variable = { global.asteroid_incoming_target_country_id = THIS.id }
	set_country_flag = asteroid_incoming_original_target_country
	save_global_event_target_as = asteroid_incoming_original_target_country
}
~~~

The capital boolean is assigned in the state block at 545 to 549.
No stored display string, current-name localisation key, cosmetic token, or flag texture is assigned here.
The country remains a live object even when referenced by a durable pointer.

Installed loc_objects_documentation.md:225 to 231 exposes GetName and GetNameWithFlag.
Lines 253 to 255 expose GetTag.
Lines 309 to 311 expose GetRulingIdeology.
Lines 381 to 383 expose GetFlag.
Each is described as reading the current country.
GetOldName:421 to 423 is also a getter, not a captured historical display.
The offline Localisation page:576 to 580 explains that old-name getters exclude cosmetic tags.
They cannot represent a lock-time cosmetic identity.

Installed dynamic_variables_documentation.md:232 to 233 exposes current_party_ideology_group and says it returns the ruling ideology-group token.
The same document:710 to 711 exposes original_tag.
It does not expose a current cosmetic-tag token, nameLocKey, cosmeticTag, current flag path, or current display-name string.
The installed COUNTRY localisation-property list and local script/documentation search likewise did not establish GetNameLocKey or GetCosmeticTag.

Installed triggers_documentation.md:3605 to 3613 documents has_cosmetic_tag = INS1.
It tests one supplied cosmetic tag.
It does not enumerate or return the current cosmetic.
Vanilla common\scripted_triggers\00_scripted_triggers.txt:724 to 728 checks known BYZ_UNIFIED variants explicitly.
That demonstrates bounded matching, not a generic arbitrary-country snapshot getter.

### Supported narrow ideology binding

At successful lock, inside the explicit candidate-country block, the following field is source-supported:

~~~txt
event_target:asteroid_incoming_candidate_country = {
	set_variable = {
		global.asteroid_incoming_target_ruling_ideology_token = current_party_ideology_group
	}
}
~~~

This captures the selected country because THIS is the candidate here.
It must not use ROOT.current_party_ideology_group, since ROOT is the chooser/event receiver.
Vanilla common\scripted_effects\00_scripted_effects.txt:4195 to 4197 stores ROOT.current_party_ideology_group in a normal variable.
Chaos Redux common\scripted_effects\015_utopia_manifesto_identity_effects.txt:165 to 169 stores the current scope's ideology token without ROOT.

Supported display distinction, using the offline token-variable documentation:

~~~txt
[?global.asteroid_incoming_target_ruling_ideology_token.GetTokenKey]
[?global.asteroid_incoming_target_ruling_ideology_token.GetTokenLocalizedKey]
~~~

The first yields the raw registered token, such as democratic.
The second asks for that token's localised text, when its token type/key supports that lookup.
Neither expression yields a country's name, cosmetic tag, flag filename, or frozen pixels.

### Strings, localisation keys, tokens, and escaping

A raw display string such as United States, a localisation key such as USA_democratic, a country pointer, and a registered ideology/database token are different values.
Normal variables store numbers or typed object/token values.
The token: prefix does not establish an arbitrary Unicode string store.
The wiki's Data structures:955 to 985 documents tokens as indexes into a token string table and identifies supported registered types.
Its advanced raw-language-token observations do not establish interning of arbitrary runtime GetName output.
No verified vanilla/project precedent was found for storing an arbitrary GetName/GetFlag result as a durable token.

Bindable localisation objects and formatted-localisation strings are documented in script_concept_documentation.md:12 to 21 and 162 to 180.
They are contracts of accepting text fields.
They do not turn every set_variable value into a persistent bound string.
A field called localization_key selects a localisation key, not a lock-time character sequence.
Dynamic scripted localisation can construct a key when displayed, as documented in offline Localisation:706 to 719.
That still needs an exact captured immutable input identifying the chosen key.
The installed getters above do not provide the selected current-name key.

meta_effect can substitute strings into script.
It does not create a string-storage API or guarantee automatic escaping.
Interpolating a display name containing a quote, backslash, bracket, line break, or formatting marker into compiled script cannot be described as safe without a verified escaping and storage contract.
Therefore no executable token:[NAME], set_localisation, save_scope_value_as, GetNameLocKey, GetCosmeticTag, nameLocKey, or cosmeticTag binding is proposed.
The queried save_scope_value_as reference search returned zero results.

The offline Localisation page:216 to 219 says @TAG displays the default gfx\flags\TAG.tga.
It is not proof of a lock-time cosmetic/ideology flag.
Similarly, GetTag plus the stored ideology token cannot reproduce arbitrary cosmetic names or flag lookup exceptions.
No static base-tag fallback is offered.

Scripted GUI image properties accept a sprite string or scripted-localisation result, documented in offline Scripted GUI:391 to 440.
The current shared super-event consumer uses super_event_image.image = "[GetSuperEventImage]".
That is a display consumer, not a capture API.
A generated flag sprite identifier would require a proven lock-time flag identity/texture resolver first.
Current GetFlag output is not documented as a sprite name or a texture path.

### Proposed display bindings and unresolved inputs

| Consumer need | Required durable input | Binding status |
| --- | --- | --- |
| Intended target country name in news, super-event text, and history | A stored literal name with safe serialization, or the exact selected immutable localisation token/context | No supported generic capture binding established. Keep F06 blocked. |
| Intended target flag | Exact lock-time resolved flag/cosmetic/ideology context and an existing compatible flag/sprite consumer | No supported generic capture binding established. Keep the flag part separately blocked. |
| Lock-time ruling ideology | global.asteroid_incoming_target_ruling_ideology_token | Supported capture and raw/localised token display as above. |
| Original country identity | Current saved original-country pointer and numeric ID | Preserve as identity, with existence checked only when executing country effects. |
| Geographic lock | Current original/locked state pointers and state ID | Preserve independently of annexation and current country cosmetics. |
| Current crater controller | Enter the stored state, then CONTROLLER | Read live only for operational control and recovery. Never overwrite original intended-target identity. |

At minimum, supported identity/ideology fields belong to the successful acceptance transaction before scheduling the two-day resolver.
Canceling confirmation must not rewrite a prior accepted snapshot.
Historical display context must be associated with the incident/transaction used by its existing parent-owned history row, and retained after presentation close.
No new shared UI framework or country registry is designed here.
The report does not populate unavailable fields with a guessed country-name/flag value.

In event localisation, named targets use [asteroid_incoming_original_target_country.GetName], without event_target: in the namespace.
A variable namespace requires the question mark, as in [?global.some_token.GetTokenKey].
In script blocks the explicit event_target: prefix remains required.
PREV follows nesting, ROOT remains the original event receiver, and FROM depends on the event/callback origin.
In the shared player_context GUI, ROOT is the viewing player, not the intended target.
Prefer explicit global snapshot fields for display and explicit stored state/country targets for effects.
Current-country existence checks must not become a prerequisite for reading a truly stored historical text field if such a field becomes supported.

## Constants, target cleanup, and migration boundaries

No constants were added.
A parent-owned visual settings category may hold validated numeric presentation tuning such as zoom, vertical offset, and cleanup timing, while entity IDs/handles and transaction receipts remain runtime data.
Installed script-constant documentation explicitly limits constant support to accepting fields.
Resolve constants through variables and meta literal injection for fields whose parsing is not established.
Preserve the existing entity scale until an actual source/runtime crosswalk establishes the desired override.
No balance tuning table, damage percentage, or AI target is changed by this plan.

Do not create event targets for arbitrary text.
Existing original-target and locked-state targets remain the scope pointers.
Clear only transient graphical handles and presentation receipts after verified cleanup, and reject stale-transaction cleanup so it cannot destroy a later incident's entity.
Preserve historical identity/display receipts for existing history consumers.
Never use clear_global_event_targets or nuclear-ledger resets as visual cleanup.

Migration, within the parent's accepted scope:

1. Validate a graphics-only activation/lifecycle contract for the exact existing normal and large entities.
2. Supply a verified same-state province anchor and preserve the current asteroid damage/Death receipts.
3. Replace only the two launch_nuke presentation call sites with the corresponding owner helper.
4. Remove dependence on a global nuclear-suppression window for the new visual path after checking all consumers.
5. Keep name and flag completion blocked until an actual supported capture/consumer API is supplied.
6. Add owner helper documentation with scopes, inputs, defaults, handles, cleanup, call sites, and native evidence limits when implementation occurs.

No step above was implemented in this research.
The unavailable name/flag API must not be repaired by a new country tag, clone, borrowed annexer identity, hidden world consequence, or weaker presentation.

## Meaningful validation and native acceptance limits

Research verified the installed effect entries, exact normal/large entity and animation linkage, particle registrations, ordinary vanilla raid visual consumer, current Event028 detonation blocks, project graphical placement precedent, and vanilla/project ideology snapshots.
These checks could change the implementation choice, notably replacing a nuclear detonation API with a graphical entity API.
No asset pixels were accepted as native-behavior proof.

The following are concrete acceptance questions for parent/user-owned evidence, not instructions to this worker to launch the game:

- Can a placed normal and large entity enter attack and emit the same complete particles, lights, and map sound as the accepted existing visuals?
- Are the main visual, all fragment visuals, and their order visible at relevant zoom, pause, game speeds, and human-country views?
- Does graphical handle creation/readback/destruction work without replacing another system's entities or leaving replay/save/MP leaks?
- Does each visual leave native nuclear-use statistics, achievements, stockpiles, callbacks, condemnation, retaliation, fallout, nuclear Chaos and Deaths untouched?
- Does each fragment leave population/building values equal to its measured asteroid receipt, without an extra physical detonation?
- For any subsequently supported snapshot API, do cosmetic changes, ideology changes, annexation, and state-controller transfer preserve the original intended name/flag while operational reports use the current holder?
- Can a stored name containing non-ASCII text or quote/format characters survive serialization and render correctly without meta-script injection?
- Does closing the shared super-event or resolving a later incident leave the earlier history row's snapshot intact?

These native checks were skipped because this worker is read-only and all game validation belongs to the user.
No current capability finding claims native playback, a frozen name, a frozen flag, or full Event028 completion.

## MCP results and precise limitations

The connected ALL_TOOLS catalog and schemas were inspected.
These tools report offline source graphs and declared scenario models, not observed engine execution.
Reference context/search/read, older source_lookup, event inspect/render/compare, map inspect, and GUI inspect were exposed.
source_lookup has no view/keyPath fields in this connection.
script_validate was absent.
Server version/health and native task negotiation were not established, so helper_expansion, jobs, and tasks were not used.

Fresh connected workspace ID is mod_chaos_redux_ea3b2d67c2c0.
The fresh reference reads succeeded after the client reconnect.
Earlier submitted operations whose client handles were lost have unobserved terminal status, not a fabricated 600-second timeout.
The last fresh calls listed below returned real results.

| Route | Exact result/evidence | Bound |
| --- | --- | --- |
| reference_context event | OK. Installed effects and offline wiki sources identified. | Initial limit eight omitted On actions and Localisation. Relevant Localisation rules were subsequently obtained through the localisation context and direct cited reads. Context headings alone were not counted as detailed rules. |
| reference_context localisation | OK. Installed loc objects/formatters plus offline namespaces identified. | Detailed current-country getters, contextual/bindable rules, and GUI/text sections were read locally with hashes below. |
| reference_search/create_entity and reference_read | OK. Section ID 73de3e3b4f224f7c577b73832dd99c30f4b0d147419037c53e2d5cd9cfe2abe2, revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af, lines 3046 to 3068. | Entire relevant section read, nextLine null. |
| reference_read/launch_nuke | OK. Section ID f5f15283912e2ff586286ef1cf2185c9ab7714f4e5acace73ddbbe837ebeefb2, same effects revision, lines 4745 to 4761. | Entire section read, nextLine null. |
| reference_search/token and reference_read | OK. Section ID 68deaf09648560a92ed1eb4308c2a016cb816d339224d4432e5be9f2c055d592, revision 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4, lines 955 to 972. | Entire token-valued section read, nextLine null. Advanced-token caveats also read locally at 973 to 985. |
| source_lookup/asteroid_incoming_apply_state_profile | OK. Fresh index revision 4dd167ec0da1ba280bf9661b0fea3e837d6bcfc16e1e412e05f38225c2b56fd7, one unshadowed definition, lines 1217 to 1234 returned, nextLine 1235. | Definition spans 1171 to 1311. Remaining relevant source was read directly, including fragment lines 1272 to 1281. References deliberately disabled. |
| source_lookup/nuke_big_entity | OK with zero definitions, index revision 5119b42a3ba2d6b26e4bc505201ae413e1d7b99c1b7d9bed04c794caaba061fa before reconnect. | Not evidence that the entity is absent. The actual installed GFX source was read. A kind=entity retry had no observed result after handle loss. |
| event_inspect trace | Fresh .4 selector, depth/node/edge each one, expandHelpers false. EVENT_INSPECTED_PARTIAL, focused, revision 828ca59a9a1fa1a44d0bf5a12bce75e5cb65e717d2d055388d5ac1994d71fe92. | Zero projected helpers, workspace helper/lifecycle passes deferred. Inline inventory returned 64 of 388 paths. Not a native or helper-lifecycle audit. |
| map_inspect | MAP_LOOKUP_COMPLETED, lookupOnly true, stateIds [64], provinceIds [6521], includeOverview false. Revision c693134be279ed7d9bfc46b8b521eea2a473436a798198101a4190e5c3eb2a3e. | One state/one province inspected, no unknown province IDs. Full map validation/overview not requested. Inline inventory returned 64 of 2065 paths. |
| gui_inspect | GUI_INSPECTED for existing chaosx_super_events, scenario event028_presentation_capabilities_readonly, generatedScenarios enabled false. Revision 51c712e5c19ac0956275b4a191132dcee192b5c3111f4b888b17de1c51257e5c. | Eight elements inspected. Five unresolved dynamic values, missing Quote of the Day localisation, clipping/overlap findings and validation.passed false. This minimal source-consumer specimen supplied no complete Event028 world fixture and is not a visual acceptance report. Shared layout remains parent-owned. |

Initial request-shape mistakes were corrected rather than counted as service gaps.
event_inspect requires selector.kind = event.
GUI inspection requires windowName together with scenario.id.
Initial reference_read attempts used a root-heading section ID for a later section and correctly returned REFERENCE_POSITION_OUTSIDE_SECTION.
The subsequent targeted search and matching-section reads above succeeded.
No source-only substitute is presented as matching MCP engine evidence.

Returned artifact references:

- Event: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bc1b93a0c577cab799456ed3c73f56196b232a8f4b283fc798da55b8c8739e53/44082249c887c74bb639f87a17e1a6e1d35970a749b4bccfd3a0e1cf604d51c9/event-trace-828ca59a9a1f.json, declared size 1,070,813 bytes.
- Map: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f20c456b5db785950cb91ce47a1c9d4bcb0b26d443c17337c85218ba09081c37/075a83981d81eb341aff8603b9c9af31d56453fd157c14fb8042a033d4f46462/map-lookup.c693134be279ed7d.7f4bb8ad66327b5e.json, declared size 240,017 bytes.
- GUI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9432d1236421241647df597d11376de110f5bf93cb1d808b5ab1d72b554cf9c9/6af7de7d31b383f6428a92bff4b3e2a44d80e4718f5a4eb16cc6efb65e5fbe64/gui-inspect.51c712e5c19ac095.json, declared size 492,857 bytes.

The live artifact template advertises byte-offset/length reads.
Full map artifact retrieval and the offset=0,length=3000 retry both returned MCP -32603: Artifact provenance manifest is unavailable.
The fresh event artifact's offset=0,length=3000 read returned the same exact blocker.
No complete resource body or verified retrieved artifact hash was available from those reads.
The supplied URI hashes are server-declared identities.
The GUI result's inline diagnostics were retained, and its linked bulk report was not consumed.
No current successful event render/compare result was observed after client handle loss.
No source changes were made to compare, and no GUI layout/render construction task was undertaken.

## Exact local source identities

All paths below are Windows paths.
R means C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux.
V means C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV.
K means C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\1521695605.
These root aliases plus each suffix resolve an exact absolute path.
Hashes are physical file SHA-256 values, not acceptance labels.

| Path under root | Relevant lines or sections read | SHA-256 |
| --- | --- | --- |
| R\AGENTS.md | Required repo instructions | 38E479CB75828BA888860BE8BC3739F9286C0D925CC7D8DE5ECD3B8DADEC46CF |
| R\docs\specs\028_asteroid_incoming_specs\028_asteroid_incoming_spec_part_2_targeting_and_trajectory.md | Confirmation, snapshot, two-day lock and original/current-holder separation, entire spec read | D7CB71FB76B018A604427CDE9F6D84689EB620D97ED59BA9921364840167F20D |
| R\docs\specs\028_asteroid_incoming_specs\028_asteroid_incoming_spec_part_3_impact_damage_and_aftermath.md | Entire spec, especially nuclear-system separation | F81C3B5C3FDBAF72879DE8AF5C34A1DF1D93926D2EA5DF5D9640C4F6878973E0 |
| R\docs\specs\028_asteroid_incoming_specs\028_asteroid_incoming_spec_part_9_visual_and_audio_direction.md | Entire spec, main/fragment map presentation and independent music role | 84D700D60E6E627E1F01DF0F6B97C9DC88C346647396BA6200BE8252A48F3209 |
| R\docs\plans\028_asteroid_incoming_plans\subagent_handoffs\completion_audit_20261003.md | F06:154 to 167, F18:349 to 367, MCP limits:506 to 550 | 692A8254508C782B696D0BCDB3A6E3661AD1C7ABF4CA305DBE7D45FB89B216D7 |
| R\common\scripted_effects\028_asteroid_incoming_runtime_effects.txt | 522 to 579, 1171 to 1290, targeted surrounding presentation/receipt source | 377003CD7FA7337BD60B95BEA4F22886D133595C842369B314AAD015BC1DCC8B |
| R\common\scripted_effects\chaosx_dynamic_effects.txt | Registry header, existing dynamic helper contracts and token interpolation | F9591FE2BEAB4AC7570813BA76D1B4DBF63FC9FF10DC3315ADFFFCCAB2A895C2 |
| R\common\scripted_effects\chaosx_dynamic_effects.md | Owner boundary and documented dynamic helper interfaces | ABA7E66BDC5D81ACC27D1B335EA3C23CAFB8466C909570B23DE3471F42492DE6 |
| R\common\scripted_effects\fallout_consolidated_effects.txt | 8092 to 8135, 8160 to 8280, graphical placement and cleanup | 0985283AB00A337493065E9EBCDC4CD0BD042DAAB4C5371D8D77622CB6E8D0ED |
| R\common\scripted_effects\015_utopia_manifesto_identity_effects.txt | 151 to 172, ruling ideology snapshot | 6E1E31A550C4B9267301E5393733E69C0A011D78BAA154FF1E11F110CCABD5F5 |
| R\common\scripted_effects\023_sov_nuclear_bombs_runtime_effects.txt | Native launch boundary at 703 to 743 | 5C2780FA15193EA7A815FB5CA340B46C92F6B40DD7B343FC68C64D533A0E279A |
| R\common\on_actions\023_sov_nuclear_bombs_on_actions.txt | Guarded callback at 91 and surrounding scope contract | 8D350CCBD1F73B049C05ABAE91FFD41070D371341883D8794999ECF4BA65D7A5 |
| R\common\script_constants\fallout_consolidated_constants.txt | 2715 to 2725, occupied graphical ID bands | 79ABF5C6D7746077DC8EEDFA98AEEC432EF651D6B9D59E59E5C6CCE7076FA010 |
| R\common\scripted_guis\chaosx_scripted_gui_super_events.txt | 1 to 40, player context and image binding | 1B0BF25E6226D906E35CAA9010E8A24547B38FFB9B57A9DBCCBF38235F29BC2B |
| R\interface\chaosx_super_events.gui | Existing chaosx_super_events window and textbox identifiers at 129 to 206 | C3C681D008C96832A1B5B543F8D84DD19D04B8BB737FF55EDB40555D82E7E8CC |
| R\localisation\english\028_asteroid_impact_l_english.yml | Live target/name/flag strings, notably 6 to 8, 24, 30, 67, 92 to 96 | D341770684E8B4CEACDFD7F3CDA501636E41A8CFAA370AD0B30710C58D5D41CC |
| R\paradox_wiki\Effects - Hearts of Iron 4 Wiki.md | 366 to 372, 496 to 512, 564 to 570, 1517 | 997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C |
| R\paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md | 263 to 301, scoped/temporary variables, 955 to 985 | 62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4 |
| R\paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md | 216 to 219, namespaces/getters, 649 to 650, 656 to 728 | 1A8F72362A34B4BB653186746B9FAE0B98E463205CB02F12CCF2C3D9CCD3A064 |
| R\paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md | 260 to 263, ROOT/THIS/PREV/FROM rules | 18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49 |
| R\paradox_wiki\Scripted GUI modding - Hearts of Iron 4 Wiki.md | 144 to 164, 391 to 440 | B07D850EA78C4E1E3FC113574059AD2F3EA37DF320B9259128D66814023C1F30 |
| V\documentation\effects_documentation.md | 3046 to 3068, 3528 to 3537, 4745 to 4761, 4833 to 4851, 6826 to 6837, 7888 to 7907 | 2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF |
| V\documentation\dynamic_variables_documentation.md | Country entry search, 232 to 233, 710 to 711 | 538525747F0C285062C9CE8DB14B4E07C3CF6BAC1013115FA4F57291CB4EBDDA |
| V\documentation\loc_objects_documentation.md | Entire COUNTRY property inventory at 185 to 423 and scope-accessor sections | A5D06DA0B42E615FA0C40D0103D9125ED68A7691778E20C0315ACA7C82822C81 |
| V\documentation\loc_formatter_documentation.md | Formatter inventory searched for string/name/flag capture contracts | 1FBD9A031FD09100D79BAC08DEC3C16E19468F23516C5E67C67578156282AF08 |
| V\documentation\triggers_documentation.md | 3605 to 3613, has_cosmetic_tag | 7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29 |
| V\documentation\script_concept_documentation.md | 12 to 21, 126 to 180, 216 to 245 | 884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7 |
| V\common\script_constants\documentation.md | Schema and support limitations, first 45 lines | E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C |
| V\common\scripted_effects\00_scripted_effects.txt | 4188 to 4205, persistent ruling-ideology variable | 93DDD0D2E9F7A1A5640CFDAFBAE6B9FF0E1B4EE57E829C81D13B0CAC23AD90BF |
| V\common\scripted_effects\CZE_scripted_effects.txt | 437 to 462, meta numeric substitution precedent | CB5EE5136B5759EFE4CAAAACE23189964FCE57AF18558D0AC535336EA93319C6 |
| V\common\scripted_triggers\00_scripted_triggers.txt | 724 to 728, known cosmetic-tag matching | C8470B1937095F1AEC1C09EE78365D770FAB1AA7E28EB21D35924CA1253DD1DB |
| V\common\raids\air_raids.txt | 961 to 990, ordinary blast visual consumer | 4BC5CED6AFB625B65DCF01E45CFB6583B555BD8A045B53064675CCFE0DDBC657 |
| V\gfx\entities\nuke.asset | Entire 1 to 25, both entity definitions | 80168286679E3F6C0C69E57FB5F941C576841A122237BE936170700DAB017BC6 |
| V\gfx\entities\nuke.gfx | Entire 1 to 18, mesh/animation registrations | F6A4657A2643E860190F342DFA5922EE18DC6A3459EC168F7110CC86196A8611 |
| V\gfx\entities\particles.gfx | 657 to 685, four blast particle registrations | AF261D416ACCB89C4FD222B41E2846BEE8DC1D20DEF37B7B232C67DDB8D50D35 |
| V\gfx\entities\particle_entities.asset | 1 to 65 and 138 to 184, visual entity/default-state precedents | 4C0BC57D3F23C5E04F0F6E98952A386EBEEC8A512503F12FEE7243AC19A25C56 |
| V\gfx\entities\buildings.asset | 800 to 803, native entity clone/name registration | BEAA11ACE5B2A455DF5EFFCA36A955371FF399989D67C099D9F1CABBBA43C15B |
| V\gfx\models\animations_test.asset | 1 to 18, nuke animation source | 10B444358D19209B1880726227B03976650486195E882BF08EBAB2F4C599DA3F |
| V\gfx\particles\environment\nuke.asset | Ordinary particle type, shockwave and emitter fields | 6D45A52D11A12EFFF66D9AD8DE9F3B5144E1053526B92A8BD0D21254FCABDFCD |
| V\gfx\particles\environment\nuke_top.asset | Existing type/package linkage | 43CF874C6DF6006A8538D6749A0948C0B48F4270542A3479478AC09AF61882A9 |
| V\gfx\particles\environment\nuke_big.asset | Particle package, particularly 1 to 44 and emitter timing fields | BA4CFAF16E7F895510F454B73385B93758F50AD7B618D66B4A6530D6EF5E1AD3 |
| V\gfx\particles\environment\nuke_big_top.asset | Existing top package and event-linked type | D2D1725E2CF33B9B04A78476D6824E3167FD336D8F6C6DFE39FC4C2E607BCAF4 |
| V\gfx\entities\map_lights.asset | Names at 100 and 228, big-light fields at 227 to 246 | E84BF76058B28DA2B64108EB26FA92B3E5F8B98166FDED4B4CCF3E278D4F85CC |
| V\sound\sound.asset | 964 to 969, existing large-blast source registrations | 263A6DFD6C53C4881E1133C403AF0AE3ED68DF40821B14FF7FD69CD66C48C2D9 |
| V\sound\soundeffects.asset | 1156 to 1176, large-blast soundeffect consumers | CB13BE6F368723DD48BE9D9544F7B7B50CFD228B850C88EF55600187BA65B01F |
| V\history\states\64-Brandenburg.txt | 2, 16, 57 to 58, reference province membership | 3BD06F88BA34DD9E81927820768FD3E90EC4532E3928552A34FF8B80B4666B6F |
| K\common\scripted_effects\00_ambient_object_effects.txt | Entire 1 to 40, graphical-only create_entity placements | 7F9D1532ECB9162D62DF9FC073C89FCED584EA47702A270F19CF5668EEB0C2FC |

Additional searches inspected installed/project scripted effects/events for create_entity/set_entity_animation and arbitrary-name token capture, installed COUNTRY property/dynamic-variable inventories, known cosmetic triggers, and project GFX entity overrides.
They are bounded negative-search evidence, not an exhaustive reverse-engineering proof.
Workshop 1458561226's common\scripted_effects path was absent in this installation.
No unsupported workshop substitution was made.

## Completed work, blockers, and simplifications

Completed: this source-supported capability research and the requested single-file handoff, including exact native command schemas, existing consumer/art chain, candidate bindings, narrow migration/cleanup boundaries, and current MCP results.
Files changed by this worker: only docs\plans\028_asteroid_incoming_plans\subagent_handoffs\presentation_capabilities_20261003.md.
Helpers/call sites/constants/cleanup logic implemented: none, as required by the read-only assignment.
Native game validation and runtime helper execution: not performed.
A generic durable name snapshot remains blocked.
A generic durable flag/cosmetic snapshot remains separately blocked.
Exact large-visual equivalence, blast state-event activation, sequencing, handle cleanup, and zero native nuclear consequences remain unobserved.
MCP artifact delivery gaps remain recorded above.

No simplifications, visual removals, dummy actors, nuclear suppression/reset workaround, arbitrary name/flag fallback, new window, Meshy/custom-3D work, plugin/tool changes, or gameplay design expansion were made.
The research handoff is complete as evidence.
The accepted Event028 presentation and durable-snapshot implementation is not complete and must not be reported as complete from this document.
