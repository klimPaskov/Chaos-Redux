# Co-located custody receipt skill handoff

Disposition: implemented as reusable skill guidance; gameplay and live acceptance remain with the owning implementation.

Changed `.agents/skills/chaos-redux-state-ledgers/SKILL.md` by adding one `Co-located custody receipts` section after reception accounting. The rule derives a closure or release receipt obligation from current administered-site infrastructure, living custody, and actor authority, rechecks it when the action executes, and refuses cleanup and rewards while refunding a paid cost when proof fails. It distinguishes a closed-empty unrelated site from a truly facility-only target and names valid and invalid living rows, closed-live, closed-empty, facility-only, capture, and stale-target validation cases.

This belongs in the state ledger skill because custody rows, site lifecycle, authority, and stale scope proof are its existing contracts. The decisions and missions skill already covers receipt lifecycle for timed missions and did not need a parallel rule. No other skill, gameplay file, GUI, test, localisation, or workbook was edited by this handoff.

Evidence: `.agents/skills/chaos-redux-state-ledgers/SKILL.md` previously covered cohort resolution and stale targets but not cross-package co-location. The current source-level case and its validation limits are recorded in `uwr_aftermath_receipt_handoff_2026-09-27.md`. This handoff does not claim Clausewitz execution, native decision acceptance, or a live survivor-release receipt.

Validation: the official skill quick validator passed with Python UTF-8 mode, and the skill diff passed whitespace validation. No HOI4 run or log inspection was performed.
