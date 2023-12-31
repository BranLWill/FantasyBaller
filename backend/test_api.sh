echo Basic public endpoint test with user Auth 
curl --request GET \
  --url http://127.0.0.1:5000/api/public

echo Basic private endpoint test with user Auth 
curl --request GET \
  --url http://127.0.0.1:5000/api/private \
  --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJfOTR4TG45U0lVaTVVZTgxemFrZiJ9.eyJpc3MiOiJodHRwczovL2FjY2Vzcy1hdXRoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJPSFFQUndES05XVDlqaFNLOGtpTHJLMHFpZnppcDg2VkBjbGllbnRzIiwiYXVkIjoibWluZCIsImlhdCI6MTY5NjY5MjA3NSwiZXhwIjoxNjk2Nzc4NDc1LCJhenAiOiJPSFFQUndES05XVDlqaFNLOGtpTHJLMHFpZnppcDg2ViIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbXX0.h-9PwaTw59kH-xw5Wh6-AFtGag33UMYCv713nS6Xz3e8uD15b6x3uiJG_bmdMkCXARJKAg3E1YiZQgDBxB2Q4r-cb97ksJfhbqzfOeSoynpy8Rc4smg9c-iZIBKVd4MkX2V01LFqK8x-U9mfIqlNTmNVXo7upGiTklBC0u46py3gymUVjjq8Hs_llx7I5Ti8mFjb0BBQ2kclGE7B6eGEI7uUxS_EYJUqocNSrtp2YIZc6SMFIRNV-D0bWcf1285JJXTHukT0Z6RzFgbANL4CZNRLkBNiNGo1PS4KbAmMY7qT0qiqAWKZCr55EwiiGsenA9c9urqxN7hfEA-bnksWaQ'

echo Basic private-scoped endpoint test with user Auth
curl --request GET \
  --url http://127.0.0.1:5000/api/private-scoped \
  --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJfOTR4TG45U0lVaTVVZTgxemFrZiJ9.eyJpc3MiOiJodHRwczovL2FjY2Vzcy1hdXRoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJPSFFQUndES05XVDlqaFNLOGtpTHJLMHFpZnppcDg2VkBjbGllbnRzIiwiYXVkIjoibWluZCIsImlhdCI6MTY5NjY5MjA3NSwiZXhwIjoxNjk2Nzc4NDc1LCJhenAiOiJPSFFQUndES05XVDlqaFNLOGtpTHJLMHFpZnppcDg2ViIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbXX0.h-9PwaTw59kH-xw5Wh6-AFtGag33UMYCv713nS6Xz3e8uD15b6x3uiJG_bmdMkCXARJKAg3E1YiZQgDBxB2Q4r-cb97ksJfhbqzfOeSoynpy8Rc4smg9c-iZIBKVd4MkX2V01LFqK8x-U9mfIqlNTmNVXo7upGiTklBC0u46py3gymUVjjq8Hs_llx7I5Ti8mFjb0BBQ2kclGE7B6eGEI7uUxS_EYJUqocNSrtp2YIZc6SMFIRNV-D0bWcf1285JJXTHukT0Z6RzFgbANL4CZNRLkBNiNGo1PS4KbAmMY7qT0qiqAWKZCr55EwiiGsenA9c9urqxN7hfEA-bnksWaQ'

