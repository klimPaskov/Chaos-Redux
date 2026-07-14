# Event 15 Country Package Audit

## Verdict

**FAIL**

The current package preserves the recipient country through the opening, defines five distinct scripted identities, charges the active formation path, preserves existing forces, and implements route succession. It is not completion-ready. Required route flags, institutional leader portraits, advisor portraits, and league emblems are absent. The accepted three-track idea lifecycle is incomplete and can reach five simultaneous Event 15 spirits. Military decisions can repeatedly create the same generic Household Guard divisions. One achievement is impossible, another proves the wrong condition, and several required disqualifiers have no producer. Country AI inverts the documented war-restraint sign and does not use the accepted route-choice state inputs. Terminal cleanup is neither fully wired nor sufficient to remove a formed identity safely.

The existing focus-tree audit also remains **FAIL**. Its audited source hash is stale because the focus file changed afterward, so its findings cannot be treated as cleared without a fresh audit.

## Audit basis

This source audit used:

- `AGENTS.md` and the `chaos-redux-events`, `chaos-redux-event-assets`, and `chaos-redux-subagents` skills.
- All accepted Event 15 specifications, handoffs, and matrices under `docs/specs/015_utopia_manifesto_specs/`, especially the country package, idea lifecycle, achievement, AI strategy, focus route, decision mission, asset manifest, and completion matrices.
- The required offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, country creation, national focuses, portraits, achievements, interfaces, and cosmetic tags.
- Installed vanilla documentation for script concepts, effects, triggers, on actions, characters, AI strategies, resources, equipment, and localisation, plus vanilla cosmetic-tag, character, AI strategy, and country-identity precedents.

Snapshot anchors at audit close:

- `common/national_focus/015_utopia_manifesto_focus_tree.txt`: SHA-256 `9379C7883038ADBB8959B012105879E5EE5471F5BF0DED8A38E32979FD836A94`
- `common/scripted_effects/015_utopia_manifesto_country_effects.txt`: SHA-256 `1F0F9A4061C3BAEB6FAEEAA5AC1827B0F5CBC7B1B8BE79EA3CD9A431EE46A8A2`
- `common/scripted_effects/015_utopia_manifesto_identity_effects.txt`: SHA-256 `238A0BCF2EFF91D5BC0C4BB01DDBEA1EB02504DBEF4BFF77AB5434A581F6FE04`
- `common/decisions/015_utopia_manifesto_decisions.txt`: SHA-256 `A1525068790D31225C5A3D86906D156A60A4565E6D1FCF5F0F49D82FB9DA2647`
- `events/015_utopia_manifesto.txt`: SHA-256 `917042E6A30D9F1C49886B58060AABAF062296FEF8B88D69FF3C8A7658DA6155`
- `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt`: SHA-256 `DBAC91EC9095993CED1C2304066E00286C9892D4717707983B329AF6A84558F2`

The prior focus audit used focus SHA-256 `C5447DDA420F9FCE41E49125C4B6E0FA2D0940D7D575FF690323D2DE03592931`. Current source therefore postdates that audit.

## Country continuity and identity

### PASS: original tag, flag, leader, and army survive the opening

- `utopia_manifesto_accept_manifesto` initializes the Ledger, geography, and focus package without changing the country tag or cosmetic tag.
- The only Event 15 `set_cosmetic_tag` calls are inside the five formation identity effects at `common/scripted_effects/015_utopia_manifesto_identity_effects.txt:221`, `:244`, `:267`, `:290`, and `:301`.
- No Event 15 gameplay file changes the actual country tag, annexes the recipient, replaces state ownership, adds blanket cores, loads a replacement OOB, deletes divisions, or replaces existing templates.
- The existing country leader remains in office through the founding debate. Four institutional routes add a governing-body leader only at formation. The hidden humanist route retains the existing leader.

This satisfies original-tag and base-flag preservation before transformation.

### PASS in script, FAIL in presentation: five route identities

