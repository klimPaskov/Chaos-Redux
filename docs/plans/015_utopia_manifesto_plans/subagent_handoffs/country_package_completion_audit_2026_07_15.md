# Event 15 Country-Package Completion Audit — 2026-07-15

## Verdict

**FAIL — not acceptance-ready.**

The current live package preserves the recipient tag, base flag, map, existing
forces, and opening leader; implements all five route identities, political
organizations, institutional leaders, succession paths, paid military growth,
and non-annexing formation; and contains a technically complete active visual
package. Penal Works also uses the shared exact population-loss and Deaths
transaction.

Two accepted-scope lifecycle gaps remain:

1. the non-annexed regime-collapse aftermath has no producer after the invalid
   war-entry producer was removed; and
2. terminal identity teardown cannot faithfully restore an arbitrary
   recipient's pre-event political state.

The runtime flag folders also retain four obsolete, unwired Event 15 flag
families whose ideology variants are identical and whose old documentation
still presents them as live. These files are explicitly distinguished below
from the corrected five-route package, which passes.

## Closing snapshot

This audit was re-baselined after `on_war` changed during the review. The
closing source inspected here is identified by these SHA-256 hashes:

| File | SHA-256 |
| --- | --- |
| `common/on_actions/015_utopia_manifesto_on_actions.txt` | `9F50786EFD19B7EEF56DCB36ACF82DFC59775F7BA3BFAAA5B27027CC6F5D5A8F` |
| `common/scripted_effects/015_utopia_manifesto_identity_effects.txt` | `AC2A56D4859FAAFF641E5567E7B0C34FBDC60F47C4A9ED5AB6E2399B19579488` |
| `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt` | `0A64A88CC9C9D44A1465A2C72D64932204020C33B3924C9164954E01FDDACAA6` |
| `events/015_utopia_manifesto.txt` | `A44FAE2E8B6D6FA7A0AAB71ED496F522AFC3AA6D186DF6E4FC16D80466430752` |
| `common/characters/015_utopia_manifesto_characters.txt` | `5CDF2EA793216351B5A250BBB1BB0EEA84103E7668791B30867216AF436749CB` |
| `common/scripted_effects/015_utopia_manifesto_effects.txt` | `9CEEF77E0C71A84FAD6D6B08D2CC3C6D892E8D2B9EE29CA05D220CE288C16AAB` |
| `common/decisions/015_utopia_manifesto_decisions.txt` | `16097FCFD0DCA2C45B15ECDBC16EFFE8B002B470BFD7713E34119771D9A4BB0E` |
| `common/national_focus/015_utopia_manifesto_focus_tree.txt` | `CEF02BF44C1020B13EAA4423DF19218BD888B82C12C1A8687C654EBDCB3A1DA7` |
| `interface/015_utopia_manifesto.gfx` | `218CC01E81AD28ABEA77F9AF2C0E6B50049C7376BB68691E01ED0E9F627A8E39` |

## Severity findings

### P0 — none in the closing snapshot

The earlier live defect that scheduled the terminal aftermath whenever an
accepted country entered any war is no longer present. The closing `on_war`
hook only refreshes the Ledger and explicitly excludes war entry as a collapse
condition at
`common/on_actions/015_utopia_manifesto_on_actions.txt:19-28`.

This correction preserves the live defensive-war and mature-war surfaces,
including the Closed Circle proof at
`common/achievements/chaos_redux_achievements.txt:2491-2522` and the mature war
focus at `common/national_focus/015_utopia_manifesto_focus_tree.txt:3489-3505`.

### P1 — the genuine regime-collapse aftermath branch is unreachable

Accepted Part 6 requires local aftermath when the country collapses, abandons
the constitution, or is annexed:
`docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_6_evolutions_events_and_reactions.md:1037-1051`.

The live call graph covers two of those terminal cases:

- Total Repeal calls Event `chaosx.nr15.120` through
  `utopia_manifesto_begin_total_repeal_aftermath` at
  `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt:10-15`.
