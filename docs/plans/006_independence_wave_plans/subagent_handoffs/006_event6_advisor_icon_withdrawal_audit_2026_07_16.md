# Event 006 advisor icon withdrawal audit

Date: 2026-07-16
Scope: Event 006 character records, advisor presentation, runtime advisor
assets, current documentation, and live leader portrait inventory

## Verdict

**PASS for the custom advisor icon withdrawal.**

The current working tree contains no Event 006 custom advisor DDS, advisor
sprite registration, advisor portrait reference, advisor `portraits` block, or
explicit character gender metadata. The gameplay advisor definitions retain
their slots, exact package gates, traits, costs, and AI weights.

This audit made narrow corrections before issuing the verdict:

- removed six redundant `female = no` declarations so the requirement is zero
  Event 006 gender metadata rather than only zero female characters.
- corrected the source-of-truth map and resume packet so withdrawn advisor
  dossiers are not listed as current assets.
- corrected the NWE advisor-trait header and current package documentation so
  they describe asset-neutral offices rather than withdrawn dossier cards.

No advisor trait, hiring cost, availability condition, AI weight, active-role
hook, or recruitment effect was changed.

## Runtime withdrawal evidence

The complete prior runtime tranche consisted of fifteen `65x67` DDS files,
three for AJX and twelve for SCO, WLS, RHI, and BAY. All fifteen are deleted
from the working tree. The directory
`gfx/interface/ideas/006_independence_wave/advisors/` no longer exists.

The dedicated registry
`interface/006_independence_wave_nwe_advisors.gfx` is deleted. The three AJX
advisor sprite blocks are absent from
`interface/006_independence_wave_region_01_portraits.gfx`.

An exact runtime search found:

- zero Event 006 `GFX_portrait_advisor_*` references
- zero Event 006 references to the deleted advisor runtime path
- zero advisor portrait blocks in the Event 006 character registries
- zero remaining advisor-art files under the Event 006 asset documentation
  tree.

The old asset-production subtrees and AJX advisor artifacts are deleted. The
AJX package manifest now covers only its Municipal Neutral Commission focus
icon and states that advisor offices are asset-neutral.

## Gameplay advisor record audit

Twenty-one current Event 006 advisor records were parsed. Every record retains
all of the following fields:

- `slot = political_advisor`
- exact `allowed`, `visible`, and `available` gates
- one defined advisor trait
- a centralised hiring cost
- an `ai_will_do` block.

None of the twenty-one records has a `portraits` block.

| Package group | Advisor records | Presentation | Recruitment state |
|---|---:|---|---|
| SCO | 3 | asset-neutral | all three recruited by hidden Event 006 setup event `.10` |
| WLS | 3 | asset-neutral | all three recruited by hidden Event 006 setup event `.10` |
| RHI | 3 | asset-neutral | all three recruited by hidden Event 006 setup event `.10` |
| BAY | 3 | asset-neutral | all three recruited by hidden Event 006 setup event `.10` |
| AJX | 3 | asset-neutral | all three recruited by hidden Event 006 setup event `.10` |
| COR | 2 | asset-neutral | no current recruitment site, existing IW-017 blocker |
| ARX | 2 | asset-neutral | both recruited by the dormant ARX country shell |
| ASX | 2 | asset-neutral | both recruited by the dormant ASX country shell |

The fifteen established SCO, WLS, RHI, BAY, and AJX advisor recruitments are
unchanged. Their current character-file diffs remove only portrait and earlier
female-gender lines. Their recruitment call sites in
`events/006_independence_wave.txt` remain present and individually guarded by
`has_character`.

All referenced traits are still defined in
`common/country_leader/006_independence_wave_nwe_advisor_traits.txt` or
`common/country_leader/006_independence_wave_saar_advisor_traits.txt`.
Northern and western European costs and AI factors remain in
`common/script_constants/006_independence_wave_nwe_advisor_constants.txt`.
Mediterranean costs and AI factors remain in
`common/script_constants/006_independence_wave_mediterranean_constants.txt`.

### Existing IW-017 recruitment blocker

`COR_paolo_pietri` and `COR_antone_rocchi` have complete advisor definitions,
but no current Event 006 effect recruits them. COR is a registered living tag,
so adding them to ordinary country history would be unsafe. The in-flight
IW-017 adapter needs to own guarded recruitment when that package is completed.

This gap predates and is independent of the icon withdrawal. It does not
invalidate the withdrawal verdict, but IW-017 must remain fail-closed and this
audit does not claim its gameplay package is ready. No recruitment fallback or
out-of-scope mechanic was added.

## Gender metadata and Mediterranean key audit

An exact search across Event 006 character databases, generated-character
effects, events, and country history returns no `female =`, `gender =`, or
female-name-pool assignment. HOI4's default male character handling therefore
applies without explicit metadata.

The six current Mediterranean advisor keys are:

- `COR_paolo_pietri`
- `COR_antone_rocchi`
- `ARX_michele_corda`
- `ARX_efisio_satta`
- `ASX_giuseppe_lo_giudice`
- `ASX_leone_messina`.

No alternate COR, ARX, or ASX advisor key remains in current character,
history, trigger, effect, interface, localisation, event, or Event 006
documentation searches. The retired female working keys are therefore absent.
Their exact superseded spellings were not retained in the repository because
the Mediterranean character registry is still an untracked in-flight file.
The absence verdict rests on the exhaustive current-key inventory rather than
a one-to-one comparison against a committed predecessor.

