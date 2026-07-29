# Event 015 Country-Package Completion Re-audit

> Dated snapshot. Its visual findings are superseded by `asset_workflow_and_identity_regeneration_handoff_2026_07_15.md`, and later League and association-charter reverse-link changes require a fresh country-package audit before repository completion. The audit body remains unchanged as evidence for the source it inspected.

Date: `2026-07-15`  
Event: `015_utopia_manifesto`  
Auditor role: `chaosx_country_package_auditor`  
Mode: read-only audit apart from this handoff; no gameplay, localisation, interface, or asset edits; no commit

## Verdict

**Live country-package implementation: PASS.**

The former gameplay and runtime-asset failures are closed. The current source
now has a genuine non-annexed capitulation producer, a genuine
constitutional-abandonment producer, an exact political snapshot and restore
path, only the five active cosmetic identity families, the complete leader and
advisor packages, bounded paid military growth, explicit succession, complete
terminal cleanup, league continuity, and all fourteen achievements.

**Repository completion status: FAIL - documentation-only blocker.**

The implementation is not yet eligible for a repository-wide completion claim
because the current-facing Event 015 asset manifest and event document still
make false claims about removed flag families and already-completed visual/UI
integration. These stale documents are listed separately below. I found no
remaining live gameplay, localisation, or active route-identity asset blocker.

## Disposition of the prior audit failures

| Prior finding | Current result | Evidence |
| --- | --- | --- |
| No genuine non-annexed regime-collapse producer | **CLOSED** | `common/on_actions/015_utopia_manifesto_on_actions.txt:63-99` invokes `utopia_manifesto_begin_regime_collapse_aftermath` for a formed, accepted country in `on_capitulation`. This is independent of `on_annex`. |
| No constitutional-abandonment collapse producer | **CLOSED** | `common/scripted_triggers/015_utopia_manifesto_reachability_triggers.txt:185-206` detects a formed route whose enforced government has been abandoned; `common/on_actions/015_utopia_manifesto_on_actions.txt:101-112` sends it into the same aftermath chain. |
| Political teardown did not restore the original ruling group, election permission, or exact leader | **CLOSED** | `common/scripted_effects/015_utopia_manifesto_identity_effects.txt:54-175` saves the ruling ideology group, exact current character, exact active leader ideology subtype, and election permission. `:261-294` restores them. |
| Exact leader restoration passed an ideology-group token to `promote_character` | **CLOSED** | `:64-161` enumerates all 24 loaded subtypes; `:278-285` injects the saved subtype into `promote_character`. The group token is used only by `set_politics` at `:263-267`. |
| Event 015 overwrote or rescheduled recipient politics | **CLOSED** | No Event 015 source call to `set_party_name`, `hold_election`, `last_election`, or `election_frequency` remains. Formed identities keep native elections disabled, and scripted succession does not advance the pre-event election clock. |
| Sixty obsolete lower-case runtime flag files remained deployed | **CLOSED** | Fresh enumeration found zero `utopia_new_utopia`, `utopia_necessary_commonwealth`, `utopia_league_of_need`, or `utopia_marked_bounds_state` TGAs in `gfx/flags/`, including medium/small and ideology variants. |
| Current documentation described those obsolete flags as live | **OPEN, DOCUMENTATION ONLY** | `docs/assets/015_utopia_manifesto/manifest.md:50-52` and `:345-375`, plus `docs/events/015_utopia_manifesto/overview.md:117-125`, still describe the removed package as current. |

## Exact political lifecycle audit

### Acceptance snapshot

The acceptance event recruits all 24 Event 015 characters and then initializes
the identity package at `events/015_utopia_manifesto.txt:24-60`. Recruitment
does not add a political role. The preceding acceptance helper at
`common/scripted_effects/015_utopia_manifesto_effects.txt:303-326` initializes
the Ledger and focus package but does not set politics, promote a character,
rename a party, change an election field, replace an OOB, or set a cosmetic
tag. The recorded snapshot is therefore the recipient's pre-Event 015 political
state.

