import argparse
from pathlib import Path
CHECKS={"PermitRootLogin":{"no"},"PasswordAuthentication":{"no"},"X11Forwarding":{"no"}}
def main():
    p=argparse.ArgumentParser(); p.add_argument("--config",default="/etc/ssh/sshd_config"); a=p.parse_args()
    vals={}
    for line in Path(a.config).read_text(errors="replace").splitlines():
        s=line.strip()
        if s and not s.startswith("#"):
            x=s.split()
            if len(x)>1 and x[0] in CHECKS: vals[x[0]]=x[1].lower()
    for k,good in CHECKS.items():
        v=vals.get(k,"unset/default")
        print(("PASS" if v in good else "REVIEW"),f"{k}={v}")
if __name__=="__main__": main()
