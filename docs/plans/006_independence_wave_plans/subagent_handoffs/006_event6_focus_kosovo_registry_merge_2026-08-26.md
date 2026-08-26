# Event 006 focus and Kosovo decision registry merge

Date: 2026-08-26

## Disposition

The source-layout pass is complete for two small, ownership-compatible parser files.

## Focus registry

The 20 Pacific `shared_focus` blocks formerly loaded from `common/national_focus/006_independence_wave_pacific_focus.txt` now live under the source marker `# SOURCE: 006_independence_wave_pacific_focus.txt` in `common/national_focus/006_independence_wave_focus.txt`.

The three Pacific file-scoped focus constants remain declared in the receiver before their consumers.

The standalone Pacific focus parser file was removed.

The receiver now contains 184 direct focus blocks and 43 full `shared_focus` blocks, preserving the resolved 318-focus tree and its existing import roots.

## Kosovo decision registry

The IW-031 category and eleven decision blocks formerly loaded from `common/decisions/006_independence_wave_kosovo_decisions.txt` now live under the source marker `# SOURCE: 006_independence_wave_kosovo_decisions.txt` in `common/decisions/006_independence_wave_balkan_decisions.txt`.

The Kosovo civilian-factory file-scoped constant remains declared in the receiver before its decision consumers.

The standalone Kosovo decision parser file was removed.

Kosovo trigger, effect, and localisation files remain separate because their package ownership and active lifecycle work are distinct.

## Equivalence and checks

The executable Pacific focus body and Kosovo decision body compare equal to their pre-merge source after line-ending normalization; only source markers and redundant comment banners changed.

The Pacific receiver plus removed file shrinks by 618 normalized UTF-8 bytes, and the Balkan receiver plus removed file shrinks by 432 normalized UTF-8 bytes, for 1,050 bytes saved across two fewer parser files.

The Pacific focus count remains 20 in the migrated block, and the Kosovo decision count remains one category plus eleven decisions.

No package gate, focus prerequisite, focus reward, decision cost, timer, trigger, effect, cancellation, cleanup, AI block, admission count, or runtime contract was changed.

This handoff records source-layout evidence only and does not claim live parser, save/load, or in-game execution evidence.
