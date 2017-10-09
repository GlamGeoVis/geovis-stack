#!/bin/bash
source /home/xenon/simcity/bin/activate
python /home/xenon/simulations/necklace/makeNecklace.py $SIMCITY_IN/input.json $SIMCITY_OUT/test.geojson > $SIMCITY_OUT/log.log
