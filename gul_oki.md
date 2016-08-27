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

This is a setup for c.hk (1st hit) KDR/KD - that is, the first hit of crouching
heavy kick and quick-rise or no recovery. After scoring a hit off c.hk, with
no delay, input s.mp. If the opponent quick-rises, you will land a hit (unless
they use an invulnerable reversal) and the brackets indicate the advantage on
hit and block (hit/block) - in this case: +4 on hit, +3 on block. Counterhits
confer +2f of advantage, so on CH, it's +6.

The pipe signifies the end of the KDR string and the beginning of the KD
string. Braces denote a set of interchangeable options. In this case, an option
ending with s.mp or another ending with b.hp.

If the opponent doesn't quick-rise and instead opts to recover normally (no
recovery), after the s.mp whiffs, continue, without delay, to input the
remainder of the string: either `s.hp s.mp` or `c.mk b.hp`. As with the KDR
s.mp previously, the advantage is specified in parens (); e.g., `c.mk
b.hp(4/1)`.

These options will allow some flexibility after oki is complete. Further
referencing the above: s.mp gives Guile very close range positioning at
excellent advantage; b.hp may yield a crush counter. Be sure to mix your
options up based on your tactical requirements rather than *auto-piloting* the
same setups.

## Syntax
* **pipe (|)** separates KDR/KDBR option from KD option
* **{a OR b}** interchangeable options
* **(4/3)** brackets indicate hit/block advantage
* **1f gap** may suffix a setup - this means the pressure isn't meaty
* **~** (tilde) represents "chain" timing (fast)

## Notes
* c.mp and s.mp are fully interchangeable; s.mp has better advantage on hit or block and is more active.
* s.mk and s.hp have the same start-up and active frames; s.mk is slightly faster to recover.
* any setup which ends with b.hp can likely be ended with f.hp or c.hp (mind the advantage).
* sobat, f.hp, c.hp, and b.lk all share the same final active frame and all bar sobat recover in 28f (sobat: 29f).
* 2 x f.dash is 36f - the same total frames as f.hk.
* boom and df.hk (ghk) share the same total frames and are interchangeable for frame kills.
* s.mk and whiffed throw both total at 24f.


## A Word About Tools
In any okizeme setup, the character is going to burn frames just getting into range.
In Guile's case, there are only 4 means of closing distance that his setups usually rely on.

| move | total f | notes |
|--------:|:-------:|--------------------------------------------|
| f.dash | 18 |  |
| bazooka | 28 | Always use b.lk to maintain charge |
| sobat | 29 | Execute like you would a boom, but with mk |
| s.hk | 34 | Always use b.hk to maintain charge |

After movement comes pressure and the prominent normals suitable for this
manner of work are:

| move | startup | total f | active f range | notes |
|--------:|:-------:|:-------:|-----------------------------------|----------------------------------------------------|
| s.mp | 5 | 20 | `-----###` | c.mp with better active and adv., but lesser range |
| s.hp | 7 | 27 | `-------###` | s.mk has the same start-up and active |
| b.hp | 8 | 30 | `--------###` |  |
| bazooka | 8 | 28 | `--------#####` | interchangeable with c.hp |
| f.hp | 10 | 28 | `----------###` | can be used instead of bazooka or c.hp |
| sobat | 11 | 29 | `-----------##` | has interchangeability with f.hp |

By understanding the fundamental properties of Guile's primary oki toolset, the
player is able to make on-the-fly adjustments to compensate for meaty or late
knock-downs.

For example, knowing that an FK followed by `f.dash s.mp` is the limit for
s.mp, if the fk connects later than 1st active frame, the s.mp will whiff; b.hp
is a good backup plan here. Another example might be knowing that `f.mk b.hp`
is a valid follow-up, but the preceeding hit was meaty or late in some way. One
might switch the sobat out for s.hk to eat the extra frames.


---
## Crouching HK, 1st hit
### KDR / KD
`c.lp(4/2) | c.mp c.lp s.mp(4/3)`

`s.mp(4/3) | {s.hp s.mp(5/4) OR c.mk b.hp(4/1)}` *1f gap*

`s.lk(4/2) | b.hp s.mp(6/5)` *1f gap*


### KDBR / KD
`b.hp(3/0) | {s.lp b.hp(4/1) OR s.lk s.mp(6/5)}`


---
## Crouching HK, 2nd hit
There are, perhaps coincidentally, 18 frames of extra knock-down advantage for
hitting with the second hit. Guile's forward dash is 18 frames.

