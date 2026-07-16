# Event 006 IW-010 Saar advisor and focus GFX handoff

The four runtime DDS files exist at the exact paths below. Parent integration
has been verified in the live Event 006 character, localisation, recruitment,
interface, and focus files. This asset tranche did not edit those parent-owned
surfaces or any readiness gate.

## Advisor records and sprite registrations

Verified character file:
`common/characters/006_independence_wave_saar_characters.txt`.

Verified sprite file: `interface/006_independence_wave_region_01_portraits.gfx`.

Verified localisation file:
`localisation/english/006_independence_wave_saar_l_english.yml`.

Verified recruitment consumer: `events/006_independence_wave.txt`.

| Approved character key | Gender metadata | Exact small portrait sprite | Exact DDS |
| --- | --- | --- | --- |
| `AJX_independence_wave_mine_rail_dispatch_superintendent` | `gender = female` | `GFX_portrait_advisor_AJX_independence_wave_mine_rail_dispatch_superintendent` | `gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent.dds` |
| `AJX_independence_wave_cross_border_accounts_comptroller` | male default; do not set female | `GFX_portrait_advisor_AJX_independence_wave_cross_border_accounts_comptroller` | `gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_cross_border_accounts_comptroller.dds` |
| `AJX_independence_wave_factory_security_inspector` | `gender = female` | `GFX_portrait_advisor_AJX_independence_wave_factory_security_inspector` | `gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_factory_security_inspector.dds` |

Verified live sprite definitions:

```text
	spriteType = {
		name = "GFX_portrait_advisor_AJX_independence_wave_mine_rail_dispatch_superintendent"
		texturefile = "gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent.dds"
	}
	spriteType = {
		name = "GFX_portrait_advisor_AJX_independence_wave_cross_border_accounts_comptroller"
		texturefile = "gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_cross_border_accounts_comptroller.dds"
	}
	spriteType = {
		name = "GFX_portrait_advisor_AJX_independence_wave_factory_security_inspector"
		texturefile = "gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_factory_security_inspector.dds"
	}
```

Each live character record uses its exact corresponding handle under
`portraits = { civilian = { small = ... } }`. The Event 006 setup event recruits
all three characters for AJX, and the Saar localisation file contains each
role-title key and description. Parent-owned traits, costs, availability, AI
weights, flags, and cleanup behavior remain outside this asset handoff.

## Municipal Neutral Commission focus

Approved sprite: `GFX_goal_independence_wave_ajx_neutral_commission`.

Exact DDS:
`gfx/interface/goals/006_independence_wave/goal_independence_wave_ajx_neutral_commission.dds`.

Verified sprite file: `interface/006_independence_wave.gfx`.

Verified live definitions following the existing Event 006 focus/shine pair:

```text
	spriteType = { name = "GFX_goal_independence_wave_ajx_neutral_commission" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_ajx_neutral_commission.dds" }
	spriteType = { name = "GFX_goal_independence_wave_ajx_neutral_commission_shine" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_ajx_neutral_commission.dds" effectFile = "gfx/FX/buttonstate.lua" }
```

AJX neutral-route nodes reviewed during integration verification:

- `independence_wave_ajx_appoint_neutral_commission_focus`;
- `independence_wave_ajx_codify_municipal_neutrality_focus`;
- `independence_wave_ajx_bind_security_to_commission_focus`;
- `independence_wave_ajx_entrench_neutral_commission_focus`.

The stable approved icon is assigned to
`independence_wave_ajx_appoint_neutral_commission_focus`. The live tree retains
`GFX_goal_independence_wave_recognition_diplomacy` for codification,
`GFX_goal_independence_wave_army_integration` for security, and
`GFX_goal_independence_wave_founding_administration` for entrenchment.

## Integration status

The DDS files are installed and hash-validated. All three advisor handles are
registered and consumed by the matching AJX characters; all three characters
have localisation and setup recruitment. The focus base and shine handles are
registered, and the base handle is consumed by the neutral-commission entry
focus. No asset-integration blocker remains.
