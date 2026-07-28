# Event 006 IW-156, IW-196, IW-197, and IW-204 Vanilla Overlay Adapter Handoff

Status: implemented as a bounded additive overlay tranche; package admission remains held by the Event 006 completion audit.

## Scope

This tranche adds four identity-gated route overlays for existing vanilla carriers. It does not release a tag, create a country history file, overwrite state history, replace a meaningful vanilla focus tree, create a leader, add a portrait, add an advisor icon, or add a new flag asset.

Each route has centralized values, concrete resource and military costs, four lifecycle ideas, five decisions, one timed guard mission, a carrier-specific daily hook, suspension and resumption behavior, and a source-backed route gate.

## Vanilla contracts

### IW-156: democratic TNE / United States of Maluku

Installed vanilla history confirms TNE's capital and core in state 668 in `history/countries/TNE - Ternate.txt`. The installed build did not expose a separate `United States of Maluku` cosmetic token or a literal route string in the searched country, focus, decision, and event sources. The accepted route therefore uses the exact available identity contract: `original_tag = TNE`, `has_government = democratic`, `is_subject = no`, and ownership/control of state 668. This is an explicit build-level inference, not a claim that an uninstalled cosmetic token exists.

### IW-196: vanilla Antilles formable

Vanilla `common/decisions/formable_nation_decisions.txt` defines `antilles_category` and `unite_the_antilles`, allows original tags `HAI DOM PUE CUB JAM BAH GDL BAS`, sets cosmetic tag `antilles`, cores the Caribbean member states, and sets `antilles_formed_flag`. The overlay requires that original-tag allowlist, `has_cosmetic_tag = antilles`, and `has_global_flag = antilles_formed_flag`. It selects one controlled/owned anchor from states 689, 691, 692, or 694 without changing member consent or the vanilla formable's history.

### IW-197: CHL Mapuche State cosmetic route

Vanilla Chile focus/event content sets `CHL_mapuche_state` and includes Mapuche institutions and leaders. The overlay requires `original_tag = CHL` plus `has_cosmetic_tag = CHL_mapuche_state` and uses state 950 (Araucania) as its anchor. The Chilean tree, history, and existing institutions remain authoritative.

### IW-204: Kingdom of Araucania and Patagonia restoration

Vanilla `events/TOA_Chile.txt` sets `kingdom_of_araucania_and_patagonia` together with `CHL_chile_is_a_monarchy`. The overlay requires `original_tag = CHL`, that cosmetic tag, and the monarchy flag. It selects state 512 (Patagonia) first and state 507 (Southern Chile) second, only when the state is owned and controlled by the carrier.

## Runtime files

- `common/script_constants/006_independence_wave_iw156_iw196_iw197_iw204_overlays_constants.txt`
- `common/scripted_triggers/006_independence_wave_iw156_iw196_iw197_iw204_overlays_triggers.txt`
- `common/scripted_effects/006_independence_wave_iw156_iw196_iw197_iw204_overlays_effects.txt`
- `common/ideas/006_independence_wave_iw156_iw196_iw197_iw204_overlays_ideas.txt`
- `common/on_actions/006_independence_wave_iw156_iw196_iw197_iw204_overlays_on_actions.txt`
- `common/decisions/categories/006_independence_wave_iw156_iw196_iw197_iw204_overlays_categories.txt`
- `common/decisions/006_independence_wave_iw156_iw196_iw197_iw204_overlays_decisions.txt`
- `localisation/english/006_independence_wave_iw156_iw196_iw197_iw204_overlays_l_english.yml`

The hooks are one carrier definition per tag. `on_daily_TNE` refreshes IW-156; `on_daily_HAI`, `DOM`, `PUE`, `CUB`, `JAM`, `BAH`, `GDL`, and `BAS` refresh IW-196; and one `on_daily_CHL` refreshes both IW-197 and IW-204. Route identity triggers prevent unrelated countries from seeing the surfaces.

## Route surfaces

IW-156 tracks Maritime Mobility, Federal Legitimacy, and Island Logistics; its actions convene the Moluccan Congress, secure inter-island depots, integrate the Island Guard, hold state 668, and ratify a Moluccan Charter.

IW-196 tracks Maritime Cohesion, Federal Legitimacy, and Member Consent; its actions convene the Antilles Congress, secure member depots, integrate the Maritime Guard, hold a selected member sea anchor, and ratify the Antilles Charter.

IW-197 tracks Mountain Mobility, Territorial Representation, and Federal Legitimacy; its actions convene the Mapuche Territorial Council, secure Araucania depots, integrate the Mountain Guard, hold state 950, and ratify the Mapuche Charter.

IW-204 tracks Frontier Mobility, Restoration Legitimacy, and Volunteer Control; its actions convene the Restoration Court, secure Patagonia depots, integrate the Frontier Guard, hold a selected southern anchor, and ratify the Restoration Charter.

Every force action activates its route's timed guard mission. Loss of the owned/controlled anchor or mission timeout resets the guard progress, applies the centralized stability and legitimacy penalty, and removes the running state. Suspension removes the active idea and pauses an interrupted guard; resumption restores the overlay only when the vanilla route gate remains true.

## Validation evidence

The decision probability adapter inspected 16 non-mission weighted surfaces with zero unresolved inputs. The mission probability adapter inspected four missions with zero unresolved inputs. Static brace, quote, unsupported-operator, BOM, decision-localisation, and idea-reference checks passed for this tranche.

This evidence is source-level only. It does not prove live save/load behavior, AI completion, scenario coverage, focus-tree geometry, or package readiness. Those remain explicit blockers in the Event 006 completion audit.

## Assets and boundaries

No IW-156/IW-196/IW-197/IW-204 portrait, flag, advisor icon, or other asset was added. The Event 006 portrait master shelf remains flat at `docs/assets/006_independence_wave/portraits_generated_png`; it contains original-size HOI4-style PNG masters directly in that folder and no normalized 156×210 files or nested subfolders.

## Remaining risks

- The TNE gate is the documented installed-build inference described above and should be checked against any future vanilla version that adds an explicit Moluccan cosmetic tag.
- The Antilles anchor is selected from the first owned/controlled member state in the ordered contract; a live save test must verify the mission and tooltip present the selected member correctly.
- These adapters intentionally do not claim complete Event 006 country packages or meaningful-tree insertion. The shared focus geometry audit, live scenario evidence, AI/balance evidence, SCN-008 cell proof, and the broader country/package blockers remain open.