Thus, if you score a knock-down with the second hit of c.hk, dash forward and
apply a first hit setup from the previous section.


---
## Crouching HK, Crush Counter
*Note: Opponent cannot quick recover.*
Obviously, this is just a KD scenario, so the above setups apply. Below are
some CC-specific options if that suits.
### 1st hit (+52)
`b.lk f.dash s.mp(6/5)`

`b.lk s.mp {s.mp(4/3) OR throw}`

`b.lk s.lk b.hp(3/0)`


### 2nd hit (+70)
`b.lk f.dash f.dash s.mp(6/5)`

`b.lk boom {s.mp(4/3) OR throw}`


---
## Guile High Kick (df.hk)
### KDR / KD
`{f.dash f.dash OR f.hk} s.mp(5/4) | df.hk s.mp(6/5)`


### KDBR / KD
`{f.dash f.dash OR f.hk} f.hp(5/0) | {b.hp s.mp(6/5) OR s.hp b.hp(4/1) OR s.hp f.hp(4/-1)}`

`{f.dash f.dash OR f.hk} sobat(2/-2) | {sobat s.mp(6/5) OR s.hp b.hp(3/0)}`


---
## Burn Straight, Crush Counter (b.hp)
The following setups are for crush-counter b.hp on the first frame. If you use
the b.hp meaty and get a CC, the advantage will change by either 1 or 2 frames.
The following headers include the advantage.

### b.hp(2/-1) KDR / KD
`sobat b.hp(4/1) | {s.hk s.mp(4/3) OR sobat b.hp(4/1)}`

`sobat f.hp(4/-1) | sobat f.hp(6/1)`


### b.hp(3/0) KDR / KD
*Use b.hp(4/1)*


### b.hp(4/1) KDR / KD
`s.hk b.hp(2/-1) | {s.hp b.hp(3/0) OR b.hp s.mp(5/4)}` *1f gap*

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


---
## Swing Out / Bullet Revolver
### KDR / KD
`b.lk throw | s.hk throw`

`b.lk s.lp(5/4) | c.mp throw s.mp(6/5)`

`b.lk s.mp(4/3) | boom s.mp(5/4)`


### KDBR / KD
`b.lk b.hp(4/1) | throw b.hp(4/1)`

`b.lk b.hp(4/1) | s.hp s.mp(6/5)`

`b.lk {f.hp(4/-1) OR c.hp(4/-1)} | {f.hp b.hp(2/-1) OR sobat s.mp(6/5)}`


---
## Dragon Suplex (throw)
### KDR / KD


---
## Judo Throw (b.throw)
After this throw, Guile is *just* in range for a c.mp if they block or press a
button - the timing is, however, manual.
### KDR / KD
`s.hk(2/-2) | {s.mp b.hp(4/1) OR c.mk s.mp(6/5) OR f.dash c.hp(6/1)}`


---
## Flying Mare (throw(air))
Depending on circumstance, this throw either leaves Guile at +28 or +30 for
KDR. If the means by which this effect applies is discovered, I will post
detail of it here.
### KDR / KD

`f.dash b.hp(4/1)` *+28*

`f.dash c.hp(6/1) | c.mk b.hp(4/1)` *+30*


---
## Flying Buster Drop (b.throw(air))
There are no safe options against KDR, only KD - thus, some of these setups use
a normal at the start to keep Guile a little safer.
### KDR / KD
`c.lp sobat b.hp(4/1)` *KD only*

`c.mp b.lk {s.lp(4/3) OR s.mp(4/3)}` *KD only, 1f gap for s.mp*

`f.dash b.lk s.mp(5/4)` *KD only, unsafe vs. KDR*


---
## Reverse Back Knuckle (V-Reversal)
### KDR / KD
`f.dash b.hp(4/1) | sobat b.hp(4/1)`

`f.dash f.hp(4/-1) | sobat f.hp(6/1)`


### KDBR / KD
`f.dash s.hk(2/-1) | b.lk s.mp(6/5)`

`f.dash f.hk(3/-1) | b.lk s.mp(4/3)` *1f gap*


---
## EX Sonic Boom / Sonic Tempest
A common follow-up for ex.boom is b.lk which can air-reset the opponent. This
only works at close range, but allows for some sterling pressure.  It's worth
noting that ex.boom has, probably, the most esoteric setups as the advantage
doesn't really suit Guile.
### KDR / KD
`b.lk(early reset) {s.hp(8/-2) OR c.hp(3/-2)}` *reset (no KD)*

