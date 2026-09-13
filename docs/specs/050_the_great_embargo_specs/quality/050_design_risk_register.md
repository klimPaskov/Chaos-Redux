# Event 050 design risk register

| Risk | Severity | Failure pattern | Required mitigation | Acceptance evidence |
| --- | --- | --- | --- | --- |
| Fake bilateral trade precision | High | UI claims exact lost trade that script cannot observe | Use supported proxies, qualitative exposure, and bounded modifiers | Tooltips and Event Details contain no unsupported percentages |
| Dependence becomes a second meter | Medium | Player must track Pressure plus another custom score | Keep dependence internal and show one urgent exposure label | Only Embargo Pressure is persistent and numeric |
| Raw coalition count dominates | High | Ten irrelevant minors outweigh one oil supplier | Weight practical contribution by resources, routes, shipping, finance, and power | Coalition scenario matrix shows correct ordering |
| Evolution II ledger collision | Critical | One target overwrites another's Pressure, routes, or cleanup | Use sequence-scoped ledgers and bounded active registry | Three-crisis cleanup scenario passes |
| Whole-world scan | High | Daily or monthly processing iterates every country | Process active crises and stored participants | Source audit shows bounded registered loops |
| Condemnation duplication | High | Event 50 applies a second copy of existing sanction state or clears it | Keep source ownership separate and combine effects safely | Condemnation overlap scenario passes |
| Native DLC dependency | High | Event has no effect without native embargo feature | Maintain event-owned baseline and add native mechanics only as reinforcement | DLC-off acceptance test remains playable |
| Unsupported agreement cancellation | High | Existing lend-lease or research sharing is claimed removed without engine support | Block new support where supported and use event pressure for the rest | Vanilla and wiki evidence matches final behavior |
| Decision clutter | Medium | Six responses, targets, and missions appear at once | Phase actions, selected-target flow, five-action cap, one mission cap | Category audit at every stage |
| Political power shop | Medium | Every response is a PP purchase | Use varied economic, logistics, stockpile, route, and obligation costs | Cost matrix and decision audit |
| Self-sufficiency farming | High | Repeat firings grant unlimited resources or factories | Use project ceilings, state receipts, and bounded upgrades | Repeat-firing scenario shows no infinite growth |
| Defiance dominates | High | Strong temporary bonuses have weak aftermath | Scale by regime capacity, raise coalition resolve, apply exhaustion | AI and balance scenarios compare against other routes |
| Resource Seizure suicide | Critical | AI attacks a stronger faction only because Pressure is high | Require military, supply, reachability, resource value, and retaliation checks | Unsafe seizure scenario gives zero or near-zero AI willingness |
| Smuggling becomes useless under Evolution I | High | Secondary sanctions remove the evasion route | Preserve high-value success paths and make enforcement costly | Baseline and evolved probability comparison |
| Popup spam | Medium | Every member reports every review | Direct events only for important changes and human choices | Twelve-month progression has bounded reports |
| Human choice deadlock | Medium | Multiplayer review waits forever for one event | Timed choice with visible continuation default | Multiplayer intermediary scenario |
| Famine and death duplication | Critical | Embargo applies direct deaths or creates famine without validation | Use owner systems and validated adapters only | Famine scenario and source audit |
| Cluster target pileup | High | Several Negative Economy events hit one country without accepted rule | Use target collision and severity checks | Cluster acceptance scenario |
| Catalog mismatch | Medium | Event row and cluster row remain contradictory | Update authoritative XLSX only after verified implementation facts | Exported CSVs match workbook and final localisation |
| Crisis state survives resolution | Critical | Decisions, modifiers, routes, or targets remain | Idempotent cleanup and per-ledger removal | Full cleanup and repeat-firing scenarios |
| Working labels become final text | Medium | Planning prose is pasted into localisation | Localisation audit writes final in-world wording | No placeholder or planning language in runtime text |
