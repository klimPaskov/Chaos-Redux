# New Ore, part 8: Campaign continuity and changing control

## The deposit is the durable fact

A deposit belongs to a real state for the rest of the campaign. Its original discovery, later control changes, current controller, and participation in the expanding ore network remain distinct facts. The current country advantage is a consequence of those facts. Losing an idea, changing a government, releasing a country, or loading a save cannot create or destroy the geological deposit.

Each country receives one effective direct ore tier derived from the number of unique deposits it currently controls. Its strongest valid foreign entitlement is considered only when it has no direct deposit. A country that loses one of several deposits keeps the correct benefit from those remaining. A country that loses its last direct deposit may immediately fall back to a still-valid purchased agreement at another source.

Control changes must remove and grant the relevant advantage in the supported control-change resolution before the next applicable combat-stat evaluation. A periodic daily correction is not an acceptable definition of immediate transfer. Visual panels may redraw on the next normal UI refresh, but their underlying gameplay entitlement must already be correct.

The original state remains identifiable throughout the campaign. Evolution I refers to its deep vein, the first-discovery achievement refers to that exact site, and an expanded network never silently renames a later deposit as the original.

## Political and military changes

| Campaign change | Direct benefit | Foreign agreements and other consequences |
| --- | --- | --- |
| Ordinary hostile occupation | Moves to the actual new controller | Agreements supplied from that state end immediately under the old controller. The occupier may make its own offers |
| Ownership changes while control does not | Continues with the actual controller | Do not terminate a source agreement merely because the legal title changed while supplier and control remain valid |
| Liberation or peace returns control | Moves to the restored actual controller | Old terminated agreements stay terminated. New terms require consent |
| A controller becomes a puppet | Remains with that country's own controlled deposits | Its overlord receives no automatic direct or foreign access. Apply the protected paid-term rule to existing commercial/security periods while actors and control remain valid and non-hostile. New agreements and renewal purchases require current legality |
| Overlord takes a subject's actual state control | Recalculate both countries from post-transfer control | Source agreements end when the actual supplier changes. Event-controlled voluntary non-hostile transfers settle paid terms first, and other unsettled non-hostile losses use part 3's supplier-wide reliability rule |
| Civil war creates a new country | Each side benefits only from the deposits it actually controls | Do not duplicate an inherited national spirit, agreement, or payment onto the new side. A deposit retained by the original supplier can continue supporting valid agreements |
| Annexation removes a country | Every affected site follows its actual live controller | Agreements involving the extinct country end. Its extinct identity cannot retain payments, claims to access, demands, or action targets |
| A country is released later | Gains direct access only through states it actually controls | It receives no dormant ore licence merely because the same country tag had one in the past |
| Capitulation leaves a country alive | Follows actual state control throughout occupation | A capitulated customer can retain foreign access if it remains a valid country and all agreement requirements hold. Native limits on ordinary diplomacy still apply |
| An ore state temporarily has no valid controller | The state remains a deposit with no active direct beneficiary | Source agreements end because their supplier no longer controls it. The next valid controller receives the direct benefit immediately |
| A deposit is excluded by a later content change | Preserve its historical identity and report the incompatibility | A compatibility migration must resolve the real state reference. Never silently redirect the deposit to a convenient replacement state |

Normal war outcomes continue to matter. Possessing ore does not create supplies, fuel, manpower, organization, air superiority, repair speed, invulnerability, or a guaranteed peace settlement. A vastly better armored force can still be encircled, unsupplied, bombed, outmaneuvered, or defeated by a more capable coalition. These are the intended military responses to the event's extreme armor advantage.

Bombing the state, damaging infrastructure, blockading a coast, or reducing local compliance does not lower a valid direct controller below its ore tier. Those conditions can change how attractive a contract or defense commitment is. They do not insert an unannounced extraction failure into the core promise.

## Forces, equipment, and changing ownership

The ore entitlement belongs to the country using the armor according to the verified native ownership rules for the consumer. It is not a permanently upgraded inventory item that can be manufactured once and exported to the whole world.