`f.dash b.lk throw | s.hk throw` *2f gap on KDR, 1f gap on KD*

`f.dash c.lp~c.lp s.hp(8/-2) | s.hk s.mp(6/5)`

`f.dash b.lk s.mp(4/3) | f.hk s.mp(5/4)` *2f gap*


### KDBR / KD
`f.dash f.dash f.hk(5/1) | sobat s.mp(6/5)`


---
## Flash Kick (light, medium, heavy)
There are some real subtlties to Guile's Flash Kick in SFV, but the summary is
as follows (some exceptions apply for EX FK):

* all FKs have some period of full invulnerability
* all FKs start with throw invulnerability
* all FKs start grounded
* oki is only stable after a grounded FK
* the most stable oki setups rely on the first active frame connecting
* all FK strengths have the same KDR, KDBR, and KD advantages
* hk.fk's 1st active frame is the farthest range of the 3
* lk.fk starts up and gains full invulnerability the quickest

Here is [TOOLASSISTED's](https://twitter.com/TOOLASSlSTED) flash kick chart
(taken from TOOLASSISTED's [SFV Guile Wiki on
Reddit](https://www.reddit.com/r/SFV_GUILE/wiki/index)):

| FLASH KICK | START UP | PROJ INV | ALL INV | GROUND | THROW INV |
|:----------:|:--------:|:--------:|:-------:|:------:|:---------:|
| LK | 4 | 1-3 | 4-6 | 1-3 | 1-6 |
| MK | 5 | 1-4 | 5-7 | 1-4 | 1-7 |
| HK | 6 | 1-5 | 6-8 | 1-5 | 1-8 |
| EX | 4 |  | 1-9 | 1-6 | 1-9 |

The takeaway is this:
* always use hk.fk in grounded combos
* always use lk.fk for standard AA (mk or hk for ranged AA)

Okizeme off 1st active frame (AF1) is the most desirable situation, but
knowledge of what to use for later hits is essential. Some practice and a keen
eye are required.

The setups will be broken up into 3 versions: 1st active frame (AF1), 1st
airborne frame (AB1), and last frame (LF).

Although there are a few frames between AF1 and AB1, AB1 setups should cover the gap handily, but bear the following in mind:
* AF1 setups whiff for AB1
* AB1 setups *may* whiff for LF
* AB1 and LF setups are likely interruptible vs. AF1

### AF1 KDR / KD
`f.dash s.mp(6/5) | {c.mp c.mp s.mp(5/4) OR c.mk s.lk s.mp(6/5)}`

`f.dash b.hp(2/-1) | s.hp b.hp(3/0)` *1f gap, works for AB1*

`f.dash s.lk(6/4) | s.mk s.mp s.mp(5/4)` *not as good as s.mp, but different*


### AF1 KDBR / KD
`f.dash {f.hp(6/1) OR b.lk(2/-2) OR c.hp(6/1)} | {b.lk b.hp(4/1) OR s.hk s.mp(4/3)}` *some 1f,2f gaps*

`f.dash sobat(3/-1) | b.hp s.mp(6/5)` *great option if you read KD*

`f.dash s.hk(1/-3) | {throw b.hp(2/-1) OR c.mk b.hp(3/0) OR s.hp s.mp(4/3) OR s.mp f.hp(6/1)}` *2f gap, covers AB1*


---
## EX Flash Kick
Okizeme play after an EX FK is more restricted than a regular FK, but there are
still some solid options.
### KDR / KD
`f.dash b.hp(3/0) | {b.hp b.hp(2/-1) OR b.lk b.hp(4/1) OR s.hk s.mp(4/3)}`

`f.dash s.hp(8/-2) | s.hk s.mp(6/5)`

**CNR** `c.lp~c.lp throw | s.hk throw`


### KDBR / KD
`f.dash s.hk(1/-3) | s.hp s.mp(6/5)`

**CNR** `s.hp throw | b.hp throw`


---
## Sonic Hurricane
These setups, for now at least, only focus on a grounded hit from Sonic
Hurricane. Due to the distance from opponent after knock-down, they only work
in the corner.
### KDR / KD
**CNR** `f.dash s.lp(5/4) | s.mp throw s.mp(6/5)`

**CNR** `f.dash s.mp(4/3) | df.hk s.mp(5/4)`

### KDBR / KD
**CNR** `f.dash b.hp(4/1) | {s.hp s.mp(6/5) OR throw b.hp(4/1)}`