echo Basic data endpoint test with user Auth
curl --request GET \
  --url http://127.0.0.1:5000/api/data \
  --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJfOTR4TG45U0lVaTVVZTgxemFrZiJ9.eyJpc3MiOiJodHRwczovL2FjY2Vzcy1hdXRoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJPSFFQUndES05XVDlqaFNLOGtpTHJLMHFpZnppcDg2VkBjbGllbnRzIiwiYXVkIjoibWluZCIsImlhdCI6MTY5NjY5MjA3NSwiZXhwIjoxNjk2Nzc4NDc1LCJhenAiOiJPSFFQUndES05XVDlqaFNLOGtpTHJLMHFpZnppcDg2ViIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbXX0.h-9PwaTw59kH-xw5Wh6-AFtGag33UMYCv713nS6Xz3e8uD15b6x3uiJG_bmdMkCXARJKAg3E1YiZQgDBxB2Q4r-cb97ksJfhbqzfOeSoynpy8Rc4smg9c-iZIBKVd4MkX2V01LFqK8x-U9mfIqlNTmNVXo7upGiTklBC0u46py3gymUVjjq8Hs_llx7I5Ti8mFjb0BBQ2kclGE7B6eGEI7uUxS_EYJUqocNSrtp2YIZc6SMFIRNV-D0bWcf1285JJXTHukT0Z6RzFgbANL4CZNRLkBNiNGo1PS4KbAmMY7qT0qiqAWKZCr55EwiiGsenA9c9urqxN7hfEA-bnksWaQ'

echo Basic data endpoint test with user Auth
curl --request GET \
  --url http://127.0.0.1:5000/api/data \
  --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJfOTR4TG45U0lVaTVVZTgxemFrZiJ9.eyJpc3MiOiJodHRwczovL2FjY2Vzcy1hdXRoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwOTU2NDAyOTI0ODEwODg3NDUyMSIsImF1ZCI6WyJtaW5kIiwiaHR0cHM6Ly9hY2Nlc3MtYXV0aC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjk2Njk0NzAyLCJleHAiOjE2OTY3ODExMDIsImF6cCI6IkpNU1NEYk1oZEtJVGowczBTcEsxSjFrTnNiTTh0UXkzIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbXX0.YhAKm7CNwMkRaywV1Wvpfn7WsSaCrFR6eBohRkL_xH8asfc7CKR1yqtjPzKxj8T4pGpjC9xB_YcJRk9dH4Ejkp75v6Y9bl2PRYAfDSJcRzteB2HCi8rQLc5cgKWZ7HupbR60gWsLi8TamI0HAmk09xUGcDPfaUX9TLFSfJdvbouL7AB5dStorKMqohYGlMVyl-0jlQ9MNwRgQ-DcPwcp9NwDBnrWbJz7AygmLkY_fpxs5z-pGSN6vnPjXAsKq-EzEha2SrnhQndhJ27BuQxkIXL-G8_pcx-gKNx4p0ESfNG8OdH--dhzzIBFHDSafrCZrtALRb8HusVguyTA4Xm8ew'

echo Basic players endpoint test with user Auth
curl --request GET \
  --url http://127.0.0.1:5000/api/players \
  --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJfOTR4TG45U0lVaTVVZTgxemFrZiJ9.eyJpc3MiOiJodHRwczovL2FjY2Vzcy1hdXRoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwOTU2NDAyOTI0ODEwODg3NDUyMSIsImF1ZCI6WyJtaW5kIiwiaHR0cHM6Ly9hY2Nlc3MtYXV0aC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjk2Njk0NzAyLCJleHAiOjE2OTY3ODExMDIsImF6cCI6IkpNU1NEYk1oZEtJVGowczBTcEsxSjFrTnNiTTh0UXkzIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbXX0.YhAKm7CNwMkRaywV1Wvpfn7WsSaCrFR6eBohRkL_xH8asfc7CKR1yqtjPzKxj8T4pGpjC9xB_YcJRk9dH4Ejkp75v6Y9bl2PRYAfDSJcRzteB2HCi8rQLc5cgKWZ7HupbR60gWsLi8TamI0HAmk09xUGcDPfaUX9TLFSfJdvbouL7AB5dStorKMqohYGlMVyl-0jlQ9MNwRgQ-DcPwcp9NwDBnrWbJz7AygmLkY_fpxs5z-pGSN6vnPjXAsKq-EzEha2SrnhQndhJ27BuQxkIXL-G8_pcx-gKNx4p0ESfNG8OdH--dhzzIBFHDSafrCZrtALRb8HusVguyTA4Xm8ew'
