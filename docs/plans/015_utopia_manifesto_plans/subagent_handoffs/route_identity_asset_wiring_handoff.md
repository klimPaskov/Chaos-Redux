# Event 015 route-identity asset wiring handoff

> Current disposition, `2026-07-15`: the missing decision-category attachment recorded in this dated handoff is closed. `utopia_manifesto_ledger_category` now contains `scripted_gui = utopia_manifesto_ledger_scripted_gui`. The sprite, portrait, advisor, and emblem evidence below remains valid.

Handoff date: `2026-07-14`  
Role: route-identity asset wiring specialist  
Source package: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/`

## Outcome

The parent-owned sprite and character wiring from the route-identity package is implemented:

- all `25` requested sprites are registered in the existing Event 015 GFX file
- all `16` Event 015 advisor `small` portrait references use the delivered stable portrait handles instead of idea-icon stand-ins
- the `5` league emblems have exact flag-driven consumers in the existing Commonwealth Ledger header
- the generic animated Ledger seal remains the pre-formation presentation and is hidden once one of the five formed-identity emblem flags is present
- cosmetic-tag flags remain filename-driven and require no `.gfx` registration

The league-emblem source wiring is complete, but its intended Ledger window is not yet reachable in game because the existing decision category does not attach the existing scripted GUI. The exact parent-owned blocker is documented below; this subtask did not edit the prohibited decision-category file or invent a substitute surface.

## Files changed

- `interface/015_utopia_manifesto.gfx`
  - registered `4` institutional leader portrait sprites
  - registered `16` advisor portrait sprites
  - registered `5` league-emblem sprites
- `common/characters/015_utopia_manifesto_characters.txt`
  - replaced exactly `16` advisor `small = GFX_idea_...` stand-ins
  - updated the file overview to describe the dedicated advisor portraits
- `interface/015_utopia_manifesto_ledger.gui`
  - added five route-emblem `iconType` consumers in the existing header seal position
- `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt`
  - mapped each emblem element to its existing formed-identity flag
  - limited the generic animated Ledger seal to the pre-formation/no-emblem state
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/route_identity_asset_wiring_handoff.md`
  - this handoff

No Event 015 focus, decision, decision-category, gameplay effect, event, or localisation file was edited. No binary asset was modified by this wiring pass.

## Registered sprite identifiers

### Institutional leaders

- `GFX_portrait_utopia_manifesto_household_assembly`
- `GFX_portrait_utopia_manifesto_council_of_callings`
- `GFX_portrait_utopia_manifesto_board_of_measure`
- `GFX_portrait_utopia_manifesto_stewardship_council`

The eight existing founder/successor character entries retain their package-specified sharing of these four institutional portraits.

### Advisors

- `GFX_portrait_utopia_manifesto_interpreter_small`
- `GFX_portrait_utopia_manifesto_general_provisioner_small`
- `GFX_portrait_utopia_manifesto_secretary_of_callings_small`
- `GFX_portrait_utopia_manifesto_surveyor_of_shores_small`
- `GFX_portrait_utopia_manifesto_civic_engineer_small`
- `GFX_portrait_utopia_manifesto_keeper_of_stores_small`
- `GFX_portrait_utopia_manifesto_league_envoy_small`
- `GFX_portrait_utopia_manifesto_advocate_of_limits_small`
- `GFX_portrait_utopia_manifesto_public_auditor_small`
- `GFX_portrait_utopia_manifesto_constitutional_jurist_small`
- `GFX_portrait_utopia_manifesto_council_organizer_small`
- `GFX_portrait_utopia_manifesto_social_workshop_planner_small`
- `GFX_portrait_utopia_manifesto_chief_surveyor_small`
- `GFX_portrait_utopia_manifesto_standards_engineer_small`
- `GFX_portrait_utopia_manifesto_steward_of_service_small`
- `GFX_portrait_utopia_manifesto_contract_broker_small`

Each matching character ID in `common/characters/015_utopia_manifesto_characters.txt` now references the same-suffixed handle listed above. No `small = GFX_idea_...` reference remains in that file.

### League emblems

| Ledger element | Sprite | Existing state flag |
| --- | --- | --- |
| `utopia_ledger_household_congress_emblem` | `GFX_utopia_manifesto_household_congress_emblem` | `utopia_manifesto_identity_household_congress_emblem` |
| `utopia_ledger_common_tables_emblem` | `GFX_utopia_manifesto_congress_of_common_tables_emblem` | `utopia_manifesto_identity_common_tables_emblem` |
| `utopia_ledger_network_directorate_emblem` | `GFX_utopia_manifesto_network_directorate_emblem` | `utopia_manifesto_identity_network_directorate_emblem` |
| `utopia_ledger_island_hierarchy_emblem` | `GFX_utopia_manifesto_island_hierarchy_emblem` | `utopia_manifesto_identity_island_hierarchy_emblem` |
| `utopia_ledger_plural_compact_emblem` | `GFX_utopia_manifesto_plural_compact_emblem` | `utopia_manifesto_identity_plural_compact_emblem` |

