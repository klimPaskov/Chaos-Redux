# Event 23 current localisation audit and patch handoff

## Disposition

`implemented` for the bounded localisation defects identified in this audit. Source coverage is complete for the requested Event 23 files. Production-render validation is blocked because the active tool inventory does not expose the required HOI4 event, ordinary decision-category, or shared Event Details inspection and rendering routes.

This was a fresh audit of the current dirty worktree. Historical claims and artifact URIs in the previous version of this handoff were not reused as current evidence.

## Authorised scope and files reviewed

The audit used the current Event 23 goal prompt and Part 8 presentation specification, then read:

- `events/023_soviet_nukes.txt`
- `common/decisions/023_sov_nuclear_bombs_decisions.txt`
- `common/decisions/categories/023_sov_nuclear_bombs_categories.txt`
- `common/scripted_localisation/023_sov_nuclear_bombs_scripted_localisation.txt`
- `localisation/english/023_soviet_nukes_l_english.yml`
- `interface/023_sov_nuclear_bombs.gfx`
- Event 23 achievement registrations and GFX names
- the shared event-name, Event Log, Event Details, evolution, and super-event localisation selectors
- Event 5's Event 23 custody snapshot calls
- the Event 23 shared atomic-action calls and first confirmed multi-major exchange registration

The required offline Paradox wiki pages and current vanilla documentation were consulted before the patch, including localisation, events, decisions, data structures, triggers, effects, modifiers, scopes, on actions, ideas, AI, localisation formatter, and localisation objects.

No gameplay, GFX, workbook, export CSV, shared localisation, or unrelated localisation file was edited.

## Changed files

- `localisation/english/023_soviet_nukes_l_english.yml`
- `common/scripted_localisation/023_sov_nuclear_bombs_scripted_localisation.txt`
- this handoff

The first two files already contained uncommitted work when this audit began. The changes listed below are the only edits owned by this subagent.

## Changed localisation keys

- Event and news prose: `chaosx.nr23.100.d`, `chaosx.nr23.106.d`, `chaosx.nr23.110.d`, `chaosx.nr23.120.d`, `chaosx.nr23.161.d`, `chaosx.nr23.162.d`, `chaosx.nr23.163.d`, and `chaosx.news.234.d`.
- Decision category: `sov_nuclear_bombs_command_category_desc`.
- Cost explanations: `sov_nuclear_bombs_cost_command_tooltip`, `sov_nuclear_bombs_cost_security_tooltip`, `sov_nuclear_bombs_cost_logistics_tooltip`, `sov_nuclear_bombs_cost_diplomatic_tooltip`, and `sov_nuclear_bombs_cost_strategic_tooltip`.
- Requirement and action clarity: `sov_nuclear_bombs_registered_site_requirements_tt`, `sov_nuclear_bombs_dismantle_batch_desc`, and `sov_nuclear_bombs_breakaway_operationalization_mission_desc`.
- Evolution prose: `sov_nuclear_bombs.evolution.i.body`, `sov_nuclear_bombs.evolution.ii.body`, `sov_nuclear_bombs.evolution.iii.body`, and `sov_nuclear_bombs.evolution.iv.body`.
- Super-event prose: `chaosx_super_event.108.d`.

## Scripted localisation fix

`GetSovietNuclearBombsDemandName` previously checked `sov_nuclear_bombs_demand_kind` only in the current localisation scope. This worked in Soviet decision-category context but failed in recipient event `chaosx.nr23.120`, whose ROOT is the target government while the demand variable belongs to `sov_nuclear_bombs_coercion_actor`. The fallback could therefore display `Accept Soviet protection` for a different demand.

Six actor-scoped branches now check the existing `sov_nuclear_bombs_coercion_actor` event target before the existing current-scope branches. Recipient ultimatums and Soviet settlement review therefore resolve the actual configured demand while Soviet-scope callers retain their previous behaviour.

Dynamic text added or fixed:

- `chaosx.nr23.120.d` now names `[ROOT.GetName]` and resolves the actor-owned `[GetSovietNuclearBombsDemandName]`.
- `chaosx.nr23.162.d` now names `[sov_nuclear_bombs_coercion_target.GetName]` and the verified demand.
- `chaosx.nr23.163.d` preserves `[?sov_nuclear_bombs_standdown_offer_nonce|0]` but presents it as a verification number rather than exposing the internal term `nonce`.