The snapshot at
`common/scripted_effects/015_utopia_manifesto_identity_effects.txt:165-175`
stores:

- `current_party_ideology_group` as the original ruling ideology group;
- `country_leader` as the exact original character pointer;
- the active country-leader ideology subtype through the helper at `:64-161`;
- the original `has_elections = yes/no` state as a country flag.

### Exact subtype proof

The only loaded ideology database file is
`common/ideologies/00_ideologies.txt`. A nested-block enumeration found 24
actual entries inside its four `types` blocks. The snapshot helper contains 24
`has_country_leader_ideology` branches. Set comparison produced:

- missing loaded subtypes: `0`;
- extra snapshot subtypes: `0`;
- duplicate snapshot branches: `0`.

Coverage includes the two Chaos Redux subtypes `ritual_predation` and
`resonant_brood_hierarchy` as well as all 22 vanilla subtypes in the loaded
file.

This distinction is necessary. Installed official documentation at
`documentation/effects_documentation.md:5149-5170` says that
`promote_character` requires an ideology when a character has several leader
roles and demonstrates a subtype (`nazism`). Official trigger documentation at
`documentation/triggers_documentation.md:4052-4067` explicitly distinguishes
`has_ideology = stalinism` from `has_ideology_group = communism`. The offline
wiki likewise defines the argument as an ideology type/sub-ideology. The live
repair now follows that contract.

### Formed package and scripted succession

The five formation helpers at
`common/scripted_effects/015_utopia_manifesto_identity_effects.txt:403-483`
implement:

- Voluntary Commonwealth: democratic/socialist Household Assembly;
- Council Union: communist/anarchist-communist Council of Callings;
- Planned Utopia: neutral/oligarchic Board of Measure;
- Closed Island: fascist/fascist-ideology Stewardship Council;
- Practical Commonwealth: the recipient's saved political group and leader,
  with a visible Humanist Cabinet/organization layer rather than a party-name
  overwrite.

All five formed routes set `elections_allowed = no`. The four institutional
routes install explicit successor bodies at `:538-605`; the Practical route
records its constitutional succession at `:606-611` while retaining the
recipient's constitutional leader. `utopia_manifesto_advance_current_route_succession`
dispatches all five at `:613-653`. The Second Generation focus calls it at
`common/national_focus/015_utopia_manifesto_focus_tree.txt:3410-3414`.

### Teardown

`utopia_manifesto_teardown_identity_package` at
`common/scripted_effects/015_utopia_manifesto_identity_effects.txt:296-340`:

1. removes all Event 015 institutional leader roles;
2. retires all 24 Event 015 characters;
3. sets the saved ruling ideology group with native elections still disabled;
4. promotes the exact surviving original character using the exact saved
   subtype;
5. restores the original election-permission boolean;
6. drops the cosmetic tag;
7. clears route, successor, advisor, achievement, snapshot, and initialization
   state.

The promotion is guarded by the saved variable, `has_character`, and
`can_be_country_leader`. A dead or otherwise invalid original character is not
silently replaced, matching the requested "exact surviving leader" contract.

## Requirement matrix