| Route | Scripted identity | Institution and leadership | Result |
| --- | --- | --- | --- |
| Consent of Households | `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH` | Household Assembly, then Commonwealth Council | Script and localisation present, runtime flag and portrait absent |
| Common Table | `UTOPIA_MANIFESTO_COUNCIL_UNION` | Council of Callings, then Rotating Congress | Script and localisation present, runtime flag and portrait absent |
| Guardians of Measure | `UTOPIA_MANIFESTO_PLANNED_UTOPIA` | Board of Measure, then College of Measure | Script and localisation present, runtime flag and portrait absent |
| Closed Island | `UTOPIA_MANIFESTO_CLOSED_ISLAND` | Stewardship Council, then Directorate of Service | Script and localisation present, runtime flag and portrait absent |
| The Joke Understood | `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH` | Humanist Cabinet flag, retained leader, constitutional elections | Script and localisation present, runtime flag absent |

The five cosmetic colors exist in `common/countries/cosmetic.txt`. Country-name and party localisation exists for all routes. Route commitment removes Found Manifesto, installs the matching institution, applies the matching property settlement, and names the route party. Formation sets the appropriate ruling ideology for the four literal routes. The humanist helper renames the current ideology's party without forcing an ideology change.

The visual package fails:

1. All fifteen canonical route-flag files are absent. None of the five tags has an 82x52 file under `gfx/flags/`, a 41x26 file under `gfx/flags/medium/`, or a 10x7 file under `gfx/flags/small/`. No ideology variants were found either. The offline cosmetic-tag reference confirms that ideology-specific flag resolution can override a no-suffix cosmetic fallback, so the accepted distinct ideology variants also need explicit coverage.
2. The eight founder and successor characters reference four large sprites in `common/characters/015_utopia_manifesto_characters.txt:20-83`. `GFX_portrait_utopia_manifesto_household_assembly`, `GFX_portrait_utopia_manifesto_council_of_callings`, `GFX_portrait_utopia_manifesto_board_of_measure`, and `GFX_portrait_utopia_manifesto_stewardship_council` have no sprite definition or image file.
3. All sixteen advisors use national-spirit sprites as `small` character portraits. This is an unapproved weaker substitute for the accepted advisor portrait coverage. The specification allows reuse of suitable existing country people, while fictional advisors require portrait direction and regional identity. It does not approve idea icons as the final advisor portrait package.
4. The five route-emblem flags at `common/scripted_effects/015_utopia_manifesto_identity_effects.txt:37-41` and `:223-303` have no art, no sprite definitions, and no GUI or league consumer. They are state markers only, not registered emblems.

Required correction: produce and install five genuinely distinct route flag families at all three HOI4 sizes, with the ideology variants needed by the accepted package. Register the four institutional council portraits. Replace the advisor icon fallback with approved portrait coverage. Produce five small-scale league emblems and wire stable sprite IDs into the league or identity presentation that consumes the existing route-emblem state.

## Institutions, parties, advisors, and succession

### PASS with asset dependency

- Acceptance recruits eight institutional founder or successor characters and sixteen advisors, but it does not add country-leader roles.
- Shared advisors appear after route institution establishment. Route advisors are gated to Consent or humanist, Common Table, Guardians, or Closed Island as appropriate.
- `utopia_manifesto_form_current_route_identity` installs exactly one final identity after formation proof succeeds.
- `utopia_manifesto_the_second_generation` calls `utopia_manifesto_advance_current_route_succession`. The four institutional routes remove the founder role and promote the matching successor. The humanist route enables constitutional elections and retains the recipient's leadership continuity.

The logic meets the accepted institutional succession shape. It cannot be accepted as a finished country package until the missing leader and advisor portraits are installed and the post-edit focus audit confirms that the Second Generation path remains reachable.

## Idea lifecycle and spirit ceiling

### FAIL

