# Event 006 FORM-03 promotion re-audit

Date: 2026-07-16
Mode: narrow read-only source and documentation audit
Gameplay, readiness, localisation, and asset edit authority: none
Runtime execution claim: none

## Verdict

**Pass. FORM-03 is safe to promote with the exact readiness bundle listed below. No blocker remains in the requested promotion surface.**

The wider operational re-audit in `006_form01_04_operational_reaudit_2026_07_16.md` passed the shared transaction, FORM-03 runtime proof, processed-member sentinel, sovereign-state policy, progression, identity, assets, AI, cleanup, and Event 5 isolation. It left FORM-03 fail-closed only for findings F03-P1 and F03-P2. The current source resolves both findings. The restored FORM-01, FORM-02, and FORM-04 readiness helpers also match the exact audited contract.

This report does not set any readiness flag. It authorizes the parent to make the exact FORM-03 restoration after reviewing this handoff.

## References used

- Repository skills: `chaos-redux-subagents`, `chaos-redux-events`, and `chaos-redux-event-assets`.
- Offline wiki core pages required by `AGENTS.md`, with the localisation, data-structure, effect, trigger, and scope rules used directly for this audit.
- Vanilla official `effects_documentation.md` entries for `clear_variable`, `clr_country_flag`, `set_country_flag`, and `set_variable`.
- Vanilla official `triggers_documentation.md` entries for `check_variable`, `has_country_flag`, and `has_variable`.
- Vanilla official `script_concept_documentation.md` and `common/script_constants/documentation.md` for `constant:` values assigned to scoped variables.
- Vanilla SIA constant-to-variable examples and INS/SOV/TOA clear-then-set flag transitions as syntax precedents.

## 1. FORM-03 localisation finding F03-P1

Status: **resolved**.

`localisation/english/006_independence_wave_form03_l_english.yml` contains no player-facing match for raw `state 34`, `state 36`, `state #34`, `state #36`, `34 state`, or `36 state` language.

The corrected strings retain the intended project identities:

- line 111 names the Sambre-Meuse industrial-corridor and northern-waterway works projects
- lines 140-141 name the Sambre-Meuse works program and industrial corridor
- lines 143-144 name the northern waterway district and retain the West Frisian, Dutch-language, pumping, navigation, and waterline meaning
- lines 190 and 194 keep the matching Sambre-Meuse and northern-waterway cost descriptions
- lines 240 and 242 describe the same corridor and waterway effects without exposing map IDs

The dynamic values remain intact and agree with the live decisions and cost triggers:

| Project | Player-facing dynamic values | Gameplay proof |
|---|---|---|
| Sambre-Meuse | major civilian-factory use, major train cost, standard command-power cost, long duration, cancellation delta, anchor-works gain, and infrastructure level | `006_independence_wave_form03_decisions.txt:389-429`, `006_independence_wave_form03_triggers.txt:412-419`, and `006_independence_wave_form03_effects.txt:721-727,757-785` |
| Northern waterway | major civilian-factory use, standard train cost, light convoy cost, standard command-power cost, long duration, cancellation delta, anchor-works gain, and infrastructure level | `006_independence_wave_form03_decisions.txt:431-471`, `006_independence_wave_form03_triggers.txt:421-429`, and `006_independence_wave_form03_effects.txt:729-738,788-816` |

Ownership and control loss still cancel each project. Completion still applies the correct state-bound dynamic modifier and bounded infrastructure construction. The localisation file retains its UTF-8 BOM.

## 2. FORM-03 report-scene finding F03-P2

Status: **resolved**.

`docs/assets/006_independence_wave/low_countries_form03_progression/report_scene/submanifest.md:81-84` now states that:

- the package-root FORM-03 manifest and Event 006 root manifest record the ASSET-048 child, runtime sprite, and nine consumers
- `docs/events/006_independence_wave/systems/form03_progression.md` records the dedicated icon and report package
- no parent merge action remains

No stale instruction remains saying that a manifest was not edited, that the system document still claims no distinct art, or that the parent must reconcile the package later.

