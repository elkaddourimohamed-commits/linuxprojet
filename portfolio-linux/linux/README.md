# Linux Sysadmin Portfolio

8 petits projets Linux pour l'administration systèmes et réseaux. Python et Bash, documentation et exemples.

## Projets

- **01-healthcheck** — Résumé hôte, système, CPU, mémoire et espace disque.
- **02-user-audit** — Inventaire des comptes locaux et détection des UID 0.
- **03-log-triage** — Recherche d'erreurs dans un fichier de logs.
- **04-backup-verify** — Validation SHA-256 d'une sauvegarde à partir d'un manifeste.
- **05-permission-audit** — Repérage de fichiers world-writable sous un chemin choisi.
- **06-service-audit** — Liste des services systemd actifs.
- **07-ssh-hardening-check** — Contrôle de paramètres sshd sans modification.
- **08-network-diagnostics** — Résolution DNS et test de connectivité TCP.

## Utilisation

- Lire le README de chaque projet avant de lancer les scripts.
- Tester dans une VM ou un laboratoire, pas directement en production.
- Ne jamais publier de mots de passe, clés privées, tokens ou données réelles.
- Les scripts d'audit sont non destructifs ; les playbooks Ansible modifient leurs machines cibles.