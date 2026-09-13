# Event 40 Decision and Mission Implementation Prompt

Implement the decision and mission layer for Chaos Redux Event 40, Lawrence of Arabia, from the accepted specification pack.

## Required reading

Read in full:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- every file under `docs/specs/040_lawrence_of_arabia_specs/`
- relevant offline Paradox wiki decision, trigger, effect, localisation, modifier, scope, and data-structure pages
- relevant installed vanilla decision and mission files and documentation
- existing Chaos Redux selected-target and intervention precedents

## Ownership

Event-owned decisions belong in:

- `common/decisions/040_lawrence_of_arabia_decisions.txt`
- `common/decisions/categories/040_lawrence_of_arabia_categories.txt`

Event-owned repeated logic belongs in Event 40 scripted effects and triggers. Use a shared dynamic helper only when its contract is neutral and useful outside Event 40.

## Presentation

Use ordinary decision categories with a static category picture. Do not create a dedicated scripted GUI.

The active target category shows one persistent value:

`Lawrence's Influence`

Show:

- exact value
- qualitative band
- trend
- next threshold
- current phase or blocking state

Do not expose British reach, cell strength, personal trust, federation readiness, or component formulas as extra counters.

Normal phases show three to five primary actions. Six is the hard maximum. Keep one or two Event 40 missions active in ordinary play.

## Target action families

Implement phased versions of these accepted actions. Final IDs and localisation should be stable and descriptive.

- Set the Mission's Terms
- Accept Arms Under National Custody
- Open an Arab Liaison Office
- Place Lawrence Under Escort
- Audit the Gold Ledger
- Build a Counterintelligence File
- Turn a Contact
- Feed Controlled Intelligence
- Expose the Network
- Restrict Tribal and Officer Travel
- Detain the Mission
- Expel the Mission
- Dismantle the Contact Network
- Offer an Independent Charter
- Play Britain Against a Rival
- Balance Foreign Sponsors
- Preserve National Custody

Do not expose every action at once. Replace opening actions after the access settlement. Show evidence actions only after enough evidence exists. Show detention or expulsion only when the target can attempt them. Show independent-charter actions only when the hidden personal route has a credible basis.

## British action families

Implement a compact sponsor category or a selected-target subsection.

- Authorize Gold and Arms
- Send Officer Cadres
- Secure the Red Sea Route
- Open the Desert Air Route
- Repair the Rail and Telegraph Link
- Back the Officer Corps
- Expand the Radio and Press Network
- Promise Constitutional Guarantees
- Tie Aid to Bases and Access
- Invite a Favored Partner Conference
- Attempt a Recovery Operation
- Negotiate an Exchange
- Disavow an Overexposed Mission
- Reinforce a Client Government

Every material action must debit real stockpiles or capacity. Do not create free equipment or route support.

## Mission families

Implement dynamic missions from these families:

- Trace the Gold Ledger
- Guard the Rail, Port, and Telegraph Nodes
- Secure the Officer Corps
- Keep the Arms Route Open
- Expose the Network
- Convene an Arab Congress
- Break the Revolt Cells

Use named states, ports, rail hubs, supply nodes, or routes. Do not show generic required-state text.

Use varied durations:

- ordinary urgent work: roughly 90 to 120 days
- medium institutional work: roughly 120 to 180 days
- large congress, cleanup, or revolt work: roughly 150 to 240 days

Implement success, partial success, and failure where the specification defines them.

## Cost rules

One action can spend at most four distinct cost types.

Use action-appropriate costs:

- political power for laws, promises, negotiations, and charters
- command power for escorts, detention, garrisons, and recovery, never above the project cap
- army experience for command reform and training integration
- infantry and support equipment for arms, guards, depots, and inspections
- fuel, convoys, trains, or aircraft for routes
- civilian factory burden for offices and infrastructure
- stability or war support as a real political consequence
- temporary division commitments for map objectives
- intelligence exposure as a consequence

Use compact icon-first cost localisation with correct texticons.

## Intelligence behavior

With La Résistance, use agency, counterintelligence, operatives, networks, and decryption where valid.

Without La Résistance, use the accepted fallback factors:

- stability
- government capacity
- encryption and decryption
- control of capital, ports, and routes
- military or security presence
- relevant national spirits
- earlier regional preparedness

The same core routes must remain playable without the DLC.

## Evolution changes

### Evolution I

Unlock cell incidents, revolt-network actions, cell detection, route security, officer loyalty work, government-replacement preparation, and the Break the Revolt Cells mission.

Do not create a civil war until the validated territorial and force package exists.

### Evolution II

Unlock client contribution, favored-partner politics, regional institutions, counter-bloc actions, and the Arab congress.

Clients can refuse or demand compensation. Do not force every British partner into one faction.

### Evolution III

Unlock congress, ratification, core-candidate, and federation-formation decisions.

Formation must call the validated transaction. It cannot directly annex participants through loose decision effects.

## AI

Implement the accepted target profiles:

- cooperative client
- sovereign pragmatist
- counterintelligence state
- anti-imperial challenger
- opportunistic double gamer
- fractured government

British AI must consider war, equipment, convoys, fuel, access, strategic value, exposure, and client cost.

Before changing any weight, run `chaosx_ai_probability_auditor` with the named scenarios in `quality/040_lawrence_of_arabia_probability_scenarios.md`. After the owner patch, run `hoi4.probability_compare` through the same auditor.

## Lifecycle and cleanup

Use generation IDs and one-shot receipts for aid, detention, exchanges, mission rewards, and settlements.

Clean up when:

- target is annexed
- Britain loses sponsor capacity
- Lawrence is captured, expelled, defects, retires, or dies
- active route becomes invalid
- a settlement completes
- federation formation supersedes the campaign
- the regional campaign ends

Preserve durable settlement memory.

## Audit

After implementation, run `chaosx_decision_mission_auditor` in patch-capable mode for narrow fixes. Require a handoff under:

`docs/plans/040_lawrence_of_arabia_plans/subagent_handoffs/`

Test every acceptance scenario that touches decisions and missions. Report any merged action, omitted mission, fallback, AI gap, or unresolved tooltip.