| Lifecycle | Current implementation | Result |
| --- | --- | --- |
| Found Manifesto | Starts at acceptance. Public and failure stages are called. Route commitment clears the family before adding the route institution. | PASS. The book is absorbed into the institution as required. |
| Unmeasured Country | Starts at acceptance and reaches the survey mitigation. `utopia_manifesto_finalize_public_administration` exists at `common/scripted_effects/015_utopia_manifesto_country_effects.txt:134`, but no gameplay file calls it. Common Store later replaces the Unmeasured family. | FAIL. The accepted final administrative replacement is unreachable before the track becomes Common Store. |
| Inherited Order | Starts at acceptance. Route commitment calls `utopia_manifesto_apply_route_property_settlement` and produces land trusts, common ownership, measured tenure, state allotment, or mixed property. The Island Made Real later replaces that track with Garden District Network, matching the accepted mature three-track closure. | PARTIAL. The route settlement is real, but the Land Registration mitigation helper has no producer. |
| Route institution | Five founding, mitigation, failure, and final families exist. Founding is installed at route commitment and final is installed at formation. | PASS for the primary path. |
| Common Store Network | Founding, rotation, failure, and final helpers all have live producers. It replaces the Unmeasured track. | PASS. |
| Garden District Network | Founding and mitigation have live producers. `utopia_manifesto_break_garden_district_network` and `utopia_manifesto_complete_garden_district_network` have no gameplay callsite. | FAIL. Failure and final stages are unreachable. |

The accepted ceiling is three simultaneous Event 15 spirits. The stable intended mature set is route institution, Common Store Network, and Garden District Network. The current source can reach five:

1. Route institution, Common Store, and a mitigated Garden Network are active.
2. Hiring auxiliaries adds Auxiliary Dependency without replacing a track, producing four.
3. `utopia_manifesto_stewardship_obligations` at `common/national_focus/015_utopia_manifesto_focus_tree.txt:2742-2764` replaces only the base Garden idea. If Garden is mitigated, the `else_if` adds Stewardship Burden beside it, producing five.

The current `utopia_manifesto_military_growth_batches` and related counters do not constrain spirit count. Ending an auxiliary contract can leave a bounded auxiliary spirit, so this is not limited to a brief mission window.

Required correction: wire the Unmeasured final administrative stage, the Inherited registration mitigation, and both missing Garden outcomes to real milestones. Centralize transitions so every member of a track family is cleared, not only one exact base idea. Auxiliary and Stewardship must replace or temporarily occupy an approved track, or use another explicitly approved presentation, so no compatible path exceeds three visible Event 15 spirits. Preserve the mature route, store, and garden set after temporary liabilities resolve.

## Formation proof, territory, and costs

### PASS in the current active path, with a stale completion gate

- Formation remains decision-owned through `decision_utopia_prove_the_commonwealth` and `decision_utopia_proclaim_the_commonwealth` at `common/decisions/015_utopia_manifesto_decisions.txt:4113-4205`.
- The proof mission charges political power, support equipment, trains, and motorized equipment. Proclamation charges political power, support equipment, trains, and convoys before calling `utopia_manifesto_form_current_route_identity`.
- Common proof requires the island project, an external case, external network evidence, Ledger thresholds, no constitutional crisis, and no failed stewardship. Route triggers add their capstone and route-specific proof.
- The current decision effects now provide `utopia_manifesto_broad_recognition_proven` through a real league legitimacy outcome, correcting the older practical-route producer gap.
- Formation does not annex countries, transfer states, add blanket cores, refill reserves, finish districts, create units, refund prior costs, or erase the costs of the proof and proclamation.

`chaosx.nr15.10` still contains an uncharged direct call to the identity formation helper, but no gameplay file calls that event. It is dormant, not a live bypass. It should remain unwired or be removed so a later integration cannot accidentally restore a free formation path.

The formation surface cannot receive a package PASS while the required focus audit remains FAIL. The old focus audit's broad-recognition, route-spirit, and batch-cap findings were edited after its snapshot. Those corrections need a new audit rather than an assumption of success.

## Military growth and force preservation

### FAIL

The sound parts are present:

- Existing divisions and templates remain.
- Acceptance grants no divisions.
- `utopia_manifesto_apply_paid_military_growth` at `common/scripted_effects/015_utopia_manifesto_effects.txt:1890-1932` charges dynamically scaled manpower, army experience, infantry equipment, and support equipment before unit creation.
- Institutional growth separately charges manpower, support equipment, and political power.
- Auxiliary contracts add transport and convoy costs and can only be hired once.

