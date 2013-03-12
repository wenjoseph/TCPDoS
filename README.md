TCPDoS
======

"Low-Rate TCP-Targeted Denial of Service Attacks" experiment on Mininet

# Setup Instruction #
1. Goto Amazon US West (Oregon) EC2 data center
2. Launch a new instance with AMI "CS244-Win13-Mininet (ami-7eab204e)". Select machine type c1.medium.
3. checkout the git repo.
        git checkout https://github.com/wenjoseph/TCPDoS.git
4. Run `sudo ./run.sh` in directory `TCPDoS`.
5. Run `python -m SimpleHTTPServer` to open a HTTP server. The result is in `http://host:8000/last/result.html`.
