from flask import Flask, render_template, redirect, url_for, request
import os

app = Flask(__name__)

questions = [
    {
        "question": "1. Dans quelle situation un technicien utilise-t-il la commande de commutateur show interfaces ?",
        "options": [
            "A. Pour déterminer l’adresse MAC d’un périphérique réseau directement connecté sur une interface donnée",
            "B. Lorsque des paquets sont reçus d’un hôte donné qui est directement connecté",
            "C. Lorsqu’un terminal peut atteindre les périphériques locaux, et non les périphériques distants",
            "D. Pour déterminer si l’accès à distance est activé"
        ],
        "answer": "B",
        "explanation": "",
        "image": ""
    },
    {
        "question": "2. Faites correspondre le numéro d’étape à la séquence des étapes qui se produisent pendant le processus de basculement HSRP. (Les propositions ne doivent pas être toutes utilisées.)",
        "options": [
            "Étape 1 : Le routeur de transfert échoue.",
            "Étape 2 : Le routeur en veille cesse de voir les messages Hello du routeur de transfert.",
            "Étape 3 : Le routeur de secours assume le rôle du routeur de transfert en utilisant à la fois les adresses IP et MAC du routeur virtuel."
        ],
        "answer": "",
        "explanation": "",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2024-10-16_102955.jpg"
    },
    {
        "question": "3. Reportez-vous à l’illustration. Un administrateur tente de configurer une route statique IPv6 sur le routeur R1 pour atteindre le réseau connecté au routeur R2. Après la saisie de la commande de la route statique, la connectivité au réseau est toujours défaillante. Quelle erreur a été effectuée dans la configuration de la route statique ?",
        "options": [
            "A. L’adresse du tronçon suivant est incorrecte.",
            "B. Le réseau de destination est incorrect.",
            "C. L’interface est incorrecte.",
            "D. Le préfixe réseau est incorrect."
        ],
        "answer": "C",
        "explanation": "Dans cet exemple, l’interface de la route statique est incorrecte. L’interface doit être l’interface de sortie sur R1, qui est s0/0/0.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-03_221514.jpg"
    },
    {
        "question": "4. Un nouveau commutateur de couche 3 est connecté à un routeur et est en cours de configuration pour le routage InterVLAN. Quelles sont les trois étapes requises pour la configuration? (Choisissez trois propositions.)",
        "options": [
            "A. Attribution des ports au VLAN natif",
            "B. la mise en œuvre des protocoles de routage",
            "C. Attribution de ports aux VLAN",
            "D. Activation du routage IP",
            "E. Création d’interfaces SVI",
            "F. Installation d’une route statique",
            "G. Modification du VLAN par défaut"
        ],
        "answer": ["C", "D", "E"],
        "explanation": "Étape 1 : Créez les VLAN. Étape 2 : Créez les interfaces SVI VLAN. Étape 3 : Configurez les ports d’accès et attribuez-les à leurs VLAN respectifs. Étape 4 : Activez le routage IP.",
        "image": ""
    },
    {
        "question": "5. Reportez-vous à l’illustration. En fonction de la configuration et de la sortie présentées, pourquoi manque-t-il le VLAN 99 ?",
        "options": [
            "A. Parce qu’il y a un problème de câblage sur le VLAN 99",
            "B. Parce que le VLAN 1 est activé et qu’il ne peut y avoir qu’un VLAN de gestion sur le commutateur",
            "C. Parce que le VLAN 99 n’est pas un VLAN de gestion valide",
            "D. Parce que le VLAN 99 n’a pas encore été créé"
        ],
        "answer": "D",
        "explanation": "",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-03_221532.jpg"
    },
    {
        "question": "6. Quelles paires de modes d’agrégation établissent une liaison agrégée fonctionnelle entre deux commutateurs Cisco ? (Choisissez trois réponses.)",
        "options": [
            "A. dynamic auto – dynamic auto",
            "B. dynamic desirable – dynamic desirable",
            "C. dynamic desirable – trunk",
            "D. dynamic desirable – dynamic auto",
            "E. access – dynamic auto",
            "F. access – trunk"
        ],
        "answer": ["B", "C", "D"],
        "explanation": "",
        "image": ""
    },
    {
        "question": "7. Quel protocole ou technologie nécessite que les commutateurs soient en mode serveur ou client?",
        "options": [
            "A. Protocole VTP",
            "B. HSRP",
            "C. EtherChannel",
            "D. DTP"
        ],
        "answer": "A",
        "explanation": "",
        "image": ""
    },
    {
        "question": "8. Examinez l’illustration. Après avoir essayé de saisir la configuration affichée dans le routeur RTA, un administrateur reçoit une erreur et les utilisateurs du VLAN 20 signalent qu’ils ne peuvent pas communiquer avec les utilisateurs du VLAN 30. Quelle est l’origine du problème ?",
        "options": [
            "A. La commande no shutdown aurait dû être exécutée sur Fa0/0.20 et Fa0/0.30.",
            "B. RTA utilise le même sous-réseau pour le VLAN 20 et le VLAN 30.",
            "C. Fa0/0 ne contient aucune adresse à utiliser comme passerelle par défaut.",
            "D. Dot1q ne prend pas en charge les sous-interfaces."
        ],
        "answer": "B",
        "explanation": "Le problème provient du fait que RTA utilise le même sous-réseau pour les VLAN 20 et 30, ce qui empêche la communication inter-VLAN.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-03_221548.jpg"
    },
    {
        "question": "9. Quels sont les deux modes VTP qui permettent la création, la modification et la suppression des VLAN sur le commutateur local ? (Choisissez deux propositions.)",
        "options": [
            "A. client",
            "B. distribution",
            "C. principal",
            "D. serveur",
            "E. esclave",
            "F. transparent"
        ],
        "answer": ["D", "F"],
        "explanation": "Les modes VTP serveur et transparent permettent la création, la modification et la suppression des VLAN sur le commutateur local.",
        "image": ""
    },
    {
        "question": "10. Reportez-vous à l’illustration. Un administrateur réseau configure R1 pour le routage inter-VLAN entre VLAN 10 et VLAN 20. Toutefois, les périphériques du VLAN 10 et du VLAN 20 ne peuvent pas communiquer. Selon la configuration de l’exposition, quelle est la cause possible du problème ?",
        "options": [
            "A. L’encapsulation est mal configurée sur une sous-interface.",
            "B. Une commande no shutdown doit être ajoutée dans chaque configuration de sous-interface.",
            "C. La commande interface gigabitEthernet 0/0.1 est faux.",
            "D. Le port Gi0/0 doit être configuré comme port de jonction."
        ],
        "answer": "C",
        "explanation": "La commande interface gigabitEthernet 0/0.1 est fausse et empêche la communication inter-VLAN.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-03_221606.jpg"
    },
    {
        "question": "11. Un administrateur réseau est en train de configurer un WLAN. Pourquoi l’administrateur utiliserait-il un contrôleur WLAN ?",
        "options": [
            "A. pour centraliser la gestion de plusieurs réseaux WLAN",
            "B. pour fournir un service prioritaire pour les applications sensibles au temps",
            "C. pour réduire le risque d’ajout de points d’accès non autorisés au réseau",
            "D. pour faciliter la configuration de groupe et la gestion de plusieurs WLAN via un WLC"
        ],
        "answer": "D",
        "explanation": "Un contrôleur WLAN facilite la gestion centralisée de plusieurs WLAN via un contrôleur de gestion sans fil (WLC).",
        "image": ""
    },
    {
        "question": "12. Associez la description au type de VLAN correct. (Les options ne sont pas toutes utilisées.)",
        "options": [
            "VLAN par défaut : tous les ports de commutateur sont attribués à ce VLAN après le démarrage initial du commutateur.",
            "VLAN de données : configuration destinée à acheminer le trafic généré par l’utilisateur.",
            "VLAN natif : acheminement du trafic non étiqueté.",
            "VLAN de gestion : une adresse IP et un masque de sous-réseau sont attribués à ce VLAN, ce qui permet l’accès au commutateur via HTTP, Telnet, SSH ou SNMP."
        ],
        "answer": [
            "VLAN par défaut : tous les ports de commutateur sont attribués à ce VLAN après le démarrage initial du commutateur.",
            "VLAN de données : configuration destinée à acheminer le trafic généré par l’utilisateur.",
            "VLAN natif : acheminement du trafic non étiqueté.",
            "VLAN de gestion : une adresse IP et un masque de sous-réseau sont attribués à ce VLAN, ce qui permet l’accès au commutateur via HTTP, Telnet, SSH ou SNMP."
        ],
        "explanation": "Les VLANs par défaut, de données, natifs et de gestion ont des rôles différents dans un réseau commuté, permettant de gérer efficacement le trafic et l'administration du commutateur.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2024-10-15_185331.jpg"
    },
    {
        "question": "13. Examinez l’illustration. Comment une trame envoyée depuis PCA est-elle transmise à PCC si la table d’adresses MAC du commutateur SW1 est vide ?",
        "options": [
            "A. SW1 abandonne la trame car il ne connaît pas l’adresse MAC de destination.",
            "B. SW1 diffuse la trame sur tous les ports de SW1, à l’exception du port d’entrée de la trame dans le commutateur.",
            "C. SW1 diffuse la trame sur tous les ports du commutateur, à l’exception du port interconnecté au commutateur SW2 et du port d’entrée de la trame dans le commutateur.",
            "D. SW1 transmet la trame directement à SW2. SW2 diffuse la trame sur tous les ports connectés à SW2, à l’exception du port d’entrée de la trame dans le commutateur."
        ],
        "answer": "B",
        "explanation": "Si la table d’adresses MAC est vide, le commutateur diffuse la trame sur tous les ports, sauf celui d’entrée.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-03_222651.jpg"
    },
    {
        "question": "14. Associez l’état de la liaison au statut d’interface et de protocole. (Les options ne sont pas toutes utilisées.)",
        "options": [
            "operational : up/up",
            "problème de couche 1 : down/down",
            "problème de couche 2 : up/down",
            "désactivé : Désactivé par un administrateur"
        ],
        "answer": [
            "operational : up/up",
            "problème de couche 1 : down/down",
            "problème de couche 2 : up/down",
            "désactivé : Désactivé par un administrateur"
        ],
        "explanation": "Les différents statuts d’interface sont associés à l’état de la liaison, selon qu'il y a un problème de couche 1, 2, ou si l’interface est désactivée.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2024-10-15_201613.jpg"
    },
    {
        "question": "15. Quel est le moyen d’avoir une configuration sécurisée pour l’accès à distance à un appareil sur le réseau ?",
        "options": [
            "A. Configurer SSH.",
            "B. Configurer Telnet.",
            "C. Configurer une ACL et l’appliquer aux lignes VTY.",
            "D. Configurer 802.1x."
        ],
        "answer": "",
        "explanation": "",
        "image": ""
    },
    {
        "question": "16. Examinez l’illustration. L’hôte A a envoyé un paquet à l’hôte B. Quelles sont les adresses IP et MAC source sur le paquet lorsqu’il atteint l’hôte B ?",
        "options": [
            "A. MAC source : 00E0.FE10.17A3, IP source : 192.168.1.1",
            "B. MAC source : 00E0.FE10.17A3, IP source : 10.1.1.10",
            "C. MAC source : 00E0.FE91.7799, IP source : 192.168.1.1",
            "D. MAC source : 00E0.FE91.7799, IP source : 10.1.1.10",
            "E. MAC source : 00E0.FE91.7799, IP source : 10.1.1.1"
        ],
        "answer": "D",
        "explanation": "Les adresses de couche 2 changeront à chaque saut, mais les adresses de couche 3 restent les mêmes.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-03_222840.jpg"
    },
    {
        "question": "17. Reportez-vous à l’illustration. Quels sont les rôles possibles pour les ports A, B, C et D dans ce réseau RSTP ?",
        "options": [
            "A. Désigné, racine, alternatif, racine",
            "B. Désigné, alternatif, racine, racine",
            "C. Alternatif, désigné, racine, racine",
            "D. Alternatif, racine, désigné, racine"
        ],
        "answer": "C",
        "explanation": "S1 est le pont racine, B est un port désigné, et C et D sont des ports racine.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-23_164220.png"
    },
    {
        "question": "18. Plusieurs actions peuvent pallier une attaque de VLAN. Citez-en trois. (Choisissez trois propositions.)",
        "options": [
            "A. Activer la fonction de protection BPDU.",
            "B. Utiliser des VLAN privés.",
            "C. Activer manuellement le trunking.",
            "D. Faire d’un VLAN inutilisé le VLAN natif.",
            "E. Désactiver le protocole DTP.",
            "F. Activer la fonction de protection de source."
        ],
        "answer": "C, D, E",
        "explanation": "Désactiver DTP, configurer manuellement les trunks et définir des VLANs natifs inutilisés aident à atténuer les attaques de VLAN.",
        "image": ""
    },
    {
        "question": "19. Quelle méthode de chiffrement sans fil offre la meilleure sécurité ?",
        "options": [
            "A. WPA2 avec AES",
            "B. WPA2 avec TKIP",
            "C. WEP",
            "D. WPA"
        ],
        "answer": "A",
        "explanation": "WPA2 avec AES est le plus sécurisé des protocoles de chiffrement sans fil.",
        "image": ""
    },
    {
        "question": "20. Après qu’un hôte a généré une adresse IPv6 à l’aide du processus DHCPv6 ou SLAAC, comment l’hôte vérifie-t-il que l’adresse est unique et donc utilisable ?",
        "options": [
            "A. L’hôte envoie un message de demande d’écho ICMPv6 à l’adresse DHCPv6 ou SLAAC apprise et si aucune réponse n’est renvoyée, l’adresse est considérée comme unique.",
            "B. L’hôte vérifie le cache du voisin local pour l’adresse apprise et si l’adresse n’est pas mise en cache, il est considéré comme unique.",
            "C. L’hôte envoie une diffusion ARP vers le lien local et si aucun hôte n’envoie de réponse, l’adresse est considérée comme unique.",
            "D. L’hôte envoie un message de sollicitation de voisin ICMPv6 à l’adresse DHCP ou SLAAC apprise et si aucune annonce de voisin n’est renvoyée, l’adresse est considérée comme unique."
        ],
        "answer": "D",
        "explanation": "L’hôte envoie une sollicitation de voisin ICMPv6 pour vérifier l’unicité de l’adresse IPv6.",
        "image": ""
    },
    {
        "question": "21. Un administrateur tente de supprimer des configurations d’un commutateur. Après avoir exécuté la commande erase startup-config et rechargé le commutateur, l’administrateur constate que les VLAN 10 et 100 existent toujours dans le commutateur. Pourquoi ces VLAN n’ont-ils pas été supprimés ?",
        "options": [
            "A. Ces VLAN étant enregistrés dans un fichier appelé vlan.dat qui se trouve dans la mémoire Flash, ce fichier doit être supprimé manuellement.",
            "B. Ces VLAN ne peuvent pas être supprimés, sauf si le commutateur est en mode client VTP.",
            "C. Ces VLAN peuvent être uniquement supprimés du commutateur au moyen des commandes no vlan 10 et no vlan 100.",
            "D. Ces VLAN sont des VLAN par défaut et ne peuvent pas être supprimés."
        ],
        "answer": "A",
        "explanation": "Les VLANs sont stockés dans un fichier vlan.dat dans la mémoire Flash. Ce fichier doit être supprimé manuellement.",
        "image": ""
    },
    {
        "question": "22. Examinez l’illustration. Un administrateur réseau configure le routage inter-VLAN sur un réseau. Pour l’instant, un seul VLAN est utilisé, mais d’autres seront ajoutés prochainement. Quel est le rôle du paramètre manquant, indiqué par un point d’interrogation mis en surbrillance dans l’illustration ?",
        "options": [
            "A. Il identifie le numéro du VLAN.",
            "B. Il identifie la sous-interface.",
            "C. Il identifie le numéro du VLAN natif.",
            "D. Il identifie le type d’encapsulation utilisé.",
            "E. Il identifie le nombre d’hôtes autorisés sur l’interface."
        ],
        "answer": "A",
        "explanation": "Le paramètre manquant identifie le numéro du VLAN.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-19_223727.jpg"
    },
    {
        "question": "23. Après avoir attaché quatre PC aux ports du commutateur, configuré le SSID et défini les propriétés d’authentification pour un petit réseau de bureau, un technicien teste avec succès la connectivité de tous les PC connectés au commutateur et au WLAN. Un pare-feu est ensuite configuré sur le périphérique avant de le connecter à Internet. Quel type de périphérique réseau inclut toutes les fonctionnalités décrites?",
        "options": [
            "A. Commutateur",
            "B. Pare-feu",
            "C. Point d’accès sans fil autonome",
            "D. Routeur sans fil"
        ],
        "answer": "D",
        "explanation": "Un routeur sans fil combine les fonctions de commutateur, point d’accès sans fil et pare-feu.",
        "image": ""
    },
    {
        "question": "24. Associez les types de message DHCP à l’ordre du processus DHCPv4. (Les options ne doivent pas être toutes utilisées.)",
        "options": [
            "A. Étape 1 : DHCPDISCOVER",
            "B. Étape 2 : DHCPOFFER",
            "C. Étape 3 : DHCPREQUEST",
            "D. Étape 4 : DHCPACK"
        ],
        "answer": "",
        "explanation": "",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2024-10-15_161502.jpg"
    },
    
    {
        "question": "25. Quel est l’objectif de la commande suivante : `ip route 0.0.0.0 0.0.0.0 serial 0/1/1` ?",
        "options": [
            "A. Les paquets dont le réseau de destination n’est ni 10.10.0.0/16 ni 10.20.0.0/16, ou dont le réseau de destination n’est pas connecté directement seront transférés à Internet.",
            "B. Les paquets reçus depuis Internet seront transférés à l’un des LAN connectés à R1 ou à R2.",
            "C. Les paquets destinés aux réseaux qui ne figurent pas dans la table de routage de HQ seront abandonnés.",
            "D. Les paquets provenant du réseau 10.10.0.0/16 seront transférés au réseau 10.20.0.0/16, et les paquets provenant du réseau 10.20.0.0/16 seront transférés au réseau 10.10.0.0/16."
        ],
        "answer": "A",
        "explanation": "La commande `ip route 0.0.0.0 0.0.0.0` définit une route par défaut qui dirige les paquets vers Internet.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-19_224526.jpg"
    },
    {
        "question": "26. Quelle adresse MAC de destination est utilisée lorsque des trames sont envoyées depuis la station de travail vers la passerelle par défaut ?",
        "options": [
            "A. Les adresses MAC du routeur de transfert et du routeur en veille.",
            "B. L’adresse MAC du routeur de transfert",
            "C. L’adresse MAC du routeur en veille",
            "D. L’adresse MAC du routeur virtuel"
        ],
        "answer": "D",
        "explanation": "L’adresse IP du routeur virtuel fait office de passerelle par défaut pour tous les postes de travail. Par conséquent, l’adresse MAC renvoyée par le protocole de résolution d’adresse au poste de travail sera l’adresse MAC du routeur virtuel.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-19_225318.jpg"
    },
    {
        "question": "27. Si le protocole STP fonctionne, quel sera le résultat final lorsqu’un administrateur réseau a relié deux commutateurs via la technologie EtherChannel ?",
        "options": [
            "A. Les commutateurs équilibreront la charge et utiliseront les deux EtherChannels pour transférer les paquets.",
            "B. La boucle générée créera une tempête de diffusion.",
            "C. STP bloquera une des liaisons redondantes.",
            "D. Les deux canaux de port seront fermés."
        ],
        "answer": "C",
        "explanation": "STP (Spanning Tree Protocol) bloque les liens redondants pour éviter les boucles.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-19_225512.jpg"
    },
    {
        "question": "28. Quelle route statique un technicien informatique doit-il saisir pour créer une route de secours vers le réseau 172.16.1.0 qui sera utilisée uniquement en cas de défaillance de la route principale associée à RIP ?",
        "options": [
            "A. ip route 172.16.1.0 255.255.255.0 s0/0/0 121",
            "B. ip route 172.16.1.0 255.255.255.0 s0/0/0 111",
            "C. ip route 172.16.1.0 255.255.255.0 s0/0/0 91",
            "D. ip route 172.16.1.0 255.255.255.0 s0/0/0"
        ],
        "answer": "A",
        "explanation": "Une route statique de secours, appelée route statique flottante, utilise une distance administrative plus élevée que la route principale.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-19_225649.jpg"
    },
    {
        "question": "29. Quel est l’effet de l’entrée de la commande de configuration `shutdown` sur un commutateur ?",
        "options": [
            "A. Il active portfast sur une interface de commutateur spécifique.",
            "B. Il désactive un port inutilisé.",
            "C. Il désactive le DTP sur une interface non-trunking.",
            "D. Il active la garde BPDU sur un port spécifique."
        ],
        "answer": "B",
        "explanation": "La commande `shutdown` désactive un port inutilisé sur un commutateur.",
        "image": ""
    },
    {
        "question": "30. Quelles sont les trois normes Wi-Fi fonctionnant dans la plage de fréquences 2,4 GHz ? (Choisissez trois réponses.)",
        "options": [
            "A. 802.11b",
            "B. 802.11a",
            "C. 802.11ac",
            "D. 802.11n",
            "E. 802.11g"
        ],
        "answer": "A, D, E",
        "explanation": "Les normes Wi-Fi fonctionnant dans la bande de fréquence 2,4 GHz sont 802.11b, 802.11n et 802.11g.",
        "image": ""
    },
    {
        "question": "31. Comment la configuration d’un SSID avec une bande de fréquences de 5 GHz améliore-t-elle les performances d’un réseau sans fil pour des services multimédias de transmission en continu ?",
        "options": [
            "A. La bande 5 GHz offre une plage plus étendue et est donc susceptible de ne pas comporter d’interférences.",
            "B. La bande 5 GHz offre davantage de canaux et est moins encombrée que la bande 2,4 GHz. Elle convient donc mieux à la transmission multimédia en continu.",
            "C. Obliger les utilisateurs à passer à la bande 5 GHz pour la transmission multimédia en continu est peu pratique et limite le nombre d’utilisateurs accédant à ces services.",
            "D. Les seuls utilisateurs pouvant basculer vers la bande 5 GHz sont ceux disposant des cartes réseau les plus récentes, ce qui permet de limiter l’utilisation."
        ],
        "answer": "B",
        "explanation": "La bande 5 GHz offre plus de canaux et est moins encombrée que la bande 2,4 GHz, ce qui améliore les performances du réseau pour des services multimédias.",
        "image": ""
    },
    {
        "question": "32. Sélectionnez les trois modes d’établissement de canaux PAgP. (Choisissez trois propositions.)",
        "options": [
            "A. actif",
            "B. étendu",
            "C. Activé",
            "D. desirable",
            "E. automatique",
            "F. passif"
        ],
        "answer": "A, D, E",
        "explanation": "Les trois modes d’établissement de canaux PAgP sont actif, desirable et automatique.",
        "image": ""
    },
    {
        "question": "33. Que peut-on conclure de la sortie de la commande `show port-security interface fa 0/2` ? (Choisissez trois propositions.)",
        "options": [
            "A. Le port est configuré en tant que liaison de trunk.",
            "B. Les violations de sécurité entraîneront l’arrêt immédiat de ce port.",
            "C. Ce port est actuellement en service.",
            "D. Le mode de port de commutation pour cette interface est le mode d’accès.",
            "E. Trois violations de sécurité ont été détectées sur cette interface.",
            "F. Aucun périphérique n’est actuellement connecté à ce port."
        ],
        "answer": "B, C, D",
        "explanation": "La sortie montre que le port est actif et que des violations de sécurité entraîneraient son arrêt. Le mode de port est d’accès.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-19_230812.jpg"
    },
    {
        "question": "34. Quel protocole doit être désactivé pour pallier les attaques de VLAN ?",
        "options": [
            "A. CDP",
            "B. STP",
            "C. DTP",
            "D. ARP"
        ],
        "answer": "C",
        "explanation": "Le protocole DTP (Dynamic Trunking Protocol) doit être désactivé pour éviter les attaques liées aux VLAN.",
        "image": ""
    },
    
    {
        "question": "35. Quelle technique d’atténuation empêcherait les serveurs malveillants de fournir de faux paramètres de configuration IP aux clients ?",
        "options": [
            "A. mise en œuvre des solutions de sécurisation des ports",
            "B. mise en œuvre de la sécurité des ports sur les ports périphériques",
            "C. désactivation des ports CDP sur les ports périphériques",
            "D. activation de l’espionnage DHCP"
        ],
        "answer": "D. activation de l’espionnage DHCP",
        "explanation": "L'activation de l'espionnage DHCP empêche les serveurs malveillants de fournir de faux paramètres IP.",
        "image": ""
    },
    {
        "question": "36. Quelle méthode d’attribution de préfixe IPv6 repose sur le préfixe contenu dans les messages RA?",
        "options": [
            "A. statique",
            "B. DHCPv6 dynamique",
            "C. SLAAC",
            "D. EUI-64"
        ],
        "answer": "C. SLAAC",
        "explanation": "SLAAC (Stateless Address Autoconfiguration) utilise le préfixe contenu dans les messages RA pour configurer les adresses IPv6.",
        "image": ""
    },
    {
        "question": "37. Un analyste de la cybersécurité utilise l’outil macof pour évaluer la configuration des commutateurs déployés dans le réseau de base d’une organisation. Quel type d’attaque LAN l’analyste cible-t-il au cours de cette évaluation?",
        "options": [
            "A. Usurpation DHCP (ou spoofing)",
            "B. Sauts VLAN",
            "C. Débordement de la table d’adresses IP",
            "D. Double marquage VLAN"
        ],
        "answer": "C. Débordement de la table d’adresses IP",
        "explanation": "L'outil macof est utilisé pour provoquer un débordement de la table d'adresses MAC d'un commutateur.",
        "image": ""
    },
    {
        "question": "38. Au cours du processus AAA, quand l’autorisation est-elle implémentée ?",
        "options": [
            "A. dès que la fonction de traçabilité et d’audit AAA a reçu des rapports détaillés",
            "B. immédiatement après une authentification réussie auprès d’une source de données AAA",
            "C. aussitôt qu’un client AAA a envoyé des informations d’authentification à un serveur centralisé",
            "D. dès que les ressources accessibles à un utilisateur ont été déterminées"
        ],
        "answer": "B. immédiatement après une authentification réussie auprès d’une source de données AAA",
        "explanation": "L'autorisation est mise en œuvre après une authentification réussie, permettant l'accès aux ressources en fonction des droits de l'utilisateur.",
        "image": ""
    },
    {
        "question": "39. Examinez l’illustration. Un ingénieur réseau configure le routage IPv6 sur le réseau. Quelle commande exécutée sur le routeur HQ permet de configurer une route par défaut vers Internet en vue de transférer les paquets vers un réseau de destination IPv6 qui n’est pas répertorié dans la table de routage ?",
        "options": [
            "A. ipv6 route ::/0 serial 0/0/0",
            "B. ipv6 route ::/0 serial 0/1/1",
            "C. ipv6 route ::1/0 serial 0/1/1",
            "D. ip route 0.0.0.0 0.0.0.0 serial 0/1/1"
        ],
        "answer": "B. ipv6 route ::/0 serial 0/1/1",
        "explanation": "La commande `ipv6 route ::/0 serial 0/1/1` configure une route par défaut vers Internet pour les paquets IPv6 non répertoriés.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-19_231809.jpg"
    },
    {
        "question": "40. Quel type de route statique est configuré avec une plus grande distance administrative pour fournir une route de secours vers une route associée à un protocole de routage dynamique ?",
        "options": [
            "A. route statique flottante",
            "B. Route statique récapitulative",
            "C. Route statique par défaut",
            "D. route statique standard"
        ],
        "answer": "A. route statique flottante",
        "explanation": "Les routes statiques flottantes ont une distance administrative plus élevée que les routes dynamiques, et sont utilisées comme route de secours.",
        "image": ""
    },
    {
        "question": "41. Quelle réponse indique une route statique par défaut IPv4 correctement configurée ?",
        "options": [
            "A. ip route 0.0.0.0 255.255.255.255 S0/0/0",
            "B. ip route 0.0.0.0 255.255.255.0 S0/0/0",
            "C. ip route 0.0.0.0 255.0.0.0 S0/0/0",
            "D. ip route 0.0.0.0 0.0.0.0 S0/0/0"
        ],
        "answer": "D. ip route 0.0.0.0 0.0.0.0 S0/0/0",
        "explanation": "La route statique par défaut `ip route 0.0.0.0 0.0.0.0` redirige tout le trafic vers le S0/0/0.",
        "image": ""
    },
    {
        "question": "42. Reportez-vous à l’illustration. Quelle commande de route statique peut être entrée sur R1 pour transférer le trafic vers le réseau local connecté à R2?",
        "options": [
            "A. ipv6 route 2001:db8:12:10::/64 S0/0/0 fe80::2",
            "B. ipv6 route 2001:db8:12:10::/64 S0/0/1 2001:db8:12:10::1",
            "C. ipv6 route 2001:db8:12:10::/64 S0/0/0",
            "D. ipv6 route 2001:db8:12:10::/64 S0/0/1 fe80::2"
        ],
        "answer": "D. ipv6 route 2001:db8:12:10::/64 S0/0/1 fe80::2",
        "explanation": "La commande `ipv6 route` avec l'interface et l'adresse de saut suivant est utilisée pour diriger le trafic vers le réseau local connecté à R2.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-19_232325.jpg"
    },
    {
        "question": "43. Examinez l’illustration. Quelle métrique permet de transférer un paquet de données avec l’adresse de destination IPv6 2001:DB8:ACAD:E:240:BFF:FED4:9DD2 ?",
        "options": [
            "A. 90",
            "B. 128",
            "C. 2170112",
            "D. 2681856",
            "E. 2682112",
            "F. 3193856"
        ],
        "answer": "E. 2682112",
        "explanation": "La métrique de 2682112 est utilisée pour transférer le paquet IPv6 vers la destination spécifiée.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-19_232532.jpg"
    },
    {
        "question": "44. Examinez l’illustration. Le routeur R1 entretient une relation de voisinage OSPF avec le routeur du FAI sur le réseau 192.168.0.32. La liaison réseau 192.168.0.36 doit servir de liaison de secours si la liaison OSPF tombe en panne. La commande de route statique flottante ip route 0.0.0.0 0.0.0.0 S0/0/1 100 a été exécutée sur R1 et, à présent, le trafic utilise la liaison de secours même lorsque la liaison OSPF est activée et opérationnelle. Quelle modification doit être apportée à la commande de route statique afin que le trafic utilise obligatoirement la liaison OSPF lorsque celle-ci est active ?",
        "options": [
            "A. Configuration du réseau de destination sur 192.168.0.34.",
            "B. Ajout de l’adresse voisine du tronçon suivant, à savoir 192.168.0.36.",
            "C. Réglage de la distance administrative sur 1.",
            "D. Réglage de la distance administrative sur 120."
        ],
        "answer": "D. Réglage de la distance administrative sur 120.",
        "explanation": "La distance administrative doit être réglée sur une valeur plus élevée que celle d’OSPF (qui est de 110), afin que le routeur utilise OSPF lorsque la liaison est active.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-19_232636.jpg"
    },
    {
        "question": "45. Reportez-vous à l’illustration. Quelle commande de routage peut être entrée sur R1 pour activer une route par défaut pour le réseau IPv6 ?",
        "options": [
            "A. ipv6 route ::/0 serial 0/0/0",
            "B. ipv6 route ::/0 serial 0/1/1",
            "C. ipv6 route 2001:db8::/64 serial 0/0/0",
            "D. ipv6 route 2001:db8::/64 serial 0/1/1"
        ],
        "answer": "B. ipv6 route ::/0 serial 0/1/1",
        "explanation": "La commande `ipv6 route ::/0 serial 0/1/1` configure une route par défaut pour le trafic IPv6.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-19_233015.jpg"
    },

    {
        "question": "47. Quels sont les deux types de protocoles STP pouvant générer des flux de trafic non optimaux parce qu’ils ne supposent qu’une seule instance Spanning Tree pour le réseau ponté entier ? (Choisissez deux réponses.)",
        "options": [
            "A. MSTP",
            "B. STP",
            "C. RSTP",
            "D. PVST+",
            "E. Rapid PVST+"
        ],
        "answer": "B, C",
        "explanation": "STP et RSTP supposent une seule instance Spanning Tree pour l’ensemble du réseau, ce qui peut générer des flux de trafic non optimaux.",
        "image": ""
    },
    {
        "question": "48. Pour obtenir un aperçu de l’état du mode Spanning Tree d’un réseau commuté, un technicien réseau exécute la commande show spanning-tree sur un commutateur. Quelles informations cette commande permet-elle d’afficher ? (Choisissez deux réponses.)",
        "options": [
            "A. L’adresse IP de l’interface VLAN de gestion.",
            "B. L’ID de pont racine.",
            "C. Le statut des ports VLAN natifs.",
            "D. Le rôle des ports sur tous les VLAN.",
            "E. Le nombre de diffusions reçues sur chaque port racine."
        ],
        "answer": "B, D",
        "explanation": "La commande `show spanning-tree` affiche l'ID du pont racine ainsi que le rôle des ports sur tous les VLAN.",
        "image": ""
    },
    {
        "question": "49. Examinez l’illustration. Quelles sont les deux conclusions pouvant être tirées du résultat ? (Choisissez deux réponses.)",
        "options": [
            "A. Le canal de port est un canal de couche 3.",
            "B. La méthode d’équilibrage de charge utilisée est le port source vers le port de destination.",
            "C. La liaison EtherChannel est en panne.",
            "D. Le groupement est pleinement opérationnel.",
            "E. L’ID de canal de port correspond à 2."
        ],
        "answer": "C, E",
        "explanation": "L’illustration montre que la liaison EtherChannel est en panne, et l’ID de canal de port correspond à 2.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-19_233605.jpg"
    },
    {
        "question": "50. Quelle action se déroule lorsqu’une trame entrant dans un commutateur a une adresse MAC de destination monodiffusion apparaissant dans la table d’adresses MAC ?",
        "options": [
            "A. Le commutateur réinitialise le minuteur d’actualisation sur toutes les entrées de table d’adresses MAC.",
            "B. Le commutateur met à jour le minuteur d’actualisation de l’entrée.",
            "C. Le commutateur transmet la trame à tous les ports, sauf au port d’arrivée.",
            "D. Le commutateur transmet le cadre hors du port spécifié."
        ],
        "answer": "D",
        "explanation": "Lorsque la trame est destinée à une adresse MAC présente dans la table, le commutateur transmet la trame au port spécifié.",
        "image": ""
    },
    {
        "question": "51. Reportez-vous à l’illustration. Un administrateur réseau a ajouté un nouveau sous-réseau au réseau et veut que les hôtes du sous-réseau reçoivent des adresses IPv4 du serveur DHCPv4. Quelles commandes permettent aux hôtes du nouveau sous-réseau de recevoir des adresses du serveur DHCPv4 ? (Choisissez deux réponses.)",
        "options": [
            "A. R1(config)# interface G0/0",
            "B. R1(config)# interface G0/1",
            "C. R1(config-if)# ip helper-address 10.1.0.254",
            "D. R2(config-if)# ip helper-address 10.2.0.250",
            "E. R1(config-if)# ip helper-address 10.2.0.250",
            "F. R2(config)# interface G0/0"
        ],
        "answer": "A, E",
        "explanation": "Les commandes `ip helper-address` permettent de configurer un routeur comme relais DHCPv4 pour transmettre les demandes des hôtes du sous-réseau au serveur DHCP.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-19_235737.jpg"
    },
    {
        "question": "52. Quelle action prend un client DHCPv4 s’il reçoit plus d’un DHCPOFFER de plusieurs serveurs DHCP ?",
        "options": [
            "A. Il envoie un DHCPNAK et recommence le processus DHCP.",
            "B. Il envoie un DHCPREQUEST qui identifie l’offre de location que le client accepte.",
            "C. Il rejette les deux offres et envoie un nouveau DHCPDISCOVER.",
            "D. Il accepte les deux messages DHCPOFFER et envoie un DHCPACK."
        ],
        "answer": "B",
        "explanation": "Le client DHCPv4 envoie un `DHCPREQUEST` pour accepter une des offres reçues.",
        "image": ""
    },
    {
        "question": "53. Examinez l’illustration. Si les adresses IP du routeur de passerelle par défaut et du serveur de noms de domaine (DNS) sont correctes, quel est le problème de cette configuration ?",
        "options": [
            "A. Les commandes default-router et dns-server doivent être configurées avec des masques de sous-réseau.",
            "B. L’adresse IP du serveur de noms de domaine (DNS) ne figure pas dans la liste d’adresses exclues.",
            "C. L’adresse IP du routeur de passerelle par défaut ne figure pas dans la liste d’adresses exclues.",
            "D. Le serveur de noms de domaine (DNS) et le routeur de passerelle par défaut doivent faire partie du même sous-réseau."
        ],
        "answer": "C",
        "explanation": "L’adresse IP du routeur de passerelle par défaut ne doit pas être attribuée aux hôtes, elle doit être exclue.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-19_235457.jpg"
    },
    {
        "question": "54. Les utilisateurs de la succursale ont pu accéder à un site le matin, mais n’ont pas eu de connectivité avec le site depuis l’heure du déjeuner. Que faut-il faire ou vérifier ?",
        "options": [
            "A. Vérifiez la configuration sur l’itinéraire statique flottant et ajustez l’AD.",
            "B. Utilisez la commande « show ip interface brief » pour voir si une interface est en panne.",
            "C. Créez un itinéraire statique flottant vers ce réseau.",
            "D. Vérifiez que la route statique vers le serveur est présente dans la table de routage."
        ],
        "answer": "B",
        "explanation": "La commande `show ip interface brief` permet de vérifier si une interface est en panne, ce qui pourrait expliquer la perte de connectivité.",
        "image": ""
    },
    {
        "question": "55. Associez la caractéristique de transmission à son type. (Les options ne sont pas toutes utilisées.)",
        "options": [
            "A. Full-duplex",
            "B. Half-duplex",
            "C. Simplex"
        ],
        "answer": "",
        "explanation": "",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-03_224759.jpg"
    },
    {
        "question": "56. Quelles informations un commutateur utilise-t-il pour renseigner la table d’adresses MAC ?",
        "options": [
            "A. Les adresses MAC source et de destination et le port entrant",
            "B. L’adresse MAC de destination et le port sortant",
            "C. Les adresses MAC source et de destination et le port sortant",
            "D. L’adresse MAC source et le port sortant",
            "E. L’adresse MAC de destination et le port entrant"
        ],
        "answer": "A",
        "explanation": "Un commutateur utilise l’adresse MAC source et le port entrant pour mettre à jour sa table d’adresses MAC.",
        "image": ""
    },
    {
        "question": "57. Pour quelles raisons un administrateur réseau segmenterait-il un réseau avec un commutateur de couche 2 ? (Choisissez deux réponses.)",
        "options": [
            "A. Pour créer moins de domaines de collision.",
            "B. Pour éliminer les circuits virtuels.",
            "C. Pour créer plus de domaines de diffusion.",
            "D. Pour isoler les messages de requête ARP du reste du réseau.",
            "E. Pour isoler le trafic entre les segments.",
            "F. Pour améliorer la bande passante utilisateur."
        ],
        "answer": "E, F",
        "explanation": "Segmenter un réseau avec un commutateur de couche 2 peut améliorer la bande passante et isoler le trafic entre les segments.",
        "image": ""
    },
    {
        "question": "58. Un technicien dépannage un WLAN lent et décide d’utiliser l’approche de répartition du trafic. Quels deux paramètres devraient être configurés pour le faire ? (Choisissez deux propositions.)",
        "options": [
            "A. Configurer le mode de sécurité sur WPA Personal TKIP/AES pour un réseau et WPA2 Personal AES pour l’autre réseau.",
            "B. Configurez le mode de sécurité sur WPA Personal TKIP/AES pour les deux réseaux.",
            "C. Configurez la bande 5 GHz pour le streaming multimédia et le trafic temporel.",
            "D. Configurez un SSID commun pour les deux réseaux fractionnés.",
            "E. Configurez la bande 2,4 GHz pour le trafic Internet de base qui n’est pas sensible au temps."
        ],
        "answer": "C, E",
        "explanation": "Pour améliorer la répartition du trafic, configurez des bandes 5 GHz pour le trafic multimédia et 2,4 GHz pour les applications Internet de base.",
        "image": ""
    },
    {
        "question": "59. Sur un Cisco 3504 WLC Summary page ( Advanced > Summary ), quel onglet permet à un administrateur réseau de configurer un WLAN particulier avec une stratégie WPA2 ?",
        "options": [
            "A. SÉCURITÉ",
            "B. SANS FIL",
            "C. Réseaux locaux sans fil",
            "D. GESTION"
        ],
        "answer": "C",
        "explanation": "L’onglet 'Réseaux locaux sans fil' permet de configurer un WLAN avec une stratégie WPA2.",
        "image": ""
    },
    
    {
        "question": "60. Un administrateur réseau ajoute un nouveau WLAN sur un WLC Cisco 3500. Quel onglet l’administrateur doit-il utiliser pour créer une nouvelle interface VLAN à utiliser pour le nouveau WLAN?",
        "options": [
            "A. GESTION",
            "B. CONTRÔLEUR",
            "C. Réseaux locaux sans fil",
            "D. SANS FIL"
        ],
        "answer": "B. CONTRÔLEUR",
        "explanation": "",
        "image": ""
    },
    {
        "question": "61. Quel est l’effet de l’entrée de la commande de configuration switchport mode access sur un commutateur?",
        "options": [
            "A. Il spécifie le nombre maximal d’adresses L2 autorisées sur un port.",
            "B. Il désactive le PAO sur une interface non-trunking.",
            "C. Il active le DAI sur des interfaces de commutation spécifiques précédemment configurées avec la surveillance DHCP.",
            "D. Il active manuellement un lien de trunk."
        ],
        "answer": "B. Il désactive le PAO sur une interface non-trunking.",
        "explanation": "",
        "image": ""
    },
    {
        "question": "62. Reportez-vous à l’illustration. L’administrateur réseau configure les deux commutateurs comme illustré. Cependant, l’hôte C ne peut envoyer de requête ping à l’hôte D et l’hôte E ne peut envoyer de requête ping à l’hôte F. Quelle action l’administrateur doit-il effectuer pour activer cette communication ?",
        "options": [
            "A. Inclure un routeur dans la topologie.",
            "B. Associer les hôtes A et B avec le VLAN 10 au lieu du VLAN 1.",
            "C. Configurer un port trunk en mode dynamic desirable.",
            "D. Supprimer le VLAN natif de l’agrégation.",
            "E. Ajouter la commande switchport nonegotiate à la configuration de SW2."
        ],
        "answer": "C. Configurer un port trunk en mode dynamic desirable.",
        "explanation": "",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-20_095045.jpg"
    },
    {
        "question": "63. Associez l’étape à la description de la séquence d’amorçage du commutateur correspondante. (Les options ne doivent pas être toutes utilisées.)",
        "options": [
            "A. Étape 1 : Exécution du POST",
            "B. Étape 2 : Chargement du programme d’amorçage à partir de la mémoire morte (ROM)",
            "C. Étape 3 : Initialisations du registre du processeur",
            "D. Étape 4 : Initialisation du système de fichiers Flash",
            "E. Étape 5 : Charger le logiciel IOS",
            "F. Étape 6 : Contrôle de la commutation de transfert à l’IOS"
        ],
        "answer": "",
        "explanation": "",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2024-10-16_070315.jpg"
    },
    {
        "question": "64. Reportez-vous à l’illustration. Supposons que le courant vient juste d’être rétabli. PC3 émet une requête de diffusion DHCP IPv4. À quel port SW1 transmet-il cette requête ?",
        "options": [
            "A. À Fa0/1, à Fa0/2 et à Fa0/3 uniquement",
            "B. À Fa0/1, à Fa0/2 et à Fa0/4 uniquement",
            "C. À Fa0/1 uniquement",
            "D. À Fa0/1, à Fa0/2, à Fa0/3 et à Fa0/4",
            "E. À Fa0/1 et à Fa0/2 uniquement"
        ],
        "answer": "A. À Fa0/1, à Fa0/2 et à Fa0/3 uniquement.",
        "explanation": "",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-20_095409.jpg"
    },
    {
        "question": "65. Quel préfixe IPv6 est conçu pour la communication lien-local?",
        "options": [
            "A. 2001::/3",
            "B. fe80::/10",
            "C. fc::/07",
            "D. ff00::/8"
        ],
        "answer": "B. fe80::/10",
        "explanation": "",
        "image": ""
    },
    {
        "question": "66. Comment un routeur gère-t-il le routage statique si Cisco Express Forwarding est désactivé ?",
        "options": [
            "A. Il n’effectue pas de recherches récursives.",
            "B. Les interfaces série point à point nécessitent des routes statiques entièrement spécifiées pour éviter des incohérences au niveau du routage.",
            "C. Les interfaces Ethernet à accès multiple nécessitent des routes statiques entièrement spécifiées pour éviter des incohérences au niveau du routage.",
            "D. Les routes statiques utilisant une interface de sortie sont inutiles."
        ],
        "answer": "C. Les interfaces Ethernet à accès multiple nécessitent des routes statiques entièrement spécifiées pour éviter des incohérences au niveau du routage.",
        "explanation": "Lorsque Cisco Express Forwarding est désactivé, les interfaces Ethernet nécessitent des routes statiques complètement spécifiées pour éviter les incohérences dans la table de routage.",
        "image": ""
    },
    {
        "question": "67. Reportez-vous à l’illustration. Que peut-on conclure de la configuration affichée sur R1?",
        "options": [
            "A. R1 fonctionne comme un serveur DHCPv4.",
            "B. R1 enverra un message à un client DHCPv4 local pour contacter un serveur DHCPv4 au 10.10.8.",
            "C. R1 diffusera les demandes DHCPv4 au nom des clients DHCPv4 locaux.",
            "D. Configurez R1 en tant qu’agent de relais DHCP."
        ],
        "answer": "D. Configurez R1 en tant qu’agent de relais DHCP.",
        "explanation": "",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-20_102708.jpg"
    },
    {
        "question": "68. Quelle action se déroule lorsque l’adresse MAC source d’un cadre entrant dans un commutateur n’est pas dans la table d’adresses MAC?",
        "options": [
            "A. Le commutateur ajoute à la table l’adresse MAC et le numéro de port entrant.",
            "B. Le commutateur transmet la trame à tous les ports, sauf au port d’arrivée.",
            "C. Le commutateur ajoute un mappage d’entrée de table d’adresses MAC pour l’adresse MAC de destination et le port d’entrée.",
            "D. Le commutateur transmet le cadre hors du port spécifié."
        ],
        "answer": "A. Le commutateur ajoute à la table l’adresse MAC et le numéro de port entrant.",
        "explanation": "",
        "image": ""
    },
    {
        "question": "69. Le routage inter-VLAN réussi fonctionne depuis un certain temps sur un réseau avec plusieurs VLAN sur plusieurs commutateurs. Lorsqu’une liaison de jonction entre commutateurs échoue et que le protocole Spanning Tree affiche une liaison de jonction de sauvegarde, il est signalé que les hôtes de deux VLAN peuvent accéder à certaines ressources réseau, mais pas à toutes les ressources précédemment accessibles. Les hôtes sur tous les autres VLAN n’ont pas ce problème. Quelle est la cause la plus probable de ce problème?",
        "options": [
            "A. Le routage inter-VLAN a également échoué lorsque le lien de jonction a échoué.",
            "B. Le protocole de jonction dynamique sur la liaison a échoué.",
            "C. Les VLAN autorisés sur la liaison de sauvegarde n’ont pas été configurés correctement.",
            "D. La fonction de port de bord protégé sur les interfaces de jonction de sauvegarde a été désactivée."
        ],
        "answer": "C. Les VLAN autorisés sur la liaison de sauvegarde n’ont pas été configurés correctement.",
        "explanation": "",
        "image": ""
    },
    {
        "question": "70. Un administrateur réseau utilise le modèle « Router-on-a-Stick » pour configurer un commutateur et un routeur pour le routage inter-VLAN. Comment le port du commutateur connecté au routeur doit-il être configuré ?",
        "options": [
            "A. Il doit être configuré comme port agrégé 802.1q.",
            "B. Il doit être configuré comme port d’accès et membre de VLAN 1.",
            "C. Il doit être configuré comme port agrégé et affecté au VLAN 1.",
            "D. Il doit être configuré comme port agrégé et n’autoriser que le trafic non étiqueté."
        ],
        "answer": "A",
        "explanation": "Le port du commutateur qui se connecte à l’interface du routeur doit être configuré en tant que port de jonction. Une fois qu’il devient un port de jonction, il n’appartient à aucun VLAN particulier et transmettra le trafic de divers VLAN.",
        "image": ""
    },
    {
        "question": "71. Pourquoi l’espionnage DHCP est-il nécessaire lors de l’utilisation de la fonction Dynamic ARP Inspection ?",
        "options": [
            "A. Il utilise la table d’adresses MAC pour vérifier l’adresse IP de la passerelle par défaut.",
            "B. Il s’appuie sur les paramètres des ports approuvés et non approuvés définis par l’espionnage DHCP.",
            "C. Il utilise la base de données de liaison d’adresse MAC à adresse IP pour valider un paquet ARP.",
            "D. Il redirige les demandes ARP vers le serveur DHCP pour vérification."
        ],
        "answer": "C",
        "explanation": "",
        "image": ""
    },
    {
        "question": "72. Reportez-vous à l’illustration. Un administrateur réseau a configuré les routeurs R1 et R2 comme faisant partie du groupe HSRP 1. Après le rechargement des routeurs, un utilisateur associé à l’hôte 1 s’est plaint d’une mauvaise connectivité à Internet. L’administrateur réseau a donc exécuté la commande show standby brief sur les deux routeurs pour vérifier le fonctionnement du protocole HSRP. En outre, l’administrateur a observé le tableau ARP sur Host1. Quelle entrée doit apparaître dans le tableau ARP sur Host1 pour acquérir la connectivité à Internet ?",
        "options": [
            "A. L’adresse IP virtuelle et l’adresse MAC virtuelle du groupe HSRP 1",
            "B. L’adresse IP virtuelle du groupe HSRP 1 et l’adresse MAC de R1",
            "C. L’adresse IP virtuelle du groupe HSRP 1 et l’adresse MAC de R2",
            "D. L’adresse IP et l’adresse MAC de R1"
        ],
        "answer": "A",
        "explanation": "Les hôtes enverront une requête ARP à la passerelle par défaut qui est l’adresse IP virtuelle. Les réponses ARP des routeurs HSRP contiennent l’adresse MAC virtuelle.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-20_102911.jpg"
    },
    {
        "question": "73. Une route statique a été configurée sur un routeur. Cependant, le réseau de destination n’existe plus. Que doit faire un administrateur pour supprimer l’itinéraire statique de la table de routage ?",
        "options": [
            "A. Rien. La route statique disparaîtra d’elle-même.",
            "B. Supprimez l’itinéraire en utilisant la commande no ip route.",
            "C. Modifier la distance administrative pour cet itinéraire.",
            "D. Modifier les mesures de routage pour cet itinéraire."
        ],
        "answer": "B",
        "explanation": "",
        "image": ""
    },
    {
        "question": "74. Un technicien junior ajoutait un itinéraire à un routeur LAN. Un traceroute vers un périphérique sur le nouveau réseau a révélé un mauvais chemin et un état inaccessible. Que faut-il faire ou vérifier ?",
        "options": [
            "A. Vérifiez la configuration sur l’itinéraire statique flottant et ajustez l’AD.",
            "B. Vérifiez la configuration de l’interface de sortie sur la nouvelle route statique.",
            "C. Créez un itinéraire statique flottant vers ce réseau.",
            "D. Vérifiez qu’il n’y a pas de route par défaut dans les tables de routage du routeur périphérique."
        ],
        "answer": "B",
        "explanation": "",
        "image": ""
    },
    {
        "question": "75. Quelle méthode d’authentification sans fil dépend d’un serveur d’authentification RADIUS ?",
        "options": [
            "A. WPA Personal",
            "B. WPA2 Personal",
            "C. WEP",
            "D. WPA2 Enterprise"
        ],
        "answer": "D",
        "explanation": "",
        "image": ""
    },
    {
        "question": "76. Quels sont les deux paramètres définis par défaut sur un routeur sans fil pouvant affecter la sécurité du réseau ? (Choisissez deux propositions.)",
        "options": [
            "A. Le SSID est diffusé.",
            "B. Le filtrage des adresses MAC est activé.",
            "C. Le chiffrement WEP est activé.",
            "D. Le canal sans fil est automatiquement sélectionné.",
            "E. Un mot de passe administrateur réservé est défini."
        ],
        "answer": "A, E",
        "explanation": "Les paramètres par défaut incluent souvent la diffusion du SSID et l’utilisation d’un mot de passe administratif bien connu. Ces éléments présentent un risque de sécurité pour les réseaux sans fil.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-20_103041.jpg"
    },
    {
        "question": "77. Un administrateur réseau d’une petite société de publicité configure la sécurité WLAN à l’aide de la méthode PSK WPA2. Quelles informations d’identification les utilisateurs de bureau ont-ils besoin pour connecter leurs ordinateurs portables au WLAN ?",
        "options": [
            "A. une clé qui correspond à la clé sur l’AP",
            "B. un nom d’utilisateur et un mot de passe configurés sur l’AP",
            "C. le nom d’utilisateur et le mot de passe de l’entreprise via le service Active Directory",
            "D. Phrase secrète de l’utilisateur"
        ],
        "answer": "D",
        "explanation": "",
        "image": ""
    },
    {
        "question": "78. Quelle commande permet de créer une route statique sur R2 pour atteindre PC B ?",
        "options": [
            "A. R2(config)# ip route 172.16.2.0 255.255.255.0 172.16.2.254",
            "B. R2(config)# ip route 172.16.2.1 255.255.255.0 172.16.3.1",
            "C. R2(config)# ip route 172.16.2.0 255.255.255.0 172.16.3.1",
            "D. R2(config)# ip route 172.16.3.0 255.255.255.0 172.16.2.254"
        ],
        "answer": "C",
        "explanation": "La syntaxe correcte est : R2(config)# ip route destination-network destination-mask {next-hop-ip-address | interface-sortie}",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-20_103139.jpg"
    },
    {
        "question": "79. Reportez-vous à l’illustration. R1 a été configuré avec la commande de route statique ip route 209.165.200.224 255.255.255.224 S0/0/0 et, par conséquent, les utilisateurs du réseau 172.16.0.0/16 ne peuvent pas accéder aux ressources sur Internet. Comment cette route statique doit-elle être modifiée pour permettre au trafic utilisateur du LAN d’accéder à Internet ?",
        "options": [
            "A. En ajoutant une distance administrative de 254.",
            "B. En configurant le réseau et le masque de destination sur 0.0.0.0 0.0.0.0.",
            "C. En choisissant S0/0/1 comme l’interface de sortie.",
            "D. En ajoutant l’adresse voisine du tronçon suivant, à savoir 209.165.200.226."
        ],
        "answer": "B",
        "explanation": "La route statique sur R1 a été configurée de manière incorrecte avec le mauvais réseau de destination et le mauvais masque. Le réseau et le masque de destination corrects sont 0.0.0.0 0.0.0.0.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-20_103216.jpg"
    },
    {
        "question": "80. Quel est le risque associé à la méthode de la base de données commune pour le protocole EAP ?",
        "options": [
            "A. Le protocole est facile à contourner et à fausser.",
            "B. Le secret partagé n’est pas suffisamment sécurisé.",
            "C. Le serveur d’authentification peut être déporté.",
            "D. Les informations peuvent être perdues lors de la synchronisation des bases de données."
        ],
        "answer": "B",
        "explanation": "",
        "image": ""
    },
    {
        "question": "81. Qu’est-ce qu’une méthode pour lancer une attaque de saut VLAN?",
        "options": [
            "A. inondation du commutateur avec des adresses MAC",
            "B. envoi d’adresses IP usurpées à partir de l’hôte attaquant",
            "C. introduction d’un commutateur non fiable et activation de la trunking",
            "D. envoi d’informations de VLAN natif usurpé"
        ],
        "answer": "C. introduction d’un commutateur non fiable et activation de la trunking",
        "explanation": "La méthode de saut VLAN consiste à introduire un commutateur non fiable dans le réseau et à activer la trunking pour permettre un accès non autorisé aux VLANs.",
        "image": ""
    },
    {
        "question": "82. Quel protocole ou technologie utilise l’adresse IP source vers l’adresse IP de destination comme mécanisme d’équilibrage de charge?",
        "options": [
            "A. EtherChannel",
            "B. HSRP",
            "C. Protocole VTP",
            "D. DTP"
        ],
        "answer": "A. EtherChannel",
        "explanation": "EtherChannel utilise l'adresse IP source et destination pour distribuer le trafic entre plusieurs liens physiques dans un lien logique pour l'équilibrage de charge.",
        "image": ""
    },
    {
        "question": "83. Examinez l’illustration. Tous les commutateurs affichés sont des modèles Cisco 2960 dont la priorité par défaut est identique et fonctionnant à la même bande passante. Quels sont les trois ports qui seront désignés pour STP ? (Choisissez trois réponses.)",
        "options": [
            "A. Fa0/9",
            "B. Fa0/10",
            "C. Fa0/21",
            "D. Fa0/11",
            "E. Fa0/13",
            "F. Fa0/20"
        ],
        "answer": [
            "B. Fa0/10",
            "C. Fa0/21",
            "E. Fa0/13"
        ],
        "explanation": "Le protocole STP désigne les ports en fonction de la priorité et de la bande passante. Les ports sélectionnés sont les meilleurs candidats pour le rôle de port désigné.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-20_103809.jpg"
    },
    {
        "question": "84. Un ingénieur WLAN déploie un WLC et cinq points d’accès sans fil à l’aide du protocole CAPWAP avec la fonction DTLS pour sécuriser le plan de contrôle des périphériques réseau. Lors du test du réseau sans fil, l’ingénieur WLAN remarque que le trafic de données est en cours d’échange entre le WLC et les AP en texte brut et qu’il n’est pas crypté. Quelle est la raison la plus probable pour cela?",
        "options": [
            "A. Bien que DTLS soit activé par défaut pour sécuriser le canal de contrôle CAPWAP, il est désactivé par défaut pour le canal de données.",
            "B. Le chiffrement des données nécessite l’installation d’une licence DTLS sur chaque point d’accès (AP) avant d’être activé sur le contrôleur de réseau local sans fil (WLC).",
            "C. DTLS est un protocole qui fournit uniquement la sécurité entre le point d’accès (AP) et le client sans fil.",
            "D. DTLS fournit uniquement la sécurité des données par authentification et ne fournit pas de chiffrement pour le déplacement des données entre un contrôleur de réseau local sans fil (WLC) et un point d’accès (AP)."
        ],
        "answer": "A. Bien que DTLS soit activé par défaut pour sécuriser le canal de contrôle CAPWAP, il est désactivé par défaut pour le canal de données.",
        "explanation": "DTLS est utilisé pour sécuriser la communication entre le WLC et les points d'accès. Par défaut, il protège uniquement le canal de contrôle, pas le canal de données.",
        "image": ""
    },
    {
        "question": "85. Contrairement aux routes dynamiques, quels sont les avantages qu’offre l’utilisation des routes statiques sur un routeur ? (Choisissez deux réponses.)",
        "options": [
            "A. Elles changent automatiquement le chemin vers le réseau de destination en cas de modification de la topologie.",
            "B. Elles améliorent l’efficacité de découverte des réseaux voisins.",
            "C. Elles utilisent moins de ressources du routeur.",
            "D. Elles améliorent la sécurité du réseau.",
            "E. Elles prennent moins de temps pour converger en cas de modification de la topologie de réseau."
        ],
        "answer": [
            "C. Elles utilisent moins de ressources du routeur.",
            "D. Elles améliorent la sécurité du réseau."
        ],
        "explanation": "Les routes statiques sont manuellement configurées, ce qui réduit l'utilisation des ressources du routeur et renforce la sécurité car elles ne nécessitent pas de mise à jour automatique.",
        "image": ""
    },
    {
        "question": "86. Examinez l’illustration. R1 a été configuré comme illustré. Cependant, PC1 ne parvient pas à recevoir d’adresse IPv4. Quel est le problème ?",
        "options": [
            "A. La commande ip address dhcp n’a pas été exécutée sur l’interface Gi0/1.",
            "B. R1 n’est pas configuré comme serveur DHCPv4.",
            "C. La commande ip helper-address n’a pas été exécutée sur l’interface correcte.",
            "D. Un serveur DHCP doit être installé sur le même LAN que l’hôte qui reçoit l’adresse IP."
        ],
        "answer": "C. La commande ip helper-address n’a pas été exécutée sur l’interface correcte.",
        "explanation": "La commande `ip helper-address` est nécessaire pour rediriger les requêtes DHCP vers un serveur DHCP dans un réseau différent.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-23_163055.png"
    },
    {
        "question": "87. Quel est l’effet de l’entrée de la commande de configuration ip arp inspection vlan 10 sur un commutateur?",
        "options": [
            "A. Il active le DAI sur des interfaces de commutation spécifiques précédemment configurées avec la surveillance DHCP.",
            "B. Activez globalement la surveillance DHCP (snooping) sur le commutateur.",
            "C. Il spécifie le nombre maximal d’adresses L2 autorisées sur un port.",
            "D. Il permet globalement la garde BPDU sur tous les ports compatibles PortFast."
        ],
        "answer": "A. Il active le DAI sur des interfaces de commutation spécifiques précédemment configurées avec la surveillance DHCP.",
        "explanation": "La commande `ip arp inspection` est utilisée pour activer la protection contre les attaques ARP en associant la vérification ARP à la surveillance DHCP.",
        "image": ""
    },
    {
        "question": "88. Quelle action se déroule lorsque l’adresse MAC source d’un cadre entrant dans un commutateur apparaît dans la table d’adresses MAC associée à un port différent?",
        "options": [
            "A. Le commutateur transmet le cadre hors du port spécifié.",
            "B. Le commutateur met à jour le minuteur d’actualisation de l’entrée.",
            "C. Le commutateur purge toute la table d’adresses MAC.",
            "D. Le commutateur remplace l’ancienne entrée et utilise le port le plus courant."
        ],
        "answer": "D. Le commutateur remplace l’ancienne entrée et utilise le port le plus courant.",
        "explanation": "Lorsqu'un commutateur reçoit une trame avec une adresse MAC source différente de celle déjà enregistrée, il met à jour la table MAC avec le nouveau port.",
        "image": ""
    },
    {
        "question": "89. Reportez-vous à l’illustration. Actuellement, le routeur R1 utilise une route EIGRP enregistrée via Branch2 pour atteindre le réseau 10.10.0.0/16. Quelle route statique flottante crée une route de secours vers le réseau 10.10.0.0/16 au cas où la liaison entre R1 et Branch2 serait interrompue ?",
        "options": [
            "A. ip route 10.10.0.0 255.255.0.0 Serial 0/0/0 100",
            "B. ip route 10.10.0.0 255.255.0.0 209.165.200.226 100",
            "C. ip route 10.10.0.0 255.255.0.0 209.165.200.225 100",
            "D. ip route 10.10.0.0 255.255.0.0 209.165.200.225 50"
        ],
        "answer": "C. ip route 10.10.0.0 255.255.0.0 209.165.200.225 100",
        "explanation": "Une route statique flottante doit avoir une distance administrative supérieure à celle de la route EIGRP active, et elle doit pointer vers une adresse IP valide pour être utilisée en cas de défaillance de la liaison principale.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-23_163253.png"
    },
    {
        "question": "90. Quelles sont les trois étapes à suivre avant de transférer un commutateur Cisco vers un nouveau domaine de gestion VTP ? (Choisissez trois réponses.)",
        "options": [
            "A. Redémarrer le commutateur.",
            "B. Télécharger la base de données VTP à partir du serveur VTP dans le nouveau domaine.",
            "C. Configurer le commutateur avec le nom du nouveau domaine de gestion.",
            "D. Réinitialiser les compteurs VTP pour permettre au commutateur de se synchroniser avec les autres commutateurs du domaine.",
            "E. Sélectionner le mode et la version VTP appropriés.",
            "F. Configurer le serveur VTP dans le domaine pour reconnaître l’ID de pont du nouveau commutateur."
        ],
        "answer": ["A", "C", "E"],
        "explanation": "Lors de l’ajout d’un nouveau commutateur à un domaine VTP, il est essentiel de configurer le commutateur avec un nouveau nom de domaine, le mode VTP, le numéro de version VTP et le mot de passe corrects. Un commutateur avec un numéro de révision plus élevé peut propager des VLAN non valides et effacer des VLAN valides, empêchant ainsi la connectivité de plusieurs périphériques sur les VLAN valides.",
        "image": ""
    },
    {
        "question": "91. Reportez-vous à l’illustration. Quelle opération effectue le routeur R1 sur un paquet associé à une adresse IPv6 de destination 2001:db8:cafe:5::1 ?",
        "options": [
            "A. supprimer le paquet",
            "B. transmettre le paquet en sortie sur Serial0/0/0",
            "C. transmettre le paquet en sortie sur GigabitEthernet0/1",
            "D. transmettre le paquet en sortie sur GigabitEthernet0/0"
        ],
        "answer": "B",
        "explanation": "La route ::/0 est la forme compressée de la route par défaut 0000:0000:0000:0000:0000:0000:0000:0000/0. La route par défaut est utilisée si une route plus spécifique n’est pas trouvée dans la table de routage.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-23_163433.png"
    },
    {
        "question": "92. Quelle est la principale raison pour un cybercriminel de lancer une attaque par dépassement d’adresses MAC ?",
        "options": [
            "A. pour que le cybercriminel puisse voir les trames destinées à d’autres hôtes",
            "B. pour que le commutateur cesse d’acheminer le trafic",
            "C. pour que le cybercriminel puisse exécuter un code arbitraire sur le commutateur",
            "D. pour que les hôtes légitimes ne puissent pas obtenir une adresse MAC"
        ],
        "answer": "A",
        "explanation": "",
        "image": ""
    },
    {
        "question": "93. Quelle proposition décrit le résultat de l’interconnexion de plusieurs commutateurs Cisco LAN ?",
        "options": [
            "A. Chaque commutateur comprend un espace de diffusion et un espace de collision.",
            "B. Les collisions de trames augmentent sur les segments connectant les commutateurs.",
            "C. Le domaine de diffusion s’étend sur tous les commutateurs.",
            "D. Chaque commutateur comprend un espace de collision."
        ],
        "answer": "C",
        "explanation": "Les commutateurs LAN Cisco ne filtrent pas les trames de diffusion. Une trame de diffusion est inondée vers tous les ports. Les commutateurs interconnectés forment un grand domaine de diffusion.",
        "image": ""
    },
    {
        "question": "94. Reportez-vous à l’illustration. Un administrateur réseau configure le routeur R1 pour l’attribution d’adresse IPv6. Sur la base de la configuration partielle, quel système d’attribution d’adresses IPv6 global monodiffusion l’administrateur a-t-il l’intention de mettre en œuvre ?",
        "options": [
            "A. configuration manuelle",
            "B. SLAAC",
            "C. avec état (stateful)",
            "D. Sans état"
        ],
        "answer": "C",
        "explanation": "",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-23_163717.png"
    },
    {
        "question": "95. Examinez l’illustration. Un administrateur réseau vérifie la configuration du commutateur S1. Quel protocole a été implémenté pour regrouper plusieurs ports physiques en une liaison logique ?",
        "options": [
            "A. DTP",
            "B. STP",
            "C. PAgP",
            "D. LACP"
        ],
        "answer": "C",
        "explanation": "",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2021-12-23_163739.png"
    },
    {
        "question": "96. Une politique de sécurité de l’entreprise exige que l’adressage MAC soit enregistré de manière dynamique et ajouté à la table des adresses MAC et à la configuration en cours sur chaque commutateur. Quelle configuration de la sécurité des ports permettra de respecter cette mesure ?",
        "options": [
            "A. adresses MAC sécurisées automatiques",
            "B. adresses MAC sécurisées dynamiques",
            "C. adresses MAC sécurisées statiques",
            "D. adresses MAC sécurisées fixes"
        ],
        "answer": "D",
        "explanation": "",
        "image": ""
    },
    {
        "question": "97. Un administrateur réseau utilise la commande de configuration globale spanning-tree portfastbpduguard default pour activer la garde BPDU sur un commutateur. Cependant, BPDU guard n’est pas activé sur tous les ports d’accès. Quelle est la source du problème ?",
        "options": [
            "A. PortFast n’est pas configuré sur tous les ports d’accès.",
            "B. Les ports d’accès configurés avec la protection racine ne peuvent pas être configurés avec la garde BPDU.",
            "C. Les ports d’accès appartiennent à différents VLAN.",
            "D. BPDU guard doit être activé en mode de commande de configuration de l’interface."
        ],
        "answer": "A",
        "explanation": "",
        "image": ""
    },
    {
        "question": "98. Examinez l’illustration. Un commutateur de couche 3 se charge du routage pour trois VLAN et se connecte à un routeur pour la connectivité Internet. Comment le commutateur doit-il être configuré ? (Choisissez deux réponses.)",
        "options": [
            "A. (config)# ip routing",
            "B. (config)# interface gigabitethernet 1/1",
            "C. (config-if)# no switchport",
            "D. (config-if)# ip address 192.168.1.2 255.255.255.252",
            "E. (config)# interface fastethernet0/4",
            "F. (config-if)# switchport mode trunk"
        ],
        "answer": ["A", "B"],
        "explanation": "",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2022-01-13_090443.jpg"
    },
    {
        "question": "99. Quel est l’effet de l’entrée de la commande de configuration ip dhcp snooping sur un commutateur ?",
        "options": [
            "A. Activez globalement la surveillance DHCP (snooping) sur le commutateur.",
            "B. Il active manuellement un lien de trunk.",
            "C. Il active PortFast globalement sur un commutateur.",
            "D. Désactivez les négociations DTP sur les ports trunking."
        ],
        "answer": "A",
        "explanation": "",
        "image": ""
    },
    {
        "question": "100. Un administrateur réseau est en train de configurer un WLAN. Pourquoi l’administrateur désactiverait-il la fonction de diffusion pour le SSID?",
        "options": [
            "A. pour assurer la confidentialité et l’intégrité du trafic sans fil en utilisant le chiffrement",
            "B. pour éliminer l’analyse des SSID disponibles dans la zone",
            "C. pour réduire le risque d’interférence par des dispositifs externes tels que les fours à micro-ondes",
            "D. pour réduire le risque d’ajout de points d’accès non autorisés au réseau"
        ],
        "answer": "B",
        "explanation": "Désactiver la diffusion du SSID permet d’empêcher les appareils non autorisés de détecter le réseau, augmentant ainsi la sécurité.",
        "image": ""
    },
    {
        "question": "101. Une entreprise déploie un réseau sans fil dans le site de distribution d’une banlieue de Boston. L’entrepôt est assez volumineux et nécessite l’utilisation de plusieurs points d’accès. Étant donné que certains appareils de l’entreprise fonctionnent toujours à 2,4 GHz, l’administrateur réseau décide de déployer la norme 802.11g. Quels sont les canaux que vous affecterez aux différents points d’accès afin d’éviter les chevauchements ?",
        "options": [
            "A. Canaux 2, 6 et 10",
            "B. Canaux 1, 7 et 13",
            "C. Canaux 1, 6 et 11",
            "D. Canaux 1, 5 et 9"
        ],
        "answer": "C",
        "explanation": "Les canaux 1, 6 et 11 sont les seuls canaux sans chevauchement dans la bande de fréquence 2,4 GHz en Amérique du Nord.",
        "image": ""
    },
    {
        "question": "102. Quelle attaque a pour but de créer un DOS pour les clients en les empêchant d’obtenir un crédit-bail DHCP ?",
        "options": [
            "A. Attaque par dépassement de table CAM",
            "B. Insuffisance de ressources DHCP",
            "C. Usurpation d’adresse IP",
            "D. Usurpation DHCP (ou spoofing)"
        ],
        "answer": "B",
        "explanation": "Les attaques de famine DHCP visent à épuiser les ressources DHCP en envoyant des requêtes DHCPDISCOVER, empêchant ainsi les clients légitimes d’obtenir une adresse IP.",
        "image": ""
    },
    {
        "question": "103. Les utilisateurs d’un réseau local ne peuvent pas accéder à un serveur Web d’entreprise mais peuvent se rendre ailleurs. Que faut-il faire ou vérifier ?",
        "options": [
            "A. Créez un itinéraire statique flottant vers ce réseau.",
            "B. Vérifiez que la route statique vers le serveur est présente dans la table de routage.",
            "C. Assurez-vous que l’ancien itinéraire par défaut a été supprimé des routeurs de bord de l’entreprise.",
            "D. Vérifiez la configuration sur l’itinéraire statique flottant et ajustez l’AD."
        ],
        "answer": "B",
        "explanation": "Vérifiez la table de routage pour vous assurer qu'une route statique correcte vers le serveur Web existe.",
        "image": ""
    },
    {
        "question": "104. Quelle commande permet de lancer le processus de regroupement de deux interfaces physiques afin de créer un groupe EtherChannel par le biais du protocole LACP ?",
        "options": [
            "A. channel-group 1 mode desirable",
            "B. interface range GigabitEthernet 0/4 – 5",
            "C. channel-group 2 mode auto",
            "D. interface port-channel 2"
        ],
        "answer": "B",
        "explanation": "La commande `interface range GigabitEthernet 0/4 – 5` est utilisée pour spécifier une plage d’interfaces dans un groupe EtherChannel.",
        "image": ""
    },
    {
        "question": "105. Quelle instruction est correcte sur la façon dont un commutateur de couche 2 détermine comment transférer des trames ?",
        "options": [
            "A. Le transfert de trame cut-through garantit que les trames non valides sont toujours abandonnées.",
            "B. Les décisions de transfert de trame sont basées sur l’adresse MAC et les mappages des ports dans la table CAM.",
            "C. Les trames monodiffusion sont toujours transmises indépendamment de l’adresse MAC de destination.",
            "D. Seules les trames avec des adresses de destination de diffusion sont transmises à tous les ports de commutateurs actifs."
        ],
        "answer": "B",
        "explanation": "Les décisions de transfert sont basées sur l'adresse MAC et la table CAM du commutateur.",
        "image": ""
    },
    {
        "question": "106. Reportez-vous à l’illustration. Quels sont les trois hôtes qui recevront des requêtes ARP de l’hôte A, dans l’hypothèse où le port Fa0/4 sur les deux commutateurs est configuré pour transporter du trafic pour plusieurs VLAN ? (Choisissez trois réponses.)",
        "options": [
            "A. hôte G",
            "B. hôte B",
            "C. hôte C",
            "D. hôte D",
            "E. hôte E",
            "F. hôte F"
        ],
        "answer": "C, D, F",
        "explanation": "Les requêtes ARP sont envoyées en fonction du VLAN auquel appartient l'hôte. Seuls les hôtes des VLAN associés à l'interface reçoivent la requête.",
        "image": "https://ccnareponses.com/wp-content/uploads/2022/01/2022-01-26_112504.jpg"
    },
    {
        "question": "107. Parmi les propositions suivantes, lesquelles caractérisent les ports routés d’un commutateur multicouche ? Choisissez deux réponses.",
        "options": [
            "A. Ils sont utilisés pour les liaisons point à multipoint.",
            "B. Dans un réseau commuté, elles sont principalement configurées entre les commutateurs, sur les couches principale et de distribution.",
            "C. Ils ne sont associés à aucun VLAN particulier.",
            "D. La commande interface vlan <numéro du VLAN> doit être exécutée pour créer un VLAN sur les ports routés.",
            "E. Ils prennent en charge les sous-interfaces, notamment les interfaces sur les routeurs Cisco IOS."
        ],
        "answer": "C, E",
        "explanation": "Les ports routés dans un commutateur multicouche ne sont associés à aucun VLAN particulier et prennent en charge les sous-interfaces pour le routage.",
        "image": ""
    },
    {
        "question": "108. Quel protocole ou technologie définit un groupe de routeurs, l’un d’eux défini comme actif et l’autre comme veille ?",
        "options": [
            "A. EtherChannel",
            "B. DTP",
            "C. HSRP",
            "D. Protocole VTP"
        ],
        "answer": "C",
        "explanation": "HSRP (Hot Standby Router Protocol) permet à un groupe de routeurs de partager une adresse IP virtuelle, avec un routeur actif et un autre en veille.",
        "image": ""
    },
    {
        "question": "109. Un administrateur réseau prépare l’implémentation du protocole Rapid PVST+ sur un réseau de production. Comment les types de liaisons Rapid PVST+ sont-ils déterminés sur les interfaces de commutateur ?",
        "options": [
            "A. Les types de liaisons peuvent uniquement être déterminés si PortFast a été configuré.",
            "B. Les types de liaisons peuvent uniquement être configurés sur des ports d’accès configurés au moyen d’un VLAN unique.",
            "C. Les types de liaisons doivent être configurés avec des commandes de configuration de port spécifiques.",
            "D. Les types de liaisons sont déterminés automatiquement."
        ],
        "answer": "D",
        "explanation": "Rapid PVST+ détermine automatiquement les types de liaison (point à point, partagée, etc.).",
        "image": ""
    },
    {
        "question": "110. Sur quels ports de commutation devrait-on activer la protection BPDU pour améliorer la stabilité STP ?",
        "options": [
            "A. tous les ports équipés de PortFast",
            "B. tous les ports de trunk qui ne sont pas des ports racines",
            "C. seuls les ports qui s’attachent à un commutateur voisin",
            "D. uniquement les ports qui sont élus comme ports désignés"
        ],
        "answer": "A",
        "explanation": "La protection BPDU doit être activée sur les ports configurés pour PortFast afin de prévenir les attaques de type BPDU spoofing.",
        "image": ""
    },
    {
        "question": "111. Examinez l’illustration. Un administrateur réseau configure un routeur comme serveur DHCPv6. L’administrateur exécute une commande show ipv6 dhcp pool pour vérifier la configuration. Parmi les propositions suivantes, laquelle décrit la raison pour laquelle le nombre de clients actifs est 0 ?",
        "options": [
            "A. Aucune plage d’adresses IPv6 n’est spécifiée pour la configuration du pool DHCP IPv6.",
            "B. Aucun client n’a encore communiqué avec le serveur DHCPv6.",
            "C. L’état n’est pas maintenu par le serveur DHCPv6 en mode de fonctionnement DHCPv6 sans état.",
            "D. L’adresse de la passerelle par défaut n’est pas disponible dans le pool."
        ],
        "answer": "C",
        "explanation": "Dans la configuration DHCPv6 sans état, le serveur ne conserve pas les informations d’état et les clients configurent leurs adresses IPv6 automatiquement.",
        "image": "https://ccnareponses.com/wp-content/uploads/2022/06/i210895v1n1_210895.jpg"
    },
    {
        "question": "112. Un administrateur réseau a trouvé un utilisateur envoyant une trame 802.1Q à un commutateur. Quelle est la meilleure solution pour prévenir ce type d’attaque ?",
        "options": [
            "A. Les VLAN des ports d’accès utilisateur doivent être différents des VLAN natifs utilisés sur les ports de jonction.",
            "B. Le numéro de VLAN natif utilisé sur n’importe quel tronc doit être l’un des VLAN de données actifs.",
            "C. Les ports de trunk doivent être configurés avec la sécurité de port.",
            "D. Les ports de trunk doivent utiliser le VLAN par défaut comme numéro de VLAN natif."
        ],
        "answer": "A",
        "explanation": "Séparer les VLAN des ports d'accès et des ports de jonction minimise le risque d'attaque par VLAN.",
        "image": ""
    },
    {
        "question": "113. Un nouveau commutateur doit être ajouté à un réseau existant dans un bureau distant. L’administrateur réseau ne souhaite pas que les techniciens du bureau distant puissent ajouter de nouveaux VLAN au commutateur, mais le commutateur doit recevoir des mises à jour VLAN du domaine VTP. Quelles deux étapes doivent être effectuées pour configurer VTP sur le nouveau commutateur afin de répondre à ces conditions ? (Choisissez deux propositions.)",
        "options": [
            "A. Configurer le nouveau commutateur en tant que client VTP.",
            "B. Activer l’élagage VTP.",
            "C. Configurer une adresse IP sur le nouveau commutateur.",
            "D. Configurer tous les ports du nouveau commutateur en mode d’accès.",
            "E. Configurer le nom de domaine et le mot de passe VTP corrects sur le nouveau commutateur."
        ],
        "answer": ["A", "E"],
        "explanation": "Le commutateur doit être en mode client VTP et avoir le bon nom de domaine et mot de passe pour recevoir les informations VTP.",
        "image": ""
    },
    {
        "question": "114. Deux protocoles sont utilisés pour l’authentification AAA au niveau des serveurs. Lesquels ? (Choisissez deux propositions.)",
        "options": [
            "A. SSH",
            "B. TACACS+",
            "C. RADIUS",
            "D. 802.1x",
            "E. SNMP"
        ],
        "answer": ["B", "C"],
        "explanation": "TACACS+ et RADIUS sont utilisés pour l’authentification AAA (Authentication, Authorization, Accounting).",
        "image": ""
    },
    {
        "question": "115. Quelle attaque réseau est atténuée en activant la garde BPDU ?",
        "options": [
            "A. Attaque par débordement de la table CAM",
            "B. Serveurs DHCP non fiables sur un réseau",
            "C. Commutateurs non fiables sur un réseau",
            "D. Usurpation d’adresse MAC"
        ],
        "answer": "C",
        "explanation": "La garde BPDU empêche l’ajout non autorisé de commutateurs au réseau.",
        "image": ""
    },
    {
        "question": "116. Quel est le terme commun donné aux messages de journal SNMP générés par les périphériques réseau et envoyés au serveur SNMP ?",
        "options": [
            "A. L’accusé de réception",
            "B. Audit",
            "C. Déroutements",
            "D. Avertissements"
        ],
        "answer": "C",
        "explanation": "Les messages SNMP envoyés au serveur SNMP sont appelés déroutements.",
        "image": ""
    },
    {
        "question": "117. Quel protocole ou technologie est-il un protocole propriétaire Cisco qui est automatiquement activé sur les commutateurs 2960 ?",
        "options": [
            "A. STP",
            "B. DTP",
            "C. Protocole VTP",
            "D. EtherChannel"
        ],
        "answer": "B",
        "explanation": "DTP (Dynamic Trunking Protocol) est un protocole propriétaire Cisco activé par défaut sur les commutateurs 2960.",
        "image": ""
    },
    {
        "question": "118. Un administrateur réseau est en train de configurer un WLAN. Pourquoi l’administrateur appliquerait-il WPA2 avec AES au WLAN ?",
        "options": [
            "A. Pour assurer la confidentialité et l’intégrité du trafic sans fil en utilisant le chiffrement.",
            "B. Fournir un service prioritaire pour les applications sensibles au temps.",
            "C. Pour centraliser la gestion de plusieurs réseaux WLAN.",
            "D. Pour réduire le risque d’ajout de points d’accès non autorisés au réseau."
        ],
        "answer": "A",
        "explanation": "WPA2 avec AES garantit la confidentialité et l’intégrité du trafic sans fil en utilisant un chiffrement sécurisé.",
        "image": ""
    },
    {
        "question": "119. Un technicien junior ajoutait une route à un routeur LAN. Un traceroute vers un périphérique sur le nouveau réseau a révélé un mauvais chemin et un état inaccessible. Que faut-il faire ou vérifier ?",
        "options": [
            "A. Vérifiez que la route statique vers le serveur est présente dans la table de routage.",
            "B. Vérifiez la configuration sur la route statique flottante et ajustez l’AD.",
            "C. Vérifiez la configuration de l’interface de sortie sur la nouvelle route statique.",
            "D. Créez une route statique flottante vers ce réseau."
        ],
        "answer": "C",
        "explanation": "Il faut vérifier la configuration de l’interface de sortie pour s’assurer que la route statique est correctement configurée.",
        "image": ""
    },
    {
        "question": "120. Quels énoncés décrivent précisément les paramètres de mode bidirectionnel et de débit des commutateurs Cisco 2960 ? (Choisissez trois réponses.)",
        "options": [
            "A. Les paramètres de mode bidirectionnel et de débit de chaque port du commutateur peuvent être configurés manuellement.",
            "B. Par défaut, la fonction de négociation automatique est désactivée.",
            "C. Si la vitesse est définie sur 1 000 Mbits/s, les ports de commutateur fonctionnent en mode bidirectionnel simultané.",
            "D. Par défaut, le débit est défini sur 100 Mbits/s et le mode bidirectionnel est réglé sur le mode de négociation automatique.",
            "E. L’activation de la négociation automatique sur un concentrateur prévient les erreurs de correspondance des débits des ports lors de la connexion du concentrateur au commutateur.",
            "F. La défaillance de la négociation automatique peut être à l’origine de problèmes de connectivité."
        ],
        "answer": ["A", "C", "F"],
        "explanation": "Les commutateurs Cisco 2960 peuvent être configurés manuellement pour la vitesse et le mode bidirectionnel, et une défaillance de la négociation automatique peut causer des problèmes de connectivité.",
        "image": ""
    },
    {
        "question": "121. Reportez-vous à l’illustration. Quelle instruction indiquée dans le résultat permet au routeur R1 de répondre aux demandes DHCPv6 sans état ?",
        "options": [
            "A. prefix-delegation 2001:DB8:8::/48 00030001000E84244E70",
            "B. ipv6 unicast-routing",
            "C. dns-server 2001:DB8:8::8",
            "D. ipv6 nd other-config-flag",
            "E. ipv6 dhcp server LAN1"
        ],
        "answer": "D",
        "explanation": "La commande d’interface ipv6 nd other-config-flag permet d’envoyer des messages RA sur cette interface, indiquant que des informations supplémentaires sont disponibles à partir d’un serveur DHCPv6 sans état.",
        "image": "https://ccnareponses.com/wp-content/uploads/2022/06/CCNA-2-v7-exam-answers-56.png"
    },
    {
        "question": "122. Quelle action se déroule lorsqu’une trame entrant dans un commutateur a une adresse MAC de destination multidiffusion?",
        "options": [
            "A. Le commutateur transmet le cadre hors du port spécifié.",
            "B. Le commutateur ajoute un mappage d’entrée de table d’adresses MAC pour l’adresse MAC de destination et le port d’entrée.",
            "C. Le commutateur remplace l’ancienne entrée et utilise le port le plus courant.",
            "D. Le commutateur transmet la trame à tous les ports, sauf au port d’arrivée."
        ],
        "answer": "D",
        "explanation": "Si l’adresse MAC de destination est une diffusion ou une multidiffusion, la trame est également diffusée sur tous les ports, à l’exception du port entrant.",
        "image": ""
    },
    {
        "question": "123. Quel protocole ou technologie permet à des données de transmettre via des liaisons de commutation redondantes?",
        "options": [
            "A. EtherChannel",
            "B. Protocole VTP",
            "C. DTP",
            "D. STP"
        ],
        "answer": "D",
        "explanation": "Le protocole STP (Spanning Tree Protocol) est utilisé pour éviter les boucles sur les réseaux avec des chemins redondants.",
        "image": ""
    },
    {
        "question": "124. Un administrateur réseau est en train de configurer un WLAN. Pourquoi l’administrateur modifie-t-il les adresses DHCP IPv4 par défaut sur un point d’accès?",
        "options": [
            "A. pour réduire le risque d’interférence par des dispositifs externes tels que les fours à micro-ondes",
            "B. pour restreindre l’accès au WLAN uniquement par les utilisateurs autorisés et authentifiés",
            "C. pour réduire l’interception de données ou l’accès au réseau sans fil à l’aide d’une plage d’adresses bien connue",
            "D. pour surveiller le fonctionnement du réseau sans fil"
        ],
        "answer": "C",
        "explanation": "L’administrateur modifie les adresses DHCP pour éviter l’interception de données et l’accès non autorisé à travers des plages d’adresses IPv4 prévisibles.",
        "image": ""
    },
    {
        "question": "125. Un administrateur réseau configure la fonction de sécurité des ports sur un commutateur. La politique de sécurité indique qu’au maximum deux adresses MAC sont autorisées sur chaque port d’accès. Lorsque le nombre maximal d’adresses MAC est atteint, une trame avec l’adresse MAC source inconnue est abandonnée et une notification est envoyée au serveur Syslog. Quel mode de violation de sécurité doit être configuré sur chaque port d’accès ?",
        "options": [
            "A. warning",
            "B. protect",
            "C. shutdown",
            "D. restrict"
        ],
        "answer": "D",
        "explanation": "Le mode 'restrict' permet d’abandonner les trames avec des adresses MAC inconnues et d’envoyer une notification Syslog.",
        "image": ""
    },
    {
        "question": "126. Un administrateur réseau a configuré un routeur pour une opération DHCPv6 sans état. Toutefois, les utilisateurs signalent que les stations de travail ne reçoivent pas d’informations sur le serveur DNS. Quelles sont les deux lignes de configuration du routeur qui doivent être vérifiées pour s’assurer que le service DHCPv6 sans état est correctement configuré? (Choisissez deux propositions.)",
        "options": [
            "A. La ligne de nom de domaine est incluse dans la section du pool dhcp ipv6.",
            "B. Le ipv6 nd other-config-flag entré pour l’interface qui fait face au segment LAN.",
            "C. La ligne dns-server est incluse dans la section ipv6 dhcp pool.",
            "D. La ligne de préfixe d’adresse est incluse dans la section ipv6 dhcp pool.",
            "E. Le ipv6 nd managed-config-flag est entré pour l’interface qui fait face au segment LAN."
        ],
        "answer": "B, C",
        "explanation": "Le `ipv6 nd other-config-flag` et la ligne `dns-server` dans le pool DHCPv6 permettent de configurer correctement le DHCPv6 sans état.",
        "image": ""
    },
    {
        "question": "127. Quel protocole ou quelle technologie désactive les chemins redondants pour éliminer les boucles de la couche 2 ?",
        "options": [
            "A. EtherChannel",
            "B. Protocole VTP",
            "C. STP",
            "D. DTP"
        ],
        "answer": "C",
        "explanation": "STP (Spanning Tree Protocol) désactive les chemins redondants pour éliminer les boucles dans le réseau de couche 2.",
        "image": ""
    },
    {
        "question": "128. Un administrateur réseau est en train de configurer un WLAN. Pourquoi l’administrateur utiliserait-il des serveurs RADIUS sur le réseau?",
        "options": [
            "A. pour restreindre l’accès au WLAN uniquement par les utilisateurs autorisés et authentifiés",
            "B. pour faciliter la configuration de groupe et la gestion de plusieurs WLAN via un WLC",
            "C. pour centraliser la gestion de plusieurs réseaux WLAN",
            "D. pour surveiller le fonctionnement du réseau sans fil"
        ],
        "answer": "A",
        "explanation": "Les serveurs RADIUS sont utilisés pour l’authentification et l’autorisation des utilisateurs, afin de restreindre l’accès au WLAN.",
        "image": ""
    },
    {
        "question": "129. Quel est l’effet de l’entrée de la commande de configuration show ip dhcp snooping binding sur un commutateur?",
        "options": [
            "A. Il limite le nombre de messages de découverte, par seconde, à recevoir sur l’interface.",
            "B. Il passe un port de jonction en mode d’accès.",
            "C. Il vérifie l’adresse MAC de source dans l’en-tête Ethernet par rapport à l’adresse MAC de l’expéditeur dans le corps ARP.",
            "D. Il affiche les associations d’adresses IP à Mac pour les interfaces de commutation."
        ],
        "answer": "D",
        "explanation": "La commande `show ip dhcp snooping binding` affiche les associations entre les adresses IP et les adresses MAC des interfaces de commutation.",
        "image": ""
    },
    {
        "question": "33. Quel est l’effet de la saisie de la commande de configuration spanning-tree portfast sur un commutateur ?",
        "options": [
            "A. Cela désactive un port inutilisé.",
            "B. Cela désactive tous les ports de jonction.",
            "C. Il active le portfast sur une interface de commutateur spécifique.",
            "D. Il vérifie l’adresse L2 source dans l’en-tête Ethernet par rapport à l’adresse L2 de l’expéditeur dans le corps ARP."
        ],
        "answer": "C",
        "explanation": "La commande spanning-tree portfast est utilisée pour activer le portfast sur une interface spécifique, ce qui permet de réduire le temps de transition d'un port vers l'état de transmission.",
        "image": ""
    },
    {
        "question": "34. Quel est le préfixe IPv6 utilisé pour les adresses lien-local ?",
        "options": [
            "A. FF01::/8",
            "B. 2001::/3",
            "C. FC00::/7",
            "D. FE80::/10"
        ],
        "answer": "D",
        "explanation": "Le préfixe IPv6 pour les adresses lien-local est FE80::/10. Ce préfixe est utilisé pour la communication entre les dispositifs d’un même lien sans nécessiter de routeur.",
        "image": ""
    },
    {
        "question": "49. Quelles sont les deux fonctions exécutées par un WLC lors de l’utilisation du contrôle d’accès aux médias (MAC) ? (Choisissez deux réponses.)",
        "options": [
            "A. accusés de réception et retransmissions de paquets",
            "B. Mise en file d’attente des trames et priorisation des paquets",
            "C. balises et réponses des sondes",
            "D. traduction du cadre vers d’autres protocoles",
            "E. association et réassociation de clients itinérants"
        ],
        "answer": "D, E",
        "explanation": "Le WLC (Wireless LAN Controller) gère la traduction de trames et l'association des clients, ce qui inclut l’association et la réassociation des clients itinérants.",
        "image": ""
    },
    {
        "question": "55. Un administrateur réseau configure un nouveau commutateur Cisco pour l’accès à la gestion à distance. Quels sont les trois éléments à configurer sur le commutateur pour la tâche ? (Choisissez trois réponses.)",
        "options": [
            "A. Adresse IP",
            "B. Domaine VTP",
            "C. lignes vty",
            "D. VLAN par défaut",
            "E. passerelle par défaut",
            "F. adresse de bouclage"
        ],
        "answer": "A, C, E",
        "explanation": "Pour activer l'accès à distance, un administrateur doit configurer une adresse IP, des lignes vty pour les connexions, et une passerelle par défaut pour le routage.",
        "image": ""
    },
    {
        "question": "59. Une entreprise vient de passer à un nouveau FAI. Le FAI a terminé et vérifié la connexion de son site à l’entreprise. Cependant, les employés de l’entreprise ne peuvent pas accéder à Internet. Que faut-il faire ou vérifier ?",
        "options": [
            "A. Vérifiez que la route statique vers le serveur est présente dans la table de routage.",
            "B. Vérifiez la configuration sur la route statique flottante et ajustez l’AD.",
            "C. Assurez-vous que l’ancienne route par défaut a été supprimée des routeurs périphériques de l’entreprise.",
            "D. Créez une route statique flottante vers ce réseau."
        ],
        "answer": "C",
        "explanation": "L’ancienne route par défaut pourrait interférer avec la nouvelle connexion Internet. Il est essentiel de s’assurer qu’elle a été supprimée.",
        "image": ""
    },
    {
        "question": "83. Un technicien configure un routeur pour une petite entreprise avec plusieurs WLAN et n’a pas besoin de la complexité d’un protocole de routage dynamique. Qu’est-ce que doit être fait ou vérifié ?",
        "options": [
            "A. Vérifiez qu’il n’y a pas de route par défaut dans les tables de routage du routeur Edge.",
            "B. Créez des routes statiques vers tous les réseaux internes et une route par défaut vers Internet.",
            "C. Créez des routes statiques supplémentaires vers le même emplacement avec un AD de 1.",
            "D. Vérifiez les statistiques sur la route par défaut pour la sursaturation."
        ],
        "answer": "B",
        "explanation": "Dans un environnement simple, sans protocole de routage dynamique, il est nécessaire de configurer des routes statiques vers les réseaux internes et une route par défaut vers Internet.",
        "image": ""
    },
    {
        "question": "88. Quel plan d’atténuation est le meilleur pour contrecarrer une attaque DoS qui crée un débordement de table d’adresses MAC ?",
        "options": [
            "A. Désactiver la DTP.",
            "B. Désactiver STP.",
            "C. Activer la sécurité des ports.",
            "D. Placez les ports inutilisés dans un VLAN inutilisé."
        ],
        "answer": "C",
        "explanation": "L’activation de la sécurité des ports permet de limiter les attaques par débordement de la table d’adresses MAC, empêchant ainsi une saturation de la table.",
        "image": ""
    },
    {
        "question": "90. Quel message DHCPv4 un client enverra-t-il pour accepter une adresse IPv4 proposée par un serveur DHCP ?",
        "options": [
            "A. diffusion DHCPACK",
            "B. diffusion DHCPREQUEST",
            "C. DHCPACK monodiffusion",
            "D. DHCPREQUEST en monodiffusion"
        ],
        "answer": "B",
        "explanation": "Lorsqu'un client DHCP reçoit une offre d'adresse IP, il envoie un message DHCPREQUEST en diffusion pour accepter l'offre.",
        "image": ""
    },
    {
        "question": "94. Quel protocole ajoute de la sécurité aux connexions à distance ?",
        "options": [
            "A. FTP",
            "B. HTTP",
            "C. NetBEUI",
            "D. POP",
            "E. SSH"
        ],
        "answer": "E",
        "explanation": "SSH (Secure Shell) est un protocole qui ajoute de la sécurité pour les connexions à distance en chiffrant les données échangées.",
        "image": ""
    },
    {
        "question": "95. Examinez l’illustration. Un administrateur réseau vérifie la configuration du routage inter-VLAN. Les utilisateurs se plaignent que PC2 ne peut pas communiquer avec PC1. Sur la base de la sortie, quelle est la cause possible du problème ?",
        "options": [
            "A. Gi0/0 n’est pas configuré comme port de jonction.",
            "B. L’interface de commande GigabitEthernet0/0.5 a été saisie de manière incorrecte.",
            "C. Aucune adresse IP n’est configurée sur l’interface Gi0/0.",
            "D. La commande no shutdown n’est pas entrée sur les sous-interfaces.",
            "E. La commande encapsulation dot1Q 5 contient le mauvais VLAN."
        ],
        "answer": "E",
        "explanation": "Le problème peut être lié à une mauvaise configuration du VLAN dans la commande d'encapsulation dot1Q, ce qui empêche la communication inter-VLAN.",
        "image": ""
    },
    {
        "question": "97. Faites correspondre chaque type de message DHCP avec sa description. (Toutes les options ne sont pas utilisées.)",
        "options": [
            "A. DHCPDISCOVER – un client initiant un message pour trouver un serveur DHCP",
            "B. DHCPOFFER – un serveur DHCP répondant à la requête initiale d’un client",
            "C. DHCPREQUEST – le client acceptant l’adresse IP fournie par le serveur DHCP",
            "D. DHCPACK – le serveur DHCP confirmant que le bail a été accepté"
        ],
        "answer": "",
        "explanation": "Placez les options dans l’ordre suivant : A. DHCPDISCOVER, B. DHCPOFFER, C. DHCPREQUEST, D. DHCPACK.",
        "image": "https://ccnareponses.com/wp-content/uploads/2021/12/2020-01-20_225135-1.jpg"
    },
    {
        "question": "98. Quelle attaque réseau cherche à créer un DoS pour les clients en les empêchant d’obtenir un bail DHCP ?",
        "options": [
            "A. Usurpation d’adresse IP",
            "B. Famine DHCP",
            "C. Attaque de table CAM",
            "D. Spoofing DHCP"
        ],
        "answer": "B. Famine DHCP",
        "explanation": "Les attaques de famine DHCP sont lancées par un attaquant pour créer un DoS en épuisant le pool d’adresses IP disponibles.",
        "image": ""
    },
    {
        "question": "105. Quelle commande permettra à un routeur de commencer à envoyer des messages lui permettant de configurer une adresse lien-local sans utiliser de serveur DHCP IPv6 ?",
        "options": [
            "A. un itinéraire statique",
            "B. la route ipv6 ::/0 commande",
            "C. la commande ipv6 unicast-routing",
            "D. la commande de routage ip"
        ],
        "answer": "C. la commande ipv6 unicast-routing",
        "explanation": "La commande `ipv6 unicast-routing` active le routage IPv6 et permet au routeur de configurer une adresse lien-local.",
        "image": ""
    },
    {
        "question": "119. Les utilisateurs se plaignent d’un accès sporadique à Internet chaque après-midi. Que faut-il faire ou vérifier ?",
        "options": [
            "A. Créez des routes statiques vers tous les réseaux internes et une route par défaut vers Internet.",
            "B. Vérifiez qu’il n’y a pas de route par défaut dans les tables de routage du routeur Edge.",
            "C. Créez une route statique flottante vers ce réseau.",
            "D. Vérifiez les statistiques sur la route par défaut pour la sursaturation."
        ],
        "answer": "D. Vérifiez les statistiques sur la route par défaut pour la sursaturation.",
        "explanation": "La sursaturation de la route par défaut peut entraîner un accès sporadique à Internet.",
        "image": ""
    },
    {
    "question": "122. Un nouveau commutateur de couche 3 est connecté à un routeur et est en cours de configuration pour le routage interVLAN. Quelles sont trois des cinq étapes requises pour la configuration ? (Choisissez trois réponses.)",
    "options": [
        "A. Modifier le VLAN par défaut",
        "B. Installer une route statique",
        "C. Ajustement de la métrique d’itinéraire",
        "D. Création de VLAN",
        "E. Attribution de ports aux VLAN",
        "F. Création d’interfaces SVI",
        "G. Implémenter un protocole de routage",
        "H. Activation du routage IP",
        "I. En saisissant « pas de port de commutation » sur le port connecté au routeur",
        "J. Attribution des ports au VLAN natif",
        "K. Modification du VLAN par défaut",
        "L. Attribution de ports aux VLAN"
    ],
    "answers": {
        "Cas 1": [
            "D. Création de VLAN",
            "E. Attribution de ports aux VLAN",
            "F. Création d’interfaces SVI"
        ],
        "Cas 2": [
            "H. Activation du routage IP",
            "I. En saisissant « pas de port de commutation » sur le port connecté au routeur",
            "L. Attribution de ports aux VLAN"
        ],
        "Cas 3": [
            "H. Activation du routage IP",
            "I. En saisissant « pas de port de commutation » sur le port connecté au routeur",
            "D. Création de VLAN"
        ]
    },
    "explanation": "Étape 1. Créez les VLAN. Étape 2. Créez les interfaces SVI VLAN. Étape 3. Configurez les ports d’accès. Attribuez-les à leurs VLAN respectifs. Étape 4. Activez le routage IP.",
    "image": ""
    },
    {
        "question": "132. Les employés ne peuvent pas se connecter aux serveurs sur l’un des réseaux internes. Que faut-il faire ou vérifier ?",
        "options": [
            "A. Utilisez la commande « show ip interface brief » pour voir si une interface est en panne.",
            "B. Vérifiez qu’il n’y a pas de route par défaut dans les tables de routage du routeur Edge.",
            "C. Créez des routes statiques vers tous les réseaux internes et une route par défaut vers Internet.",
            "D. Vérifiez les statistiques sur la route par défaut pour la sursaturation."
        ],
        "answer": "A",
        "explanation": "La commande `show ip interface brief` permet de vérifier si une interface est en panne.",
        "image": ""
    },
    {
        "question": "134. Un administrateur remarque qu’un grand nombre de paquets sont supprimés sur l’un des routeurs de succursale. Que faut-il faire ou vérifier ?",
        "options": [
            "A. Créez des routes statiques vers tous les réseaux internes et une route par défaut vers Internet.",
            "B. Créez des routes statiques supplémentaires vers le même emplacement avec un AD de 1.",
            "C. Vérifiez les statistiques sur la route par défaut pour la sursaturation.",
            "D. Vérifiez la table de routage pour une route statique manquante."
        ],
        "answer": "D",
        "explanation": "Vérifier la table de routage pour une route statique manquante est crucial lorsqu'un grand nombre de paquets sont supprimés.",
        "image": ""
    },
    {
        "question": "135. Quelles sont les deux caractéristiques du commutateur qui pourraient aider à réduire la congestion du réseau ? (Choisissez deux réponses.)",
        "options": [
            "A. Commutation interne rapide",
            "B. Tampons de grande taille",
            "C. Commutation store-and-forward",
            "D. Faible densité de ports",
            "E. Contrôle de séquence de contrôle de trame (FCS)"
        ],
        "answer": "A, B",
        "explanation": "La commutation interne rapide et les tampons de grande taille aident à réduire la congestion du réseau en permettant un transfert plus rapide des données.",
        "image": ""
    },
    {
        "question": "136. Quel est le résultat de la connexion de deux ou plusieurs commutateurs ensemble ?",
        "options": [
            "A. Le nombre de domaines de diffusion est augmenté.",
            "B. La taille du domaine de diffusion est augmentée.",
            "C. Le nombre de domaines de collision est réduit.",
            "D. La taille du domaine de collision est augmentée."
        ],
        "answer": "B",
        "explanation": "Lorsque deux commutateurs ou plus sont connectés ensemble, la taille du domaine de diffusion augmente.",
        "image": ""
    },
    {
        "question": "139. Quel est l’effet de la saisie de la commande de configuration switchport port-security sur un commutateur ?",
        "options": [
            "A. Il apprend dynamiquement l’adresse L2 et la copie dans la configuration en cours.",
            "B. Il active la sécurité des ports sur une interface.",
            "C. Il active la sécurité des ports globalement sur le commutateur.",
            "D. Il restreint le nombre de messages de découverte, par seconde, à recevoir sur l’interface."
        ],
        "answer": "B",
        "explanation": "La commande `switchport port-security` active la sécurité des ports sur une interface spécifique du commutateur.",
        "image": ""
    },
    {
        "question": "140. Un administrateur réseau configure un WLAN. Pourquoi l’administrateur utiliserait-il plusieurs points d’accès légers ?",
        "options": [
            "A. Pour centraliser la gestion de plusieurs WLAN.",
            "B. Pour surveiller le fonctionnement du réseau sans fil.",
            "C. Fournir un service prioritaire pour les applications urgentes.",
            "D. Pour faciliter la configuration et la gestion de groupe de plusieurs WLAN via un WLC."
        ],
        "answer": "D",
        "explanation": "L'utilisation de plusieurs points d'accès légers permet de centraliser la gestion des WLAN via un contrôleur de point d'accès sans fil (WLC).",
        "image": ""
    },
    {
        "question": "141. Examinez l’illustration. PC-A et PC-B sont tous deux dans le VLAN 60. PC-A est incapable de communiquer avec PC-B. Quel est le problème ?",
        "options": [
            "A. Le VLAN natif doit être le VLAN 60.",
            "B. Le VLAN natif est supprimé du lien.",
            "C. Le tronc a été configuré avec la commande switchport nonegotiate.",
            "D. Le VLAN utilisé par PC-A ne figure pas dans la liste des VLAN autorisés sur le tronc."
        ],
        "answer": "D",
        "explanation": "Le VLAN 60, auquel PC-A et PC-B appartiennent, n’a pas été autorisé sur le tronc, ce qui empêche la communication.",
        "image": "https://ccnareponses.com/wp-content/uploads/2022/06/i211586v1n1_Question-5.png"
    },
    {
        "question": "144. Un administrateur réseau a configuré un routeur pour un fonctionnement DHCPv6 sans état. Cependant, les utilisateurs signalent que les postes de travail ne reçoivent pas les informations du serveur DNS. Quelles lignes de configuration de routeur doivent être vérifiées pour s’assurer que le service DHCPv6 sans état est correctement configuré ? (Choisissez deux réponses.)",
        "options": [
            "A. La ligne de nom de domaine est incluse dans la section ipv6 dhcp pool.",
            "B. La ligne DNS-server est incluse dans la section ipv6 dhcp pool.",
            "C. Le ipv6 nd other-config-flag est saisi pour l’interface qui fait face au segment LAN.",
            "D. La ligne de préfixe d’adresse est incluse dans la section ipv6 dhcp pool.",
            "E. Le ipv6 et managed-config-flag est saisi pour l’interface qui fait face au segment LAN."
        ],
        "answer": "B, C",
        "explanation": "Pour utiliser la méthode DHCPv6 sans état, le routeur doit informer les clients DHCPv6 de configurer une adresse IPv6 SLAAC et contacter le serveur DHCPv6 pour obtenir des paramètres de configuration supplémentaires, tels que l’adresse du serveur DNS. Cela se fait via la commande `ipv6 nd other-config-flag` entrée dans le mode de configuration de l’interface. L’adresse du serveur DNS est indiquée dans la configuration du `pool dhcp ipv6`.",
        "image": ""
    },
    {
        "question": "147. Quelle action a lieu lorsqu’une trame entrant dans un commutateur a une adresse MAC de destination de monodiffusion qui ne figure pas dans la table d’adresses MAC ?",
        "options": [
            "A. Le commutateur met à jour la minuterie d’actualisation de l’entrée.",
            "B. Le commutateur réinitialise la minuterie d’actualisation sur toutes les entrées de la table d’adresses MAC.",
            "C. Le commutateur remplace l’ancienne entrée et utilise le port le plus récent.",
            "D. Le commutateur transférera la trame vers tous les ports à l’exception du port entrant."
        ],
        "answer": "D",
        "explanation": "Lorsque le commutateur reçoit une trame avec une adresse MAC de destination qui ne figure pas dans sa table d’adresses MAC, il la transfère vers tous les ports sauf celui d’entrée, en mode de diffusion.",
        "image": ""
    },
    {
        "question": "150. Quel protocole ou quelle technologie gère les négociations de jonction entre les commutateurs ?",
        "options": [
            "A. VTP",
            "B. EtherChannel",
            "C. DTP",
            "D. STP"
        ],
        "answer": "C",
        "explanation": "Le protocole DTP (Dynamic Trunking Protocol) est utilisé pour gérer la négociation des jonctions entre les commutateurs.",
        "image": ""
    },
    {
        "question": "154. Quel est l’effet de la saisie de la commande de configuration ip dhcp snooping limit rate 6 sur un commutateur ?",
        "options": [
            "A. Il affiche les associations d’adresses IP-MAC pour les interfaces de commutateur.",
            "B. Il active la sécurité des ports globalement sur le commutateur.",
            "C. Il restreint le nombre de messages de découverte, par seconde, à recevoir sur l’interface.",
            "D. Il apprend dynamiquement l’adresse L2 et la copie dans la configuration en cours."
        ],
        "answer": "C",
        "explanation": "La commande `ip dhcp snooping limit rate 6` permet de restreindre le nombre de messages DHCP de découverte à recevoir par seconde sur l’interface spécifiée, limitant ainsi les attaques de type DoS.",
        "image": ""
    },
    {
        "question": "156. Quel est l’effet de la saisie de la commande de configuration ip arp inspection validate src-mac sur un commutateur ?",
        "options": [
            "A. Il vérifie l’adresse L2 source dans l’en-tête Ethernet par rapport à l’adresse L2 de l’expéditeur dans le corps ARP.",
            "B. Cela désactive tous les ports de jonction.",
            "C. Il affiche les associations d’adresses IP-MAC pour les interfaces de commutateur.",
            "D. Il active le portfast sur une interface de commutateur spécifique."
        ],
        "answer": "A",
        "explanation": "La commande `ip arp inspection validate src-mac` vérifie l’adresse source L2 dans l’en-tête Ethernet par rapport à l’adresse source L2 dans la demande ARP, afin de prévenir les attaques ARP.",
        "image": ""
    },
    {
        "question": "158. Quelle longueur d’adresse et de préfixe est utilisée lors de la configuration d’une route statique IPv6 par défaut ?",
        "options": [
            "A. ::/0",
            "B. FF02::1/8",
            "C. 0.0.0.0/0",
            "D. ::1/128"
        ],
        "answer": "A",
        "explanation": "Lors de la configuration d’une route statique IPv6 par défaut, l’adresse et le préfixe utilisés sont `::/0`.",
        "image": ""
    },
    {
        "question": "159. Quelles sont les deux caractéristiques de Cisco Express Forwarding (CEF) ? (Choisissez deux.)",
        "options": [
            "A. Lorsqu’un paquet arrive sur une interface de routeur, il est transmis au plan de contrôle où le processeur fait correspondre l’adresse de destination avec une entrée de table de routage correspondante.",
            "B. Il s’agit du mécanisme de transfert le plus rapide sur les routeurs Cisco et les commutateurs multicouches.",
            "C. Avec cette méthode de commutation, les informations de flux pour un paquet sont stockées dans le cache à commutation rapide pour transférer les futurs paquets vers la même destination sans intervention du processeur.",
            "D. Les paquets sont transférés en fonction des informations contenues dans le FIB et d’un tableau de contiguïté.",
            "E. Lorsqu’un paquet arrive sur une interface de routeur, il est transmis au plan de contrôle où le processeur recherche une correspondance dans le cache à commutation rapide."
        ],
        "answer": "B, D",
        "explanation": "Cisco Express Forwarding (CEF) est un mécanisme de transfert rapide qui utilise le FIB (Forwarding Information Base) et un tableau de contiguïté pour acheminer les paquets, ce qui permet de transférer rapidement les paquets sans intervention du processeur.",
        "image": ""
    },
    {
        "question": "160. Quel terme décrit le rôle d’un commutateur Cisco dans le contrôle d’accès basé sur les ports 802.1X ?",
        "options": [
            "A. agent",
            "B. suppliant",
            "C. authentificateur",
            "D. serveur d’authentification"
        ],
        "answer": "C",
        "explanation": "Dans un système 802.1X, le commutateur Cisco joue le rôle d'authentificateur, responsable de l’authentification des périphériques tentant de se connecter au réseau.",
        "image": ""
    },
    {
        "question": "161. Quelle solution Cisco permet d’éviter les attaques d’usurpation d’identité ARP et d'empoisonnement ARP ?",
        "options": [
            "A. Inspection ARP dynamique",
            "B. Protection des sources IP",
            "C. Snooping DHCP",
            "D. Sécurité des ports"
        ],
        "answer": "A",
        "explanation": "L’Inspection ARP dynamique permet de protéger le réseau contre les attaques ARP en vérifiant la validité des messages ARP, notamment pour prévenir l’empoisonnement ARP.",
        "image": ""
    },
    {
        "question": "162. Quel est l’avantage de PVST+ ?",
        "options": [
            "A. PVST+ optimise les performances sur le réseau grâce à la sélection automatique du pont racine.",
            "B. PVST+ réduit la consommation de bande passante par rapport aux implémentations traditionnelles de STP qui utilisent CST.",
            "C. PVST+ nécessite moins de cycles CPU pour tous les commutateurs du réseau.",
            "D. PVST+ optimise les performances sur le réseau grâce au partage de charge."
        ],
        "answer": "D",
        "explanation": "PVST+ optimise les performances en permettant un équilibrage de charge entre les VLAN, grâce à la configuration manuelle des ponts racine pour différents VLAN.",
        "image": ""
    },
    {
        "question": "163. Quel protocole ou quelle technologie utilise un routeur de secours pour assumer la responsabilité du transfert de paquets si le routeur actif tombe en panne ?",
        "options": [
            "A. EtherChannel",
            "B. DTP",
            "C. HSRP",
            "D. VTP"
        ],
        "answer": "C. HSRP",
        "explanation": "",
        "image": ""
    },
    {
        "question": "165. Quelle action a lieu lorsque l’adresse MAC source d’une trame entrant dans un commutateur est dans la table d’adresses MAC ?",
        "options": [
            "A. Le commutateur transfère la trame hors du port spécifié.",
            "B. Le commutateur met à jour la minuterie d’actualisation de l’entrée.",
            "C. Le commutateur remplace l’ancienne entrée et utilise le port le plus récent.",
            "D. Le commutateur ajoute une entrée de table d’adresses MAC pour l’adresse MAC de destination et le port de sortie."
        ],
        "answer": "B. Le commutateur met à jour la minuterie d’actualisation de l’entrée.",
        "explanation": "",
        "image": ""
    },
    {
        "question": "166. Une petite maison d’édition a une conception de réseau telle que lorsqu’une diffusion est envoyée sur le réseau local, 200 appareils reçoivent la diffusion transmise. Comment l’administrateur réseau peut-il réduire le nombre d’appareils recevant du trafic de diffusion ?",
        "options": [
            "A. Ajoutez plus de commutateurs afin que moins d’appareils soient sur un commutateur particulier.",
            "B. Remplacez les commutateurs par des commutateurs dotés de plus de ports par commutateur. Cela permettra à plus d’appareils sur un commutateur particulier.",
            "C. Segmentez le réseau local en réseaux locaux plus petits et acheminez entre eux.",
            "D. Remplacez au moins la moitié des commutateurs par des concentrateurs pour réduire la taille du domaine de diffusion."
        ],
        "answer": "C. Segmentez le réseau local en réseaux locaux plus petits et acheminez entre eux.",
        "explanation": "En divisant un grand réseau en deux réseaux plus petits, l’administrateur réseau a créé deux domaines de diffusion plus petits. Lorsqu’une diffusion est envoyée, elle ne sera envoyée qu’aux appareils sur le même réseau local Ethernet. L’autre LAN ne recevra pas la diffusion.",
        "image": ""
    },
    {
        "question": "167. Qu’est-ce qui définit une route hôte sur un routeur Cisco ?",
        "options": [
            "A. L’adresse lien-local est ajoutée automatiquement à la table de routage en tant que route hôte IPv6.",
            "B. Une configuration de route hôte statique IPv4 utilise une adresse IP de destination d’un appareil spécifique et un masque de sous-réseau /32.",
            "C. Une route hôte est désignée par un C dans la table de routage.",
            "D. Une route hôte IPv6 statique doit inclure le type d’interface et le numéro d’interface du routeur du prochain saut."
        ],
        "answer": "B. Une configuration de route hôte statique IPv4 utilise une adresse IP de destination d’un appareil spécifique et un masque de sous-réseau /32.",
        "explanation": "",
        "image": ""
    },
    {
        "question": "168. Quoi d’autre est requis lors de la configuration d’une route statique IPv6 à l’aide d’une adresse lien-local de prochain saut ?",
        "options": [
            "A. distance administrative",
            "B. adresse IP du routeur voisin",
            "C. numéro de réseau et masque de sous-réseau sur l’interface du routeur voisin",
            "D. numéro et type d’interface"
        ],
        "answer": "D. numéro et type d’interface",
        "explanation": "",
        "image": ""
    },
    {
        "question": "169. Un technicien configure un réseau sans fil pour une petite entreprise à l’aide d’un routeur sans fil SOHO. Quelles sont les deux méthodes d’authentification utilisées si le routeur est configuré avec WPA2 ? (Choisissez deux réponses.)",
        "options": [
            "A. personnel",
            "B. AES",
            "C. TKIP",
            "D. WEP",
            "E. entreprise"
        ],
        "answer": [
            "A. personnel",
            "E. entreprise"
        ],
        "explanation": "",
        "image": ""
    },
    {
        "question": "171. Un PC a envoyé un message RS à un routeur IPv6 connecté au même réseau. Quelles sont les deux informations que le routeur enverra au client ? (Choisissez deux réponses.)",
        "options": [
            "A. longueur du préfixe",
            "B. masque de sous-réseau en notation décimale à points",
            "C. nom de domaine",
            "D. distance administrative",
            "E. préfixe",
            "F. Adresse IP du serveur DNS"
        ],
        "answer": [
            "A. longueur du préfixe",
            "E. préfixe"
        ],
        "explanation": "Le routeur génère un RA contenant le préfixe du réseau local et la longueur du préfixe.",
        "image": ""
    },
    {
        "question": "172. Lorsqu’ils assistent à une conférence, les participants utilisent des ordinateurs portables pour la connectivité réseau. Lorsqu’un orateur invité tente de se connecter au réseau, l’ordinateur portable ne parvient pas à afficher les réseaux sans fil disponibles. Le point d’accès doit fonctionner dans quel mode ?",
        "options": [
            "A. mixte",
            "B. passif",
            "C. actif",
            "D. ouvrir"
        ],
        "answer": "C. actif",
        "explanation": "Le mode actif permet aux clients de se connecter uniquement s’ils connaissent le SSID. Le mode passif permet de diffuser le SSID, rendant le réseau visible pour les clients.",
        "image": ""
    },
    {
        "question": "173. Quels sont les trois composants combinés pour former un identifiant de pont ?",
        "options": [
            "A. ID système étendu",
            "B. coût",
            "C. Adresse IP",
            "D. priorité du pont",
            "E. Adresse MAC",
            "F. ID de port"
        ],
        "answer": [
            "A. ID système étendu",
            "D. priorité du pont",
            "E. Adresse MAC"
        ],
        "explanation": "Les trois composants qui forment un ID de pont sont la priorité du pont, l’ID système étendu et l’adresse MAC.",
        "image": ""
    }
]