- Annexation performs non-interactive safe teardown through
  `utopia_manifesto_enter_annexation_safe_state` at
  `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt:31-38`,
  called from `common/on_actions/015_utopia_manifesto_on_actions.txt:90-147`.

The non-annexed collapse case is absent:

- `on_capitulation` only resolves defender evidence and refreshes the Ledger at
  `common/on_actions/015_utopia_manifesto_on_actions.txt:63-87`.
- `utopia_manifesto_aftermath_from_regime_collapse` has no setter. Its only
  behavioral consumer is the Event 120 AI modifier at
  `events/015_utopia_manifesto.txt:4055-4062`; the remaining references clear
  it at
  `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt:31-38`
  and `:239-250`.
- `utopia_manifesto_record_achievement_regime_collapse` is defined at
  `common/scripted_effects/015_utopia_manifesto_identity_effects.txt:898-900`
  but has no callsite.

Result: the invalid any-war collapse path is fixed, but an accepted country
that actually capitulates without being annexed cannot enter the designed
regime-collapse aftermath or set its dedicated historical evidence.

Required correction: use one bounded, documented actual-collapse edge to set
the collapse provenance, record its achievement evidence, and schedule Event
120 once. Do not restore the removed `on_war` behavior.

### P1 — repeal teardown restores only an ideology family, not the recipient's political state

The identity initializer records only one of four ruling-ideology flags at
`common/scripted_effects/015_utopia_manifesto_identity_effects.txt:54-78`.
It does not record whether elections were allowed, election frequency, the
current ruling organization name, any nonstandard party names, or a pointer to
the current leader.

Terminal restoration then:

- overwrites all four party organizations with assumed `[TAG]_..._party`
  localisation keys at
  `common/scripted_effects/015_utopia_manifesto_identity_effects.txt:156-169`;
- hardcodes democratic recipients to `elections_allowed = yes` and every
  other recipient to `elections_allowed = no` at
  `common/scripted_effects/015_utopia_manifesto_identity_effects.txt:172-189`;
- removes and retires the Event 15 leadership/advisor roster, applies that
  lossy restoration, and drops the cosmetic tag at
  `common/scripted_effects/015_utopia_manifesto_identity_effects.txt:191-236`.

This is not a faithful inverse for arbitrary recipients. A democratic regime
with suspended elections, a non-democratic constitutional regime, a country
with a custom election frequency, or a country whose parties were renamed by
another live system exits Event 15 with political state it did not have before
acceptance. The existing leader role is not deleted on formation, but the
source also does not explicitly prove which pre-event individual becomes
current again after the Event 15 role is removed.

Required correction: define an accepted restoration contract that preserves
the actual pre-event election and leadership state and does not overwrite
unmodified opposition parties. If exact arbitrary party-name restoration is
not supported by the engine, that limitation requires an explicit design
decision; it must not be silently presented as exact restoration.

### P2 — four obsolete flag families remain deployed and documented as live

The active gameplay uses only these cosmetic tags:

- `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH`
- `UTOPIA_MANIFESTO_COUNCIL_UNION`
- `UTOPIA_MANIFESTO_PLANNED_UTOPIA`
- `UTOPIA_MANIFESTO_CLOSED_ISLAND`
- `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH`

They are the only Event 15 cosmetic definitions at
`common/countries/cosmetic.txt:33-51` and the only `set_cosmetic_tag` calls at
`common/scripted_effects/015_utopia_manifesto_identity_effects.txt:328-430`.

Nevertheless, the runtime flag directories still contain 60 files for four
lower-case, undefined families:

- `utopia_new_utopia`
- `utopia_necessary_commonwealth`
- `utopia_league_of_need`
- `utopia_marked_bounds_state`

Each family has an unsuffixed stem plus four ideology stems at all three sizes.
For every family, all five main-size stems are byte-identical. Visual review of
`docs/assets/015_utopia_manifesto/contact_sheets/utopia_cosmetic_flags_imagegen_contact.png`
also found textured, shaded emblem art rather than the corrected flat
hard-fill flag treatment.