The implementation then collapses all growth into one generic result. Every paid military growth call creates one to three copies of the same four-infantry Household Guard template with engineer support. Citizen Watch, engineer companies, route defense focuses, auxiliaries, and post-formation reinforcement all use that helper. This contradicts the accepted citizen-watch, worker-defense, engineer-corps, service-formation, auxiliary, and professional-defense identities.

The repeatable decisions are not capped:

- `decision_utopia_raise_a_citizen_watch` at `common/decisions/015_utopia_manifesto_decisions.txt:3542-3565` excludes only an active training mission. It does not become unavailable after `utopia_manifesto_citizen_watch_trained`.
- `decision_utopia_form_engineer_companies` at `:3582-3610` likewise excludes only the active mission and not `utopia_manifesto_engineer_companies_formed`.
- Their completion effects at `common/scripted_effects/015_utopia_manifesto_decision_effects.txt:947-996` call paid military growth every time.
- The batch counter increments but no longer has a cap or other consumer. Costs therefore prevent free units but do not satisfy the accepted population and district cap or the prohibition on repeatedly spawning generic infantry.

Required correction: separate focus-owned progression from repeatable decision limits. Add route-safe population, district, institution, and historical-batch caps that cannot block mandatory later focuses. Make Citizen Watch and engineer completion one-time or explicitly bounded. Give route growth distinct templates, support-company changes, bonuses, or institutions instead of routing every outcome through Household Guard creation.

## Achievement evidence

### FAIL

The package registers all fourteen accepted Event 15 achievements. Their 42 normal, unavailable, and completed icon sprites are present. Several durable evidence arrays and war hooks are correctly bounded to Event 15 actors.

Completion blockers remain:

1. `utopia_manifesto_the_joke_understood` requires `utopia_manifesto_garden_district_network_final` at `common/achievements/chaos_redux_achievements.txt:2431`. The only effect that adds that idea is the uncalled helper at `common/scripted_effects/015_utopia_manifesto_country_effects.txt:313-316`. The achievement is impossible.
2. `utopia_manifesto_the_perfect_measure` requires five distinct district roles. `utopia_manifesto_refresh_achievement_planned_district_proof` at `common/scripted_effects/015_utopia_manifesto_identity_effects.txt:651-668` checks only total completed projects and total charters. Repeating projects can satisfy it. The decision system defines only four role IDs at `common/scripted_effects/015_utopia_manifesto_decision_effects.txt:465-477`, so five distinct roles cannot be proven by the current model.
3. The reserve-reset, island-reopened, regime-collapsed, forced-relocation, and total-repeal disqualifier helpers at `common/scripted_effects/015_utopia_manifesto_identity_effects.txt:740-776` have no gameplay callsite. Their flags are consumed by achievements, but the prohibited conduct cannot set them.

Required correction: award the Garden final stage from the accepted terminal district milestone. Implement and record five real distinct district roles, preferably with bounded role flags or an array rather than project totals. Call every consumed disqualifier from the exact decision, event, focus, or aftermath outcome that performs the prohibited conduct.

## Country AI

### FAIL

The AI strategy plans use `allowed = { always = yes }`, dynamic `enable` blocks, and `abort_when_not_enabled = yes`, which is appropriate for a country selected after game start. Decisions also contain many route-aware and resource-aware weights.

Two country-level defects block acceptance:

1. War-restraint values have the opposite sign from the official documentation and vanilla precedent. Installed `common/ai_strategy/_documentation.md` defines targetless `avoid_starting_wars` with a negative value because it is added to conquer weight. Vanilla `common/ai_strategy/default.txt:1891-1892` and `:1945-1946` use `-400` to avoid wars. Event 15 defines restraint, high, moderate, and crisis as positive `60` through `220`, while escalation is `-60`, at `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt:10-14`. The intended restraint increases the aggregate war score and the intended escalation reduces it.
2. Route-opener `ai_will_do` logic mostly maps democratic to Consent, communist to Common Table, neutrality to Guardians, and fascism or war to Closed Island. It does not implement the accepted state inputs such as stability, Need, Plenty, Concord, infrastructure, education or technical capacity, geography, neighbor context, council support, open debate, or penal conduct. The result is ideology selection rather than the accepted country-aware route evaluation.

