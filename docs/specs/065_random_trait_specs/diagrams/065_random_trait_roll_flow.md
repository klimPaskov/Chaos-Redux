# Event 065 Trait Pool and Roll Flow

```text
VANILLA COUNTRY-LEADER TRAIT ROOTS
                    +
CHAOS REDUX COUNTRY-LEADER TRAIT ROOTS
                    |
                    v
        Structured source parser
                    |
                    v
        Final load-order ID resolution
                    |
         +----------+----------+
         |                     |
      duplicate             unique
         |                     |
         v                     v
  Record override chain   Create canonical entry
                               |
                               v
                Attach stable registry index
                               |
                               v
          Apply source-origin and reviewed tags
                               |
                               v
      Ordinary or featured, with non-stacking reasons
                               |
                               v
                Emit complete manifest
                               |
              +----------------+----------------+
              |                                 |
              v                                 v
     Emit runtime pool                 Emit name selector
              |                                 |
              +----------------+----------------+
                               |
                               v
                     Run check mode
                               |
                  +------------+------------+
                  |                         |
                fail                       pass
                  |                         |
                  v                         v
       Block Event 65 execution       Pool can load
                                                |
                                                v
                                   Recipient needs one slot
                                                |
                                                v
                                  Remove current owned traits
                                  Remove Event 65 ledger IDs
                                  Remove accepted current slots
                                                |
                                   +------------+------------+
                                   |                         |
                                 empty                   candidates
                                   |                         |
                                   v                         v
                             Saturated              Choose stage weights
                                                           |
                                               +-----------+-----------+
                                               |                       |
                                        Baseline or I              Evolution II
                                         all weight 100            ordinary 100
                                                                    featured 125
                                                                       |
                                                                       |
                                                               Evolution III
                                                               ordinary 100
                                                               featured 150
                                               |
                                               v
                                     Weighted accepted source
                                               |
                                               v
                                  Native country-leader trait effect
                                               |
                                      +--------+--------+
                                      |                 |
                                    failed            added
                                      |                 |
                                      v                 v
                              Count and handle    Record source ID,
                              without consuming   registry index,
                              a successful slot   origin and class
                                                        |
                                                        v
                                               Continue next slot
```

## Statistical interpretation

For a recipient with eligible set `E`, each source trait `i` has:

`P(i) = weight(i) / sum(weight(j) for j in E)`

After one source trait is accepted, it leaves `E` for the next slot.

Baseline and Evolution I are uniform over `E`.

Evolution II and Evolution III use the bounded featured ratio.

Collision handling must produce this same conditional distribution.

## Generator invariants

- One final source ID creates one active registry entry.
- One registry entry creates one runtime branch.
- One runtime branch creates one name-selector branch.
- Source order does not change stable indexes.
- Several featured reasons do not stack.
- A stale source set blocks check mode.
