# Event 006 admitted leader-role crosswalk repair

Date: 2026-08-26

## Finding

A source crosswalk compared every Event 006 `promote_character` call with the country-leader ideology blocks defined for the matching character. Four admitted packages had route promotions targeting missing roles:

| Package | Character | Missing roles | Promotion consumers |
| --- | --- | --- | --- |
| IW-028 | `BBX_independence_wave_epirus_council` | `despotism`, `liberalism` | `independence_wave_install_bbx_emergency_government`, `independence_wave_install_bbx_patron_government` |
| IW-029 | `BOS_independence_wave_drina_council` | `despotism`, `liberalism` | `independence_wave_install_bos_emergency_government`, `independence_wave_install_bos_patron_government` |
| IW-031 | `KOS_independence_wave_ferhat_draga` | `oligarchism` | `independence_wave_install_kos_traditional_government` |
| IW-026 | `MAC_independence_wave_vardar_presidium` | `despotism`, `liberalism` | `independence_wave_install_mac_emergency_government`, `independence_wave_install_mac_patron_government` |

The source crosswalk found 73 matched Event 006 promotion calls before the repair and zero missing roles afterward. The role definitions are valid HOI4 country-leader ideology types. Vanilla documentation requires `promote_character` to use the character’s applicable ideology role when multiple roles exist.

## Patch

`common/characters/006_independence_wave_characters_registry.txt` now adds the missing empty country-leader blocks with each character’s existing description key and `traits = { }`. No route effect, leader identity, portrait, party, force, cost, or admission logic changed.

## Boundary

This is a shared character-definition repair for four already-admitted packages. It does not widen the 32-package attestation set, alter the 29 reservation groups, change Join order, or affect the 161 unattested rows. No fallback leader or generic substitute was introduced.

## Validation

The mechanical crosswalk now reports `roles=28 promote_calls=73 missing=0`. The Event 006 allocator, country API, strict flag-family, FORM-16, GUI semantic, and SCN-008 matrix checks all passed. A bounded `hoi4.event_inspect` lint for `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics at revision `43388d6b2737a1c8e2409f324449210941414fee69c903a1c69d441ca9d33b97`; its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6c5c72cd918951a9f236355203c84d51bf5591e136cbde9dbd070dff70e7ed79/63f5323868a4ff2b08c4fc36cdac5a44af1c5f42aa20ab927b00be8ee54b0a35/event-lint-43388d6b2737.json`. The matching overview render returned `EVENT_RENDERED_PARTIAL` with zero blocking diagnostics and manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/54c2817a8fcb96edf3cca54abd143d962d7b3267f2bb98abbce22ed7ac7eddee/219d05f4e77c65e8f210a5d4a5eec26f560d16d7f70ee311efd31ded450a32c8/event-overview-43388d6b2737-manifest.json`. The workspace deferred large helper/lifecycle projections, so no live game or save/load receipt is claimed.
