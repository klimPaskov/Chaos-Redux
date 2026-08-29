# Event-Free Famine and Migration Validation

Date: 2026-08-25.

The accepted design contains no famine incident event, migration incident event, or Event 149 replacement. Source census and workbook inspection establish that `famine_incident.1`, `migration_incident.1`, and `chaosx.nr149.1` are absent as event objects and are not present in any event pool or pacing registry.

Narrow read-only `hoi4.event_inspect` calls for all three exact event selectors returned `EVENT_INSPECTED_PARTIAL` at graph revision `f588a2607444400ec9fa9d102943fc0e10dc4482ebca9935232a4df2966f59d5`. The retained trace artifacts are:

- `famine_incident.1`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8aa418e59593a7b9190018906a5f8470142dc30cbdb42229f1087abf3ce82e10/278098b223770501fb8c676ac43f21f557269fd1198fbfae67e5c7dfaeca7032/event-trace-f588a2607444.json`.
- `migration_incident.1`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/966379b7e8415ff3d1762a8b5daf8382fe8453be298d04e83d2bb8506320ae50/bf6277ce02d8e019b9a8b6cb12cca51717ef2596a56bd86045d314d886783233/event-trace-f588a2607444.json`.
- `chaosx.nr149.1`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eda95da835f2fb2d280a32ab2aa0ea90367ba761281f70642fde44aa363e3c0e/f3dfc3d99b605d365923f60c9cfa52757d62882d9babba1f341298fe4f4fed43/event-trace-f588a2607444.json`.

The matching read-only event renders also returned `EVENT_RENDERED_PARTIAL`. Each selector's manifest contains `branches=[]`, confirming that the selected nonexistent ID has no renderable event chain:

- `famine_incident.1`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e6af71ee980c216f6b39b0888b1b901184c474f0ba614c03cd5e31b6777d2afb/25d5e75db80ec877dfe52082d5c1c50c5b9076675388ae5b6c03b7ad83b7ebf6/event-overview-f588a2607444-manifest.json`.
- `migration_incident.1`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86c21b70765861393aa75ea9987785ee2cd6b64d163dfb96f6ed4b2c8fc637f7/1716dcf6d4500545a333bc8e53adb23a6e74b14dcbca21ff6bac1fee699cdddc/event-overview-f588a2607444-manifest.json`.
- `chaosx.nr149.1`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/db91a1173c15908cc28a6f2f7304d47f9981adfa4e8244b5d34c2e22900d82fd/e63294d0d7c5c29351604ebb902e7947383be54ec90d8bea65afd2dc1b906e07/event-entries-f588a2607444-manifest.json`.

These are partial negative-selector artifacts, not a clean global event-graph validation. The repository-wide graph retains 14 blocking diagnostics and large unresolved/omitted-node counts unrelated to these nonexistent selectors. The selector-specific empty branch lists supplement, but do not replace, source and catalog absence proof.

No `event_compare` applies because there is no event object or before/after event revision to compare. No event was created to satisfy the tool.
