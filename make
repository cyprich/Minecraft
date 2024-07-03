#!/bin/bash

# Setup
cd ~/Minecraft
declare -a files
files+=(AkuAkuTotem All AmogusTotem ClearScaffolding EnderTurtle NoPumpkinBlur Plants Sugarcane Unsuspicious)

# Making CypoPack-All
rm -r CypoPack-All/assets
for i in ${files[@]}; do
        cp -r "CypoPack-$i"/assets/* "CypoPack-All/assets"
done

# Zipping files
files+=(All)
for i in ${files[@]}; do
	cd "./CypoPack-$i"
	#zip "zip/CypoPack-$i".zip "CypoPack-$i"/"*"
	zip -r "CypoPack-$i".zip *
	mv "CypoPack-$i".zip ../zip
	cd ..
done
