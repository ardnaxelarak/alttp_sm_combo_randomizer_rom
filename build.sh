#!/usr/bin/env bash
# Remember to commit an updated build.bat as well if making changes

echo Building Super Metroid + Zelda 3 Randomizer

find . -name build.py -exec python3 {} \;

cd resources
python3 create_dummies.py z_00.sfc z_ff.sfc 1
python3 create_dummies.py sm_00.sfc sm_ff.sfc 3

for f in ../src/sm/randopatches/ips/*.ips; do
  echo Applying $f
  flips --apply $f sm_00.sfc sm_00_applied.sfc
  mv sm_00_applied.sfc sm_00.sfc
  flips --apply $f sm_ff.sfc sm_ff_applied.sfc
  mv sm_ff_applied.sfc sm_ff.sfc
done

python3 create_exhirom.py sm_00.sfc z_00.sfc 00.sfc 0x00
python3 create_exhirom.py sm_ff.sfc z_ff.sfc ff.sfc 0xff

./asar --no-title-check --symbols=wla --symbols-path=../build/zsm.sym ../src/main.asm 00.sfc
./asar --no-title-check --symbols=wla --symbols-path=../build/zsm.sym ../src/main.asm ff.sfc
python3 create_ips.py 00.sfc ff.sfc zsm.ips
rm 00.sfc ff.sfc

cp zsm.ips ../build/zsm.ips > /dev/null

cd ..
echo Done
