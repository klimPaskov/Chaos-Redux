# Industrial Boom specification, part 4: Regions, legacy, and repeatability

## Industrial Regions

Industrial Regions are the few states that carry the boom's physical development.
They give bombing, disasters, occupation and permanent conversion a place on the map without asking the player to track every industrial state.

| Economy | Regions |
| --- | ---: |
| Small player country | 1 |
| Medium industrial base | 2 |
| Large major | 3 |

Three is the hard cap.
Evolution III spread states attach to a region and never become extra region slots (part 5).

### Selection

The opening ranks owned, controlled, core, passable, populated states with civilian or military factories.
The ranking prefers industrial share, infrastructure, rail connection to the capital and resources or ports, and lowers states on an active front, isolated holdings, and states already holding a strong Event 34 legacy.
The strongest state is not always chosen when it is exposed to imminent loss.

The implemented entry picks one random owned, controlled, populated state with any factory or dockyard and freezes it as the Event 35 inherited region.
The ranked selection above replaces that pick and becomes the primary region of the snapshot (part 6).

## Projects

Each region holds at most one project at a time.
A project has a profile, a stage and two flags: protected and, under Evolution II, Miracle.

### Profiles

| Profile | While active | Legacy at landing |
| --- | --- | --- |
| Production Practices | Faster efficiency growth, lower Finance and maintenance drift | National efficiency-growth and line-conversion modifier for several years, no buildings |
| Rail and Supply Integration | Lower Supply and materials drift, protects against transport shocks | Infrastructure and railway levels in the region, logistics modifier |
| Factory Conversion | Faster construction and line setup | Factory levels or a building slot in the region, within the legacy budget |

Earlier drafts listed Industrial Repair Network and Resource Efficiency as profiles.
Repair is covered by region protection, and resource efficiency is folded into Rail and Supply Integration, because a project that invents oil, rubber or tungsten in every country fails plausibility.

### Stages

| Stage | Meaning | Progress rule |
| --- | --- | --- |
| Building | Work is under way | Advances fastest in the Sustainable band, faster while running hot, pauses in Dangerous or when the region is damaged or occupied |
| Integrating | The works are connected to national production | Advances only below 70, reverses one step on a severe unabsorbed shock |
| Secured | The project has earned its legacy | Converts only at a controlled or rough landing |

Stage durations are constants: a baseline Building stage of about 90 days and Integrating of about 60 days.
The region tooltip shows the stage, protection and the main thing slowing progress, never a progress formula.
A Secured project is valuable enough that a player may cool the economy to protect it.

### Protection

A protected region absorbs most of its next local shock (bombing, disaster damage, rail or port loss) and keeps its project progress, then loses its protection.
Protection is a yes-or-no state, not a level ladder.

## Control changes

- **Occupation.** The project pauses, protection is lost, Overheating takes a shock scaled by the region's industrial share and stage, and the landing mission ignores the region until it is retaken. Retaking it within 180 days resumes the project at its previous stage; later, the project is cancelled.
- **Permanent loss, release or annexation of the state.** The project is cancelled without legacy, the original owner takes a shock, and the new owner inherits nothing from Event 34.
- **Civil war.** The boom stays with the country that keeps the Event 34 ledger, and regions on the other side count as lost.
- **No valid region left.** The boom continues without projects; a controlled landing then requires falling below 40 alone, and the outcome is rough unless a supplier contract applies.

No mission ever requires a state the country cannot control.

## Legacy

Legacy is granted only at a controlled or rough landing, never earlier and never after a crash.

| Outcome | Legacy |
| --- | --- |
| Controlled | Every Secured project converts in full; Integrating projects convert at half strength; a held reserve adds one year to timed legacy modifiers |
| Rough | Secured projects convert at half strength; nothing else converts |
| Forced | Nothing converts |
| Crash | Nothing converts; project stages enter Event 35 as regional inputs |

After any landing the country receives a reconversion modifier for 180 days that briefly lowers output while production returns to normal.

### Budgets

Permanent buildings from Event 34 are capped.

- **Country budget.** Total factory levels and building slots granted by Event 34 across the campaign cannot exceed a constant share of the factories the country had at its first boom. Once spent, Factory Conversion converts to construction and conversion-speed modifiers instead.
- **State cap.** A state can receive one strong Event 34 legacy (factories, slots or a full infrastructure package) per campaign. Later projects in that state give timed modifiers only.

These rules keep repeat firings valuable without an endless factory engine.

## Exhaustion

Rough and forced landings apply industrial exhaustion, a country modifier that lowers output and construction for 1 year (rough) or 2 years (forced).
A region whose project was abandoned or cancelled receives unfinished works for 1 year, and a later boom treats it as a weaker project candidate during that time.
Both are visible modifiers; neither keeps a hidden second Overheating.

## Repeat firings

| History | Effect on a later boom |
| --- | --- |
| Earlier controlled landing | Opening state shortened by 30 days, landing mission shortened by 30 days, smaller raw-capacity potential as the budget is used |
| Earlier rough or forced landing | Starts with any remaining exhaustion |
| Earlier crash | Starting Overheating +10 per crash up to +20, lower selection weight for 2 years |

The persistent country record holds the number of booms, landings and crashes, the highest evolution reached and the consumed legacy budget.
Each state holds its strong-legacy receipt.
The implemented collapse snapshot already passes `industrial_boom_completed_count` to Event 35 as repeat history.

## Anti-farming controls

| Risk | Control |
| --- | --- |
| Designate and cancel for relief | Abandonment relief only for projects past the first 30 days; unfinished works blocks reuse of the state for a year |
| Repeated protection stacking | One protection per region; 90-day renewal after it is spent |
| Early landing for a small reward | Opening state blocks the landing mission; legacy requires Secured or Integrating projects |
| Endless factories | Country budget and state cap |
| Occupation and reconquest duplication | State legacy receipt persists through control changes |
| Release, puppet or tag switch reset | Country record and state receipts follow the stable tag and state |
| Positive package surviving a crash | Snapshot freezes before the package is removed; Event 35 applies only after removal |
| Two booms in one country | Active, frozen and pending-delivery flags block selection |

## Acceptance

- A small player country can complete one meaningful project.
- A major never manages more than three regions.
- State loss matters in proportion to the region's importance.
- Retaking a region recovers its progress without duplicating rewards.
- Repeat firings stay useful after the raw-capacity budget is spent.
- Event 35 receives enough regional state to continue the crisis coherently.