## Coverage results

### Missing keys

- The current Event 23 event, decision, category, achievement, scripted-localisation, Event Log, Event Details, and super-event sources yielded 301 explicit Event 23 localisation references. Missing: none.
- All event/news title, description, and option keys resolve, including the distinct refusal key `chaosx.nr23.120.refuse`.
- All 31 tooltip references found across Event 23 decisions and achievements resolve.
- Five custom-cost families have their base, `_blocked`, and `_tooltip` convention keys.
- Seven achievements have all conventional `_NAME`, `_DESC`, `_tooltip`, and `_locked` keys plus the shared eligibility tooltip.

### Duplicate keys

- Duplicate keys inside `023_soviet_nukes_l_english.yml`: none among 367 definitions.
- Event 23 keys duplicated in another English localisation file: none.

### Unused or unrouted keys

The following keys have no current runtime selector reference:

- `sov_nuclear_bombs.event_log.detail`; the shared Event Details selector uses `sov_nuclear_bombs.event_details.description`, and the shared evolution summary selector uses `sov_nuclear_bombs.evolution.summary`.
- `sov_nuclear_bombs.evolution.i.stage`, `.ii.stage`, `.iii.stage`, and `.iv.stage`; shared evolution surfaces use the corresponding `.title` and `.body` keys.

After Part 8's four-value category correction, the following scripted helpers have no active player-facing caller: `GetSovietNuclearBombsPhaseName`, `GetSovietNuclearBombsCategorySiteName`, `GetSovietNuclearBombsCategoryTargetName`, and `GetSovietNuclearBombsCategoryDeadlineName`. Their `sov_nuclear_bombs_phase_*`, `sov_nuclear_bombs_category_site_none`, `sov_nuclear_bombs_category_target_none`, and `sov_nuclear_bombs_category_deadline_*` backing keys remain defined. They were not deleted because they are harmless, may be intended for a later ordinary decision surface, and were part of pre-existing work in the shared dirty files.

News title/description/button keys, idea descriptions, custom-cost `_blocked`/`_tooltip` keys, and achievement naming variants are engine-convention consumers. Their lack of literal source references does not make them unused.

### Scripted localisation issues

- Fixed: demand-name scope in recipient and settlement contexts, as described above.
- No missing `localization_key` target remains in the Event 23 scripted-localisation file.
- No direct `§` or `£` formatting character occurs in scripted localisation.
- Existing event-target name namespaces correctly omit the `event_target:` prefix in localisation tokens.

### Tooltip trigger and effect accuracy

- The current decision and mission descriptions preserve the separation between physical custody, technical access, command formation, and delivery integration. They do not imply that breakaway custody alone creates an operational route.
- `sov_nuclear_bombs_registered_site_requirements_tt` was shared by storage hardening and dismantlement despite their different checks. Its old wording falsely implied that hardening always required an eligible device group and that dismantlement used the hardening site's infrastructure checks. It now states the common ownership/registration requirement, the hardening-specific intact infrastructure requirement, and the dismantlement-specific minimum of two assigned devices.
- The five cost hover texts previously repeated the visible resource list. They now explain what each resource family commits while the adjacent dynamic cost string remains the numeric authority.
- The remaining requirement tooltips and decision/mission descriptions matched the current trigger and effect intent closely enough that no bounded wording change was necessary.

## Display and behaviour before and after

- Before: the decision category attempted to display phase, site, target, demand, deadline, an explanatory paragraph, and four status values. This exceeded Part 8's information budget and created a substantial wrapping/overflow risk. After: it contains exactly four lines for operational devices, Arsenal Readiness, Command Integrity, and compact posture/public-knowledge status.
- Before: an ultimatum recipient could see the fallback demand because the scripted localisation read the recipient's variable scope. After: it reads the Soviet coercion actor first and displays the configured demand.
- Before: stand-down events exposed `nonce`, `terminal collapse`, and a sentence semicolon. After: they describe a verification number, intact command authorities, acceptance, and refusal in player-facing terms.
- Before: settlement text referred to a generic target government and unnamed terms. After: it names the target and demand dynamically.
- Before: breakaway and dismantlement descriptions referred to implementation actions or direct launch-route absence. After: they state the physical work, custody result, and the three independent operationalisation stages.
- Before: evolution and super-event passages used generic stage language, implementation-adjacent phrases, repeated contrast structures, and an abstract government-wide decision. After: they identify reactors, production, retaliation planning, command limits, telephone failures, evacuation trains, and the still-open stand-down choice.