| Requirement | Result | Evidence |
| --- | --- | --- |
| Original tag and base flag continuity | **PASS** | Acceptance at `common/scripted_effects/015_utopia_manifesto_effects.txt:303-326` loads the focus tree without changing tag/cosmetic tag; route cosmetic tags are first applied at `common/scripted_effects/015_utopia_manifesto_identity_effects.txt:403-483` and removed at `:330`. |
| Existing leader, forces, technologies, and territory at acceptance | **PASS** | `events/015_utopia_manifesto.txt:24-60` recruits characters without adding leader roles. The acceptance path has no OOB replacement, unit deletion, technology reset, or state transfer. |
| Five playable routes and identities | **PASS** | Five route state setters exist at `common/scripted_effects/015_utopia_manifesto_effects.txt:941-1041`; five institution/formation branches and five cosmetic tags exist in the identity helper. |
| Existing parties remain intact | **PASS** | No Event 015 `set_party_name` call exists. `common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt:19-28` exposes five route organizations through `GetUtopiaManifestoPoliticalOrganization`; the Ledger consumes it at `localisation/english/015_utopia_manifesto_l_english.yml:34`. |
| Route organizations visible outside party-name mutation | **PASS** | The route organizations also have institution flags, five idea families at `common/ideas/015_utopia_manifesto_ideas.txt:150-371`, route decisions/advisors, and Ledger display. |
| Leaders and institutional councils | **PASS** | Eight founder/successor institutional characters are defined at `common/characters/015_utopia_manifesto_characters.txt:16-86`, recruited at acceptance, promoted only at formation/succession, and retired at teardown. |
| Advisor roster and lifecycle | **PASS** | Sixteen advisors are defined at `common/characters/015_utopia_manifesto_characters.txt:92-398`; each has a unique role trait, route/shared visibility, political-power cost, AI weight, and on-add/on-remove state. All 16 are recruited and retired. |
| Staged ideas never exceed three active Event 015 national spirits | **PASS** | Acceptance installs exactly three at `common/scripted_effects/015_utopia_manifesto_country_effects.txt:113-120`. Every family helper clears its predecessor before adding a replacement. Route property/institution, store, garden, auxiliary, and stewardship helpers deliberately swap slots at `:188-484`; the garden focus clears inherited order before adding garden state at `common/national_focus/015_utopia_manifesto_focus_tree.txt:2253-2257`. |
| Existing forces remain | **PASS** | No Event 015 helper deletes/disbands a unit or loads an OOB. Formation and teardown do not replace recipient divisions or templates. |
| New military growth is paid and bounded | **PASS** | The only eight Event 015 `create_unit` callsites are inside `utopia_manifesto_deploy_paid_formation` at `common/scripted_effects/015_utopia_manifesto_effects.txt:4791-4853`. `:4855-4873` deducts manpower, infantry equipment, support equipment, and army experience before deployment; `:4880-4905` rechecks affordability. |
| No free formation/league annexation | **PASS** | The formation decision charges PP/equipment at `common/decisions/015_utopia_manifesto_decisions.txt:4968-4995`. Identity and aftermath helpers contain no `annex_country`, state-core grant, or league-member transfer. |
| Succession | **PASS** | Four successor bodies and the constitutional succession result are dispatched explicitly by `common/scripted_effects/015_utopia_manifesto_identity_effects.txt:538-653`. |
| Genuine non-annexed collapse | **PASS** | `on_capitulation` at `common/on_actions/015_utopia_manifesto_on_actions.txt:63-99` calls the guarded/idempotent aftermath producer at `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt:17-37`. |
| Constitutional-abandonment collapse | **PASS** | Government mismatch trigger at `common/scripted_triggers/015_utopia_manifesto_reachability_triggers.txt:185-206`; `on_government_change` consumer at `common/on_actions/015_utopia_manifesto_on_actions.txt:101-112`. |
| Teardown, aftermath, and disable | **PASS** | `utopia_manifesto_enter_disable_safe_state` at `common/scripted_effects/015_utopia_manifesto_effects.txt:5275-5282` removes ideas, calls identity teardown, clears runtime, and disables the kernel. `utopia_manifesto_finalize_aftermath` at `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt:215-273` preserves selected legacies only after cleanup. |
| League continuity | **PASS** | `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt:102-154` chooses a viable non-subject successor, preserves member records, transfers faction leadership where applicable, and clears the founder's formal-defense flag before ordinary cleanup. It never annexes members. |
| AI and playability | **PASS** | The focus tree has 124 focus definitions and 124 `ai_will_do` blocks. The decision file has 105 AI-weight blocks. `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt` provides opening restraint, all five routes, escalation/recovery, crisis, and mature-commonwealth strategy blocks. |
| Achievements | **PASS** | The accepted matrix's 14 IDs exactly match 14 definitions at `common/achievements/chaos_redux_achievements.txt:2258-2579`. Each has NAME/DESC localisation, three registered sprites, and three runtime DDS files: 42 aliases and 42 DDS files total. |
| Obsolete lower-case runtime flags/references | **PASS for live source** | Zero obsolete TGA files exist in any runtime flag size. Active cosmetic definitions and `set_cosmetic_tag` calls name only the five uppercase families. |
| Current documentation alignment | **FAIL** | See the documentation-only findings below. |

