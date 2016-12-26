# SFV Guile
## Season 2 Okizeme Guide

Right up front: if you are the kind of person who cares about this sort
of thing, this site is built out of Markdown documents which are hosted on
Github [here](https://github.com/weirdtales/sfv). The whole thing is *very*
messy and constitutes my personal SFV note book.


## Introduction

The guide, such as it is, is broken down into sections - one for each
knock-down move. Within each section, the knock-down will be briefly discussed
and some optimal okizeme setups provided.

For further assistance, hit me up on [Twitter](https://twitter.com/melboyce).


## Notation and Nomenclature

As with prior work, the notation I use is mostly of my own devising. It is
heavily influenced by SRK and is a combination of US and JP styles.

Buttons are referred to as *light*, *medium*, and *heavy* - the first letter
of which is used in the shorthand notation.

The type of button is noted as either *p* or *k* for *punch* or *kick*.

Directions are the first letter of *stand*, *jump*, *crouch*, *forward*,
*backward*, *up*, and *down*. Or some combination thereof.

*Hash* (#) denotes an inline comment.

The shorthand notation uses *periods* to separate attributes of a move and
*parens* to apply some kind of state if applicable:

`b.throw(air)  # back throw in the air`


### Okizeme specific notation

*Pipes* split strings into those executed for *KDR* or *KDBR* and those
executed for *KD* only:

`f.dash s.mp | c.mp c.mp s.mp  # left side of pipe for KDR`

*Parens* in strings that contain *numbers split by a forward slash* will
refer to the hit and block advantage for that string's ender:

`f.dash s.mp(7/3) | ...  # s.mp is at +7 on hit and +3 on block if opp. KDRs`

An *asterisk* before a move notation indicates the move can create a *Crush
Counter*:

`f.dash *b.hp(2/-1) | ...  # on CH, b.hp CCs`


## TOC

WIP


## Flying Buster Drop

| KDR | KDBR | KD |
|:---:|:----:|:--:|
|2|2|51|

Note: use this throw for side-switch purposes.

There's nothing to work with here that is realistic. If you react to the *KD*
scenario, you have time to manually apply oki pressure with your weapon
of choice.


## Crouch HK

| Hit # | KDR | KDBR | KD |
|:-----:|:---:|:----:|:--:|
|1|3|8|52|
|2|21|26|70|

Note: 2nd hit creates and extra `18f` of advantage for Guile - this is the
same length as `f.dash`.

Scoring a knock-down with `c.hk` is not unusual and while the fastest
recovery option doesn't allow for meaty pressure, Guile still scores
counter-hits against 3f normals. As the *note* above indicates, landing the
knock-down off the second hit of crouch HK adds `18f` of extra advantage to
the equation. Simply dash forward to create a 1st hit situation.


### KDR

With advantage down at `+3f`, strong KDR advantage only comes two ways:
*stand MP* or *stand LK*.

| Option | On hit | On counter-hit | On block | Total frames |
|-------:|:------:|:--------------:|:--------:|:------------:|
|`s.mp`|6|8|2|21|
|`s.lk`|4|6|2|15|


#### stand MP

This is always a strong option when close to your opponent. Being at `+2f`
works well for trapping with throws and Guile has good `4f` tick normals.

Link straight to `c.mp` as if it will hit and if your opp. stays down, the
`c.mp` will form the first part of the next sequence.

* `s.mp(6/2) | c.mp s.mk s.mp(8/4)`
* `s.mp(6/2) | c.mp c.mk b.hp(3/0)`
* `s.mp(6/2) | c.mp c.lk f.hk(8/0)`


#### stand LK

Technically safer than `s.mp` as due to shorter total frames, `s.lk` makes
for a good tick option. The problem with a fast oki normal like this is that
branching for *KD* becomes more difficult.

* `s.lk | b.hp s.mp(8/4)`
* `s.lk | s.hp b.hp(4/1)`
* `s.lk | c.mp f.hk(8/0)`