| Equipment or force transition | Required outcome |
| --- | --- |
| A pre-existing tank or armored formation receives direct access | Its actual applicable armor gains the current direct ratio without waiting for replacement production |
| A stored old variant is deployed after access starts | It uses the current beneficiary's entitlement when consumed or fielded |
| A new model or module arrangement enters production | It benefits under the same applicability rule, with no separate ore purchase or special template requirement |
| A formation changes its mix of armored equipment | Recompute its actual armor under the same formation and equipment rules as the ore-free comparison |
| Equipment is captured, sold, or lend-leased to a country without access | The new country's actual armor uses its own entitlement. The former owner's ore bonus is not exported as a permanent upgrade |
| A beneficiary imports ordinary equipment | Its eligible imported armor gains the beneficiary's current ore advantage |
| An agreement ends while the recipient has stock or fielded units | The foreign ore contribution ends for existing and future applicable consumers |
| A country's ore access ends but Event 028 still applies | Preserve the asteroid material contribution in the new ore-free result |
| A special armored unit spawns through another Chaos Redux event | Its real positive armor contributions qualify regardless of whether its equipment type happens to be named armor |

For expeditionaries and volunteers, the intended beneficiary is the legal force owner, not a receiving ally that temporarily commands the units. This must be tested against the actual native modifier application. If the engine attributes different armor components to different scopes, the implementation must solve or explicitly escalate that mismatch before claiming compliance. An unverified ownership shortcut must not enable temporary transfer of command to launder ore access.

The rule applies to positive armor contributed by equipment, modules, and subunits. A unit carrying both an armored equipment contribution and an intrinsic armored subunit contribution receives the intended single effective ratio across the resulting statistic. Covering one contribution twice while missing the other is a failure.

## Content and expansion support

The baseline event must work in the supported base-game configuration. Installed expansions may alter the equipment and diplomacy surfaces through which the same rules operate. They do not grant a stronger ore tier simply by being installed.

| Content configuration | Coverage and integration obligation |
| --- | --- |
| Base-game equipment | Inventory conventional tanks and their applicable roles, mechanized or other positive-armor equipment, armored ships, and every active custom Chaos Redux armored consumer |
| Tank designer content | Test old and new designs, variant and module changes, manufacturer effects, production switching, and mixed equipment in existing formations |
| Naval designer content | Test actual naval armor from the installed hull and armor-module system, existing ships, refits, imported or captured ships, and independent naval modifiers |
| Armored-car content | Cover positive armor in the installed armored-car archetypes and the real subunit consumers. A reconnaissance role is not an exemption from an actual armor statistic |
| Aircraft designer content | Determine whether any installed aircraft or modded aircraft has an actual supported armor statistic. Air defense, damage reduction, and armor-themed module names alone do not qualify |
| International equipment market content | Apply ore according to the buyer's actual entitlement after ownership transfer. The commercial allocation remains a finite ore-access agreement, even when the ordinary market is available |
| Military industrial organization content | Compare otherwise identical units with organization and design bonuses held constant. Their independent armor contributions cannot dilute the promised relative ore improvement |
| Other Chaos Redux content or installed armored families | Enumerate and document actual armor consumers before release. Future content must extend this inventory whenever it adds a positive-armor family or contribution |

A native diplomatic action that requires an unavailable expansion cannot be the only entry into foreign access. Commercial, security, and faction choices must use eligible ordinary relationships in the current configuration. A country's political rules can make a particular security promise unavailable without hiding its lawful commercial choices.

### Continuity through a supported Fallout transition

