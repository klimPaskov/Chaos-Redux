# Event 097 Collaboration: Part 5, Connections and Cluster Role

Event 097 touches every war, so many systems can read it. This part defines the connections that change play and the public contract other events use.

Event 097 never depends on another event existing. Every connection below is inert until its partner exists and calls the contract.

## Public contract

Event 097 exposes a small owner API so other events can read and influence its state without touching private records. The API lives in Event 097's own scripted-effect and scripted-trigger files and is documented in their paired reference documents.

### Read surface

| Fact | Scope | Meaning |
| --- | --- | --- |
| Is a participant | country | The country participates in Event 097 firings |
| Incoming network band | country | The qualitative band of networks inside the country from Part 1 |
| Outgoing network band | country | The qualitative band of the country's networks abroad |
| Fifth Column band | country | None, Wavering, Defecting, or Collapsing |
| Strongest network country | country | The enemy with the strongest network inside the country while the Fifth Column is active |
| Is an installed government | country | The country was installed through Event 097 and its registry row is live or Abandoned |
| Installed government record | country | Installer, original tag, route, installation date, Installed Administration stage |
| Restoration pressure band | country | Low, Rising, or High, from the hidden restoration inputs below |
| Evolution states | global | Which Event 097 evolutions are active |

### Write surface

| Action | Caller proof | Bounded effect |
| --- | --- | --- |
| Burn networks | Caller id, beneficiary, host, reason | Reduces the beneficiary's collaboration inside the host by at most one base layer, never below zero, once per caller sequence |
| Retire an installed government | Caller id, government, route | Ends the registry row with a restoration or liberation record and applies the matching Chaos reversal |
| Install through Event 097 | Caller id, installer, host, route, and for the External sphere route a statement from the caller that the host lies in the installer's sphere | Calls the shared installation helper with the caller's route recorded, subject to every ordinary limit |

Every write requires the caller to supply proof that matches its own state. A call with missing or contradictory proof fails without changing anything. Event 097 owns every result.

## Event 095 Occupation Revolt

### The relationship

Collaboration makes occupied populations easier to govern. Occupation Revolt represents national resistance trying to overthrow foreign rule. A government installed through Event 097 can become the target of a national restoration uprising if enough opposition survives. Event 095 owns the uprising itself. Event 097 owns the record of who was installed and how much opposition survived.

Event 095 is marked for rework and has no specification. In its current form it returns enemy-controlled cores to a random government in exile and raises revolt divisions, without reading collaboration, compliance, or resistance. The contract below is what Event 097 offers. The Event 095 rework decides how to use it.

### Restoration pressure

Every government installed through Event 097 carries hidden restoration inputs. They combine into one qualitative band that Event 095 reads.

| Input | Points |
| --- | --- |
| The original country still exists as a government in exile | +3 |
| The original country chartered a government in exile before capitulating | +2 |
| The Installed Administration stage is Contested | +2 |
| The installer is at war and past 40 percent surrender progress | +2 |
| Each full year spent in the Entrenched stage | -1, never lowering the total below 1 while the government in exile exists |
| The installed government took Loyalty Commissions in the last year | -1 |

| Band | Points |
| --- | --- |
| Low | 0 to 2 |
| Rising | 3 to 4 |
| High | 5 or more |

The Abandoned stage sets the band to High regardless of points. The points and band edges are tuning anchors in the constant group, and the band is recomputed whenever one of its inputs changes.

The band, not the inputs, is shown, and only as a line in two reports to the original country: the report when a government is installed over it and the report when that government is Abandoned (Part 3). It is worded as the mood in the occupied homeland. It is not a persistent value the player tracks.

### What Event 095 can do with it

When the Event 095 rework exists, it can treat a High band as the condition that enough opposition survives, choose the installed government as the target of its national restoration uprising, and call the Retire action when the uprising restores the original country. Event 097 then applies its reversal Chaos and retires the registry row.

### What Event 095 changes in Event 097

When an Event 095 revolt breaks out in states seated by an Event 097 administration, the revolt calls Burn networks for the occupier inside the host, representing collaborators killed, exposed, or fled. Seated administrations in states that change hands to the revolt end through the ordinary recapture rule.

## Treaty of Tordesillas Restoration

### The relationship

A planned event in which Spain and Portugal pursue a restored partition of the world. Collaboration can make their conquests much easier to consolidate. Their expanding spheres can rely on local collaborator governments instead of direct occupation everywhere.

The Tordesillas event has no catalog row or reserved id yet. Its owner will also have to respect the existing Iberian content of Event 093 Portugal Wants Land and the Event 006 Iberian independence package. Event 097 does not depend on any of them.

### Contract

The Tordesillas owner has one entry point: Install through Event 097 on the External sphere route. It decides when one of its partners installs a government over a host inside that partner's sphere, and Event 097 performs the installation.

