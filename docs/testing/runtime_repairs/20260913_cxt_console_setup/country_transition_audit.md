# CXT country transition audit

Status: source review complete on 2026-09-13.
Parent acceptance basis: the user authorized repairing the errors and crash caused by `e chaosx_test`, and the parent accepted the reviewed activation, receiver, and capital-fixture correction within that scope.

Scope: read-only country-package and transition audit; this handoff is the only file written by this subagent.
The parent owns the gameplay implementation in `common/scripted_effects/chaosx_test_country_effects.txt` and `events/chaosx_test_country.txt`.

## Finding

The candidate has no remaining source-level transition blocker in the reviewed surface.
It establishes CXT on a real owned and controlled state before constructing the CXT country scope, moves the player tag only after that activation, and defers all setup helpers to a country event whose `ROOT` is CXT.
This directly addresses the reported missing `CXT` capital scope, invalid `State` unit creation, and `None` scope failures observed when the old inline body crossed `change_tag_from`.

The accepted camp correction assigns `genocide_responsible_country = PREV` inside the CXT `capital_scope` before the three fixture registrations at `common/scripted_effects/chaosx_test_country_effects.txt:189-207`.
Here `PREV` is the enclosing CXT country, so an inherited capital camp pointer is deliberately rebound to CXT before registration.

## Transition sequence audit

1. The public effect at `common/scripted_effects/chaosx_test_country_effects.txt:283-314` sends an already initialized CXT directly to the receiver event.
For another country, it first requires an owned capital state, saves the current country as `chaosx_test_origin_country`, and saves that capital as `chaosx_test_origin_capital_state`.

2. The saved capital executes `transfer_state_to = CXT` and then `set_state_controller_to = CXT` at `common/scripted_effects/chaosx_test_country_effects.txt:291-296`.
The installed effects documentation defines `transfer_state_to` as setting both owner and controller, while the explicit controller effect makes the later controlled-capital preflight unambiguous.

3. Only after that state transfer does the `meta_effect` construct the literal CXT country block at `common/scripted_effects/chaosx_test_country_effects.txt:299-310`.
It sets the saved state as CXT's capital, changes the player tag from the saved origin, and queues `chaosx_test_country.1` while the current country scope is CXT.

4. The hidden receiver at `events/chaosx_test_country.txt:11-63` is triggered-only and requires `tag = CXT`.
Because it is a country event fired on CXT, its event `ROOT` is CXT, which is the scope contract required by the existing facility, occupation, unit, CBRN, camp, and package-extension helpers.

5. The receiver annexes the origin only when the saved target is an existing country that is not CXT and still owns at least one state.
The annex uses `transfer_troops = no`, preserving the test harness's deliberate exclusion of vanilla divisions.

6. The receiver restores the saved capital only when that state is owned by CXT, then runs initialization or refresh only when CXT owns and controls a capital.
The nested `any_owned_state` state trigger uses `PREV` for its enclosing CXT country, so `is_controlled_by = PREV` is the intended scope relationship.

The sequence follows the installed documentation for `country_exists`, `annex_country`, `change_tag_from`, `country_event`, `set_capital`, `set_state_controller_to`, and `transfer_state_to`.
It also matches vanilla fragmentation precedents in `common/on_actions/04_mtg_on_actions.txt`, where successor land is established before `change_tag_from` and annexation is performed in the successor country scope.

## Required transition cases

### Multi-state origin

The origin retains its non-capital states after the capital transfer, so its saved country target remains useful to the receiver.
The receiver annexes those remaining states without importing their divisions, restores the recorded capital, and then invokes `chaosx_test_country_initial_setup` with CXT as `ROOT`.

### One-state origin

