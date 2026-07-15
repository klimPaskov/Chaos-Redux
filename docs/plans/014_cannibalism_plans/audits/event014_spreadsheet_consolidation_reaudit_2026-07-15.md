# Event 014 Spreadsheet Consolidation Reaudit

Date: 2026-07-15

Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Audited SHA-256: `6aa758d699d814599a1011d5f9acc1089bbf42baf053be7a4dbabadd525091a2`

## Verdict

The Event 014 and SCN-010 catalog rows already match the current implementation and localisation exactly. No workbook edit was required, and the workbook was not saved or exported during this audit.

| Severity | Open | Closed during this audit |
| --- | ---: | ---: |
| P0 | 0 | 0 |
| P1 | 0 | 0 |
| P2 | 0 | 0 |
| P3 | 0 | 0 |

The workbook records Event 014 as `Minor Fire-Once`, leaves both cluster fields blank, separates the baseline description from exactly three evolution columns, preserves two distinct terminal outcomes, and records `Fully Functional`. SCN-010 contains exactly the five live scenario types and also records `Fully Functional`.

## Source authority

The workbook was reconciled against the live source rather than against an older audit.

- `common/scripted_effects/chaosx_logic_effects.txt:179` registers Event 014 in `global.fire_once_events`.
- `common/scripted_effects/chaosx_event_cluster_effects.txt:302-397` contains the event-to-cluster mapping and does not assign Event 014 to a cluster.
- `localisation/english/014_cannibalism_l_english.yml:141-142` contains the exact pre-reveal and revealed Event Details text.
- `localisation/english/014_cannibalism_l_english.yml:185-192` contains the exact three evolution titles and descriptions.
- `common/scripted_effects/chaosx_events_log_effects.txt:2102-2117` adds Evolution I and Evolution II normally, then adds Evolution III only after `cannibalism_reveal_complete`.
- `common/scripted_effects/chaosx_events_log_effects.txt:924-948` registers `world_is_the_larder` and `no_thaw_will_come` as separate Event 014 terminal rows with separate IDs, sort orders, scenario flags, super-event IDs, title keys, and detail keys.
- `common/scripted_effects/chaosx_events_log_effects.txt:1091-1095` admits those two rows to the public world-end list only after `cannibalism_reveal_complete`.
- `localisation/english/chaosx_gui_l_english.yml:537-540` contains the exact terminal titles and details used in the workbook.
- `common/script_constants/014_cannibalism_constants.txt:2373-2379` defines the five SCN-010 type IDs.
- `common/scripted_triggers/014_cannibalism_triggers.txt:1715-1731` accepts exactly those five type IDs.
- `localisation/english/014_cannibalism_l_english.yml:1498-1513` contains the exact SCN-010 ID, name, five type descriptions, five type names, and four intensity descriptions.

An exact search of the current Event 014 implementation, localisation, specifications, and plans found no `Prison Host`, ancient-general disclaimer, or Carthaginian disclaimer. The scenario catalog cells contain no Hannibal or Lecter reference.

## Exact cell reconciliation

No target cell changed during this audit. The exact value recorded for each cell below is therefore both the before value and the after value.

### Events row

| Cell | Exact value before and after | Change |
| --- | --- | --- |
| `Events!A15` | `14` | None |
| `Events!B15` | `Cannibalism` | None |
| `Events!G15` | blank | None |
| `Events!H15` | blank | None |
| `Events!J15` | `Minor Fire-Once` | None |
| `Events!K15` | blank | None |
| `Events!L15` | blank | None |
| `Events!M15` | `Fully Functional` | None |

`Events!C15`, exact value before and after:

```text
Cannibalism begins with evidence recovered from an army at war. Burial parties vanish, ration ledgers are altered, and isolated formations report deliberate cutting and predation within their own ranks. Scarcity may explain the first crimes, but repeated methods suggest that damaged commands are protecting the perpetrators.

The crisis tests whether military institutions can restore supply, protect witnesses and the dead, and distinguish frightened soldiers from organized killers. Concealment may preserve calm while allowing the pattern to survive. Public terror may hold a front while teaching other units that predation brings rank and protection.
```

`Events!D15`, exact value before and after:

```text
Ritualized Ranks

Scattered predation has become a shared ideology of oaths, marks, promotion, and protected membership. No shared headquarters appears in the records.
```

`Events!E15`, exact value before and after:

```text
The Organized Network

Cells in separate countries use matching ledgers, routes, prisoner practices, and operational timing. Captured records identify no common headquarters.
```

`Events!F15`, exact value before and after:

```text
Hannibal Lecter Commands

The concealed command is publicly revealed, and the mature network begins unification under Hannibal Lecter.
```

`Events!I15`, exact value before and after:

```text
The World Is the Larder

Lecter's host has joined scattered feeding territories and armed kitchens into one command. Roads, farms, prisons, and conquered cities are treated as parts of a single larder, with surviving states left as prey or resistance enclaves.

Organized consumption becomes a permanent world order. Every surviving government faces the same expanding host, and the network no longer has any reason to hide.

No Thaw Will Come

Lecter's winter host has surrendered its last human restraints to the Wendigo form. Feeding grounds spread with the cold, and conquered communities are folded into a hunger that treats thaw, harvest, and mercy as weaknesses.

An advancing winter covers the world. The Wendigo command pursues every surviving country until organized human rule is consumed or driven into isolated refuges.
```

