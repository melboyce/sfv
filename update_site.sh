#!/bin/zsh

dst=~/syngin.net/sfv

pandoc -s -c pandoc.css --self-contained gul_oki-kata.md -o $dst/oki-kata.html
pandoc -s -c pandoc.css --self-contained gul_oki.md -o $dst/oki.html
pandoc -s -c pandoc.css --self-contained gul_punish_chk_maxrange.md -o $dst/punish-chk.html
pandoc -s -c pandoc.css --self-contained gul_top-players.md -o $dst/top-players.html

rsync -vazh --inplace ~/syngin.net/* hammer:
