#!/bin/sh
cd /home/simcity/simcity/csWeb
npm install node-sass

# This one fails anyway
npm install

# This one does nothing
bower install

gulp init
bower link
cd out/csServerComp/
npm link

cd /home/simcity/simcity/sim-city-cs
npm install
npm link csweb
cd /home/simcity/simcity/sim-city-cs/public
bower install
bower link csweb
cd /home/simcity/simcity/sim-city-cs
typings install
gulp init

# Content from start.sh
cd /home/simcity/simcity/sim-city-cs
gulp serve & (cd /home/simcity/simcity/csWeb/ && gulp watch2)
