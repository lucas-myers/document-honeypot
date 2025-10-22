# document-honeypot
This project implements a document-based honeypot designed to detect and monitor unauthorized access attempts on decoy files within a controlled environment(I used a VM of Ubuntu). The honeypot simulates sensitive corporate documents (e.g., “payroll_2025.xlsx”) and captures activity logs when these files are accessed or modified.

⚙️ Features

Automated deployment using Terraform and Ansible

Decoy files (e.g., payroll_2025.xlsx) hosted with Nginx to attract unauthorized access

Filebeat sends logs to Elasticsearch for indexing and analysis

Kibana dashboards visualize intrusion events and source IPs in real time


🧰 Tech Stack
Component	Tool
Infrastructure	Terraform
Configuration Management	Ansible
Logging	Filebeat
Data Storage	Elasticsearch
Visualization	Kibana
Web Server	Nginx
Containerization	Docker

🚀 How to Run

Deploy the Environment

terraform apply
ansible-playbook deploy.yml


Access Kibana
Open your browser and visit:

http://localhost:5601


View Logs
In Kibana → Discover, search for:

message: "payroll_2025.xlsx"

Purpose

This honeypot demonstrates how intrusion attempts can be safely observed and analyzed using automated tools and centralized logging systems.
It helps visualize attack patterns, source IPs, and access behavior for cybersecurity research and education.

⚠️ Disclaimer
This honeypot is for educational and research purposes only.
Do not deploy it on public networks or production systems.
