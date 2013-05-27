#!/bin/bash
# wget https://codejam-commandline.googlecode.com/files/codejam-commandline-1.2-beta1.zip

CONTEST=`cat $HOME/src/codejam-commandline-1.2-beta1/config/current_config.py |grep contest_id|cut -d "'" -f 4`


echo "[*] Google CodeJAM. Current contest: $CONTEST"
echo ""
echo "    gcj_init_contest.py XXXX"
echo "    gcj_renew_login.py"
echo "    gcj_get_tiny [XXXX]"
echo ""
echo "    gcj_run A tiny"
echo "    gcj_upload A small"
echo "    gcj_upload_retry A small"
echo "    gcj_get_status.py"
echo ""
echo "[ ] Docs: less $HOME/src/codejam-commandline-1.2-beta1/README"
export PS1="(codejam) $PS1"
export PATH="$HOME/codejam:$HOME/src/codejam-commandline-1.2-beta1:$HOME/src/pypy/bin/:$PATH"

#echo "[*] Renewing login:"
#$HOME/src/codejam-commandline-1.2-beta1/gcj_renew_login.py > /dev/null
