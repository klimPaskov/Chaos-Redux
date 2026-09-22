# Planning-package verification

The final package is checked by the included validate_package.py tool and by a ZIP integrity check.
The checks are structural and local.
They do not launch HOI4, spawn project subagents, perform probability analysis, generate runtime art or establish gameplay balance.

| Check | Result |
| --- | --- |
| Complete supplied-text reading ledger | 42 of 42 source files with contiguous logged packet coverage |
| Subagent profile inventory | 20 profiles, no claim of independent execution |
| Main focus groups | 65 unique groups with the expected lane coverage |
| Action register | D01 through D42 present exactly once |
| Spendable cost-type limit | Every action has at most four cost types |
| Diplomatic response windows | Every offer specifies 30 days separately from longer work |
| Extension payment consistency | 50 Political Power and 250 support equipment, manpower is only a gate |
| Asset planning inventory | 155 unique rows with every decision and achievement covered |
| Codex goal prompt | 3,924 characters excluding the trailing newline |
| Internal Markdown links | Resolved against included files |
| SHA-256 inventory | Validated with the included manifest checker |
| ZIP archive | CRC integrity checked after creation |
| Installer | Documentation-only copy tested in an empty temporary repository |

The asset count includes group briefs and variant families.
It is not the number of produced game textures.
No such textures were produced here.
The full final focus-node and texture counts are implementation outputs.

The unresolved game-facing checks remain in 072_parent_review_and_blockers.md and 072_validation_matrix.md.
Do not turn this structural verification record into a gameplay-completion claim.