## Prose-quality summary

### Vagueness

Generic references to the selected government, named terms, the next stage, and a direct launch route were replaced with dynamic actor/demand names or concrete command, production, and custody consequences.

### Bloat

The category description was reduced from a multi-paragraph dashboard to the four player values required by Part 8. No gameplay information owned by an active decision or mission countdown was duplicated there.

### Obvious explanation

Cost tooltips no longer say only that the listed resources are required. The dismantlement description no longer narrates an internal `non-detonating demolition action`.

### Repetition

Evolution II and the breakaway news report were split and tightened so the distinction between possession and operational capability is stated once and concretely.

### Overcomplication

Stand-down verification no longer asks the player to interpret a nonce or a terminal-collapse gate. Evolution III now leads with the existence of a nuclear opponent and the command consequences.

### Style-rule repair

The changed passages contain no em dash, sentence semicolon, stale update-history wording, prompt fragment, tuning note, or hidden-mechanic explanation. The scan also found no remaining player-facing `nonce`, `terminal collapse`, `repeatable state program`, or `first warning` phrase in the two authorised files.

## Cross-surface consistency

- Baseline and evolutions: localisation describes one hundred guarded devices and expanding production without contradicting the current additive 100 baseline or revealing disabled evolution grants. Source constants confirm increments 75/100/125/200 and reactor entitlements 2/4/6/8; the player prose does not claim a disabled stage granted or recorded anything.
- Custody: Event 5 calls `sov_nuclear_bombs_snapshot_event5_release_tranche` before releases, while Event 23's bounded `on_release_as_free` and `on_release_as_puppet` callbacks call `sov_nuclear_bombs_reconcile_event5_release_country` against the post-release owner/controller view. Event 23 custody prose consistently distinguishes physical possession from technical access, command formation, and delivery integration.
- Atomic actions: Event 23 strike authorization and retaliation source call `sov_nuclear_bombs_execute_shared_action`. Localisation assigns authorization and context to Event 23 while describing Fallout and wider consequences as results of confirmed detonations, not as Event 23-owned consequence logic.
- Super-event: slot 108 is separately routed through the shared super-event selectors and is gated by the first confirmed multi-major exchange receipt. Its text is nonterminal, preserves opportunities to limit or stand down, and treats fallout as a consequence of each blast rather than as the Fallout world-end route.
- Event Log and Event Details: Event 23's event name, evolution type, evolution titles/bodies, summary, Event Details description, and status line are routed by current shared selectors. Only the five keys listed under unused/unrouted keys lack consumers.
- Assets: `interface/023_sov_nuclear_bombs.gfx` defines 53 Event 23 sprites. Every texture path resolves. All 44 distinct event picture, decision-category picture, decision icon, and mission icon references in the audited source surfaces resolve to current GFX names.
- No dedicated Event 23 scripted GUI exists. The category uses the static `GFX_decision_category_sov_nuclear_command_picture`, as required.
- No localisation change introduced script iteration. The inspected Event 5 custody bridge uses release callbacks rather than a new whole-world recurring loop.
- No runtime Event 23 cluster or world-end localisation route was found. The workbook was not edited or treated as source evidence; the spreadsheet owner should separately ensure no Event 23 cluster/world-end row exists.

## Spreadsheet wording handoff

If catalog text differs, the spreadsheet owner should mirror these current keys exactly:

