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
| Is an installed government | country | The country was installed through Event 097 and is still registered |
| Installed government record | country | Installer, original tag, route, installation date, Installed Administration stage |
| Restoration pressure band | country | Low, Rising, or High, from the hidden restoration inputs below |
| Evolution states | global | Which Event 097 evolutions are active |

### Write surface

| Action | Caller proof | Bounded effect |
| --- | --- | --- |
| Burn networks | Caller id, beneficiary, host, reason | Reduces the beneficiary's collaboration inside the host by at most one base layer, never below zero, once per caller sequence |
| Add network depth | Caller id, host, reason | Adds at most half a base layer inside one host for every participant beneficiary, once per caller sequence |
| Register an external sphere | Caller id, sphere owner, list of host countries or states | Lets the sphere owner use the reduced installation threshold inside the sphere (below) |
| Retire an installed government | Caller id, government, route | Ends the registry row with a restoration or liberation record and applies the matching Chaos reversal |
| Install through Event 097 | Caller id, installer, host, route, sphere proof | Calls the shared installation helper with the caller's route recorded, subject to every ordinary limit |

Every write requires the caller to supply proof that matches its own state. A call with missing or contradictory proof fails without changing anything. Event 097 owns every result.

## Event 095 Occupation Revolt

### The relationship

Collaboration makes occupied populations easier to govern. Occupation Revolt represents national resistance trying to overthrow foreign rule. A government installed through Event 097 can become the target of a national restoration uprising if enough opposition survives. Event 095 owns the uprising itself. Event 097 owns the record of who was installed and how much opposition survived.

Event 095 is marked for rework and has no specification. In its current form it returns enemy-controlled cores to a random government in exile and raises revolt divisions, without reading collaboration, compliance, or resistance. The contract below is what Event 097 offers. The Event 095 rework decides how to use it.

### Restoration pressure

Every government installed through Event 097 carries hidden restoration inputs. They combine into one qualitative band that Event 095 reads.

| Input | Direction |
| --- | --- |
| The original country still exists as a government in exile | Strongly raises pressure |
| The original country chartered a government in exile before capitulating | Raises pressure |
| The Installed Administration stage is Contested | Raises pressure |
| The Installed Administration stage is Abandoned | Raises pressure to the highest band |
| The installer is at war and past 40 percent surrender progress | Raises pressure |
| Years since installation in the Entrenched stage | Lowers pressure over time, never to nothing while the government in exile exists |
| The installed government took Loyalty Commissions in the last year | Lowers pressure |

The band, not the inputs, is public. The player in the original country sees it as a line in its exile reports, worded as the mood in the occupied homeland.

### What Event 095 can do with it

When the Event 095 rework exists, it can treat a High band as the condition that enough opposition survives, choose the installed government as the target of its national restoration uprising, and call the Retire action when the uprising restores the original country. Event 097 then applies its reversal Chaos and retires the registry row.

### What Event 095 changes in Event 097

When an Event 095 revolt breaks out in states seated by an Event 097 administration, the revolt calls Burn networks for the occupier inside the host, representing collaborators killed, exposed, or fled. Seated administrations in states that change hands to the revolt end through the ordinary recapture rule.

## Treaty of Tordesillas Restoration

### The relationship

A planned event in which Spain and Portugal pursue a restored partition of the world. Collaboration can make their conquests much easier to consolidate. Their expanding spheres can rely on local collaborator governments instead of direct occupation everywhere.

The Tordesillas event has no catalog row or reserved id yet. Its owner will also have to respect the existing Iberian content of Event 093 Portugal Wants Land and the Event 006 Iberian independence package. Event 097 does not depend on any of them.

### Contract

When the Tordesillas owner exists, it registers each partner's sphere through Register an external sphere. Inside a registered sphere, for that partner only:

- the installation threshold falls by 10, within the Part 3 limits
- the Prepared Government offer and the Seat the Prepared Government decision are available from Administrations in Waiting onward instead of only from Collaboration Governments
- the route recorded in the registry is External sphere, so the competing-orders milestone and achievements still count these governments correctly

The Tordesillas owner decides who its partners are and what the sphere contains. Event 097 never creates a sphere, never names Spain or Portugal in its own logic, and never changes behavior while no sphere is registered.

## Event 052 Intel Leaked

Event 052 already reserves a connection to Event 097. When an Intel Leaked archive exposes agent registries or contact chains, foreign governments learn whom the target has recruited abroad.

- Event 052 may call Burn networks for the 052 target's networks inside each named exploiter, at most three exploiters per 052 sequence. The target's collaborators abroad are exposed and arrested.
- When Event 052 and Event 097 fire in the same Intelligence cluster burst, the 052 target becomes the most penetrated government in the world: the cluster coordinator calls Add network depth inside the 052 target once, after the Event 097 application pass. Foreign services use the leaked files to find which officials can be turned.

The second hook is a cluster combination owned by the cluster runtime context and does not need a separate cluster Chaos source, because each member keeps its own.

## Event 039 Murder Mystery

When Event 039 and Event 097 fire in the same Intelligence cluster burst, the country thrown into the Event 039 succession crisis receives Add network depth once after the Event 097 application pass. A divided successor government invites foreign patrons, and each faction looks abroad for protection. The hook does not touch Event 039's investigation, cult, or terminal content.

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
- Event 097's member row is Medium severity. The shared severity floor means Event 097 joins cluster activations only from 200 Chaos, even though the event alone is available from Chaos level 1. This fits the role, because the cluster combinations in this part matter once networks run deeper.
- The cluster is a Fire-Once cluster with repeatable members. A consumed cluster does not stop Event 097 from firing alone later.
- Event 039's own specification treats it as Fire-Once while its registration treats it as repeatable. That conflict belongs to Event 039 and must be settled before the shared cluster row is written.

If the Intelligence cluster is not built in the same tranche as Event 097, Event 097 ships without cluster membership, the two cluster hooks in this part stay dormant, and the implementation report lists the missing cluster as an open item.

## Event 063 Subjects Break Free

Governments installed through Event 097 are subjects. When Event 063 frees one of them, Event 097 retires its registry row with an independence record, removes the Installed Administration spirit, and leaves a former-collaboration marker that Event 095 and achievements can read. Event 063 may read the installed-government record to give the moment its own text, but it does not need to.

## Fallout

The Fallout transition resets diplomatic memory, including collaboration, through its own system. Event 097 respects that reset and becomes unavailable once the transition begins. It never restores collaboration that Fallout removed.

Fallout's clean-world proof fails if any country pair still holds collaboration after its reset, so every Event 097 write, the shared write surface above included, checks the Fallout transition and Fallout active gates before it touches native collaboration. Event 097 records, flags, and registry history stay in place for achievements and the Event Details history, and live registry rows retire through the ordinary rules when Fallout changes subjects.