## Active visual-package validation

### Route flags - PASS

Fresh runtime enumeration found exactly 25 expected stems in each of:

- `gfx/flags/`;
- `gfx/flags/medium/`;
- `gfx/flags/small/`.

That is five route families times one unsuffixed plus four ideology variants
times three sizes: 75 TGAs, with no missing or extra Event 015 route-identity
stem. `flag_identity_validation_2026_07_15.json` reports `passed`, 21 independent
ImageGen compositions, four explicit unsuffixed/canonical aliases, correct
`82x52`, `41x26`, and `10x7` output, bottom-left uncompressed 32-bit TGA, solid
hard-fill normalization, and four unique ideology hashes per route.

I visually inspected both
`contact_sheets/flags_corrected_imagegen_source_contact_sheet.png` and
`contact_sheets/flags_corrected_decoded_contact_sheet.png` under
`docs/assets/015_utopia_manifesto/route_identity_2026_07_14/`. The 21 active
sources are separate flat heraldic compositions, not fabric photographs,
painterly flag mockups, or palette-only copies. The decoded runtime flags retain
the intended hard-fill treatment.

`imagegen_source_evidence_2026_07_15.json` records exact byte equality between
all 21 independent package sources and their built-in ImageGen store objects.
The four unsuffixed aliases are explicitly documented rather than disguised
fallbacks.

### Institutional leaders - PASS

- Runtime files: `4`.
- Dimensions: `156x210` (DDS byte size `131,168` each).
- Unique runtime hashes: `4/4`.
- Built-in ImageGen evidence: `4/4`, status `passed`.
- Sprite registrations: `interface/015_utopia_manifesto.gfx:1752-1768`.

Visual inspection of
`institutional_portraits_corrected_processed_contact_sheet.png` found four
distinct HOI4-painted institutional collectives. Founder/successor pairs share
the same portrait intentionally because each pair represents the same durable
body, not a renamed individual.

### Advisor dossier portraits - PASS

- Runtime files: `16`.
- Dimensions: `65x67` (DDS byte size `17,548` each).
- Unique runtime hashes: `16/16`.
- Unique independent source portraits: `16/16`.
- Sprite registrations: `interface/015_utopia_manifesto.gfx:1770-1834`.

`advisor_validation_2026_07_15.json` reports `passed` with explicit per-source
crop metadata, decoded equality, and zero blocked sources. Visual inspection of
`advisor_sources_contact_sheet.png` and
`advisor_portraits_enlarged_nearest_contact_sheet.png` confirms sixteen
separately composed fictional people cropped into dark bevelled dossier cards.
They are not square portraits and not resized institutional leader images.

### Route emblems - PASS

Five distinct `64x64` transparent emblem DDS files exist for Household
Congress, Congress of Common Tables, Network Directorate, Island Hierarchy,
and Plural Compact. Their handles are registered at
`interface/015_utopia_manifesto.gfx:1836-1856`, and the Ledger scripted GUI
selects them through the matching identity flags. Visual review of
`league_emblems_decoded_contact_sheet.png` found five distinct silhouettes with
real transparency.

## Documentation-only findings

### D1 - root asset manifest makes false current-state claims

`docs/assets/015_utopia_manifesto/manifest.md` is not aligned with the live
package:

- `:50-52` says the four removed lower-case flag families and their ideology
  variants exist in runtime. They do not.
- `:345-375` presents the same removed flag paths as runtime deliverables
  without labelling the section historical/superseded.
- `:42` and `:173` say the decision file has zero `icon =` assignments. The
  current file has 144 icon assignments.
- `:12`, `:131`, and `:470` say 13 report sprites and three news sprites still
  require registration. `interface/015_utopia_manifesto.gfx:3-71` already
  registers 14 current report sprites and all four Event 015 news sprites.

