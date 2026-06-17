# Event 012 Created-Country Static OOB Handoff

Date: 2026-06-17

## Scope

Patched only the standalone/static OOB surface for the 21 Event 012 created tags:

`WAC`, `SAH`, `MAG`, `NHR`, `EAC`, `GLK`, `CBC`, `ZSC`, `SLC`, `IOC`, `GHP`, `BBS`, `TDM`, `ANW`, `OVN`, `CRR`, `CTL`, `OKP`, `TRM`, `HGD`, `GHC`.

The normal Event 012 runtime dynamic force paths were not edited.

## Files Changed

Country histories:

- `history/countries/WAC - West African Congress.txt`
- `history/countries/SAH - Sahel Caravan.txt`
- `history/countries/MAG - Maghreb Coast.txt`
- `history/countries/NHR - Nile-Horn League.txt`
- `history/countries/EAC - East African Railway Congress.txt`
- `history/countries/GLK - Great Lakes Council.txt`
- `history/countries/CBC - Congo Basin Charter.txt`
- `history/countries/ZSC - Zambezi-Stone Cities.txt`
- `history/countries/SLC - South African Liberation Congress.txt`
- `history/countries/IOC - Indian Ocean Congress.txt`
- `history/countries/GHP - Gorilla Highlands.txt`
- `history/countries/BBS - Baobab Senate.txt`
- `history/countries/TDM - Tidemark Dominion.txt`
- `history/countries/ANW - Ananse Web.txt`
- `history/countries/OVN - Orisha Vodun Nature Courts.txt`
- `history/countries/CRR - Crocodile Rivers.txt`
- `history/countries/CTL - Chimpanzee Telegraph League.txt`
- `history/countries/OKP - Okapi Court.txt`
- `history/countries/TRM - Termite Citadel Engineers.txt`
- `history/countries/HGD - Honeyguide Commons.txt`
- `history/countries/GHC - Great Herds Compact.txt`

New OOB files:

- `history/units/WAC_1936.txt`
- `history/units/SAH_1936.txt`
- `history/units/MAG_1936.txt`
- `history/units/NHR_1936.txt`
- `history/units/EAC_1936.txt`
- `history/units/GLK_1936.txt`
- `history/units/CBC_1936.txt`
- `history/units/ZSC_1936.txt`
- `history/units/SLC_1936.txt`
- `history/units/IOC_1936.txt`
- `history/units/GHP_1936.txt`
- `history/units/BBS_1936.txt`
- `history/units/TDM_1936.txt`
- `history/units/ANW_1936.txt`
- `history/units/OVN_1936.txt`
- `history/units/CRR_1936.txt`
- `history/units/CTL_1936.txt`
- `history/units/OKP_1936.txt`
- `history/units/TRM_1936.txt`
- `history/units/HGD_1936.txt`
- `history/units/GHC_1936.txt`

## Identifiers Changed

Added `set_oob` references:

- `WAC_1936`, `SAH_1936`, `MAG_1936`, `NHR_1936`, `EAC_1936`, `GLK_1936`, `CBC_1936`, `ZSC_1936`, `SLC_1936`, `IOC_1936`, `GHP_1936`, `BBS_1936`, `TDM_1936`, `ANW_1936`, `OVN_1936`, `CRR_1936`, `CTL_1936`, `OKP_1936`, `TRM_1936`, `HGD_1936`, `GHC_1936`.

Added narrow support techs required by static templates:

- `SAH`: `tech_logistics_company`
- `ANW`: `tech_signal_company`
- `CTL`: `tech_signal_company`
- `TRM`: `tech_engineers`
- `HGD`: `tech_recon`

`WAC` and `EAC` already had the support techs their new templates use.

## OOB Coverage