Required correction: make restraint and crisis values negative and escalation pressure positive, then review every plan against the documented additive behavior. Expand route-opener weights with the accepted, already-available country and Ledger evidence. Preserve the existing dynamic `enable` and cleanup structure.

## Cleanup and disable safety

### FAIL

- `utopia_manifesto_enter_disable_safe_state` exists at `common/scripted_effects/015_utopia_manifesto_effects.txt:2131-2134`, but it has no gameplay callsite.
- The dissolution event `chaosx.nr15.120` at `events/015_utopia_manifesto.txt:3420-3460` also has no callsite.
- `utopia_manifesto_clear_all_runtime_state` clears cases, league state, Ledger state, route flags, and the war-history achievement lifecycle. It does not clear country idea lifecycles, formed identity flags, institution flags, succession flags, identity achievement tracking, institutional country-leader roles, or the active cosmetic tag.
- `on_annex` records achievement history when the Event 15 actor annexes another country. It does not perform Event 15 cleanup when the actor is `FROM` and is annexed.
- The three dissolution choices clear different idea or runtime subsets, but none performs a complete, policy-consistent teardown of party, leader, identity, and cosmetic state.

Required correction: define one terminal teardown effect and call it from every approved disable, dissolution, replacement, and defeat edge. It must clear the country idea families, both achievement lifecycles, all identity and succession flags, and temporary arrays. It must remove Event 15 country-leader roles and use the documented `drop_cosmetic_tag = yes` when the accepted outcome restores the base identity. The policy for restoring parties and leaders must be specified rather than invented as a fallback. Wire `chaosx.nr15.120` or remove it if another explicit terminal system owns dissolution.

## Focus-audit dependency

### FAIL until rerun

The required focus audit remains **FAIL**, but current focus source no longer matches its audit hash. Current code appears to address three old findings by adding broad-recognition proof, clearing Found Manifesto at route commitment, and removing the global military batch cap. The last change also exposes the uncapped repeatable military-growth defect documented above.

Required correction: after the country-package blockers are fixed, rerun the focus auditor against the current hash. The rerun must trace all five formation routes, the three-track lifecycle including Auxiliary and Stewardship, every paid military call, Second Generation succession, and post-formation reachability. The old FAIL cannot be closed by source drift alone.

## Completion checklist

| Required surface | Status |
| --- | --- |
| Original tag and base flag preserved until transformation | PASS |
| Five route identities and cosmetic tags | FAIL, scripts exist but runtime flags are absent |
| Institutions and parties | PASS in script |
| Leaders, advisors, and portraits | FAIL, logic exists but required portrait coverage does not |
| Found Manifesto absorbed into route institution | PASS |
| Unmeasured Country final administrative replacement | FAIL |
| Inherited Order route property settlement | PASS for route settlement, mitigation stage missing |
| Common Store stages | PASS |
| Garden District stages | FAIL |
| Maximum compatible spirit count of three | FAIL, current maximum is five |
| Existing forces preserved | PASS |
| Military growth paid and institutionally distinct | FAIL, paid but generic and uncapped |
| Succession | PASS in script, asset and focus-audit dependent |
| Formation proof and no annexation or cost erasure | PASS in the active path |
| Achievement evidence | FAIL |
| Country AI | FAIL |
| Cleanup and disable safety | FAIL |
| Required focus completion gate | FAIL pending rerun |

## Simplifications, omissions, and risks

No audit surface was intentionally omitted. The implementation contains unapproved simplifications: idea icons stand in for advisor portraits, all military identities stand in for one Household Guard unit generator, and route-choice AI stands in for ideology-only weights. The missing route flags, institutional portraits, league emblems, lifecycle outcomes, achievement producers, and teardown wiring are omissions, not optional polish.

This audit changed no gameplay, localisation, art, workbook, specification, or shared skill file.
