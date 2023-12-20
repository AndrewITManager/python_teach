sudo apt-get updatedan
sudo apt-get install arpwatch arptables

touch /var/log/arpwatch.log

# Запустите arpwatch с логированием в этот файл:
arpwatch -i eth0 -f /var/log/arpwatch.log

# Шаг 3: Скрипт для обнаружения ARP-спуффинга
# Создайте скрипт detect_arp_spoofing.sh:
touch detect_arp_spoofing.sh

#!/bin/bash

LOGFILE="/var/log/arpwatch.log"
SPOOFED_MACS=()

tail -F $LOGFILE | while read line; do
    if echo $line | grep -q "flip flop"; then
        MAC=$(echo $line | awk '{print $NF}')
        if [[ ! " ${SPOOFED_MACS[@]} " =~ " ${MAC} " ]]; then
            echo "ARP spoofing detected: $MAC"
            SPOOFED_MACS+=($MAC)
            # Здесь можно добавить дополнительные действия, например, отправку уведомлений
        fi
    fi
done

# Этот скрипт будет следить за логом arpwatch и обнаруживать подозрительные изменения. Если MAC-адрес изменился, то он будет добавлен в список SPOOFED_MACS.

# Шаг 4: Запуск скрипта
# Сделайте скрипт исполняемым и запустите его:
chmod +x detect_arp_spoofing.sh
./detect_arp_spoofing.sh

################################################################################################

#!/bin/sh

LOGFILE="/var/log/arpwatch.log"
DETECTED_MACS_FILE="detected_macs.txt"

echo "Запуск скрипта обнаружения ARP-спуффинга."
echo "Отслеживаемый лог-файл: $LOGFILE"
echo "Файл для записи обнаруженных MAC-адресов: $DETECTED_MACS_FILE"

tail -F $LOGFILE | while read line; do
    echo "Чтение строки из лога: $line"
    if echo "$line" | grep -q "flip flop"; then
        MAC=$(echo "$line" | awk '{print $NF}')
        echo "Обнаружено изменение ARP-записи для MAC: $MAC"
        if ! grep -q "$MAC" $DETECTED_MACS_FILE; then
            echo "ARP spoofing detected: $MAC"
            echo "$MAC" >> $DETECTED_MACS_FILE
            # Здесь можно добавить дополнительные действия, например, отправку уведомлений
        else
            echo "MAC-адрес $MAC уже был обнаружен ранее."
        fi
    fi
done
###############################################################################################
apt-get install dsniff

sudo apt-get install arp-scan
sudo arp-scan --localnet

sudo arpspoof -i eth0 -t 10.0.2.2 10.0.2.3
sudo arpspoof -i eth0 -t 10.0.2.3 10.0.2.2