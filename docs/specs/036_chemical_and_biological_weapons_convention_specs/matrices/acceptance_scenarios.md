# Acceptance scenarios

| ID | Setup | Action | Expected proof |
| --- | --- | --- | --- |
| `E36_A01` | Calm World, several ordinary countries, Event 036 unfired | Fire canonical event | One global setup, one History row, correct fire-once state, all eligible countries receive one posture receipt |
| `E36_A02` | Five human countries in multiplayer | Fire canonical event | Each human chooses independently, global setup is not duplicated, shared standing resolves after responses |
| `E36_A03` | Special nonhuman actor and ordinary countries | Fire event | Nonhuman actor excluded unless explicit compatibility provider exists |
| `E36_A04` | Human selects Full Ratification | Resolve opening | Full member registry, full posture modifier, no free technology or stockpile |
| `E36_A05` | Human selects Chemical Accession | Resolve opening | Chemical rights active, biological benefits and relief absent |
| `E36_A06` | Human selects Retaliation Reservation | Resolve opening | Protection and treaty rights active, offensive first-use policy blocked |
| `E36_A07` | Human selects Public Rejection | Resolve opening | Opponent actions visible, convention benefits absent |
| `E36_A08` | Human selects covert rejection | Resolve opening | Public state reads rejection, hidden preparation actions visible only to controller |
| `E36_A09` | Country has mixed existing Condemnation sources | Apply opening normalization | Only eligible source buckets fall once, action records and hidden evidence remain unchanged |
| `E36_A10` | Full member performs ordinary chemical military action | Register action | Physical effect and action record unchanged, chemical source uses posture multiplier |
| `E36_A11` | Chemical-only member performs biological action | Register action | Biological source remains normal and no chemical-only relief leaks |
| `E36_A12` | Reservation member retaliates after valid hostile record | Register action | Retaliation multiplier applies and action remains attributed |
| `E36_A13` | Reservation member initiates chemical use | Register action | Normal or floored source value, public treaty-breach reaction, no reservation relief |
| `E36_A14` | Full member creates catastrophic biological outbreak | Register action | Final biological source stays at or above `0.70` of normal |
| `E36_A15` | Evolution III member uses thermonuclear weapon | Register action | Condemnation multiplier remains `1.00`, fallout, deaths, contamination, and Chaos remain normal |
| `E36_A16` | Baseline convention with eligible agendas | Advance scheduler | One agenda selected, one sponsor, no random-event pacing transaction |
| `E36_A17` | Treaty reaches ordinary quorum | Resolve vote | Treaty applies only to ratifiers and compatible reservations |
| `E36_A18` | Treaty fails decisively | Resolve vote | Failure memory and cooldown recorded, no false benefits or generic Chaos |
| `E36_A19` | Evolution I disabled at 250 Chaos | Advance time | Evolution I does not record or unlock first-use content, baseline conferences continue |
| `E36_A20` | Event fires first at 450 Chaos | Resolve opening and advance | Evolution I then Evolution II activate on separate accelerated ordered schedules and separate logs |
| `E36_A21` | Event fires first at 650 Chaos | Resolve opening and advance | All three evolutions activate in order, no same-transaction stacking, no Chaos from activation |
| `E36_A22` | First-use treaty adopted | Resolve treaty | First-use policy updates only for ratifiers, one-time `+5` Chaos milestone applies |
| `E36_A23` | Strategic doctrine treaty adopted | Complete doctrine mission | Integration state changes only when capability and readiness pass |
| `E36_A24` | Three unique registered project candidates | Activate program | Uniform one-third selection across unique IDs |
| `E36_A25` | Duplicate provider registration attempt | Build pool | Duplicate ID rejected or deduplicated without added weight |
| `E36_A26` | No eligible project exists | Activate program | Program becomes Dormant, no guessed selection or missing key |
| `E36_A27` | Dormant program receives new provider callback | Register eligible project | Wake-up rebuilds pool and selects project after administrative interval |
| `E36_A28` | Small eligible participant with 12 factories | Complete affordable contribution | At least minimum meaningful progress applies and receipt records exact costs |
| `E36_A29` | Major participant with large surplus | Complete contribution | Progress respects per-action and 90-day caps, project cannot finish in one unbounded action |
| `E36_A30` | Country reloads during contribution mission | Save and reload | One mission resumes, one receipt applies, no duplicated cost or progress |
| `E36_A31` | Active selected project becomes normally available | Run source owner normal unlock | Immediate cancellation, progress discarded, no project unlock, pool rebuild queued |
| `E36_A32` | Normal-availability callback omitted in test provider | Advance fail-safe heartbeat | Fail-safe detects availability within 30 days and reports provider defect |
| `E36_A33` | Project reaches target while still unavailable normally | Complete atomically | Only valid active contributors receive prerequisite, no source event state changes |
| `E36_A34` | Participant withdraws before completion | Complete project | Historical contribution preserved, country receives no unlock |
| `E36_A35` | Non-contributor remains signatory | Complete project | Country receives no unlock |
| `E36_A36` | Recipient already owns prerequisite | Complete project | No duplicate grant, recipient skip reason recorded |
| `E36_A37` | Program loses quorum | Recalculate membership | Project pauses, progress preserved, contribution decisions hidden |
| `E36_A38` | Paused program regains quorum | Recalculate membership | Same project resumes with preserved progress unless normal availability occurred |
| `E36_A39` | Charter repealed during active project | Resolve repeal | Project cancels, progress discarded, spent costs retained |
| `E36_A40` | Covert opponent has valid hidden program evidence | Complete inspection disclosure | Public exposure, cover-up source, hidden decisions close, no invented capability |
| `E36_A41` | Air Cleanliness Treaty member also joins Event 036 | Use chemical weapon | Air Cleanliness betrayal rules still apply independently |
| `E36_A42` | Member CBRN attack causes deaths and contamination | Register action | Deaths and Air Cleanliness update once, Event 036 only changes eligible Condemnation conversion |
| `E36_A43` | Country changes posture after an earlier action | Recalculate current state | Earlier action retains its original treaty snapshot and source value |
| `E36_A44` | Convention falls from Dominant to Provisional twice in same generation | Process standing | Collapse relief applies once, no threshold farming |
| `E36_A45` | Event launched through approved Diplomacy cluster | Resolve cluster | Event fires once, cluster counts one pacing event, member severity and History stay correct |
| `E36_A46` | Event Details opened before and after evolutions | Inspect views | Correct premise, Chaos level, enabled evolutions, no raw multipliers or hidden project pool |
| `E36_A47` | All seven achievement routes tested | Trigger and violate conditions | Each unlock uses exact receipts and disqualifiers, no false positive from current modifiers |
| `E36_A48` | Assets wired | Inspect every consumer | No missing texture, wrong size, opaque icon square, duplicate icon type, or unused authorized asset |
| `E36_A49` | Workbook updated | Export CSVs | Event 036 row, evolution details, cluster membership, status, type, Chaos level, and severity match in-game wording |
| `E36_A50` | Final source state | Run completion audit | No missing accepted surface, placeholder, guessed provider, unresolved addendum, or unreported simplification |
