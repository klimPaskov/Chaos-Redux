# Event 010 Death - Focus Tree Spec

## Purpose

Death needs a compact but real focus tree because it is a country actor with a changing method. The tree must not offer normal ideology, industry, diplomacy, or conquest paths. It should decide how Death spreads, how visible it becomes, how ghost formations develop, and how it crosses from island absence to world-end pressure.

Use `load_focus_tree` when Death is spawned, following the local Fury precedent.

## Structure

Tree name: `death_focus_tree`

Recommended lanes:

```text
The First Shore
  -> No Herald
  -> No Envoy
  -> No Tax Ledger
  -> method fork:
       Quiet Census
       Black Tide
       Still Front

Support lanes:
  Empty Economy
  The Unnamed Ranks
  Charts Without Coastlines
  When The Mainland Learns
  The Last Continent
```

The method fork is mutually exclusive. Support lanes can be gated by phase, route, consumed population, reveal, and world-end.

## Opening Focus Group

| Focus | Role | Reward direction |
| --- | --- | --- |
| `death_the_first_shore` | Confirms origin, initializes event variables, locks Death setup. | Calls setup effect; sets origin route flags. |
| `death_no_herald` | Death does not announce itself. | Lowers early rumor chance, slows spread. |
| `death_no_envoy` | Death cannot be diplomatically understood. | Blocks normal diplomacy and faction behavior. |
| `death_no_tax_ledger` | Death has no normal economy. | Converts consumed industry to pressure variables. |

Opening rewards should call scripted effects and set variables. Avoid factories, research slots, and ideology bonuses.

## Method Route A - Quiet Census

Fantasy: Death lists places before taking them.

Mechanical identity:

- slowest spread
- highest stealth
- more `death_listed_state` marking before consumption
- weaker immediate withering
- more stored population converted into future ghost capacity

Focus examples:

| Focus | Effect |
| --- | --- |
| `death_the_quiet_census` | Selects route and initializes listed-state logic. |
| `death_names_before_houses` | Improves target marking and hidden target arrays. |
| `death_the_unposted_letter` | Delays observer rumor events. |
| `death_no_one_to_answer` | Increases island-consumption yield if no defense is present. |
| `death_allotted_time` | Converts high silence into ghost capacity after reveal. |

Tradeoff:

- if an ordinary country discovers a listed state, containment is stronger and can cancel the listing
- route is weak if public reveal happens early

AI:

- default for isolated origins with many low-population islands
- preferred when nearby naval opposition is strong and stealth matters

## Method Route B - Black Tide

Fantasy: the sea becomes the border.

Mechanical identity:

- faster island spread
- faster post-reveal coastal jumps
- lower stealth
- more vulnerable to naval patrol and lighthouse decisions
- weaker early ghosts

Focus examples:

| Focus | Effect |
| --- | --- |
| `death_the_black_tide` | Selects route and lowers island-spread cooldown. |
| `death_every_harbor_a_mouth` | Adds port-based coastal target eligibility after reveal. |
| `death_charts_without_coastlines` | Improves adjacent sea-region targeting. |
| `death_the_unlit_channel` | Raises pressure where patrols are absent. |
| `death_every_shore_is_a_door` | Unlocks limited post-reveal coastal jumps. |

Tradeoff:

- reveals Death earlier
- navies can contain it more reliably if they act early

AI:

- choose near island chains or weak naval powers
- choose when chaos tier is already high enough that stealth is less valuable

## Method Route C - Still Front

Fantasy: Death stops moving quickly and makes every front impossible to hold.

Mechanical identity:

- lower jump frequency
- stronger adjacent-state withering
- stronger state attrition and movement penalties
- earlier passive ghost border formations
- fewer total coastal jumps

Focus examples:

| Focus | Effect |
| --- | --- |
| `death_the_still_front` | Selects route and improves withering pressure. |
| `death_where_the_road_ends` | Raises penalties in adjacent withering states. |
| `death_no_return_paths` | Punishes unsupported offensives in consumed states. |
| `death_the_white_map_orders` | Counters ordinary-country movement-mitigation decisions. |
| `death_the_line_does_not_move` | Improves defensive ghost spawn on mainland borders. |

Tradeoff:

- can be starved if surrounded before multiple coastlines are reached
- weaker island expansion after route selection

AI:

- choose after early mainland foothold
- choose when adjacent land-front opportunities are better than sea jumps

## Empty Economy Lane

Death consumes industry but does not use factories.

Focus examples:

| Focus | Effect |
| --- | --- |
| `death_factories_without_hands` | Deleted factories increase `death_consumption_yield`. |
| `death_ports_that_receive_nothing` | Consumed ports improve coastal target range but never build navies. |
| `death_the_last_inventory` | High deleted industry improves world-end foothold strength. |
| `death_no_workday_returns` | Suppresses captured-state production and resistance noise. |

Rules:

- no factory construction bonuses
- no research slots
- no dockyard/naval production logic
- pressure conversion values in script constants

## The Unnamed Ranks Lane

Ghost stage focuses should be auto-bypassed or become available only when thresholds are met. Death AI must not waste time on locked focuses.

| Focus | Unlock | Reward |
| --- | --- | --- |
| `death_pale_companies` | consumed population or 600-tier equivalent | Stage 1 ghost template and small capacity. |
| `death_mute_regiments` | higher population or 800-tier equivalent | Stage 2 ghost template and local attack permission. |
| `death_the_final_muster` | world-end only | Stage 3 template and aggressive plans. |
| `death_no_names_in_the_rolls` | route/ghost support | Reduces farming rewards and cleanup leaks. |

## Reveal And World-End Lane

| Focus | Trigger | Reward |
| --- | --- | --- |
| `death_the_name_arrives_before_the_army` | public reveal | Replaces hidden spirits and unlocks war behavior. |
| `death_the_black_continent` | continental threat | Raises dread and compact pressure. |
| `death_the_last_continent` | world-end eligibility | Prepares foothold arrays and final aggression. |
| `death_no_more_maps` | world consumed or Death player endgame | Terminal capstone. |

These focuses should be gated by scripted triggers and bypass logic. If a phase is reached by event before the focus is taken, the focus should be completed or bypassed cleanly.

## Layout And UX

The tree should read vertically from origin to reveal to endgame:

- opening group near top
- mutually exclusive methods clearly separated
- economy/ghost support lanes on sides
- reveal/world-end lane centered below method fork
- no huge empty ideological branches

Use unique focus icons or stable placeholders. Register icons before asking for final art.

## Localisation Tone

Focus names should be austere and bureaucratic:

- `The First Shore`
- `No Herald`
- `No Envoy`
- `No Tax Ledger`
- `The Quiet Census`
- `The Black Tide`
- `The Still Front`
- `Factories Without Hands`
- `Ports That Receive Nothing`
- `The Unnamed Ranks`
- `The Name Arrives Before The Army`
- `No More Maps`

Descriptions should imply method, not explain implementation history or tuning.

## AI Weights

AI focus weights should use MTTH variables or scripted route helpers.

Route inputs:

- number of valid island candidates
- origin remoteness
- nearby naval powers
- reveal pressure
- consumed population
- mainland foothold status
- chaos tier
- player proximity

Death AI should not be blocked by a focus route if event state already requires reveal/world-end behavior. Scripted effects should be able to force phase transitions independent of focus progress.

## Focus Audit Checklist

Before completion:

- no normal ideology route
- no normal industry route
- all focus rewards call scripted helpers or constants
- all icons registered and localized
- all prerequisites, mutual exclusions, bypasses, and AI weights checked
- route effects are visible in event details or tooltips
- route cannot soft-lock reveal, defeat, or world-end