They have no live cosmetic definition or script consumer, but stale
documentation still says they are applied at
`docs/events/015_utopia_manifesto/overview.md:117-125` and lists them as the current
cosmetic package at `docs/assets/015_utopia_manifesto/manifest.md:50-52` and
`:345-362`.

This does **not** invalidate the corrected active five-route package. It does
violate the literal requirement that every Event 15 flag deployed in runtime
have intentional variants and leaves completion documentation contradictory.
Remove the dead runtime files and supersede the stale documentation rather
than regenerating an unused second identity family.

### P3 — leader resumption remains an engine-behavior risk

Formation adds and promotes an institutional role without deleting the
recipient's pre-existing leader role at
`common/scripted_effects/015_utopia_manifesto_identity_effects.txt:328-419`.
Teardown removes the Event 15 role and retires its character at `:191-223`, but
does not capture or explicitly promote the original current leader. Static
source review therefore proves that the original named character is not
explicitly retired by Event 15, but cannot prove which eligible character the
engine will present after teardown. This risk should be resolved together with
the P1 political-restoration contract.

## Requirement matrix

| Requirement | Result | Evidence |
| --- | --- | --- |
| Original tag and base flag before transformation | **PASS** | Acceptance loads the focus package without changing tag, cosmetic tag, state ownership, or OOB at `common/scripted_effects/015_utopia_manifesto_effects.txt:303-325`; cosmetic tags are applied only at formation in `common/scripted_effects/015_utopia_manifesto_identity_effects.txt:328-430`. |
| Existing leader during the opening | **PASS** | Acceptance recruits Event 15 characters but adds no country-leader role at `events/015_utopia_manifesto.txt:24-60`; the first promotions occur only in the four formed identities. |
| Five distinct route identities | **PASS** | Route institutions are committed at `common/scripted_effects/015_utopia_manifesto_identity_effects.txt:273-321`; five formation dispatch branches exist at `:432-475`. |
| Ideologies and governments | **PASS for formation; FAIL for exact repeal restoration** | Democratic/socialism, communism/anarchist communism, neutrality/oligarchism, fascism/fascist ideology, and retained-ideology constitutional humanism are implemented at `:328-430`; teardown issue is P1 above. |
| Parties | **PASS for route presentation; FAIL for exact repeal restoration** | Five route organizations are applied at `:328-430` and localised at `localisation/english/015_utopia_manifesto_country_package_l_english.yml:80-90`. |
| Institutions and leaders | **PASS** | Eight founder/successor institutional characters are declared at `common/characters/015_utopia_manifesto_characters.txt:16-86`; four formed routes promote the appropriate founder body at `common/scripted_effects/015_utopia_manifesto_identity_effects.txt:328-419`. |
| Succession | **PASS** | Four successor bodies plus the humanist constitutional election are installed at `common/scripted_effects/015_utopia_manifesto_identity_effects.txt:481-598`; the Second Generation focus invokes succession at `common/national_focus/015_utopia_manifesto_focus_tree.txt:3397-3408`. |
| Advisor roster and lifecycle | **PASS** | Sixteen advisors are defined at `common/characters/015_utopia_manifesto_characters.txt:92-398`; all 24 Event 15 characters are recruited at `events/015_utopia_manifesto.txt:29-54` and all 24 are retired in terminal teardown at `common/scripted_effects/015_utopia_manifesto_identity_effects.txt:191-223`. |
| Existing forces preserved | **PASS** | No Event 15 formation/identity/aftermath helper loads an OOB, deletes a unit, or replaces an existing template. |
| New units paid, gated, and institutionally distinct | **PASS** | Dynamic costs are prepared at `common/scripted_effects/015_utopia_manifesto_effects.txt:4499-4616`; eight distinct templates/deploy branches are at `:4618-4834`; payment precedes creation at `:4837-4887`; affordability/capacity triggers are at `common/scripted_triggers/015_utopia_manifesto_triggers.txt:2505-2613`. |
| Auxiliaries paid and bounded | **PASS** | Contract costs and the paid auxiliary formation are at `common/decisions/015_utopia_manifesto_decisions.txt:4310-4397`; dependency state is set only after military payment succeeds at `:4366-4375`. |
| Formation paid and does not annex members | **PASS** | Proclamation charges political power, support equipment, trains, and convoys before Event 10 at `common/decisions/015_utopia_manifesto_decisions.txt:4946-4973`; formation proof and identity effects change flags, politics, leader presentation, and cosmetic identity only at `common/scripted_effects/015_utopia_manifesto_effects.txt:4138-4175` and `common/scripted_effects/015_utopia_manifesto_identity_effects.txt:432-475`. |
| League survives/dissolves without member annexation | **PASS** | Post-founder succession records members and may transfer faction leadership without annexation at `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt:80-132`; colonial/stewardship scopes are returned or reconciled at `:134-172`. |
| Total Repeal cleanup | **PARTIAL / FAIL** | Domestic systems and Event 15 characters are torn down and the cosmetic tag is dropped, but political restoration is lossy as described in P1. |
| Regime-collapse dissolution | **FAIL** | Accepted aftermath exists, but its non-annexed collapse producer is missing as described in P1. |
| Penal Works real project and shared deaths | **PASS** | The paid targeted decision is at `common/decisions/015_utopia_manifesto_decisions.txt:1394-1434`; start/completion request exact civilian loss at `common/scripted_effects/015_utopia_manifesto_decision_effects.txt:885-978`; the shared transaction delegates to `chaos_meter_register_deaths` at `common/scripted_effects/chaosx_dynamic_effects.txt:720-800`. |

