# Stock-planning skill correction

Disposition: implemented under the parent's bounded instruction.
Added three generic sentences in the AI section of `.agents/skills/chaos-redux-decisions-missions/SKILL.md` because existing affordability and AI guidance did not cover planning before first stock exists or priorities spanning upkeep and allocation passes.
Planning and receiving now explicitly share structural eligibility, with first-production stock and programme-receipt checks reserved for execution, while resource priorities govern both passes.
No event-specific context, thresholds, routing changes, gameplay changes, or other skill edits belong to this contribution.

Scratch directory: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.git\chaosx_skill_scratch\stock_planning_20261009`.
`owned.patch` contains only the addition against HEAD, anchored to the existing AI guidance.
Original HEAD, index, and working bytes plus their hashes are retained there, alongside the exact addition, expected final bytes, and working-tree-owned patch.
All prior dirty bytes were preserved, and the index was not changed.
Final skill SHA-256: `f54c17338e496774736a8bb6b30f61dff8867b490b5f2d5baff25102e2c832a8`.

Used `skill-creator` and `chaos-redux-decisions-missions`.
The official `quick_validate.py` check returned `Skill is valid!`, and the owned diff was reviewed for scope and overlap.
No requested skill work is blocked or omitted.
Nothing was staged or committed, and the parent owns the isolated commit.
