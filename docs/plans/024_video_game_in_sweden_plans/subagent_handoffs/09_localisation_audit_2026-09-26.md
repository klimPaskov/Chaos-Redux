# Event 24 localisation audit and integration handoff

## Disposition

Implemented and parent-reviewed for source wording and cost localisation. Visual fit of the ordinary decision cost rows remains unverified because the production decision render was unavailable.

## Scope and source surfaces

The fresh localisation pass audited Event 24 event text, decisions, category text, missions, scripted localisation, event names, debug names, History, Event Details, evolution titles and bodies, achievements, cost texticons, the English catalog row, and encoding.

The auditor edited only `localisation/english/024_hearts_of_iron_l_english.yml`. The parent then reduced the five four-value inline cost rows to the decision skill's three-value display limit and moved the fourth cost, with its matching texticon and dynamic amount, into each matching `_cost_tooltip` key.

The final cost mapping is:

| Decision | Inline values | Hover cost tooltip adds | Total spendable costs |
|---|---|---|---:|
| Logistics Module | Trains, lorries, support equipment | Civilian factory | 4 |
| Field Validation | Fuel, support equipment, trains | Army experience | 4 |
| Reality Audit | Army experience, support equipment, fuel | Trains | 4 |
| Narrow Reality Audit | Army experience, support equipment, fuel | Trains | 4 |
| Trust the Model | Command power, political power, stability | War support | 4 |

The offline Decision Modding page confirms that `custom_cost_text` automatically uses the matching `_blocked` localisation when its trigger fails and the matching `_tooltip` key on hover. This resolves the auditor's provisional concern that three `_cost_tooltip` keys had no direct source references.

## Edited keys

The auditor changed 22 keys: five event descriptions, the dynamic category description, two requirement tooltips, seven cost rows, and their seven blocked variants. The parent updated five matching hover cost tooltips to list all four spendable costs explicitly. The category description now scopes the Stockholm requirement to field reports, consistent with host eligibility.

No Event Details or evolution body key changed. The authoritative Event 24 catalog Details and three evolution body cells therefore remain aligned with their in-game wording.

## Validation and MCP evidence

The auditor found 279 unique Event 24 English keys with no duplicates, no missing key among 105 direct Event 24 event and decision references, all 15 scripted-localisation calls resolved, no missing key among 59 Event 24 scripted-localisation references, and a UTF-8 BOM. Parent validation after the cost-display patch confirms 279 unique keys, no duplicates, the BOM, and exactly three texticons in each affected normal and blocked inline string.

Current Event MCP lint is partial with no blocking diagnostics at revision `60d7bb069cf4775966ed1d430b161f4789d7de3f3784d2498cfa95def6ac54b8`, graph hash `f23b9d50107bf08726e0adb7041010a015574c496828940bde71067286de654f`. Lint artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/61e90d82e8c38aeae505eb1ab8d1339ae088084cfc030e7d2dab36e430acdb05/d05a9ee620f766bd3aac27feeecd47b185b25ff4424fb4c446db95e17c636559/event-lint-60d7bb069cf4.json`.

Current Event MCP options rendering is partial with no blockers at the same revision. Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/57a005fe8ff59f52c92f65e12c1b2791e256ccef299fd244eb659e69f451ef12/781345d576d778e3451e93f2e7eaa7ced158c580017fe57325bf180c169adbd7/event-options-60d7bb069cf4-manifest.json`.

## Remaining limitations

The MCP event graph is partial because workspace-wide helper and lifecycle projections were deferred. The production decision-row visual check timed out, so the inline cost rows have source-level evidence for the three-value limit but no current in-game fit confirmation. Shared Event Details and map presentation renders also timed out. Live game validation remains user-owned.
