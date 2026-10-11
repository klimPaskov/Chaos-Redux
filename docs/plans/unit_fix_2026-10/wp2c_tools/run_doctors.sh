#!/bin/bash
cd "<mod root>/.tmp/unitfix2"
for u in "$@"; do python run.py wp1_doctor.py "$(cat cfg_${u}_doctor.json)" 8000 > doctor_$u.out 2>&1; echo "$u done" >> doctors.log; done
