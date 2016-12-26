#!/bin/zsh

dst=~/s/syngin.net/sfv

for f in *md; do
	pandoc -s -c pandoc.css --self-contained $f -o $dst/${f%%md}html
done

rsync -vazh --inplace ~/s/syngin.net/* hammer:
