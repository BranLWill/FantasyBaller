## Steps Run the app - (You will need docker)

1. Building the app - `docker compose build`
2. Running the app - `docker compose up`
3. Stop the app - `docker compose down`
4. Access the webapp - `http://localhost:3000`

NOTE: It does take a good minute for the flask rest api to start up.

## TASKS

- Models will include at least…
  - Two classes with primary keys at least two attributes each
  - [Optional but encouraged] One-to-many or many-to-many relationships between classes
- Endpoints will include at least…
  - Two GET requests
  - One POST request
  - One PATCH request
  - One DELETE request
- Roles will include at least…
  - Two roles with different permissions
  - Permissions specified for all endpoints
- Tests will include at least….
  - One test for success behavior of each endpoint
  - One test for error behavior of each endpoint
  - At least two tests of RBAC for each role
