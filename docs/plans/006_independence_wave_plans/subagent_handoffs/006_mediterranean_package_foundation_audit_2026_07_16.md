# Event 006 Mediterranean package foundation audit

Date: 2026-07-16

Packages: IW-017 Corsica (`COR`), IW-018 Sardinia (`ARX`), IW-019 Sicily
(`ASX`)

Mode: bounded patch-capable audit of the six parent-authorized foundation
files; no shared loader, focus, event, decision, localisation, asset, FORM-05,
or vanilla COR file was edited

## Verdict

The six-file Mediterranean foundation is internally consistent after the
repairs recorded below, but the three packages are **not content-ready**. This
handoff grants no readiness attestation and no
`independence_wave_package_content_ready` flag.

The audit introduced no fallback art, placeholder localisation, generic
country package, or substitute route. Missing presentation and integration
work remains fail-closed and is listed explicitly below.

## Required references consulted

- Repository `AGENTS.md`.
- Repo skills: `chaos-redux-events`, `chaos-redux-focus-trees`,
  `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
- Offline wiki: Data structures, Triggers, Effects, Modifiers, Localisation,
  Scopes, On actions, Event modding, Decision modding, Idea modding, AI
  modding, Country creation, Character modding, and National focus modding.
- Vanilla documentation: `script_concept_documentation.md`, script-constant
  schema documentation, character documentation, and relevant trigger,
  effect, and modifier entries.
- Vanilla/project precedents: vanilla COR history and country definition,
  CAT/GLC country histories, vanilla character/adviser records, and the mature
  Event 006 AJX package proof/roster pattern.
- Event 006 source-of-truth specifications: country-package contract, focus
  assignment and idea lifecycle, AI/assets/acceptance, candidate registry,
  tag collision/reuse audit, and IW-017 through IW-019 research rows.

Direct onomastic checks also supported the fictional male identities. Corsican
records attest the Petru/Santucci combination; Sardinian regional records
attest Antioco Melis and the Pala/Vittorio components; Sicilian regional
records attest the Restivo/Sebastiano components and Vincenzo Lanza. These are
used as fictional alternate-history characters, not as claims that a real
person held the scripted office.

## Files and repairs

### `common/characters/006_independence_wave_mediterranean_characters.txt`

- Preserved stable institutional script tokens because the current setup,
  trigger, history, and decision surfaces already reference them.
- Replaced every institutional/council **display identity and portrait
  consumer** with a distinct fictional male individual. This follows the
  binding user correction that Event 006 country leaders use male HOI4-style
  portrait subjects rather than people-free establishment images.
- Kept the Event 006 default-male metadata contract: no explicit `gender`
  field is added. All personal names are male and the five head-of-state
  portrait consumers are male one-person assets.
- Kept all six gameplay advisers asset-neutral: none has a `portraits` block,
  sprite reference, or custom adviser-dossier dependency.
- Added an `oligarchism` leader role to the Sardinian and Sicilian crown
  leaders while retaining their `conservatism` roles. The traditional route
  can therefore promote them under neutrality without a democratic workaround.
- Corrected the COR adapter comment so it states the recruitment/cleanup
  contract instead of claiming that an external adapter had already fulfilled
  it.

Stable internal token to player-facing male identity:

| Stable internal token | Display-name key | Exact portrait sprite consumer |
|---|---|---|
| `COR_corsican_municipal_congress` | `COR_petru_santucci` | `GFX_portrait_COR_independence_wave_petru_santucci` |
| `ARX_sardinian_provisional_assembly` | `ARX_antioco_melis` | `GFX_portrait_ARX_independence_wave_antioco_melis` |
| `ARX_sardinian_crown_consultative_council` | `ARX_vittorio_pala` | `GFX_portrait_ARX_independence_wave_vittorio_pala` |
| `ASX_sicilian_provisional_assembly` | `ASX_sebastiano_restivo` | `GFX_portrait_ASX_independence_wave_sebastiano_restivo` |
| `ASX_sicilian_crown_council` | `ASX_vincenzo_lanza` | `GFX_portrait_ASX_independence_wave_vincenzo_lanza` |

The complete frozen live portrait-consumer list after the user correction is:

1. `GFX_portrait_COR_independence_wave_petru_santucci`
2. `GFX_portrait_COR_independence_wave_pasquale_venturi`
3. `GFX_portrait_COR_independence_wave_pasquale_venturi_small`
4. `GFX_portrait_ARX_independence_wave_antioco_melis`
5. `GFX_portrait_ARX_independence_wave_vittorio_pala`
6. `GFX_portrait_ARX_independence_wave_gavino_piras`
7. `GFX_portrait_ARX_independence_wave_gavino_piras_small`
8. `GFX_portrait_ASX_independence_wave_sebastiano_restivo`
9. `GFX_portrait_ASX_independence_wave_vincenzo_lanza`
10. `GFX_portrait_ASX_independence_wave_salvatore_licata`
11. `GFX_portrait_ASX_independence_wave_salvatore_licata_small`

All eight large consumers require male one-person HOI4-style portraits. The
three `_small` consumers are commander army-small dossiers, not gameplay
adviser icons.

### `common/ideas/006_independence_wave_mediterranean_ideas.txt`

- Audited without editing.
- The 19 IW-017 through IW-019 ideas are structurally defined and referenced;
  their crisis/mature and route modifiers have the expected negative/positive
  direction and use the central modifier ladder.
- No picture-token substitution was made because five exact picture families
  do not resolve and no fallback was authorized.
- The three FORM-05 ideas were observed but left outside this assignment.

### `common/script_constants/006_independence_wave_mediterranean_constants.txt`

- Added shared pressure bounds `minimum = 0` and `maximum = 100`. The current
  package effects clamp all three island pressure variables to these constants;
  those references were previously undefined.
- Retained centralized pressure starts/thresholds, political distributions,
  durations, adviser cost/AI values, modifier ladder, and FORM-05 values.

### `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt`

- Expanded each command-roster proof to require both advisers and confirm
  `is_advisor = yes`, in addition to the commander role check.
- Corrected the COR government proof from the excluded popular-council route
  to the enabled traditional route and
  `independence_wave_cor_traditional_government` flag.
- Added region, depth, archetype, anchor ownership/control, former-host
  protected-state ownership, baseline-law, focus-assignment, route exclusion,
  host-route, power-struggle, ambition, league/formable, force-package, AI,
  lifecycle, incident, and capital proof where applicable.
- Superseded by the focus-engine audit: COR, ARX, and ASX require the full
  framework and reject the additive flag. COR additionally requires the
  vanilla `generic_focus` tree before assignment and restores it on cleanup,
  so a meaningful external COR tree is never replaced.
- Corrected Sicily's Level-2 proof to
  `independence_wave_asx_level2_module_ready`; the obsolete signature-module
  spelling is absent.
- Did not add any content-readiness grant.

### `history/countries/ARX - Event 006 Country Shell.txt`

### `history/countries/ASX - Event 006 Country Shell.txt`

- Audited the current in-flight histories and preserved their baseline laws
  and five-character recruitment lists.
- Added an explicit comment that country history never grants package-content
  readiness; final admission is external.
- No COR history file was created or changed. COR remains a registered vanilla
  tag with an additive, exact-origin adapter contract.

## Validation evidence

- The character file contains 14 definitions. All 14 roster-trigger character
  references resolve, and all 10 ARX/ASX history recruitments resolve.
- All six advisers are present in roster proofs with `is_advisor = yes`; all
  six adviser character blocks contain zero portrait or sprite consumers.
- Both crown leaders expose an `oligarchism` role, the COR route-government
  trigger checks the traditional route, and the ASX prepared proof checks the
  exact Level-2 flag.
- No institutional/council/congress portrait sprite token remains. The five
  retained institutional script identifiers expose the male name/sprite pairs
  listed above.
- Across the live character, idea, trigger, package-effect, and decision
  consumers, 61 distinct Mediterranean `constant:` references resolve with
  zero missing definitions.
- All eight political distributions sum to 100: COR/ARX/ASX start,
  constitutional, popular, traditional, military, and patron.
- All 19 IW-017 through IW-019 idea references resolve to a definition, and all
  five referenced adviser traits resolve to their live trait definitions.
- State-file inspection confirms the contracted anchors: state 1 Corsica,
  state 114 Sardinia, and state 115 Sicily, with no mod state override found.
  The HOI4 map inspector was also attempted but returned
  `MAP_MODEL_BUDGET_BLOCKED`; direct installed state history was used for this
  bounded check instead.
- None of the six authorized files grants
  `independence_wave_package_content_ready`.
- At the final read, the concurrently authored Mediterranean event file
  contains IDs `chaosx.nr6.21` through `.27`, the shared package dispatcher
  calls the Mediterranean setup/final-validation/cleanup adapters, and the COR
  cleanup adapter retires all four Event 006-only COR characters. These files
  were cross-referenced but not edited or fully audited under this assignment.

## Missing implementation and readiness blockers

1. **Portrait assets and registration:** all 11 exact sprite consumers listed
   above are live and none is registered or backed by a runtime DDS. The first
   five must now be produced as fictional male individual portraits; the
   earlier people-free institutional guidance is superseded.
2. **Focus/decision art:** the current concurrent focus and decision content
   has 14 unregistered package sprite consumers: seven `GFX_goal_*` and seven
   `GFX_decision_*` families for COR customs/mountain communes, ARX
   shipping/mountain guards, and ASX port/grain-straits/Two Sicilies.
3. **Idea art:** 15 of the 19 package ideas point to five nonexistent exact
   `GFX_idea_*` families (`generic_political_reform`,
   `generic_communist_revolution`, `generic_military_sphere`,
   `generic_trade_connections`, and `generic_neutrality_home_defense`). The
   other four resolve only to the same generic volunteer image and are not
   final distinct package art. No substitute was authorized.
4. **Localisation:** the live localisation corpus contains 0/14 character
   display-name keys, 0/19 package idea names, 0/19 package idea descriptions,
   0/19 package focus names/descriptions, 0/29 package decision
   names/descriptions, and 0/21 sampled event title/description/option keys for
   `.21` through `.27`. The five corrected male keys are the exact keys shown
   in the table above.
5. **AI strategy consumption:** COR/ARX/ASX setup currently publishes package
   AI-profile flags, but no matching country/package entries were found under
   `common/ai_strategy/` or `common/ai_strategy_plans/`. Focus and decision
   `ai_will_do` blocks do not replace the missing strategic profile consumer.
6. **Flag route/provenance closure:** COR vanilla flag reuse is valid. ARX and
   ASX have installed base triplets, but route coverage/ownership remains
   unresolved; the ASX base art is specifically constitutional-route evidence,
   not a neutral all-route baseline. The generated flag package also retains
   the migrated-reference hash-ledger defect recorded in the Mediterranean
   asset inventory handoff.
7. **Final acceptance surfaces:** event log/detail mappings, package
   documentation, spreadsheet/catalog alignment, and final asset manifests
   still need a parent-owned completion audit after the concurrent gameplay
   tranche settles. No readiness flag should be issued before those checks and
   the blockers above are closed.
8. **FORM-05 remains excluded and fail-closed:** its three idea definitions do
   not authorize a formable tag, identity, flag, emblem, decision icon, or
   readiness grant.

## Simplifications and handoff status

No fallback or simplification was introduced by this audit. The work is a
sound package-foundation repair, not a completion claim. No commit was made.

Skills used: `chaos-redux-events`, `chaos-redux-focus-trees`,
`chaos-redux-decisions-missions`, and `chaos-redux-subagents`. No skill was created or
updated.
