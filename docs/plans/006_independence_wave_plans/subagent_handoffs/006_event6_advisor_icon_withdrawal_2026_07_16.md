# Event 006 custom advisor icon withdrawal

Date: 2026-07-16
Scope: all custom Independence Wave advisor portrait cards

## User decision

Event 006 does not use custom advisor icons. The gameplay advisor offices stay
available where their package implements them, but they carry no Event 006
`portraits` block and no custom advisor sprite handle. This decision supersedes
the earlier NWE and AJX advisor-dossier asset handoffs.

All Independence Wave character records also use male/default character gender.
The earlier female metadata was removed. Mediterranean working records were
renamed to male fictional specialists before their package could be admitted.

## Removed runtime and wiring surfaces

- `gfx/interface/ideas/006_independence_wave/advisors/` and all fifteen runtime
  DDS files beneath it;
- `interface/006_independence_wave_nwe_advisors.gfx`;
- the three AJX advisor sprite blocks formerly in
  `interface/006_independence_wave_region_01_portraits.gfx`;
- every custom advisor `portraits` block in the Event 006 NWE, Saar, and
  Mediterranean character registries;
- `docs/assets/006_independence_wave/nwe_advisor_dossiers_2026_07_15/`;
- all AJX advisor-source, processing, DDS, decode, and contact-sheet artifacts
  from `ajx_asset_completion_2026_07_15/`.

The AJX package was reduced to its distinct Municipal Neutral Commission focus
icon and its focus-only evidence. The generic vanilla advisor reference library
under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/` is not
an Event 006 gameplay icon set and remains available as reusable skill guidance.

## Gameplay boundary

No advisor trait, hiring cost, AI weight, setup recruitment, availability gate,
or package mechanic was removed. HOI4 supplies its normal non-custom
presentation when a character has no explicit small portrait. No deleted sprite
handle remains in Event 006 character or interface script.

## Validation boundary

The final asset audit must confirm:

- no runtime file remains under the deleted Event 006 advisor path;
- no Event 006 `.gfx` file registers a `GFX_portrait_advisor_*` handle;
- no Event 006 character uses a custom advisor `portraits` block;
- no Event 006 character carries female gender metadata; and
- current asset and package documentation describes the asset-neutral advisor
  presentation.

## Simplifications, omissions, fallbacks, and blockers

The absence of custom advisor icons is the explicit user-selected design, not a
fallback. No blocker remains within this withdrawal scope.
