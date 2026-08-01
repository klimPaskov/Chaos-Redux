# Event 012 royal sovereign presentation tranche

## Scope

This tranche gives the sixteen existing priority-member sovereigns a shared visible leader trait and removes council wording from the highest-visibility priority-member and Charter surfaces. It does not create a tag, replace an Independence Wave carrier, or add a second political store.

## Changed files

- `common/country_leader/012_africa_priority_member_traits.txt` defines `africa_priority_crowned_sovereign_trait`.
- `common/script_constants/012_africa_priority_member_constants.txt` centralises the modest stability, political-power, and war-support values.
- `common/scripted_effects/012_africa_priority_member_character_effects.txt` applies the trait once after each of the three explicit political settlement routes installs the named sovereign.
- `localisation/english/012_africa_priority_member_characters_l_english.yml` adds the player-facing trait name and description.
- `localisation/english/012_africa_priority_member_l_english.yml` replaces the priority package's visible council language with crown, court, and civic-institution wording while retaining technical route keys.
- `localisation/english/012_africa_priority_member_focus_l_english.yml` carries the same crown-and-court vocabulary through the priority focus overlay and settlement ideas.
- `localisation/english/012_african_union_l_english.yml` replaces the principal Charter Court display strings, while `localisation/english/012_africa_charter_gui_l_english.yml` changes the constitution card to Court of Crowns; technical keys remain stable.

## Runtime contract

The trait is applied in country scope after `add_country_leader_role` and `promote_leader = yes`, guarded by `africa_priority_member_crowned_sovereign_trait_applied`. It therefore follows the named sovereign on the existing carrier, including Independence Wave niche carriers, without touching country definitions or cosmetic tags.

## Validation and limits

Static source inspection confirms one trait definition, three guarded application sites, and matching localisation keys. The remaining `council` tokens are technical identifiers, historical documentation, or lower-visibility regional route prose that still requires a separate wording pass; they were not renamed because those identifiers are wired into the constitutional matrix and focus/action dispatch.
