# Engine proof gates and design decisions

This package does not certify engine support. The supplied archive contains planning rules, mechanics, helper descriptions, catalog snapshots, and agent profiles. It does not contain the installed game documentation or a runnable game.

## Critical gates

| Gate | Required proof | Why it matters | Forbidden shortcut |
| --- | --- | --- | --- |
| E79-G01 Actual puppet relationship | A valid independent sponsor can make the target its direct normal puppet, with a verified ordinary puppet autonomy state where applicable | The central victory result | Replacing puppeting with opinion, faction membership, or a spirit |
| E79-G02 Player subject as winner | Test an already-subject player as direct overlord of a new target and verify hierarchy behavior | The user's universal player participation rule includes this case | Excluding the player, giving its overlord the reward, or freeing it without approval |
| E79-G03 Ancestry cycle | Test or explicitly reject a target that is already an ancestor of a participating player in the subject hierarchy | Puppeting one's own overlord can require an impossible cycle under a tree-based hierarchy | Silently rewriting the subject tree or treating a failed effect as victory |
| E79-G04 Faction member and leader | A target in another faction, including a minor faction leader, can enter a legal subject relationship without deleting unrelated countries or accidentally dissolving the faction | The user did not require factionless targets | Blanket faction exclusion inherited from legacy code |
| E79-G05 Third-party wars | Preserve unrelated wars and handle incompatible alignments through a verified sequence | The user did not require a peaceful target | Broad `end_wars = yes` cleanup |
| E79-G06 Political restoration | Native puppet/autonomy effects plus intended current leader, ruling group, and popularity remain consistent | The autonomy reference warns about political overwrites | Restoring the opening government over a legitimate later change |
| E79-G07 Civilian factory reservation | Donor usable construction capacity genuinely falls by the promised amount and returns at release | Economic payment must be real | Paying only political power while pretending factories were reserved |
| E79-G08 Project work and aftermath | Partial funded work, valid building placement, completed output, and post-race completion are persistent and nonduplicating | Investment must create real work and output | An indefinite national spirit presented as a completed factory |
| E79-G09 Equipment escrow | Concrete donor stockpile is debited, held, delivered or refunded once, with type and variant conservation | Prevents free equipment and wrong-variant debits | Checking aggregate stock then removing an unrelated type |
| E79-G10 Optional data providers | Bilateral trade, previous political influence, military cooperation, and intelligence presence are read from documented values | Seed reasons must be factual | Fake bilateral trade inferred from a shared faction |
| E79-G11 Parallel persistence | Several targets, scores, receipts, and callbacks survive save/load independently | The Great Game requires actual independent races | One mutable global target reused by every decision |
| E79-G12 Local UI isolation | Each player's selected view cannot mutate world state or another player's action target | Multiplayer correctness | Shared global selected-target variable |
| E79-G13 No-DLC play | Full baseline contest, AI, progression, interference, investment, and actual puppet ending work in the supported base configuration | Core premise cannot depend on spies | Disabling the entire event when a DLC is absent |
| E79-G14 Discount boundaries | Supported administration quotes agree with debits. Direct material transfers remain conserved. Factory commitment policy is explicit | Shared cost integration and honest tooltips | Half-price donor weapons with full-price recipient creation |

## The ancestry decision cannot be hidden

If the engine forbids a subject from being an overlord or forbids a new hierarchy containing the target as the winner's ancestor, the original universal participant promise cannot be met by an ordinary puppet effect in that case. This is a release-blocking design conflict, not a reason to fake implementation success.

The smallest possible amendment might be a narrowly defined target restriction for hierarchy-cycle cases. Another amendment could explicitly transform the existing hierarchy at victory. Neither is accepted by this package. The implementation owner must report the observed limitation and obtain an explicit decision before changing the user's rule.

## Evidence hierarchy

Read current installed effect, trigger, modifier, GUI, and autonomy definitions. Compare with the repository's offline wiki and the actual working project code. Then prove the narrow operation in the game's runtime, including save and reload where state persists. A source declaration proves intent, not live behavior.

The fetched repository autonomy page establishes that default puppet selection and political overwrite behavior need attention. It does not prove nested subjects or every war/faction combination. The legacy Event 79 proves that the old code called a puppet effect. It does not prove that its delayed, global-state implementation is correct.

## Required source completion

Before implementation, fully read the relevant AGENTS-required offline core wiki pages and installed vanilla documentation. The current package audit explicitly lists which additional sources were not fully read. Read the universal cost helper's full argument contract, current MTTH source, existing Event 79 localization/news/category definitions, and the canonical asset reference materials.

No unresolved gate may be replaced by an invented Clausewitz command or a plausible-looking pseudocode block. Keep proposed helper names separate from installed effect names.
