# Guile OKI / setplay
This is, hopefully, a comprehensive detailing of Guile's okizeme / setplay
game.  Everything is safe on block, has been vetted for execution and
usefulness, and considers the situation *after* the pressure tool. I've also
tried to consider rhythm - for example, two forward dashes is more prone to
execution error than two medium or heavy normals or a dash followed by a
normal.

As with all frame-perfect setups, execution must be on point and there is wild
fluidity when trying to setup pressure after AA - you must manually execute AA
oki setups.  

Some setups will only work in the corner. It should be obvious which ones - I
may call it out. Or not.

For the uninitiated, oki setups such as these utilize *frame kills* in order to
burn a requisite number of frames such that the pressure is frame perfect.
Using the following setup as an example, let's walk through it to make sure
everything is understood.
`s.mp(4/3) | {s.hp s.mp(5/4) OR c.mk b.hp(4/1)}`
This is a setup for c.hk (1st hit) KDR/KR - that is, the first hit of crouching
heavy kick and quick-rise (or no recovery). After recovering from a c.hk, with
no delay, input s.mp. If the opponent quick-rises, you will score a hit (unless
they use an invulnerable reversal) and the brackets indicate the advantage on
hit and block (hit/block) - in this case: +4 on hit, +3 on block. Counterhits
confer +2f of advantage, so on CH, it's +6.
If the opponent doesn't quick-rise and instead opts to recover normally (no
recovery), after the s.mp whiffs, continue, without delay, to input the
remainder of the string: either `s.hp s.mp` or `c.mk b.hp`.
The obvious caveat is that you probably need to get a read on KDR or KDBR
(quick-rise or back-rise).

## Syntax
 * **pipe (|)** separates KDR/KDBR option from KD option
 * **{a OR b}** interchangeable options
 * **(4/3)** brackets indicate hit/block advantage

## Notes
 * c.mp and s.mp are fully interchangeable; s.mp has better advantage on hit or block and is more active.
 * s.mk and s.hp have the same start-up and active frames; s.mk is slightly faster to recover.
 * any setup ending in sobat can use f.hp instead; f.hp recovers 1f quicker than sobat though.
 * b.hp setups can use c.hp instead, but the advantage isn't great. +4 on hit, -1 on block.
 * 2 x f.dash is 36f - the same total frames as f.hk.
 * boom and df.hk (ghk) share the same total frames and are interchangeable for frame kills.
 * any setup which ends with b.hp can likely be ended with f.hp.
 * s.mk and whiffed throw both total at 24f.


## c.hk (1)
### KDR / KD
`c.lp(4/2) | c.mp c.lp s.mp(4/3)`
On block or non-CH hit, the c.lp will create a trap into the c.mp.

`s.mp(4/3) | {s.hp s.mp(5/4) OR c.mk b.hp(4/1)}`
1f gap on KDR.
To cover KD, choose either a b.hp or s.mp option depending on taste.

`s.lk(4/2) | b.hp s.mp(6/5)`
1f gap on KDR.
Might be useful as s.lk can be optioned into s.lk~s.mk.

### KDBR / KD
`b.hp(3/0) | {s.lp b.hp(4/1) OR s.lk s.mp(6/5)}`

## c.hk (2)
### KDR / KD
`f.dash s.mp(4/3) | s.hp s.mp(5/4)`
1f gap on KDR.

### KDBR / KD
`f.dash b.hp(3/0) | s.lp b.hp(4/1)`

## c.hk (cc)
Note: no quick-recovery options for opponent.
### 1st hit (+52)
`b.lk f.dash s.mp(6/5)`

`b.lk s.mp {s.mp(4/3) OR throw}`

`b.lk s.lk b.hp(3/0)`

### 2nd hit (+70)
`b.lk f.dash f.dash s.mp(6/5)`

`b.lk boom {s.mp(4/3) OR throw}`


## df.hk / GHK
### KDR / KD
`{f.dash f.dash OR f.hk} s.mp(5/4) | df.hk s.mp(6/5)`

### KDBR / KD
`{f.dash f.dash OR f.hk} f.hp(5/0) | {b.hp s.mp(6/5) OR s.hp b.hp(4/1) OR s.hp f.hp(4/-1)}`

`{f.dash f.dash OR f.hk} sobat(2/-2) | {sobat s.mp(6/5) OR s.hp b.hp(3/0)}`

## b.hp (cc)
The following setups are for crush-counter b.hp on the first frame. If you use
the b.hp meaty and get a CC, the advantage will change by either 1 or 2 frames.
The following headers include the advantage.
### b.hp(2/-1) KDR / KD
`sobat b.hp(4/1) | {s.hk s.mp(4/3) OR sobat b.hp(4/1)}`
`sobat f.hp(4/-1) | sobat f.hp(6/1)`

### b.hp(3/0) KDR/KD
*Use b.hp(4/1)*

### b.hp(4/1) KDR / KD
`s.hk b.hp(2/-1) | {s.hp b.hp(3/0) OR b.hp s.mp(5/4)}`
1f gap on KDR.

`f.dash s.lk s.mp(6/5) | c.mp c.mp s.mp(5/4)`

### b.hp(2/-1) KDBR / KD
`f.dash s.mp s.mp(5/4) | s.hk s.mp(5/4)`

`f.dash s.lk b.hp(4/1) | throw b.hp(4/1)`

### b.hp(3/0) KDBR / KD
*Use b.hp(4/1)*

### b.hp(4/1) KDBR / KD
`f.dash c.mk s.mp(4/3) | s.hk s.mp(4/3)`

`f.dash c.mk s.mp(4/3) | sobat b.hp(4/1)`

`f.dash f.dash b.hp(4/1) | s.mk b.hp(4/1)`

`f.dash f.dash b.hp(4/1) | s.hp s.mp(6/5)`

## swing-out
### KDR / KD
### KDBR / KD

## throw
### KDR / KD
### KDBR / KD

## b.throw
### KDR / KD
### KDBR / KD

## throw (air)
### KDR / KD
### KDBR / KD

## b.throw (air)
### KDR / KD
### KDBR / KD

## v-reversal / vr / f.ppp
### KDR / KD
### KDBR / KD

## ex.boom / tempest
### KDR / KD
### KDBR / KD

## fk
### KDR / KD
### KDBR / KD

## ex.fk
### KDR / KD
### KDBR / KD

## hurricane
### KDR / KD
### KDBR / KD
