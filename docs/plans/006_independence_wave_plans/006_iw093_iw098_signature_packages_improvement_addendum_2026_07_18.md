# Event 006 IW-093 / IW-098 signature-package improvement addendum

**Date:** 2026-07-18
**Status:** accepted implementation handoff, not runtime admission
**Packages:** IW-093 Asante (`DOX`) and IW-098 Sokoto (`SOK`)

This addendum turns the two researched West African registry rows into bounded
playable-package work. It does not grant content readiness. Both packages stay
fail-closed until their gameplay, identity, visual, localisation, AI, scenario,
and country-package audits pass.

## Shared implementation rules

- IW-093 uses new Event 006 tag `DOX`, state 274, the Kumasi capital policy,
  `RG-GHANA-ASANTE-FANTE`, and the high-chaos pool only.
- IW-098 reuses dormant vanilla `SOK`, state 902, and
  `RG-NIGERIA-COARSE`. A living SOK is rerolled, never overwritten.
- Event 006 owns only the mechanics, focus/decision overlay, roles, cleanup,
  ambitions, and formables created by this release. Event 012 remains a
  separate origin/promotion system and must not replace an active Event 006
  tree or clear Event 006 state.
- Setup uses the frozen Event 006 release ledger. Optional territory is trimmed
  before a candidate is rejected; no package performs ownership changes before
  the synchronized incident commits.
- Tuning belongs in
  `common/script_constants/006_independence_wave_iw093_iw098_constants.txt`.
  Values are clamped and every paid action writes a concrete receipt. Neither
  package uses a political-power store, passive checklist mission, reward-dust
  loop, or free-unit loop.
- Independence Wave has no advisor icons, advisor portraits, advisor sprites,
  advisor dossiers, or advisor asset manifests. Characters used as country
  leaders or commanders are separate consumers.

## IW-093 Asante

### Playable identity and starting problem

Prempeh II anchors the restored 1935 Asante Confederacy. The opening state is
not a medieval reconstruction: the Asantehene and chiefs share authority with
Kumasi administrators, veterans, railway and market officials, and a modern
cabinet. The package begins with weak transport, exposed cocoa and gold trade,
an unsettled former-host account, and a dispute over how much authority belongs
to the court.

The visible values are:

1. **Confederated authority** (0-100): ability of Kumasi and the member stools
   to execute common policy.
2. **Court-cabinet balance** (-100 to 100): negative values favor court rule;
   positive values favor constitutional administration.
3. **Cocoa and rail throughput** (0-100): usable export, internal transport,
   and supply capacity.
4. **Host settlement** (0-100): progress toward a recognized property,
   railway, debt, and security settlement with the former host.

Focuses and decisions must visibly move these values. Low authority increases
consumer burden and resistance exposure; high authority improves stability and
division organization. Throughput changes construction, supply, and trade
effects rather than awarding cash-like points. The balance value locks the
royal-confederate, constitutional-cabinet, veterans' emergency, and wider
federal routes. Host settlement changes claims, non-aggression, guarantees,
trade access, and the risk of a reclamation war.

### Lanes and transactions

- **Survival:** seat the Kumasi administration, register member delegations,
  secure the state capital, and establish a forest guard. The first emergency
  action costs 35 command power, 1,000 infantry equipment, and 90 days of
  training; it upgrades an existing Event 006 formation and cannot create a
  repeatable free division.
- **Government:** a paid 70-day constitutional conference chooses the
  royal-confederate or cabinet route. It consumes 100 political power and
  requires authority and balance thresholds; the veterans route instead needs
  severe host threat and 50 command power.
- **Economy:** repair the Kumasi rail and cocoa depots through two staged
  120-day projects. Each consumes civilian-factory use through decisions and
  a 500-equipment security receipt; completion adds state infrastructure or a
  building only after the corresponding project ledger closes.
- **Military:** forest infantry, colonial-veteran screening, and supply patrols
  improve existing units and doctrine. Mobilization increases instability and
  host tension, so it is not a costless force ladder.
- **Diplomacy and host:** negotiate railway stock, public debt, customs, and
  border policing. Rejection can produce sanctions, a timed frontier crisis,
  or a defensive host war; agreement produces mutual obligations rather than
  a free relation bonus.
- **Ambition:** the constitutional-cabinet route opens FORM-24 only after authority,
  throughput, host settlement, and member-consent proofs. The sovereign route
  permanently locks the founding congress for that generation.

AI prioritizes survival and throughput while the host is threatening, favors
the royal-confederate route when court balance is negative, the constitutional
route when cabinet balance and host settlement are high, and FORM-24 only when
three attested members can actually consent.

