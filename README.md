TCPDoS
======

"Low-Rate TCP-Targeted Denial of Service Attacks" experiment on Mininet

# Setup Instruction #
1. Launch a new instance at Amazon US West (Oregon) EC2 with AMI "CS244-Win13-Mininet (ami-7eab204e)".
   Select machine type c1.medium. Open port 8000 if you want to see the result via HTTP.
2. Clone the git repo. `git clone https://github.com/wenjoseph/TCPDoS.git`.
3. Run `sudo ./run.sh` in directory `TCPDoS`. It will take around 1 hour.
4. Run `python -m SimpleHTTPServer &` to open a HTTP server. The result is in `http://host:8000/last/result.html`.
