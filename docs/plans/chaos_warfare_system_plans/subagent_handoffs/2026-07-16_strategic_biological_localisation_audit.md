# Strategic Biological Localisation Audit Handoff

## Scope and status

This audit covers only the bounded strategic ordinary-pathogen raid and lifecycle tranche named by the parent. It does not claim completion of the overall CBRN goal or Stage 7.

No gameplay, GFX, asset, or design-document file was edited. This mandatory patch handoff is the only documentation file added.

## Files changed

- `localisation/english/biological_strategic_raids_l_english.yml`
- `localisation/english/cbrn_doctrine_l_english.yml`
- `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-07-16_strategic_biological_localisation_audit.md`

## Changed keys

Strategic staging and outcome keys:

- `bio_designate_strategic_raid_staging_state_desc`
- `bio_strategic_raid_staging_invalid_tt`
- `bio_strategic_raid_anthrax_limited_success_actor_tt`
- `bio_strategic_raid_anthrax_limited_success_target_tt`
- `bio_strategic_raid_anthrax_success_actor_tt`
- `bio_strategic_raid_anthrax_success_target_tt`
- `bio_strategic_raid_anthrax_critical_success_actor_tt`
- `bio_strategic_raid_anthrax_critical_success_target_tt`
- `bio_strategic_raid_plague_limited_success_actor_tt`
- `bio_strategic_raid_plague_limited_success_target_tt`
- `bio_strategic_raid_plague_success_actor_tt`
- `bio_strategic_raid_plague_success_target_tt`
- `bio_strategic_raid_plague_critical_success_actor_tt`
- `bio_strategic_raid_plague_critical_success_target_tt`
- `bio_strategic_raid_tularemia_limited_success_actor_tt`
- `bio_strategic_raid_tularemia_limited_success_target_tt`
- `bio_strategic_raid_tularemia_success_actor_tt`
- `bio_strategic_raid_tularemia_success_target_tt`
- `bio_strategic_raid_tularemia_critical_success_actor_tt`
- `bio_strategic_raid_tularemia_critical_success_target_tt`
- `bio_strategic_raid_smallpox_limited_success_actor_tt`
- `bio_strategic_raid_smallpox_limited_success_target_tt`
- `bio_strategic_raid_smallpox_success_actor_tt`
- `bio_strategic_raid_smallpox_success_target_tt`
- `bio_strategic_raid_smallpox_critical_success_actor_tt`
- `bio_strategic_raid_smallpox_critical_success_target_tt`

Doctrine keys:

- `cbrn_theater_contamination_doctrine_spirit_tt`
- `cbrn_terminal_hazard_doctrine_spirit_desc`
- `cbrn_terminal_hazard_doctrine_spirit_tt`
- `mobile_decontamination_columns_desc`

No localisation key was added, removed, or renamed.

## Display before and after

- The staging description hardcoded a 90-day relocation period. It now reads `constant:bio_strategic_raid_staging.relocation_cooldown_days`, preserving the displayed value while preventing drift.
- The invalid-staging text described a state as being supplied by an air base. It now states the actual requirement that the state contain an air base and have functioning infrastructure.
- Limited, successful, and critical native result text previously asserted that release and consequence records always existed. Those 24 actor and target keys are now conditional on the release being successfully established. Actor text also states that a failed establishment loses collected material without creating a biological consequence record.
- Doctrine refund lines previously named only a strategic biological Command Power refund. They now state that Command Power is refunded after a resolved strategic biological raid.
- Terminal Hazard Doctrine previously described a general political defense against consequences and named only a short set of protected records. It now says the defense is focused on Condemnation and explicitly states that only Condemnation impact is reduced. Payload debit, evidence, attribution, deaths and their history, contamination and its history, medical saturation and its history, use counters, confirmed-use history, domestic war-support penalties, accident records, resistance trauma, and public-harm floors remain unchanged.
- `mobile_decontamination_columns_desc` contained the prohibited semicolon. It now uses two sentences.

## Audit findings

### Missing keys

None. All 57 expected category, raid, raid-description, native-result, target, staging-decision, requirement, rejected-context, and outcome keys resolve.

### Duplicate keys

None among the bounded localisation keys across English localisation.

### Scripted and dynamic localisation issues

No broken scripted-localisation call was found. The bounded text uses direct dynamic constant values rather than a scripted-localisation selector. All 76 unique constant paths used by the two patched localisation files resolve in `common/script_constants/`.

The hardcoded staging cooldown was the only safe bounded dynamic-text opportunity. It is now dynamic.

### Stable migration keys

The stable raid ids `anthrax_strike`, `plague_strike`, `tularemia_strike`, and `smallpox_strike` retain their automatic `raid_type_*`, `raid_type_*_desc`, and `raid_*_tt` keys. All `bio_strategic_raid_*` result and rejected-context keys remain unchanged. The patch changes values only.

### Cross-surface consistency

- The four raid blocks each retain one native state target, one tactical-bomber requirement, one strategic-bomber requirement, one exact agent equipment reservation, and four calls to `bio_resolve_strategic_raid_outcome`, one for each native engine result.
- No ordinary raid block references a zombie helper.
- Rejected-context text states that collected payload is lost without release or consequence records.
- Conditional result text now agrees with the documented lifecycle-dispatch failure behavior.
- Doctrine potency, biological death, duration, medical pressure, and the accepted 10 percent or 20 percent resolved-operation Command Power refund remain disclosed through dynamic values.
- The Condemnation-only doctrine exception now agrees with the authoritative consequence-record boundary.
- `common/on_actions/chaosx_on_actions_biowarfare.txt` is absent as expected.

### Encoding

All three bounded English localisation files retain UTF-8 with BOM. No encoding concern remains.

### Icon references

The staging decision sprite and all four ordinary-pathogen map-icon sprites resolve to existing DDS files. The existing files under `gfx/interface/military_raids/map_icons/` remain at their stable tracked paths. The four agent equipment icons resolve through `interface/chaosx_equipment.gfx`, and `GFX_other_target_icon` resolves through vanilla. No duplicate bounded sprite name was found.

### Prohibited punctuation

No semicolon or em dash remains in the eight bounded audit files.

## Meaningful validation

- Cross-checked 57 expected strategic keys against all English localisation: 0 missing and 0 duplicate.
- Parsed 97 dynamic constant references representing 76 unique paths: 0 malformed and 0 missing.
- Checked all four ordinary-pathogen raid blocks for native state targeting, tactical and strategic bomber requirements, shared resolver calls, and zombie-helper references.
- Resolved the staging icon, four existing raid map icons, four equipment icons, the biological category icon, and the vanilla target icon to their definitions and existing textures.
- Confirmed all limited, success, and critical result pairs use conditional release wording for all four agents.

## Skipped meaningful validation

No in-game or native raid-result UI render was available, so visual wrapping and overflow were not rendered. The Technology Tree Viewer is absent from the installed package and is not relevant to these native raid and doctrine tooltip surfaces.

## Remaining issues and parent follow-up

No unresolved wording decision remains in this bounded tranche. The parent should review these localisation-only edits during final integration. The overall CBRN goal and Stage 7 remain incomplete outside this handoff.