The capital transfer gives CXT the origin's only state before the player switch.
The origin can remain landless long enough to serve as the `change_tag_from` target; vanilla Yugoslav fragmentation in `common/on_actions/04_mtg_on_actions.txt` contains the corresponding landless-origin switch precedent.
The receiver's `NOT = { tag = CXT }` and `any_owned_state = { always = yes }` guard skips an empty or self-annex, while the saved state still supplies the CXT capital.
This path is source-supported but was not live-engine tested by this subagent.

### Already initialized CXT

The public effect does not capture or transfer an origin when the current tag is CXT.
It queues the same receiver, which finds no origin targets, validates the existing CXT capital, and selects `chaosx_test_country_refresh` because `chaosx_test_country_initialized` is already set.
The refresh path preserves the 261 static divisions and existing processed markers for registered content.

### Missing owned capital

The non-CXT branch safely does nothing when the current country has no owned capital state.
No generic fallback capital is introduced, and the bounded fixture remains faithful to its recorded-country contract.

## Country package coverage checklist

- [x] `CXT` is registered consistently in `common/country_tags/chaosx_test_country.txt:3`, with its country definition and landless history in `common/countries/Chaos Redux Test Country.txt` and `history/countries/CXT - Chaos Redux Test Country.txt`.
- [x] The public scripted effect, hidden receiver event, capital transfer, player switch, annexation, and initialized refresh are wired under stable identifiers `chaosx_test`, `chaosx_test_country.1`, `chaosx_test_origin_country`, `chaosx_test_origin_capital_state`, and `chaosx_test_country_initialized`.
- [x] State ownership, controller, capital restoration, and controlled-capital gating are covered by the reviewed sequence.
- [x] The CXT capital camp fixture rebinds `genocide_responsible_country` to CXT before registration, including an inherited state that already carried an origin pointer.
- [x] The extension bus, registered project/equipment/unit synchronizers, daily CXT repair, and weekly technology/stockpile hooks remain in `common/scripted_effects/chaosx_test_country_effects.txt` and `common/on_actions/chaosx_test_country_on_actions.txt`.
- [x] The existing 87 static templates and three divisions per template remain intact, for 261 static divisions.
- [x] Country identity, flags, localisation, and hidden debug infrastructure remain aligned with `docs/testing/chaosx_test_country.md`.

## File surface checklist

| Surface | Reviewed path and result |
| --- | --- |
| Tag registration | `common/country_tags/chaosx_test_country.txt:3`; `CXT` is registered. |
| Country definition | `common/countries/Chaos Redux Test Country.txt`; existing graphical culture and color shell remain valid. |
| Country history | `history/countries/CXT - Chaos Redux Test Country.txt`; landless dormant start is intentional. |
| Public setup effect | `common/scripted_effects/chaosx_test_country_effects.txt:283-314`; deferred activation sequence is sound. |
| Hidden receiver event | `events/chaosx_test_country.txt:11-63`; triggered-only CXT receiver supplies `ROOT = CXT`. |
| Static unit setup | `common/scripted_effects/chaosx_test_country_unit_effects.txt`; unchanged 87-template/261-division contract. |
| Tag hooks | `common/on_actions/chaosx_test_country_on_actions.txt`; daily and weekly hooks remain tag-scoped. |
| Localisation and flags | `localisation/english/chaosx_test_country_l_english.yml` and `gfx/flags/CXT.tga` variants; no new player-facing key or asset is needed for the hidden receiver. |
| Contract documentation | `docs/testing/chaosx_test_country.md`; transition, camp-pointer, roster, and extension behavior are documented. |

## Missing or stale surfaces

No missing or stale country-package surface was found within this bounded audit.
The receiver is hidden and has no title, description, option, event-log entry, or event-catalog row by design, so no player-facing event localisation or log registration is required.
No new focus tree, decision, mission, idea, leader, advisor, portrait, doctrine, or AI surface is introduced by this repair.

## Map and state setup issues

The dormant CXT history intentionally has no starting state.
The new sequence makes the recorded origin capital the activation state, explicitly controls it for CXT, and only runs setup after the state passes the owned-and-controlled-capital gate.
The existing occupation fixture can then select a separate populated non-capital foreign state as documented in `docs/testing/chaosx_test_country.md:25`.
No generic or unrelated state transfer was added.

