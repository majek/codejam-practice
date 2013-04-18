#!/bin/bash
# wget https://codejam-commandline.googlecode.com/files/codejam-commandline-1.2-beta1.zip

echo "[*] New competition: gcj_init_contest.py XXXX"
echo ""
echo "    gcj_run A tiny"
echo "    gcj_upload_the_answer A small"
echo "    gcj_get_status.py"
echo ""
echo "[ ] Docs: less $HOME/src/codejam-commandline-1.2-beta1/README"
export PS1="(codejam) $PS1"
export PATH="$HOME/codejam:$HOME/src/codejam-commandline-1.2-beta1:$PATH"