The focused active route-identity manifest at
`docs/assets/015_utopia_manifesto/route_identity_2026_07_14/manifest.md` is
accurate and remains the correct visual-package authority.

### D2 - Event 015 mechanic document describes removed identities and missing visuals

`docs/events/015_utopia_manifesto/overview.md` is also stale:

- `:117-125` describes the four removed lower-case cosmetic identities as the
  live late package instead of the five current identities.
- `:142` says the five current super-event DDS files do not exist. They are
  present and registered.

These are documentation contradictions, not runtime fallbacks. The obsolete
lower-case TGA deployment itself is gone. Historical source PNGs and other
explicitly labelled legacy visual records remain under the asset history, but
none is used as an active route flag.

## Maintenance note

Exact leader restoration now depends on the explicit 24-subtype enumeration in
`utopia_manifesto_record_original_leader_ideology`. This is complete for the
sole currently loaded ideology file. If a future change adds an ideology
subtype, the snapshot helper must be extended in the same change. This is a
maintenance invariant, not a current blocker.

## Validation evidence snapshot

| Check | Result |
| --- | --- |
| Loaded ideology types vs snapshot branches | `24 / 24`; missing `0`; extra `0`; duplicates `0` |
| Active flag families/files | `5`; `75`; missing `0`; extra `0` |
| Obsolete lower-case runtime TGAs | `0` |
| Institutional leader DDS | `4`; unique hashes `4`; `156x210` |
| Advisor DDS | `16`; unique hashes `16`; `65x67` |
| Character declarations/recruitment | `24 / 24` |
| Advisor traits | `16` |
| Country identity name/DEF/ADJ keys | `75 / 75` |
| Focus AI blocks | `124 / 124` focuses |
| Achievement definitions/matrix IDs | `14 / 14` |
| Achievement aliases/runtime DDS | `42 / 42` |
| Event 015 `set_party_name`, `election_frequency`, `last_election`, `hold_election` calls | `0` |
| Event 015 `create_unit` callsites outside the paid deploy helper | `0` |

## References and audit scope

Skills used:

- `chaos-redux-events` for Event 015 integration/lifecycle expectations;
- `chaos-redux-event-assets` for source provenance, visual review, manifests,
  and runtime-format evidence;
- `hoi4-focus-trees` for package loading, route, AI, and post-formation review;
- `chaos-redux-subagents` for the bounded auditor handoff contract.

Required offline wiki pages consulted:

- Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On
  actions, Event modding, Decision modding, Idea modding, AI modding;
- National focus modding, Country creation, Portrait modding, and Achievement
  modding.

Installed vanilla documentation consulted included
`script_concept_documentation.md`, `effects_documentation.md`,
`triggers_documentation.md`, `dynamic_variables_documentation.md`,
`loc_formatter_documentation.md`, the on-actions documentation, and script
constants documentation. Vanilla precedents were checked for token-valued
ruling-party snapshots, `has_country_leader_ideology`, and
`promote_character`.

The audit traced acceptance, route commitment, formation, paid growth,
succession, capitulation collapse, government-change collapse, Total Repeal,
annexation safe state, aftermath, disable cleanup, and league succession. It
also independently checked runtime counts, hashes, dimensions, source evidence,
sprite registration, character recruitment, achievement coverage, and active
visual contact sheets.

No live-game scenario was executed by this read-only auditor. The conclusions
above are static-source and binary/package evidence; no unresolved engine
behavior is being presented as proven.

## Files changed by this audit

- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/country_package_completion_reaudit_2026_07_15.md`

No gameplay, localisation, interface, source asset, processed asset, manifest,
spreadsheet, or skill file was changed by this auditor. No commit was created.

## Simplifications, omissions, blockers, and risks

- Audit simplifications: none.
- Audit-surface omissions: none within the country-package prompt.
- Live gameplay blockers: none.
- Active route-identity asset blockers: none.
- Fallbacks or placeholder substitutions found: none.
- Repository completion blocker: stale current-facing documentation D1-D2.
- Current maintenance risk: future ideology subtypes must be added to the exact
  leader-subtype snapshot enumeration.