## IW-098 Sokoto

### Playable identity and date-aware leadership

IW-098 represents the Sokoto sultanate and native administration in a modern
1930s setting. It does not flatten Hausa civic interests, Fulani dynastic
institutions, the emirates, Islamic legal scholarship, or neighboring peoples
into one identity. Hasan dan Mu'azu Ahmadu is the ruler before 17 June 1938;
Siddiq Abubakar III is the ruler on and after that date. A missing pre-cutover
leader package is a hard readiness failure, not permission to install the later
ruler early.

The visible values are:

1. **Emirate compact** (0-100): consent and administrative reach among the
   emirates.
2. **Court-civic balance** (-100 to 100): dynastic/religious authority versus
   Hausa municipal and constitutional administration.
3. **Caravan and livestock network** (0-100): trade, supply, and cavalry
   sustainment.
4. **Frontier security** (0-100): control of routes and ability to resist host
   or regional coercion.

The legal and administrative route must distinguish religious jurisdiction,
municipal law, taxation, education, and military command. It must never use a
generic sacred-text icon or invented historical banner.

### Lanes and transactions

- **Survival:** reconvene the emirate council, register Sokoto's native
  administration, and secure the caravan approaches.
- **Government:** a 70-day compact costs 100 political power and chooses a
  sultanic-federal, constitutional northern, or emergency military settlement.
  Court-civic balance and emirate consent provide the route locks.
- **Economy:** caravan wells, livestock markets, and route guards use staged
  90/120-day decisions with civilian-factory and equipment costs. Results
  change infrastructure, supply, trade, and state output; they do not award a
  substitute currency.
- **Military:** cavalry and frontier infantry are upgraded from frozen release
  forces. A cavalry reorganization costs 40 command power, 750 infantry
  equipment, and 250 support equipment; repeat execution is blocked by a
  formation receipt.
- **Diplomacy and host:** negotiate native-administration accounts, railway and
  customs access, and frontier security. Belligerent scenario types can begin
  with an unresolved host war, while negotiated types begin with a timed
  settlement mission.
- **Ambition:** religious, federal, or defensive routes may open FORM-25 only
  after three exact active members, three anchors, and three explicit consents
  are frozen. A sovereign northern settlement permanently closes the founding
  route for that generation.

AI weighs the sultanic route when emirate compact is high and court balance is
negative, the constitutional route when civic balance and frontier security are
high, and the defensive route under severe threat. FORM-25 is attempted only
when its frozen consent proof can pass; route labels alone never count as
members.

## Implemented route and former-host settlement tranche

The route conferences lock their compatible shared Event 006 route and apply
centralized party distributions, election policy, package-value shifts, and
all five country-mechanic deltas. They fail without overwriting an incompatible
route selected elsewhere in the shared framework.

Both former-host actions dispatch to the exact frozen surviving host after 90
paid days. Recognition creates a non-aggression settlement; association adds a
host guarantee and military access; rejection imposes an embargo, creates a
reclamation wargoal, and writes the unresolved crisis. All outcomes write the
shared host ledger, country values, network standing, and package values. The
settlement receipt is written only after an accepted host answer, or after a
paid 75-day post-crisis ratification once the shared outcome proves
recognition, guarded coexistence, client settlement, or host collapse.

## FORM-24 and FORM-25 disposition

FORM-24 West African Federation and FORM-25 Sahel Confederation remain
registered but fail-closed until their exact identity packages exist. `WFX`
and `SFX` are collision-free candidates from the 2026-07-18 installed-mod
audit, not yet admitted tags. Each formable needs a frozen carrier generation,
exact member-country/generation/anchor arrays, explicit consent receipts,
identity and integration adapters, member-sovereignty policy, cleanup, flags,
localisation, AI, and a rerun collision audit. No assumed Fante, Hausa, Darfur,
Wadai, Benin, Oyo, or Kanem-Bornu member may be materialized from a name alone.

## Implementation and audit surfaces

The package tranche requires dedicated constants, exact package
triggers/effects, characters, ideas, decisions/missions, focus branches,
events, AI strategy, localisation, country-leader portrait registrations,
historically researched ImageGen-authored flat flag packages, and central
dispatch/import edits. Final admission requires country, focus, decision,
localisation, asset, Event 005 collision, host-survival, and SCN-008 intensity
audits. The Asante painted HOI4 portrait, opening Sokoto likeness, and exact
period flag identities remain explicit blockers; neither package may receive
runtime content attestation while those blockers remain.
