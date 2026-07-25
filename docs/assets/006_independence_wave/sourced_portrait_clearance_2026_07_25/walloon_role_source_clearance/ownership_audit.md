# Exact portrait-owner audit

The audit searched exact subject names and likely character keys in these five roots: current Chaos Redux, vanilla HOI4, Kaiserreich `1521695605`, reference `2265420196`, and reference `1458561226`.

The searched paths were `common/characters`, `history/countries`, `gfx/leaders`, `interface`, and `localisation/english`. Common-name pools and unrelated prose were excluded from the ownership decision so surname fragments could not create false positives.

## Results

| Candidate | Chaos Redux | Vanilla | Kaiserreich 1521695605 | Reference 2265420196 | Reference 1458561226 | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| Fernand Jacquet | NO_MATCH | NO_MATCH | NO_MATCH | NO_MATCH | NO_MATCH | Safe additive candidate, subject to source-rights review |
| Charles de Broqueville | NO_MATCH | NO_MATCH | NO_MATCH | NO_MATCH | NO_MATCH | Safe additive candidate |
| Albert Devèze | NO_MATCH | ACTIVE `BEL_albert_deveze` in `common/characters/BEL.txt` and `history/countries/BEL - Belgium.txt` | NO_MATCH | NO_MATCH | NO_MATCH | Blocked by vanilla owner |
| Jules Destrée | ACTIVE AFX owner | NO_MATCH in audited vanilla owner paths | NO_MATCH in audited owner paths | NO_MATCH in audited owner paths | NO_MATCH in audited owner paths | Blocked by current Chaos Redux owner |
| Gérard Leman | NO_MATCH | NO_MATCH | NO_MATCH | NO_MATCH | NO_MATCH | Rejected because deceased in 1920 |
| Henri Denis | NO_MATCH in current package audit | NO_MATCH | ACTIVE Kaiserreich owner per parent audit | NO_MATCH | NO_MATCH | Blocked by Kaiserreich owner |

## Command shape

The search used case-insensitive word-boundary matching for each subject and key variant and was run from each root with `rg` restricted to the five ownership paths above. No fuzzy surname-only hit was treated as an owner.

## Interpretation

No additive transfer is required for Jacquet or de Broqueville. Devèze cannot be selected without an explicit safe transfer decision, and Destrée cannot be cloned because Chaos Redux already assigns the identity to the AFX civic character. Historical viability was checked separately from ownership; a no-match does not by itself prove that a candidate is appropriate for every role.
