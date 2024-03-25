#!/bin/sh

set -e

envsubst < /etc/ngingx/default.conf.tpl > /etc/nginx/conf.d/default.conf
ngingx -g 'daemon off;'