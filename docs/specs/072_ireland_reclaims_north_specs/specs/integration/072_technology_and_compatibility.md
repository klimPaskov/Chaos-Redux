# Technology, country identity, and compatibility matrix

| Surface | Intended behavior | Required verification |
| --- | --- | --- |
| Opening infantry and support | Coherent current-era ordinary equipment floor | Technology IDs, dates, battalion unlocks, support prerequisites, actual production variants |
| Artillery and trucks | Existing equipment families, usable reinforcement | Template costs, supply consumption, stockpile delivery and technology scope |
| Trains and convoys | Practical transport support | Installed equipment keys, immediate usable stock and DLC availability |
| Marines and other special forces | Ordinary battalions and real cap | Cap queries, training unlocks, doctrine and support compatibility |
| Mechanization | Earned research and production | Existing technology chain, fuel and maintenance, no automatic mass conversion |
| Aircraft | Verified fighter, support and maritime roles | Designer versus non-designer variants, role-count queries and airfield capacity |
| Ships | Verified escort, submarine and optional carrier families | Hull and module dependencies, unit-family count queries and doctrine |
| Ireland identity | Existing IRE or explicit approved identity mapping | Country history, cosmetic tags, focus ownership and alive-country checks |
| Celtic partners | Reuse existing valid identities | Vanilla, repository, Workshop and local-mod tag inventory before any new identity |
| Northern state | Existing event uses 119 | Active map membership, state identity, provinces, owner/control helpers |
| Formable maps | Exact finite approved state sets | Registry provenance, ordered mod overlays, generated assets and runtime category links |
| Political institutions | Existing ideology and actual government | Supported laws, party and leader data, no forced character replacement |
| Procurement and factory reservations | Real finite resources and obligations | Existing helper or documented engine representation, exact cost and cleanup |
| Intelligence and industrial organizations | Only when a verified existing feature is used | DLC presence, established consumers, native baseline equivalent |

The planning package deliberately does not invent exact unverified state, technology, character, ship-role, aircraft-role, or modifier identifiers.
Those fields are implementation evidence requirements.
Resolving them is normal engineering work, but they remain unresolved until inspected.
A developer must not mark a source-only design table as a successful engine check.

Use technology inspection, rendering, and comparison for the changed part of the graph and its dependencies.
Record the source revision, before and after artifacts, any removed or bypassed requirements, and whether every granted item is available in the tested DLC fixture.
A valid technology key is not enough if its equipment or support prerequisites are missing.

The minimum compatibility set is the supported base game, the user's normal installed DLC set, an advanced Ireland, a different northern holder, independent Celtic countries, and an Ireland with a cosmetic identity.
A map overhaul that changes essential state meanings is an explicit supported-mapping task.
It is not solved by reusing state numbers from another version.