- The installation threshold on this route is 10 lower, within the Part 3 limits, because the sphere already prepared the ground.
- The route works whether or not Collaboration Governments is active, because the partner event owns the moment. Every other ordinary limit applies, including the network requirement, the one-per-original-tag rule, the reinstallation cooldown, and the Fallout gate.
- The route recorded in the registry is External sphere, so the Installed Administration lifecycle, the competing-orders milestone, Event 095, and achievements treat these governments like any other.
- The capitulation offer and the Seat the Prepared Government decision stay Evolution IV content and have no sphere exception.

The Tordesillas owner decides who its partners are and what their spheres contain. Its caller id is registered when that owner exists, not reserved in advance. Event 097 never names Spain or Portugal in its own logic.

## Event 052 Intel Leaked

Event 052 already reserves a connection to Event 097. When an Intel Leaked archive exposes agent registries or contact chains, foreign governments learn whom the target has recruited abroad.

Event 052 may call Burn networks for the 052 target's networks inside each named exploiter, at most three exploiters per 052 sequence. The target's collaborators abroad are exposed and arrested. This is the one Event 052 hook, and it keeps the global layer symmetrical because it only removes depth.

## Intelligence cluster role

Event 097 joins the Intelligence cluster as a Medium-severity optional member beside Event 039 and Event 052. Its role is the slow political infiltration that sits between Event 039's violent leadership crisis and Event 052's archive exposure.

| Member | Role in the cluster |
| --- | --- |
| Event 039 | Leadership murder, investigation, assassin networks |
| Event 052 | Archive exposure, counterintelligence, deception |
| Event 097 | Collaboration networks inside every country |

A cluster burst still counts as one pacing event. Event 097 applies its own firing, history row, repeatable handling, and Chaos. It skips within a burst when an application pass is already running, when fewer than two participants exist, or when the event is disabled. The skip reason appears in the cluster history through the established cluster log.

The cluster type is not changed by adding a repeatable member. The cluster runtime treats Event 097's global firing as having no actor.

### Building the Intelligence cluster

The Intelligence cluster is described in the catalog but has not been built in the runtime cluster system, and its numeric id differs between the catalog, the cluster documentation, and the Event 052 package. This specification does not fix a numeric id. The integration follows these rules:

- The cluster is built once, by whichever of Events 039, 052, or 097 is implemented first with its cluster integration, with every cluster surface the shared cluster system requires. The catalog id and the runtime id are reconciled in the same change through the workbook worker, and the catalog alignment handoff records the result.
- Event 097's member row is Medium severity. The shared severity floor means Event 097 joins cluster activations only from 200 Chaos, even though the event alone is available from Chaos level 1.
- The cluster is a Fire-Once cluster with repeatable members. A consumed cluster does not stop Event 097 from firing alone later.
- Event 039's own specification treats it as Fire-Once while its registration treats it as repeatable. That conflict belongs to Event 039 and must be settled before the shared cluster row is written.

The Intelligence cluster is built in the Event 097 tranche with all three member rows, because the brief makes Event 097 a member and the catalog already names the other two. The Event 039 type conflict must be settled with the user before that row is written. If that decision is not available, Event 097 ships without cluster membership and the implementation report lists the missing cluster as an open item.

## Event 063 Subject Independence

Event 063 is listed in the catalog as End Subject Status and named Subject Independence in game. Governments installed through Event 097 are subjects. When Event 063 frees one of them, the government enters the Abandoned stage from Part 3: it has lost its protector and its restoration pressure is at its highest. Its registry row stays in the registry, outside every live count, until the Abandoned stage ends. It then retires with an independence record and leaves a former-collaboration marker that Event 095 and achievements can read. Event 063 may read the installed-government record to give the moment its own text, but it does not need to.

## Fallout

The Fallout transition resets diplomatic memory, including collaboration, through its own system. Event 097 respects that reset and becomes unavailable once the transition begins. It never restores collaboration that Fallout removed.

Fallout's clean-world proof fails if any country pair still holds collaboration after its reset, so every Event 097 write, the shared write surface above included, checks the Fallout transition and Fallout active gates before it touches native collaboration.

Fallout resets a pair only when its collaboration trigger reads above zero, and the clean-world proof uses the same trigger. If that trigger reads zero for pairs where neither side occupies the other, Event 097 collaboration would survive the Fallout reset unnoticed. The promise that no Event 097 collaboration outlives the Fallout reset therefore holds only once this read is verified. It is a coverage question for the Fallout owner, who must verify the read and change the reset if needed. Event 097 does not patch Fallout. Event 097 records, flags, and registry history stay in place for achievements and the Event Details history, and live registry rows retire through the ordinary rules when Fallout changes subjects.
