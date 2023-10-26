#!/bin/sh
# Version 1.0

METRIC="$1"

if [ -z "$1" ]; then
    echo "Please specify a metric"
    exit 1
fi

case $METRIC in

        'gw-col')       python /var/log/asterisk/cdr-csv/consumo_cdr_troncal.py | grep 'gw-col' | awk '{print $5}' ;;
        'gw-col2')       python /var/log/asterisk/cdr-csv/consumo_cdr_troncal.py | grep 'gw-col2' | awk '{print $5}';;
        'gw-pecall02')       python /var/log/asterisk/cdr-csv/consumo_cdr_troncal.py | grep 'gw-pecall02' | awk '{print $5}';;
        'gw01')       python /var/log/asterisk/cdr-csv/consumo_cdr_troncal.py | grep 'gw01' | awk '{print $5}';;
        'gw02')       python /var/log/asterisk/cdr-csv/consumo_cdr_troncal.py | grep 'gw02' | awk '{print $5}';;
        'gw03')       python /var/log/asterisk/cdr-csv/consumo_cdr_troncal.py | grep 'gw02' | awk '{print $5}';;
        'sip-col')       python /var/log/asterisk/cdr-csv/consumo_cdr_troncal.py | grep 'sip-col' | awk '{print $5}';;
        'sip')       python /var/log/asterisk/cdr-csv/consumo_cdr_troncal.py | grep 'sip' | awk '{print $5}';;
        'softsw01')       python /var/log/asterisk/cdr-csv/consumo_cdr_troncal.py | grep 'softsw01' | awk '{print $5}';;
        'softsw02')       python /var/log/asterisk/cdr-csv/consumo_cdr_troncal.py | grep 'softsw02' | awk '{print $5}';;
        'softsw03')       python /var/log/asterisk/cdr-csv/consumo_cdr_troncal.py | grep 'softsw03' | awk '{print $5}';;
        'softsw04')       python /var/log/asterisk/cdr-csv/consumo_cdr_troncal.py | grep 'softsw04' | awk '{print $5}';;
        'softsw05')       python /var/log/asterisk/cdr-csv/consumo_cdr_troncal.py | grep 'softsw05' | awk '{print $5}';;

    *)  echo "Not selected metric"
        exit 0
        ;;
esac