## Active visual-package validation

### Corrected route flags — PASS

- Runtime coverage: 75 TGA files, consisting of five route families, five
  stems per family, and normal/medium/small sizes.
- Header contract: all 25 normal flags are `82x52`, all 25 medium flags are
  `41x26`, and all 25 small flags are `10x7`; every inspected file is
  uncompressed 32-bit TGA with bottom-left origin.
- Ideology distinctness: all four ideology compositions in every route family
  have unique hashes. The only duplicate art is the four documented
  unsuffixed/canonical pairs; Practical Commonwealth has five unique stems.
- Provenance: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/imagegen_source_evidence_2026_07_15.json`
  records 21 flag compositions and four institutional portraits, 25 distinct
  built-in ImageGen handles, exact package-source hashes, and zero failed
  records. The four unsuffixed aliases are explicit.
- Art direction and finishing: the flat, hard-fill, non-fabric requirement is
  recorded at
  `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/prompts/corrected_flag_and_institutional_prompts_2026_07_15.md:7-17`;
  all 21 distinct calls are listed at `:19-41`, with aliases at `:43-48`.
  Visual review used `flags_corrected_decoded_contact_sheet.png` and
  `flags_corrected_small_10x7_readability_contact_sheet.png` from that
  package.

The four unsuffixed aliases are engine coverage from an independently
generated canonical ideology composition, not a placeholder or a generic
fallback asset.

### Institutional leaders — PASS

- Four runtime DDS files are present, byte-distinct, and exactly `156x210`.
- All four package/runtime pairs are byte-identical.
- Four independent ImageGen handles and exact-byte source evidence are present
  in `imagegen_source_evidence_2026_07_15.json`.
- Sprite registration is complete at
  `interface/015_utopia_manifesto.gfx:1752-1768`.
- The eight founder/successor characters intentionally share the four route
  institutional portraits within their route family.

### Advisor dossiers — PASS

- Sixteen runtime DDS files are present, all exactly `65x67`, with 16 unique
  runtime hashes and 16 unique source hashes.
- Package/runtime DDS mismatch count is zero; advisor/leader hash overlap is
  zero.
- `advisor_validation_2026_07_15.json` records 16 separate fictional ImageGen
  people, separate explicit crops, unique processed hashes, decoded equality,
  and approved native-size review.
- The native dossier and source review sheets were inspected at
  `contact_sheets/advisor_portraits_native_contact_sheet.png` and
  `contact_sheets/advisor_sources_contact_sheet.png` under the active package.
- All 16 sprites are registered at
  `interface/015_utopia_manifesto.gfx:1770-1834`; all 20 unique character
  portrait sprite references resolve to existing runtime textures.

## Character and localisation checks

- Character declarations found: 24.
- Recruited on acceptance: 24 of 24.
- Retired on terminal teardown: 24 of 24.
- Unique character portrait handles: 20; unresolved handles or textures: 0.
- Character name/description pairs: 24 of 24 present. The Board of Measure
  description is supplied at
  `localisation/english/015_utopia_manifesto_focus_l_english.yml:67-68`.
- Advisor traits: 16; missing definitions, names, or descriptions: 0.
- Five country identity families have base plus four ideology name/DEF/ADJ
  sets at
  `localisation/english/015_utopia_manifesto_country_package_l_english.yml:4-78`.

## Files inspected

Gameplay and presentation:

- `events/015_utopia_manifesto.txt`
- all `common/scripted_effects/015_utopia_manifesto*.txt` files
- `common/scripted_effects/chaosx_dynamic_effects.txt` and its API documentation
- `common/scripted_triggers/015_utopia_manifesto_triggers.txt`
- `common/on_actions/015_utopia_manifesto_on_actions.txt`
- `common/decisions/015_utopia_manifesto_decisions.txt`
- `common/national_focus/015_utopia_manifesto_focus_tree.txt`
- `common/characters/015_utopia_manifesto_characters.txt`
- `common/country_leader/015_utopia_manifesto_traits.txt`
- `common/countries/cosmetic.txt`
- `common/achievements/chaos_redux_achievements.txt`
- `interface/015_utopia_manifesto.gfx`
- Event 15 English localisation files
- active and obsolete Event 15 flag folders, leader/advisor runtime folders,
  manifests, metadata, JSON validation records, source files, and contact sheets

Design and reference basis:

- all accepted Event 15 specifications and matrices under
  `docs/specs/015_utopia_manifesto_specs/`
- the formal improvement-loop addendum at
  `docs/plans/015_utopia_manifesto_plans/015_utopia_manifesto_formal_improvement_loop_addendum_2026-07-15.md`
- required offline wiki pages for data structures, triggers, effects,
  modifiers, localisation, scopes, on actions, events, decisions, ideas, AI,
  cosmetic tags, country creation, divisions, and units
- installed vanilla documentation for effects, triggers, on actions,
  characters, script concepts, and script constants
- vanilla character, cosmetic-tag, political-transition, and member-status
  precedents

## Validation scope

The audit traced acceptance, route commitment, formation, succession, Total
Repeal, annexation cleanup, and the intended collapse edge statically. It also
performed independent binary header, dimension, hash, package/runtime equality,
sprite-resolution, character-lifecycle, and localisation-coverage checks.

No live game scenario was executed as part of this read-only audit. The lack of
an explicit prior-leader promotion after teardown is therefore retained as a
P3 engine-behavior risk rather than asserted as a confirmed runtime defect.

## Files changed by this audit

- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/country_package_completion_audit_2026_07_15.md`

No gameplay, localisation, interface, source asset, processed asset, manifest,
spreadsheet, or skill file was changed. No commit was created.

## Simplifications, omissions, blockers, and risks

The auditor made no fallback, implementation simplification, or audit-surface
omission. The implementation remains incomplete because of the two P1
lifecycle gaps. The obsolete lower-case flag deployment and stale documents
are a P2 cleanup requirement. The original-leader resumption behavior is a P3
risk until the political restoration contract makes it explicit or otherwise
proves the engine result.

The corrected five-route flag package, four institutional portraits, and
sixteen advisor dossiers contain no placeholder or unapproved fallback.
