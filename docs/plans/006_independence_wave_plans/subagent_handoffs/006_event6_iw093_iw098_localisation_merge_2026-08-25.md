# Event 006 IW-093/IW-098 localisation merge

## Scope

This source-layout pass folds the two tiny IW-093/IW-098 idea and category localisation files into the existing country-core localisation registry. It changes no localisation key, character token, category id, decision id, idea id, party name, or player-facing wording.

The receiving file is `localisation/english/006_independence_wave_iw093_iw098_country_core_l_english.yml`. Source markers identify the preserved country-core, idea, and category sections. The former `006_independence_wave_iw093_iw098_ideas_l_english.yml` and `006_independence_wave_iw093_iw098_categories_l_english.yml` files are removed.

## Preservation evidence

The merged registry retains all 38 executable localisation keys from the three source files: 26 country-core keys, 8 idea keys, and 4 category keys. A key inventory comparison found no missing or duplicate keys, and all three inputs and the receiver use UTF-8 with BOM.

The two category descriptions retain balanced yellow colour markers around every scripted value. No gameplay source, package admission, event, decision, focus, idea, character, portrait, or country definition changed.

## Boundary

This is a source-layout consolidation only. It does not promote IW-093 or IW-098, change the adapter-only fail-closed boundary, add pre-event UI, or claim live localisation rendering or in-game acceptance. Historical handoffs may retain the removed paths for provenance; current package source uses the consolidated registry.