## Current live leader portrait inventory

This section records runtime registrations and file headers only. It does not
assess the in-progress replacement artwork.

| Package | Live `156x210` DDS files | Live `65x67` army-small DDS |
|---|---|---|
| AFX | `portrait_AFX_walloon_provisional_assembly.dds`, `portrait_AFX_walloon_reserve_commander.dds` | `portrait_AFX_walloon_reserve_commander_small.dds` |
| AGX | `portrait_AGX_friesland_coastal_council.dds`, `portrait_AGX_friesland_coastal_commander.dds` | `portrait_AGX_friesland_coastal_commander_small.dds` |
| AJX | `portrait_AJX_saar_municipal_neutral_commission.dds`, `portrait_AJX_saar_industrial_security_commissioner.dds` | `portrait_AJX_saar_industrial_security_commissioner_small.dds` |
| BRI | `portrait_BRI_independence_wave_civic_commission.dds`, `portrait_BRI_independence_wave_coastal_commandant.dds` | `portrait_BRI_independence_wave_coastal_commandant_small.dds` |
| RHI | `portrait_RHI_independence_wave_provisional_directorate.dds`, `portrait_RHI_independence_wave_river_commandant.dds`, `portrait_RHI_josef_friedrich_matthes.dds` | `portrait_RHI_independence_wave_river_commandant_small.dds` |
| BAY | `portrait_BAY_independence_wave_state_council.dds`, `portrait_BAY_independence_wave_mountain_commandant.dds`, `portrait_BAY_rupprecht_of_bavaria.dds` | `portrait_BAY_independence_wave_mountain_commandant_small.dds` |
| SCO | `portrait_SCO_independence_wave_civic_convention.dds`, `portrait_SCO_independence_wave_territorial_commandant.dds` | `portrait_SCO_independence_wave_territorial_commandant_small.dds` |
| WLS | `portrait_WLS_independence_wave_national_council.dds`, `portrait_WLS_independence_wave_mountain_commandant.dds` | `portrait_WLS_independence_wave_mountain_commandant_small.dds` |

The live inventory is eighteen large portraits and eight army-small dossiers,
for twenty-six registered Event 006 portrait textures. Every registered path
exists. Each large DDS declares `156x210`. Each army-small DDS declares
`65x67`. All twenty-six have the DDS magic header.

The only portrait-regeneration exemptions are exactly:

1. `gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds`
2. `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds`.

They are the two real historical route leaders. No other live Event 006 leader
or army-small DDS is exempt from the replacement tranche.

Six ACX and AEX DDS files also exist in the Event 006 leader folder, but no
current `.gfx` sprite or gameplay consumer registers them. They are not part of
the live count and are not exemptions:

- `portrait_ACX_cornish_port_and_mines_committee.dds`
- `portrait_ACX_cornish_coastal_commander.dds`
- `portrait_ACX_cornish_coastal_commander_small.dds`
- `portrait_AEX_flemish_civil_industrial_board.dds`
- `portrait_AEX_flemish_industrial_security_commander.dds`
- `portrait_AEX_flemish_industrial_security_commander_small.dds`.

The new portrait worker was still producing its package during this audit. No
raw output, processed portrait, contact sheet, or visual quality was reviewed.
A separate post-production audit must reassess the final runtime set after that
worker finishes and the parent completes any sprite handoff.

## Documentation result

The following current sources describe asset-neutral advisor offices:

- `docs/events/006_independence_wave/northern_western_europe_packages.md`
- `docs/assets/006_independence_wave/manifest.md`
- `docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/manifest.md`
- `006_event6_advisor_icon_withdrawal_2026_07_16.md`
- the corrected Event 006 source-of-truth map and resume packet.

The source-of-truth map now marks the advisor portions of the earlier BRI/AJX
audit as superseded by the withdrawal. Historical handoffs remain historical
evidence and are not rewritten to pretend their pre-withdrawal inventory never
existed.

## Files changed by this audit

- `common/characters/006_independence_wave_wallonia_frisia_characters.txt`
  removed two redundant `female = no` lines
- `common/characters/006_independence_wave_saar_characters.txt` removed one
  redundant `female = no` line
- `common/characters/006_independence_wave_mediterranean_characters.txt`
  removed three redundant `female = no` lines
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` records
  the current asset-neutral boundary and supersession
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`
  records the withdrawal in its current facts and reading order
- `common/country_leader/006_independence_wave_nwe_advisor_traits.txt` removes
  the stale claim that the advisor offices use dossier portraits
- `docs/events/006_independence_wave/northern_western_europe_packages.md`
  replaces the stale advisor-card inventory with the asset-neutral boundary
- this final audit handoff.

## Simplifications, omissions, and blockers

The absence of custom advisor icons is the explicit user-selected design. It
is not a fallback or missing-art substitution.

No advisor mechanic was simplified or removed. The pre-existing COR recruitment
gap is recorded as an IW-017 package blocker. The in-progress portrait artwork
was deliberately not assessed, and no claim about its quality or completion is
made.

## Skills used

- `chaos-redux-subagents`
- `chaos-redux-events`
- `chaos-redux-event-assets`

No skill was created or updated during this audit.