- `WAC`: Lagos Congress Guard, `Congress Port Guard`, province `2050`, state `558`.
- `SAH`: Mali Caravan Guard, `Caravan Logistics Column`, province `4927`, state `556`.
- `MAG`: Algiers Harbor Watch and Oran Coastal Watch, `Harbor Watch Brigade`, provinces `7132` and `1145`, state `459`.
- `NHR`: Addis Highland Guard and Harar Pass Guard, `Highland League Rifles`, provinces `5010` and `8036`, state `271`.
- `EAC`: Dar es Salaam Rail Guard and Interior Track Repair Guard, `Railway Guard Section`, provinces `2196` and `8144`, state `546`.
- `GLK`: Kampala Lakes Watch, `Lake Council Askari`, province `12989`, state `548`.
- `CBC`: Leopoldville Charter Patrol and Matadi River Gate, `Basin Charter Patrol`, provinces `5117` and `12925`, state `295`.
- `ZSC`: Lusaka Enclosure Guard, `Stone City Defence Column`, province `5199`, state `771`.
- `SLC`: Johannesburg Liberation Guard, `Liberation Congress Brigade`, province `10400`, state `275`.
- `IOC`: Madagascar Port Guard and Antananarivo Congress Watch, `Island Passage Guard`, provinces `5222` and `5128`, state `543`.
- `GHP`: Rwanda Sanctuary Guard, `Gorilla Highland Sanctuary Band`, province `9962`, state `768`.
- `BBS`: Ouagadougou Root Guard, `Baobab Root Senate Guard`, province `10836`, state `778`.
- `TDM`: Mombasa Tide-Court Guard, `Tidemark Littoral Guard`, province `5210`, state `905`.
- `ANW`: Abidjan Ledger Couriers, `Ananse Courier Web`, province `10803`, state `779`.
- `OVN`: Cameroon Grove Guard, `Orisha Vodun Grove Guard`, province `2080`, state `773`.
- `CRR`: Brazzaville River Toll Guard and Loango Crossing Watch, `Crocodile River Toll Column`, provinces `8193` and `12975`, state `772`.
- `CTL`: Stanleyville Canopy Relay, `Chimpanzee Telegraph Relay Band`, province `1950`, state `718`.
- `OKP`: Albertville Shadow Guides, `Okapi Shadow Guide Column`, province `4941`, state `890`.
- `TRM`: Elisabethville Citadel Engineers, `Termite Citadel Engineer Guard`, province `191`, state `889`.
- `HGD`: Garissa Route Guides, `Honeyguide Route Guard`, province `8133`, state `903`.
- `GHC`: Rift Migration Guard, `Great Herd Migration Guard`, province `5160`, state `904`.

## Before And After

Before:

- All 21 Event 012 created country histories lacked static OOB references.
- No matching `history/units/TAG_1936.txt` files existed for the created tags.
- Standalone or alternate package startup could create empty tags despite normal runtime paths spawning dynamic forces.

After:

- Each tag loads a small, role-specific static land OOB from country history.
- Each OOB has at least one valid `division_template` and at least one placed `division`.
- Nonhuman and supernatural actors are explicitly identified in OOB comments and template names without joke identifiers.
- Province placements use real province IDs from the matching tag capital/seat state.

## Why The Change Is Bounded

- No scripted effects, localisation, focus trees, decisions, GUI, assets, Event 010 files, or unrelated docs were edited.
- The patch only fills the static OOB gap for already-created Event 012 country packages.
- The new support techs are limited to cases where the static template directly needs the support company.

## Meaningful Validation

Ran a task-specific Python validation that checked:

- all 21 `set_oob` references resolve to existing `history/units/*.txt` files
- each referenced OOB has at least one `division_template` and one `division`
- every `location =` province belongs to that tag's capital state province list from vanilla state history
- all OOB braces balance
- every subunit/support-company ID used by the OOBs exists in vanilla unit definitions
- every support company used has its matching starting tech in the country history

All checks passed.

## Skipped Validation

- No game launch or in-game spawn validation was run from this subagent context.
- No broad Event 012 completion audit was run, because this task was limited to the static OOB gap.

## Remaining Risks

- These are deliberately small static forces. The normal runtime dynamic force creation remains the main path for Event 012 balance.
- Parent follow-up, 2026-06-17: naval and air static OOBs are no longer absent for the actors with suitable seat infrastructure. `MAG`, `EAC`, `IOC`, `TDM`, `CRR`, `WAC`, `CBC`, `ANW`, and `OVN` now have DLC-split static naval OOBs; `MAG`, `IOC`, `OVN`, `NHR`, and `SLC` now have DLC-split static air OOBs. This remains small patrol/liaison setup, not full bespoke naval or air branch depth.
- The Event 012 country files and new OOB files are untracked in the current dirty worktree, matching the surrounding Event 012 package state at the time of this patch.