- `chaosx.event_name.23` and `chaosx.nr23.1.t`: `SOV Nuclear Bombs`.
- `sov_nuclear_bombs.event_log.evolution_type`: `Nuclear Escalation`.
- Evolution I body: `The Soviet breakthrough has become an international race. Reactor compounds, production batches, observers, and bomber patrols turn the hidden arsenal into a permanent state program.`
- Evolution II body: `The arsenal becomes an instrument of political pressure. Selected demands can reach independent minor governments and eligible breakaways. Credibility, foreign backing, target behavior, and delivery evidence determine the result.`
- Evolution III body: `Another major power can answer a nuclear strike. Every authorization must account for retaliation windows, survivable command, hotlines, limited response profiles, and reserve preservation.`
- Evolution IV body: `The Soviet command can prepare its widest response profiles only during an extreme strategic emergency. A verified stand-down can still halt the order.`
- Evolution summary: `The Soviet nuclear escalation begins with one hundred guarded devices. As the crisis deepens, the arsenal and reactor network can expand, but custody, command authority, and verified delivery govern every physical action.`
- Event Details description: `The Soviet atomic arsenal is governed through production, testing, coercion, and disputed custody. Every weapon remains tied to a physical depot, a command authority, trained delivery crews, and a release order. A Soviet collapse may scatter the stockpile among successor authorities, but possession alone does not provide the knowledge or command structure needed to launch it. Any confirmed detonation can bring fallout, condemnation, and retaliation far beyond its target.`

No Event 23 cluster or world-end row should be created.

## Encoding and token preservation

- `localisation/english/023_soviet_nukes_l_english.yml` retains UTF-8 BOM bytes `EF BB BF`.
- `common/scripted_localisation/023_sov_nuclear_bombs_scripted_localisation.txt` remains valid UTF-8. A localisation BOM is not required for this script file.
- Existing dynamic variables, constants, event-target names, formatting codes, and scripted-localisation calls were preserved. The only dynamic additions are existing actor/target/name calls in contexts where their required event targets are guaranteed by the current event chain.

## Sourced quotation preservation

`chaosx_super_event.108.q` remains verbatim: `The first blow or series of first blows may be the last.` The existing research handoff attributes it to General Leslie R. Groves's 2 January 1946 memorandum reproduced in FRUS document 600. No word, punctuation mark, or capitalization in the quotation was changed. No other sourced or attributed quotation was found on the inspected Event 23 surfaces.

## Meaningful validation

- Localisation definition audit: 367 keys, zero local duplicates, zero cross-English duplicates for those keys.
- Explicit reference audit: 301 references, zero missing.
- Scripted demand audit: six actor-scoped demand branches precede the six existing current-scope branches and fallback.
- GFX audit: 53 definitions with zero missing texture files; 44 in-scope surface references with zero unresolved names.
- Style scan over the two authorised files found no em dash, sentence semicolon, stale update-history marker, or repaired internal term.

Skipped meaningful validation and exact blockers:

- `mcp__hoi4_agent_tools__hoi4_event_inspect` and `mcp__hoi4_agent_tools__hoi4_event_render` are not exposed in the active tool inventory, so event localisation coverage and visual wrapping could not be inspected or rendered through the required read-only service.
- No read-only ordinary decision-category inspect/render route is exposed, so the four-line category's production wrapping and overflow could not be visually proven. Source-only review is not equivalent to this missing evidence.
- The shared Event Details GUI likewise has no exposed `hoi4.gui_inspect` or `hoi4.gui_render` route in this session, so its Event 23 description/status wrapping remains visually unverified.
- Standalone Technology Tree Viewer availability was checked separately from route assumptions. No standalone viewer or technology inspect/render route is exposed in the installed package. This is a package gap, not evidence about service health. Event 23 adds no localisation-owned technology surface.
- HOI4 was not launched, as required.

## Remaining issues and uncertainty

- The five unrouted Event Log/evolution stage keys and the dormant category helper families should be retained or removed deliberately by the owning parent after confirming whether a later ordinary decision surface will consume them.
- Production visual overflow remains uncertain because the required MCP renderers are unavailable. The category was reduced to the strict four-line Part 8 budget, which lowers risk but does not substitute for rendering.
- The workbook was not opened or changed. Catalog mirroring and confirmation that no Event 23 cluster/world-end row exists remain with `chaosx_spreadsheet_doc_worker`.
- No design-depth gap was found, so no additional plan handoff was created.
- No commit was created because both authorised source files were already dirty or untracked with work beyond this subagent's exact edits; committing whole files would capture changes this audit does not own.

## Simplifications, omissions, and blockers

No prose fallback, invented capability, gameplay simplification, or placeholder was introduced. The only omissions are the read-only MCP visual validations and workbook confirmation listed above, each blocked by tool exposure or owner boundaries rather than treated as complete.
