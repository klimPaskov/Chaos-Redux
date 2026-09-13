# Event 065 Probability Scenario Matrix

## Required workflow

The auditor must begin with `hoi4.probability_inspect` on the actual generated Event 65 pool and dispatcher.

Use `hoi4.probability_evaluate` for exact scenario results.

Use `hoi4.probability_sweep` for thresholds, class-share sensitivity, and high-saturation behavior.

Use `hoi4.probability_compare` after the owner applies any patch and for direct-versus-cluster parity.

Use `hoi4.probability_sequence` only for the declared multi-slot without-replacement scenarios when the complete pool and state transition are supplied.

Use `hoi4.probability_render` for the full-pool class matrix, threshold sweep, dispatcher comparison, and unresolved high-saturation view.

Use seeded simulation only when the exact tool cannot represent an implementation detail.

A simulated result must be labeled sampled and cannot replace exact evidence where exact evaluation is available.

## Core equations

For one slot with eligible source set `E`:

`P(i) = w(i) / sum(w(j) for j in E)`

After source `i` is accepted:

`E_next = E - {i}`

Baseline and Evolution I use `w(i) = 100` for every eligible source.

Evolution II uses `100` for ordinary and `125` for featured.

Evolution III uses `100` for ordinary and `150` for featured.

Several featured reasons do not multiply.

## Dominance and starvation limits

- Maximum Evolution II per-entry featured ratio: `1.25`
- Maximum Evolution III per-entry featured ratio: `1.50`
- Evolution II ordinary mass floor: at least `70%` of its uniform-class mass
- Evolution III ordinary mass floor: at least `55%` of its uniform-class mass
- Every eligible entry must have positive probability
- Every excluded entry must have zero probability
- A dispatcher must match the equivalent flat weighted pool
- Collision and saturation handling must not create source-order bias

## Named scenarios

| ID | Scenario | Declared state | Weight input | Required result | Tool route |
| --- | --- | --- | --- | --- | --- |
| P01 | Baseline full pool | All loaded registry entries eligible and no leader exclusions. | All entries weight 100. | Exact uniform distribution. Every entry probability is `1/N`. | Evaluate |
| P02 | Evolution I full pool | All loaded registry entries eligible. | All entries weight 100. | Exact uniform distribution. Two slots sample without replacement. | Evaluate |
| P03 | Evolution II full pool | Ordinary and featured entries eligible. | Ordinary 100, featured 125. | Per-entry ratio is 1.25. Ordinary mass meets floor. | Evaluate and render |
| P04 | Evolution III full pool | Ordinary and featured entries eligible. | Ordinary 100, featured 150. | Per-entry ratio is 1.50. Ordinary mass meets floor. | Evaluate and render |
| P05 | Several featured reasons | One trait carries powerful, rare, extreme, and Chaos Redux reasons. | One featured weight only. | No multiplier stacking. | Inspect and evaluate |
| P06 | Existing ordinary trait removed | One ordinary source is already owned. | Owned source excluded. | Remaining probabilities renormalize exactly. | Evaluate |
| P07 | Existing featured trait removed | One featured source is already owned. | Owned source excluded. | Remaining probabilities renormalize exactly. | Evaluate |
| P08 | Prior ledger exclusion | A source is absent visibly but present in Event 65 ledger. | Ledger source excluded. | No probability remains for that source. | Evaluate |
| P09 | Same-firing exclusion | First slot accepts one source. | Accepted source removed for later slots. | Later slot distribution is exact over remaining entries. | Sequence evaluation |
| P10 | One ordinary remains | Every source except one ordinary entry is excluded. | One ordinary entry eligible. | Remaining entry has probability 1. | Evaluate |
| P11 | One featured remains | Every source except one featured entry is excluded. | One featured entry eligible. | Remaining entry has probability 1. | Evaluate |
| P12 | Mixed near saturation | Two ordinary and two featured entries remain at Evolution III. | Weights 100, 100, 150, 150. | Each probability matches weight divided by 500. | Evaluate |
| P13 | No-DLC profile | Use generated no-DLC manifest. | Profile-specific active entries only. | Every active source has positive probability and missing definitions have zero by explicit gate. | Inspect and evaluate |
| P14 | Full-DLC profile | Use generated full-DLC manifest. | All final loaded entries active. | Class totals and ratios match manifest. | Inspect and evaluate |
| P15 | Chaos Redux additions | Add several test Chaos Redux traits. | Each new entry featured once through source origin. | No old index or probability is altered beyond normalized pool expansion. | Compare |
| P16 | Load-order override | One trait ID has vanilla and Chaos Redux definitions. | Final ID appears once. | Probability contains one entry at the final loaded weight class. | Inspect and evaluate |
| P17 | Duplicate runtime branch | Inject the same source ID twice in a test output. | Check mode should fail. | Probability audit reports duplicate normalization distortion and blocks. | Inspect |
| P18 | Hierarchical dispatcher | Use production generated groups. | Group and entry totals declared. | Final per-entry probabilities equal flat reference distribution. | Compare and render |
| P19 | Direct path | Invoke Event 65 directly from declared state. | Production stage pool. | Distribution matches manifest. | Inspect and evaluate |
| P20 | Cluster path | Invoke Event 65 through Randomizations from identical state. | Same production stage pool. | Distribution matches direct path exactly. | Compare |
| P21 | Evolution threshold sweep | Sweep raw Chaos across 199, 200, 399, 400, 599, and 600 with settings declared. | Stage weights change only at accepted manifestation boundaries. | No off-by-one or rank reversal outside intended featured shift. | Sweep and render |
| P22 | Evolution disabled sweep | Repeat threshold sweep with each Evolution disabled in turn. | Highest enabled manifested or available form applies. | Disabled stage weights never appear. | Sweep |
| P23 | Ordinary mass sensitivity | Vary featured class share from small to large declared profiles. | Use 100, 125, and 150 weights. | Mass floors hold for supported real profiles. Unsupported synthetic failures are documented. | Sweep and render |
| P24 | Collision implementation | Use the actual runtime exclusion method. | Declare a small exact pool with owned and unowned entries. | Conditional result matches direct exact calculation. | Inspect, evaluate, compare |
| P25 | High-saturation fallback | Use the actual runtime fallback with most entries excluded. | Declare every remaining entry and weight. | No remaining entry is starved or biased by fallback order. | Evaluate and render |
| P26 | Missing localisation | One valid source uses fallback name mapping. | Gameplay weight unchanged. | Presentation fallback does not alter selection probability. | Inspect |
| P27 | Technical exclusion | One source has an evidence-backed technical exclusion. | Source absent from active manifest. | All included entries renormalize exactly and report counts agree. | Inspect and evaluate |
| P28 | Registry order change | Regenerate after source ordering changes without ID changes. | Stable index map retained. | Probability by source ID remains unchanged. | Compare |
| P29 | New ordinary source | Append one new ordinary trait. | One new weight 100 entry. | Existing per-entry ratios stay correct after normalization. | Compare |
| P30 | New featured source | Append one new featured trait. | One new featured entry. | Existing per-entry ratios stay correct after normalization. | Compare |

## Required audit output

The audit report must include:

- inspected source paths
- registry version and checksum
- content profile
- total active entries
- ordinary and featured counts
- exact class probability mass
- per-entry weight ratio
- every scenario result
- artifact references
- unresolved or unrepresentable behavior
- comparison after any patch
- final status of pass, fail, blocked, or needs user review

The auditor remains read-only.

Balance changes belong to the main implementation agent and require a repeated compare pass.
