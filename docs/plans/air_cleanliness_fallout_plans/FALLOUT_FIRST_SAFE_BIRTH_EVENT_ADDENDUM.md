# Fallout First Safe Birth event addendum

## Status

This is a manually authored dormant global-survival candidate for the Fallout
living-world scheduler. It uses candidate `282`, transaction key `710014`,
route `7114`, and history `9119`. It does not authorize scheduler activation.

## Player contract

The first safe birth after the mass-death winter is a political and social
decision, not a free morale popup. The country has enough shelter and medicine
to protect one delivery, while food, recognition, and Cohesion decide how the
birth is carried into public life. The event occurs only during the first
post-Fallout year, after the Ash-week grace period and before the first year
closes.

The opening presents four distinct choices:

1. hold a public celebration and spend Food, Medicine, and Recognition to make
   the birth a shared civic marker
2. protect the family privately and spend Medicine, Shelter capacity, and a
   small Scrap reserve to keep the room quiet
3. make the birth a demographic campaign and spend Food, Power, and
   Recognition to recruit families and administrators into a visible recovery
   program
4. let shelter elders choose the rite and spend Food, Medicine, and
   Recognition to give local custom authority over the first ceremony

Every choice reserves a three-beat human envelope. The opening, delayed result,
and delayed callback are each visible to a human country. Hidden AI uses the
same branch costs, outcome bands, effects, memory, and cleanup, with zero
visible budget cost for its result and callback rows.

## Outcome and delayed structure

The result is due after 21 days. Its deterministic viability score blends the
frozen country Cohesion, Medicine, Shelter capacity, and the recorded civilian
Deaths total. The Deaths term is normalized through the candidate's explicit
0 to 100 severity formula. Each branch has a success, partial, and failure
band. Failure requests a small state population loss through the Deaths
contract rather than subtracting population directly.

The callback is due after 180 days. It checks the surviving generation marker,
current Cohesion, and the original branch memory. Success records a durable
generation-change memory and grants a modest manpower and resource return.
Partial success preserves the memory but leaves a visible demographic dispute.
Failure records a closed nursery, applies the lower callback Deaths rate, and
keeps the country eligible for later recovery events rather than retrying this
chain.

## Identity and scheduler fields

| Surface | Contract |
| --- | --- |
| Primary family | global survival and society |
| Event class | routine incident |
| Cooldown family | generation change |
| Preferred phase | first winter year |
| Secondary phase | consolidation |
| Target | country, with no state target |
| Resource pressure | Medicine source, normalized from the live survival row |
| State value | frozen Country Cohesion, with Shelter retained in the result ledger |
| Severity | recorded civilian Deaths normalized to 0 through 100 |
| Human visible budget | 3 at opening, 1 for the visible result and callback |
| Hidden AI visible budget | 0 for hidden result and callback |
| Delays | 21 days for result, 180 days for callback |
| History | 9119 with branch and outcome payloads |

The candidate requires a current scheduler row, durable schema-3 survival
resources, Cohesion at or above the reviewed floor, Medicine at or above the
reviewed floor, Shelter capacity at or above the reviewed floor, and a current
campaign day in the first-year window. A completed birth memory closes the row
permanently for that country. There is no generic fallback branch.

## Mechanical connections

- Food, Medicine, Power, Shelter capacity, Recognition, Cohesion, stability,
  war support, and intelligence exposure all have branch-aware result deltas.
- The success path adds a controlled manpower return and stores a durable
  generation-change counter for later school, citizenship, and succession
  chains.
- Failure routes use the Deaths system and a lower callback rate. They never
  use direct building damage or a second population subtraction.
- Dynamic modifiers distinguish public celebration, private protection,
  demographic campaign, elder rite, maintained nursery, and a failed nursery
  memory.
- The callback closes the chain only after its delayed receipt and the result
  receipt have both passed authenticated cleanup.

## Localisation direction

The opening should stay inside the shelter maternity room, the attendant's
measured supplies, and the family decision. The four options should sound like
distinct social authorities. Public celebration is civic and exposed. Private
protection is protective and suspicious of spectacle. The demographic campaign
uses administrative ambition without turning people into a statistic. The elder
rite is local, oral, and rooted in a community that has buried too many names.
Result text should mention concrete supplies, attendants, family witnesses,
and the country's named government authority. Callback text should show how the
first child changes a school, ration queue, clinic, or succession conversation.
Avoid generic birth symbolism, abstract hope language, and process notes.

## Asset contract

Use one dedicated generated report image at 210x176. The scene should show a
cold shelter maternity room with a covered lamp, an attendant's hands, a
wrapped infant, a family witness, and a ration or medicine tray. It must be a
fictional symbolic scene with no readable text, real person, real institution,
flag, logo, or reused Fallout picture. Generate through the approved event-art
workflow, retain source and processed evidence, convert to DDS, and wire only
through the Fallout-owned GFX file.

## Review boundary

The chain remains dormant and earns no release-floor credit until the existing
candidate registry review, scheduler activation, host authority, save recovery,
multiplayer behavior, and runtime Event Log delivery are proven. The accepted
numerical contract remains authoritative for cadence, fatigue, visible budget,
deterministic selection, hidden AI parity, and cleanup.
