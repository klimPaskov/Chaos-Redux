# Event 016 Mengele Biomedical no-DLC Prototype

Disposition: implemented in source under the accepted portfolio closure plan; probability and native decision acceptance remain unresolved.

The existing conventional provider decision file already owns Biomedical Theory, Deployment, and Weaponization, so this tranche adds only `mengele_event016_biomedical_prototype` in `common/decisions/016_mengele_biomedical_prototype_decision.txt` with exact private gates in `common/scripted_triggers/016_mengele_biomedical_prototype_decision_triggers.txt` and player-facing text in `localisation/english/016_mengele_biomedical_prototype_l_english.yml`.
The accepted no-DLC route uses a 240-day timer, reserves two civilian factories, and pays 90 Political Power, 300 Support Equipment, and 100 Fuel through the private family-stage core.
The wrapper uses Biomedical family ID 6 and aligned receipt index 5, literal Prototype selectors for begin, cancel, and finish, and the existing Biomedical Prototype icon and DDS.
The native `sp_brilliant_scientist_biomedical_acceleration` remains authoritative with Götterdämmerung and retains its own clock and payment.
The private Prototype completion records the stage receipt and modifier only; the later established Deployment stage grants the conventional operational package.
The no-DLC Prototype AI matches the existing Kruger fallback high base and wartime preferred factor, with a provider-specific no-spare-factory cautious condition rather than Kruger's Capacity variable.

The source check found one decision ID, a defined private receipt predicate, existing icon/DDS, matching quote and duration values, and UTF-8 BOM localisation.
The lifecycle, interactions, and assets are documented in `docs/events/016_brilliant_scientist/systems/mengele_biomedical_stages.md`.
No HOI4 process was launched; the mandatory `chaosx_ai_probability_auditor` baseline/scenario pass, native timer and refund ordering, current decision-list render, and live consumer acceptance remain open.