`Events!C15` is the spoiler-safe baseline and exactly matches `chaosx.events_log.window.event_details.cannibalism.pre_reveal`. Evolution columns `D15:F15` are the exact three live evolution stages. `G15:H15` remain blank, so no fourth or fifth evolution is implied. Evolution III names Hannibal Lecter because it describes the reveal stage, while the live Event Details preview withholds that stage until the reveal flag is set.

The workbook combines both terminal descriptions in `I15` because the catalog has one terminal-summary column. The runtime does not combine them. It maintains two independently keyed post-reveal terminal rows, `world_is_the_larder` and `no_thaw_will_come`.

### Scenario row

| Cell | Exact value before and after | Change |
| --- | --- | --- |
| `Scenarios!A10` | `SCN-010` | None |
| `Scenarios!B10` | `The Hunger Lines` | None |
| `Scenarios!D10` | `Discipline Collapse, Ritual Cells, Silent Islands, Warlord States, Convergence` | None |
| `Scenarios!F10` | `Fully Functional` | None |

`Scenarios!C10`, exact value before and after:

```text
Discipline Collapse: A wartime supply crisis has broken discipline inside selected formations. Field Hunger rises while damaged commands attempt containment before predation spreads beyond the first theaters.

Ritual Cells: Officer circles and hidden field kitchens have become organized ritual cells. Cult Cohesion is already visible, and several countries may begin with compromised commands.

Silent Islands: Remote ports and island garrisons have fallen quiet behind broken convoy schedules. Communes begin with mature cells, exposed sea routes, and a growing risk of armed island hosts.

Warlord States: Armed host countries emerge from occupied feeding grounds. Each begins with a regional command, an origin doctrine, scavenged stores, and forces raised from the territory it has seized.

Convergence: Several mature host countries answer a common signal. A public convergence warning begins after launch, leaving the world time to destroy the likely hosts and sever their routes before a final authority emerges.
```

`Scenarios!E10`, exact value before and after:

```text
Low: A narrow crisis begins with limited territory and forces. Containment remains possible, but delay will strengthen the cells.

Medium: Several formations or theaters enter the crisis. Supply pressure, concealment, and foreign routes will demand an organized response.

High: Mature cells and armed hosts begin with strong cohesion, severe command damage, and multiple routes across the map.

Maximum: A broad international network begins with numerous theaters and host countries. Escalation is immediate, but its supply lines, leaders, territories, and convergence routes can still be attacked.
```

`Scenarios!D10` contains exactly five comma-separated type names. `Scenarios!C10` contains exactly five corresponding descriptions in the same order. Neither cell contains `Prison Host`, Hannibal, or Lecter. `Scenarios!E10` matches all four current intensity descriptions exactly.

## `Fully Functional` status evidence

`Events!M15` and `Scenarios!F10` legitimately use `Fully Functional`.

- The current final completion reaudit reports no open P0, P1, P2, or P3 finding and independently matches the workbook hash and both target rows.
- The current integration/catalog, localisation/asset, documentation, improvement-loop, decision/mission, focus-tree, country-package, and super-event visual audits report no open finding in their assigned surfaces.
- The live implementation exposes all five scenario types, all three evolution stages, both reveal-gated terminal paths, and the required Event Details variants.
- No accepted Event 014 spreadsheet field, scenario type, terminal row, localisation surface, or accepted implementation item remains missing, simplified, or represented by a placeholder.

## Workbook structure and links

- The `Events` table covers `A1:M1015`, including `Events!M15`.
- The `Manual_Scenarios` table covers `A1:F11`, including `Scenarios!F10` and the unrelated concurrent SCN-013 row.
- Event category validation covers `J2:J1015` and includes `Minor Fire-Once`.
- Event status validation covers `M2:M1015` and includes `Fully Functional`.
- Scenario status validation covers `F2:F11` and includes `Fully Functional`.
- Conditional formatting covers `Events!J15`, `Events!M15`, and `Scenarios!F10`. The rendered category cell is yellow and both rendered status cells are green.
- `Events!M15` retains style ID 64, Arial 10, wrapping, borders, and the green status fill.
- `Scenarios!F10` retains style ID 11, Arial 10, wrapping, borders, and the green status fill.
- Event row 15 retains height 409.5. Scenario row 10 retains height 400.
- The workbook contains no formulas, formula-error values, defined-name links, or threaded comments. No linked formula or comment required repair.

## Render evidence

The authoritative workbook was rendered with the bundled spreadsheet runtime after the exact-value inspection.

Event 014 range render:

![Event 014 catalog row](../spreadsheet_audit/event014_catalog_consolidation_reaudit_2026-07-15.png)

SCN-010 range render:

![SCN-010 catalog row](../spreadsheet_audit/scn010_catalog_consolidation_reaudit_2026-07-15.png)

Both renders were reviewed at original detail. Text wrapping, row height, column placement, status fills, category fill, borders, and neighboring-row continuity are legible. No clipping, overlap, stale formula display, or visual repair requirement was found.

## Files changed by this audit

- `docs/plans/014_cannibalism_plans/audits/event014_spreadsheet_consolidation_reaudit_2026-07-15.md`
- `docs/plans/014_cannibalism_plans/spreadsheet_audit/event014_catalog_consolidation_reaudit_2026-07-15.png`
- `docs/plans/014_cannibalism_plans/spreadsheet_audit/scn010_catalog_consolidation_reaudit_2026-07-15.png`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_spreadsheet_consolidation_reaudit_handoff_2026-07-15.md`

The workbook itself was not changed by this audit. No commit was created.

## Simplifications, omissions, fallbacks, and blockers

None. The official loader-provided spreadsheet runtime was used. No fallback, placeholder, omission, weaker substitute, or blocker was involved.