All five elements occupy the existing `64x64` header-seal slot at `x = 18`, `y = 16`. The scripted GUI shows an element only when its matching formed-identity flag is present. `utopia_manifesto_form_current_route_identity` clears the formed-identity flag family before setting the selected route, so these consumers follow the existing one-route identity contract.

## Behavior change

Before this pass:

- institutional leader handles had no Event 015 sprite definitions
- all sixteen advisors displayed idea art through `GFX_idea_...` handles
- league emblem DDS files and state flags existed, but no UI element consumed the stable emblem sprites

After this pass:

- the four institutional handles resolve to their delivered `156x210` DDS portraits
- every advisor resolves to its delivered role-specific `65x67` dossier portrait
- the existing Ledger header selects the matching `64x64` route emblem after formation and retains its existing animated seal before formation

## Meaningful validation

- Parsed the package's `gfx_handoff.md` and compared all `25` supplied name/path pairs against `interface/015_utopia_manifesto.gfx`; every pair matches exactly.
- Searched all repository `interface/*.gfx` files for the `25` names; every sprite definition occurs exactly once.
- Confirmed every registered runtime DDS path exists. All `25` files have the required one-level legacy BGRA header, exact file length, and declared dimensions: `4` at `156x210`, `16` advisor dossier cards at `65x67`, and `5` emblems at `64x64`. Institutional portrait alpha is opaque; advisor-card and emblem alpha span `0..255` as intended.
- Compared the package finals with runtime files by SHA-256: `4` institutional portraits, `16` advisor portraits, `5` league emblems, and `39` cosmetic-tag flags all match their package copies exactly (`64` pairs, no missing files or mismatches).
- Parsed all `16` character replacement rows from the supplied handoff and verified each character block contains exactly its assigned handle. The character file contains `16` dedicated small portrait references and zero advisor idea-icon stand-ins.
- Verified all five Ledger `iconType` elements consume the exact stable sprite, all five scripted-GUI visibility triggers consume the exact matching identity flag, and the generic Ledger seal excludes all five formed-emblem states.
- Confirmed the five identity flags are established by the existing route-formation effects after the formed-identity flag family is cleared.

The optional offline `hoi4.gui_inspect` pass could not produce an inspection artifact because the shared MCP artifact store returned `ARTIFACT_STORAGE_LIMIT`. This did not change source files. Visual/runtime layout evidence from that optional renderer is therefore not available in this handoff.

## Unresolved parent-owned attachment blocker

`common/decisions/categories/015_utopia_manifesto_categories.txt` defines `utopia_manifesto_ledger_category`, but that block does not contain:

```txt
	scripted_gui = utopia_manifesto_ledger_scripted_gui
```

The identifier `utopia_manifesto_ledger_scripted_gui` currently appears only in its definition in `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt`; no decision category references it. Because a `decision_category` context scripted GUI requires that category attachment, the existing Commonwealth Ledger window—and therefore the five correctly wired emblem elements—will not be instantiated until the parent adds the line to `utopia_manifesto_ledger_category`.

This subtask explicitly forbids edits to Event 015 decisions and decision categories, so the attachment was not added here. No alternate UI surface, fallback emblem, scripted-localisation router, or localisation key was invented.

## Simplifications, omissions, and blockers

- Sprite registrations omitted: none.
- Advisor replacements omitted: none.
- League-emblem source consumers omitted: none.
- Fallbacks used: none.
- Localisation needs introduced: none.
- Runtime blocker: missing decision-category attachment described above.
- Commit: not created, per parent instruction.

## Skills and references used

- `chaos-redux-subagents` for bounded ownership and handoff requirements
- `chaos-redux-event-assets` for stable sprite/path consumption, runtime-format checks, and no-fallback asset handling
- required offline Paradox wiki core pages plus Graphical Asset Modding, Interface Modding, Scripted GUI Modding, Portrait Modding, and Country Creation
- vanilla `common/characters/_documentation.md`, `common/scripted_guis/_documentation.md`, `common/decisions/_documentation.md`, character/advisor examples, portrait sprite examples, and scripted-GUI image-property examples

No skill was created or updated; this pass exposed no reusable workflow gap beyond the existing asset-wiring guidance.