@app.route('/')
def home():
    return redirect(url_for('quiz_page', question_index=0))

@app.route('/quiz/<int:question_index>', methods=['GET', 'POST'])
def quiz_page(question_index):
    # Vérifier si l'index est valide
    if question_index >= len(questions):
        return redirect(url_for('quiz_end'))  # Redirige vers la page de fin du quiz

    question = questions[question_index]
    feedback = None
    next_question_index = question_index + 1

    if request.method == 'POST':
        user_answer = request.form.get('answer')
        correct_answer = question['answer']
        print(f"Réponse de l'utilisateur: {user_answer}")
        # Comparer la réponse de l'utilisateur avec la bonne réponse
        if user_answer == correct_answer:
            feedback = f"La bonne réponse est :  {correct_answer}"
        else:
            feedback = f"La bonne réponse est :  {correct_answer}"

    # Si on a fini toutes les questions, redirige vers la fin du quiz
    if question_index + 1 >= len(questions):
        next_question_index = None  # Pas de prochaine question, quiz terminé

    return render_template('quiz_page.html', question=question, question_index=question_index, feedback=feedback, next_question_index=next_question_index)

@app.route('/quiz_end')
def quiz_end():
    return render_template('quiz_end.html')

if __name__ == '__main__':
    app.run(debug=True)