The submanifest checksum is current:

```text
e1bf4c0ab711cb38df83e94a4776578528837bbb7080351c1e9b91c27a8015bb
```

That is both the freshly calculated SHA-256 of `report_scene/submanifest.md` and the value recorded for it in `report_scene/checksums.sha256`.

The reconciled claims are supported by all parent documentation surfaces:

- `docs/assets/006_independence_wave/manifest.md:191-210` records ASSET-048, the report-scene package, runtime DDS, registered sprite, and `.300-.308` consumers
- `docs/assets/006_independence_wave/low_countries_form03_progression/manifest.md:17-26` records the child submanifest and the wired report-scene row
- `docs/events/006_independence_wave/systems/form03_progression.md:98-110` records six focus icons, six idea icons, six decision icons, the report sprite registration, all nine consumers, retained source and review material, and the absence of animation

The asset documentation is internally aligned. No fallback or placeholder claim is being used for promotion.

## 3. FORM-01, FORM-02, and FORM-04 readiness restoration

Status: **pass**.

`common/scripted_effects/006_independence_wave_form01_02_04_effects.txt:16-28` still provides the shared clear-first effect. It clears all six generic flags, all four family attestations, the FORM-03 progression attestation, and `independence_wave_formable_readiness_family`.

Each restored helper then performs the exact approved sequence:

| Helper | Clear first | Matching family variable | Six generic flags | Only family attestation |
|---|---|---|---|---|
| `independence_wave_form01_register_readiness` at lines 31-41 | yes | `constant:independence_wave_formable_family.celtic_cooperation_state` | exact set | `independence_wave_form01_readiness_attested` |
| `independence_wave_form02_register_readiness` at lines 43-53 | yes | `constant:independence_wave_formable_family.north_atlantic_compact` | exact set | `independence_wave_form02_readiness_attested` |
| `independence_wave_form04_register_readiness` at lines 55-65 | yes | `constant:independence_wave_formable_family.rhine_federation` | exact set | `independence_wave_form04_readiness_attested` |

The six generic flags in every helper are exactly:

- `independence_wave_formable_territory_adapter_ready`
- `independence_wave_formable_x_tag_reserved`
- `independence_wave_formable_flag_package_ready`
- `independence_wave_formable_identity_adapter_ready`
- `independence_wave_formable_integration_adapter_ready`
- `independence_wave_formable_member_policy_audited`

No helper sets another family's attestation or the FORM-03 progression attestation. `independence_wave_formable_register_selected_family_readiness` at lines 69-86 also clears before dispatch, so a SCO family switch cannot retain the prior family's proof.

This structure matches `has_independence_wave_formable_commit_readiness` in `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:459-503`. That trigger requires the stored readiness family to equal the selected profile family, all six generic flags, the selected identity, and the matching family-specific proof.

## 4. Exact FORM-03 promotion bundle

FORM-03 is now safe to restore in `independence_wave_form03_register_readiness` with this exact carrier-scope sequence:

1. Call `independence_wave_formable_clear_selected_family_readiness = yes`.
2. Set `independence_wave_formable_readiness_family` to `constant:independence_wave_formable_family.low_countries_federation`.
3. Set the six generic readiness flags listed above.
4. Set `independence_wave_form03_readiness_attested`.
5. Set `independence_wave_form03_progression_attested`.

Do not set a FORM-01, FORM-02, or FORM-04 attestation in that helper. Do not omit either FORM-03-specific flag. The shared readiness trigger requires both the base FORM-03 proof and its progression proof.

The current clear-only FORM-03 helper remains safe until the parent applies that promotion. After the exact bundle is added, family switching remains fail-safe because both the selected-family dispatcher and the family helper clear stale readiness before setting the new proof.

## Validation boundary and blockers

This is a static promotion audit. HOI4 was not launched and no live event execution is claimed.

No blocker, fallback, simplification, missing checksum update, stale merge instruction, raw state-ID localisation, or readiness-bundle mismatch remains in the requested surface. The only file created by this subagent is this report.
