# Operations and delivery

Status: procedural requirements only. No server has been deployed.

Candidate target: VPS with containerized services and durable volumes. Identify development, staging and production environments.
Build a versioned image from an identified commit; verify in staging before promotion.
Retain previous versions and document migration compatibility before rollback.
Back up database, files, sessions and secret-recovery material; test restoration.
Never expose secrets in logs or publish an application preview by default.
Document provider selection and exact deployment commands after the prototype.