If the Fallout owner supports continuation of an existing ore system, Event 098 preserves each geological identity at its actual state while Fallout applies its [state rewrite and tag-preservation contract](../air_cleanliness_fallout_specs/specs/69_fallout_tag_preservation_technology_and_fracture.md).
Changed state grades, survival resources and technology do not turn that deposit into a Scrap allowance.
[Fallout salvage](../air_cleanliness_fallout_specs/specs/baseline/04_survival_mechanics.md#survival-resources) retains its own stock and spending rules.
Salvaged armored equipment uses the receiving country's current Event 098 entitlement, and neither salvage nor a former ore-equipped item grants export access.

Event 098 reconciles actual post-transition control, valid actors and diplomacy through the same rules as other transformations.
A changed controller terminates the former source agreements.
Dissolved faction membership ends faction allocations.
A non-hostile guarantee or qualification reset with unchanged valid actors and source control retains commercial/security paid-term protection under part 3, including any already paid future period.
Renewal and new offers require an owner-supported current relationship and legality assessment rather than revival of obsolete guarantees.

Remaining positive-armor consumers use the current material grade against their otherwise equivalent post-regression armor.
The connection grants no replacement technology or relaxed armor floor.
The Fallout owner keeps the [transition and presentation boundaries](../air_cleanliness_fallout_specs/specs/68_fallout_consequence_boundary.md), and unresolved continuation or negotiation support remains an explicit owner dependency.

## Time, eligibility, and saved campaigns

All continuing periods use campaign dates and recorded episode identity. Loading a save, changing controller, opening a decision tab, or receiving a repeated callback cannot extend an already confirmed term or finish a sustained achievement early.

An evolution that becomes eligible creates one pending opportunity under the shared MTTH system. Its existing due information survives save/reload. Relevant changes in Chaos, security, and discovery circumstances update that opportunity through the system's supported dynamic pacing contract. They do not repeatedly draw a fresh full delay every time a country changes hands.

If Chaos falls below an evolution's requirement before that evolution manifests, the pending opportunity pauses while ineligible. Its earned waiting progress is retained and it resumes when eligibility returns. Once manifested, the evolution's physical discoveries, refining knowledge, diplomatic behavior, and armor tier persist even if Chaos later falls.

For a disabled evolution that has never manifested, its pending opportunity pauses under the same rule. Re-enabling it resumes eligible work. A disabled evolution does not block the independent tracks that remain enabled. Changing an evolution toggle after manifestation prevents future scheduled manifestations owned by that toggle, such as additional New Deposits, but does not delete existing deposits, end paid access arbitrarily, or reverse known refining.

The initial fire-once event can remain disabled or not yet selected without creating ore. Its details accurately describe the enabled evolution configuration. On a first firing at high Chaos, the world still receives exactly one baseline deposit. The eligible enabled tracks then use their normal opportunities, including the recent-discovery spacing in part 2. Their separate effects must not be folded into an undocumented simultaneous opening.

## Resumption and old Event 098 saves

The existing public event identity and fire-once history are retained. An upgrade from the old implementation migrates a demonstrated old physical ore state to the new registered-deposit system. The resulting direct beneficiary is its actual current controller, even if an old owner-based spirit had persisted elsewhere.

When the old save has one valid state marker and a consistent old reference, that state becomes the original deposit. An already-fired record does not roll another one. Old speed, attack, or defense modifiers that were merely bundled into Event 098 are removed with the superseded ore implementation, leaving unrelated sources intact. Their removal must be explained in the rework documentation because the new design concentrates power in real armor.

When an old global reference and old local state markers disagree, migration inspects the actual old data and reports the discrepancy. Multiple physical old markers cannot be silently converted into a free Evolution II network. The implementation must establish which marks were real Event 098 manifestations from the available save history or provide an explicit migration disposition. It must never destroy valid player territory or invent a new original site to hide an ambiguous save.

Fresh saves have a clean original identity and unique registry from the first discovery. Their later source counts, contracts, milestones, and evolution history must be identical before and after saving and loading.

Debug invocation follows the project's current player and initialization routing. It must not manufacture paid agreement receipts, extend terms, grant achievement progress, or create repeated first-discovery Chaos. Startup registration is idempotent. Repeated monthly repair scans are not a substitute for correct lifecycle ownership.

## What remains under each event's control

Event 098 owns its ore deposits, current direct and foreign contribution, agreements including protected paid terms and one early-renewal period, demands, state-defense commitments, ore milestone memory, and achievements. Event 029 continues to own mines and mine concessions. Event 092 owns its sale, bids, price settlement, and actual territory transfer. Event 086 owns its claimant and claims. Event 028 owns its separate mineral sites and contribution.

The event observing a connection asks for a verified public result from the event that owns it. It does not edit another event's private history to make the interaction work. Two systems observing the same capture must remain idempotent and preserve each other's valid benefits.

This division gives the player one consistent physical rule through every campaign transformation: the ore is still in its state, the current controller receives its direct advantage, and every foreign country needs a live agreement of its own.
