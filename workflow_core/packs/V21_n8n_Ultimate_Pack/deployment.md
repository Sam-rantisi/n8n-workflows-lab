n8n is an open-source workflow automation tool that you can self-host. Render is a cloud service that allows you to host your applications in the cloud. Supabase is an open-source alternative to Firebase, providing user management, database, real-time subscriptions, and serverless functions. Here's how you can deploy an n8n automation pack on Render with Supabase:

1. **Set up your Supabase project:**

   - Go to the Supabase.io and sign up for a new account if you don't already have one.
   - Create a new project in Supabase and note down the `Supabase URL` and `Supabase Service Role Key`.

2. **Create a new Render account:**

   - Go to render.com and sign up for a new account if you don't already have one.

3. **Deploy the n8n to Render:**

   - Click on the `New` dropdown button and select `YAML`.
   - Click on the `New Document` button.
   - Paste the following YAML code:

```yaml
services:
- type: web
  name: n8n
  env: docker
  healthCheckPath: /
  envVars:
  - key: N8N_BASIC_AUTH_ACTIVE
    value: 'true'
  - key: N8N_BASIC_AUTH_USER
    sync: false
  - key: N8N_BASIC_AUTH_PASSWORD
    sync: false
  - key: N8N_HOST
    value: n8n.onrender.com
  - key: N8N_PORT
    value: '5678'
  - key: N8N_PROTOCOL
    value: https
  - key: VUE_APP_URL_BASE_API
    value: n8n.onrender.com
  - key: GENERIC_TIMEZONE
    value: Europe/Berlin
  - key: EXECUTIONS_PROCESS
    value: main
  - key: N8N_ENCRYPTION_KEY
    sync: false
  - key: WEBHOOK_TUNNEL_URL
    value: n8n.onrender.com
  - key: N8N_LICENSE_KEY
    sync: false
  - key: SUPABASE_URL
    value: 'Your_Supabase_URL' # Replace with your Supabase URL
  - key: SUPABASE_KEY
    value: 'Your_Supabase_Service_Role_Key' # Replace with your Supabase Service Role Key
  disk:
    name: n8n-disk
    sizeGB: 10
    mountPath: /root/.n8n
```

   - Replace `'Your_Supabase_URL'` and `'Your_Supabase_Service_Role_Key'` with your Supabase project details.

   - Click on the `Save` button to create the service.

4. **Configure the n8n automation:**

   - Once the n8n service is deployed, you can access the n8n web interface using the service URL.
   - You can now create and manage your workflows on the n8n platform.

Remember to secure your n8n instance as it can be accessed from the internet. You can do this by setting up basic authentication via the `N8N_BASIC_AUTH_ACTIVE`, `N8N_BASIC_AUTH_USER`, and `N8N_BASIC_AUTH_PASSWORD` environment variables.