./moncat -d frags/ -o schema.xml
MONDRIAN_REST_CONF=`pwd`/config.yaml puma config.ru -b tcp://0.0.0.0:9292 -t 8:32 -e production