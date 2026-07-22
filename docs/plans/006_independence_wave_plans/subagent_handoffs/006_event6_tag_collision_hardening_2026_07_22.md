# Event 006 tag/cosmetic collision hardening handoff

Date: 2026-07-22
Scope owner: `/root/event6_current_tag_collision_verify`

## Outcome

The installed country-tag audit now excludes only the exact current Event 006 country-history filenames whose three-character tag and normalized filename identity match the registered Event 006 country row. A same-tag history file with another identity remains collision evidence. The audit also checks all 16 Event 006 custom cosmetic identifiers (including route identifiers longer than three characters) across exact definitions, aliases, `set_cosmetic_tag` call sites, localisation keys, and flags without changing the existing three-character metrics.

Final report result:

- generic country/tag collisions: **0**
- all-length custom-cosmetic collisions: **0**
- Event 006 history filenames owned by exact path/identity match: **85**
- custom cosmetic identifiers defined: **16**; Event 006 call sites: **16**
- external custom-cosmetic surfaces: **0**; non-Event 006 Chaos Redux custom surfaces: **0**
- identity matches: **50** (`binding_identity_match_count=0`, `manual_identity_match_count=50` across `manual_identity_package_count=16` packages)
- collision-free `??X` candidates: **446**

The 85 owned history files cover 85 distinct country tags. Of 102 Event 006 country tags, 17 custom country tags have no current history file (the six formable three-character IDs are also historyless, for 23 historyless tags across the combined 108 owned identifiers). This is an inert setup observation, not a collision admission.

## Files changed

Gameplay, country registries, history, flags, localisation, and map files were not edited.

- `.tools/audit_hoi4_country_tags.py`
  - added exact all-length custom-cosmetic surface scanners for direct roots and ZIP members;
  - added exact Event 006 custom-cosmetic call/registry parity checks;
  - replaced tag-only history exclusion with an exact 85-path/normalized-identity ownership set;
  - excludes Event 006's own exact custom flag paths from the non-Event 006 custom scan while preserving unrelated same-tag evidence;
  - writes a separate custom-cosmetic collision CSV.
- `docs/plans/006_independence_wave_plans/tag_audit/006_installed_tag_collision_audit_2026_07_22.json`
- `docs/plans/006_independence_wave_plans/tag_audit/006_installed_tag_collision_audit_2026_07_22.md`
- `docs/plans/006_independence_wave_plans/tag_audit/006_installed_tag_collisions_2026_07_22.csv`
- `docs/plans/006_independence_wave_plans/tag_audit/006_installed_custom_cosmetic_collisions_2026_07_22.csv`
- `docs/plans/006_independence_wave_plans/tag_audit/006_vanilla_identity_review_2026_07_22.csv`
- this handoff.

The two collision CSVs are UTF-8-with-BOM header-only files because both collision sets are empty.

## Scan coverage

The run covered vanilla, 122 Workshop directories, 8 embedded ZIP archives, and 3 sibling local mod directories (`agentic_hoi4_modding`, `chaos_redux_music`, `slop_redux`). Generic metrics remain the prior baseline: 7,981 external/vanilla country-tag definitions, 69,485 extended surfaces, 49 non-Event 006 Chaos Redux country-tag definitions, 969 non-Event 006 extended surfaces, 8 archives (1 with tag surfaces), and 1 sibling local mod with extended surfaces. The all-length scanner found no external or non-Event 006 custom-cosmetic surfaces.

Inventory fingerprints from the final JSON:

- vanilla tag surfaces: `57dfbe267a32983680c3fa385cce69e7e7a9cd52af06d8ec8bf8bb6508004d09`
- Workshop tag surfaces: `c4e0f8f99a79be4459ad4a8c0068c9c4bf6319c594c2d8a0cc6c756a65035fb3`
- sibling local-mod tag surfaces: `eaf2cadf169eb541a7d89b33ccac8d8d19d0953532c4a01e5815ff09ed28dc19`
- non-Event 006 Chaos Redux surfaces: `bb2b8a29136b8cfac7a63cf3f682b94cf042b2e120860bae6e5ede9e85e82bd9`
- archive inventory: `c190bac538705eeb79d7dd04e5f87c0fd59c7c7688856f30c419450d8029305c`
- exact Event 006-owned history filename inventory: `d68e3b52a78b42ff00bb397e19b7d12d522d59e7c2278f517b476caf8c0ebcaa`
- exact custom-cosmetic external and non-Event 006 inventories (empty): `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`

Final artifact SHA-256 values:

- audit script: `074c457b2d1d6b3ad25e82ee88af351c6bac5c93ceb0084ee08da6c6bd86aeb6`
- JSON report: `f3e5d8873a4c34857d65bf797252cdcff7e88bd30c43ee1fec0c23852fd4bf5a`
- Markdown report: `99255590feed79886445fb59261178227ed0b41620b2b15a7f68d09285c346f7`
- generic collision CSV: `873b5bfc9f60258558a53b125effe8cc440acd8b9ea614c34a0b4f2941855d30`
- custom collision CSV: `7039714a0f1c577885dff51f66d8a1c07007f3204f7ccbd59e82fa61dfb80ba9`
- vanilla identity review CSV: `002859800866447da026a0ced4bf40c3b2952060cf7fa3ee1c6c921dbdbe5283`

## Validation commands

```text
python -m py_compile .tools/audit_hoi4_country_tags.py
python .tools/audit_hoi4_country_tags.py --write-reports
```

The full write run completed successfully and ended with:

```text
collisions=0 custom_cosmetic_collisions=0 identity_matches=50 safe_x_tags=446
```

The generated JSON was re-read to verify 16 registry IDs equal 16 Event 006 call IDs, both custom surface counts are zero, custom collision list is empty, and exact history ownership count is 85. No meaningful validation was skipped for this audit scope.

## Remaining risks

- The scanner cannot prove cosmetic identifiers constructed dynamically through meta effects/scripted localisation, non-text archives, or paths outside standard HOI4 country/alias/localisation/flag trees; these remain documented manual-review surfaces.
- Workshop coverage is the currently installed 122-directory/8-ZIP set; a changed installed-mod set requires a fresh run.
- Existing generic three-character flag exclusion remains tag-based for the legacy metrics; all-length custom flags use explicit exact identifier/path ownership. No tag remap or gameplay fallback was introduced.

No simplification or fallback was used. Parent should review the generated reports and carry this handoff into the Event 006 tag reservation decision.