The remaining state-level risk is limited to unusual saves where the current player has no owned capital; the public effect then performs no transition by contract.
This is a guarded boundary rather than an invalid scope path.

## Politics, leader, portrait, flag, advisor, and party issues

No issue is introduced in these surfaces.
CXT's existing history supplies the intended neutral no-election shell, and the existing country name, adjective, flag variants, and localisation remain the package's only identity surfaces.
The hidden receiver does not expose text or character assets.

## Focus, decision, idea, and asset issues

No focus tree, decision category, mission, player-facing idea, or new visual asset is part of this repair.
The existing modifier-free hidden idea carriers used by the documented extension contract remain untouched and are consumed only by the CXT setup bus.

## Starting military, technology, industry, supply, and production issues

The setup helpers remain unchanged apart from the accepted CXT camp responsibility assignment.
They now execute from the receiver's CXT country scope, so facility transfers, `create_unit`, stockpile, technology, doctrine, supply, and production targets resolve against CXT rather than the original console country.
The static roster remains 87 templates with three divisions each, preserving the 261-division baseline; registered units continue through the existing idempotent extension bus.
The receiver's `transfer_troops = no` annex prevents vanilla origin divisions from entering that roster.

## AI and playability issues

No AI weight, probability, MTTH, strategy factor, focus selection, or research-selection surface changed, so a probability audit is not applicable.
The source establishes the capital and controller prerequisites before setup, and the existing daily/weekly replenishment hooks remain bounded to CXT.

## Validation and evidence limits

The offline references consulted for this audit were `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, the required core wiki pages, and the installed documentation files `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` and `triggers_documentation.md`.
The relevant vanilla precedents are `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/on_actions/04_mtg_on_actions.txt`, `events/AAT_Norway.txt`, and `events/Baltic.txt` under the installed game directory.
Existing Chaos Redux dormant-tag patterns were also consulted in the mod's `events/002_zombie_outbreak.txt` and `events/091_the_great_revolution.txt`.

The read-only HOI4 event routes were invoked against `chaosx_test_country.1`.
The inspector returned `EVENT_INSPECTED_PARTIAL` and the renderer returned `EVENT_RENDERED_PARTIAL` with no blocking diagnostics, but the workspace-wide helper projection was deferred with the exact message `Large workspace analysis deferred workspace-wide helper projections and lifecycle passes; direct evidence is linked`.
The focused route reported `helpers = 0`, so it does not prove runtime scope resolution or event-target lifetime.
Useful artifacts are the event trace `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bbf61daf76b3cb8ca49c46d34c423eebe7f1a1cb0eb0d0e0f8ecf51b5bf05420/03f7af4065bdaf36dae984e089fd3de86e66e0388ffc1fb94ebf20b4c93acbc4/event-trace-3ac0bcfca142.json` and the target render `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d5837aca26942b325517041282dd0f4fc7e02a320331a3927db52a70782c819d/f509c98538295bdf2adfb9ca56ea82c43da2e8d99e2f6b6dc974d4ec3cb76b59/event-targets-3ac0bcfca142.json`.
The parent packet also records the exact `EVENT_REVISION_NOT_CACHED` limitation in `docs/testing/runtime_repairs/20260913_cxt_console_setup/README.md`, `mcp_before.json`, and related repair artifacts.

Live game execution, console control, and log inspection were not performed by this subagent, so this handoff makes no engine-execution claim.
The one-state path and dormant-tag activation are supported by source and vanilla precedent, while their final runtime behavior remains outside this read-only audit.

## Handoff disposition

Disposition: implemented in the parent-owned source surface and accepted for parent review.
No transition blocker remains in this audit.
The only recorded residual is the deliberate live-engine and deferred MCP helper-lifecycle limitation above.
