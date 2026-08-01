# Event 12 Africa Court Presentation Follow-up

## Scope

This tranche aligns the remaining high-visibility Africa-facing localisation with the requested decorated-sovereign presentation. Player-facing references to the continental and regional governing bodies use courts, assemblies, crowns, or named sovereign institutions instead of presenting councils as the leaders. Technical route identifiers, dispatch keys, focus IDs, and existing carrier tags remain unchanged.

## Changed surfaces

- `localisation/english/012_africa_focus_l_english.yml` replaces visible continental and regional council wording with courts or assemblies while retaining the existing focus and route keys.
- `localisation/english/012_africa_achievements_l_english.yml` and `localisation/english/012_africa_evolutions_l_english.yml` align achievement and evolution prose with Court of Crowns and court records.
- `localisation/english/012_africa_rsa_l_english.yml` presents the South African exile settlement as a continental court without renaming the technical council identifiers.
- `localisation/english/012_africa_world_order_l_english.yml` and `localisation/english/012_africa_world_sponsorship_l_english.yml` use courts for Africa's ultimatum, sponsorship, and aftermath surfaces. Other world packages retain their own council vocabulary because those strings describe their separate constitutional institutions.
- `docs/events/012_africa/overview.md` records that court labels describe institutions and never replace the named sovereign portrait.

## Contract and safety

No gameplay effects, tags, cosmetic carriers, focus IDs, stores, decisions, or model references changed. The 16 priority members continue to use the existing Independence Wave carriers and the shared crowned-sovereign trait. The two required Afaan Oromoo flavour strings remain deferred pending full-string and native-speaker review.

## Validation

The touched localisation files were scanned for visible council wording, with remaining occurrences limited to intentional technical identifiers and the separate external package vocabulary described above. Event 12 localisation files retain their UTF-8 BOM. The change is text-only and introduces no unsupported Clausewitz operators or new runtime references.

## Remaining risks

This presentation tranche does not close the Event 12 live gates. W5 still lacks authoritative six-package pre-install receipts; three compact hosts remain unbound; late action families, RSA, Scramble, focus payoff, AI probability evidence, achievement proof, workbook/export alignment, audio, models, and native-language review remain recorded in the completion audit.
