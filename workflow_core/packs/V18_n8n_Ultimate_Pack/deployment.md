n8n is an extendable workflow automation tool that allows you to connect anything to everything via its open, fair-code model. Render is a unified platform to build and run all your apps and websites with free SSL, a global CDN, private networks and auto deploys from Git. Supabase adds real-time and RESTful APIs to your existing PostgreSQL database without a single line of code. 

Here are the steps you need to follow to deploy an n8n automation pack on Render + Supabase:

1. **Setting up Supabase:**

   - Go to supabase.io and sign up for a new account.
   - Create a new project and note down the `SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY` from the settings.

2. **Setting up n8n:**

   - Install n8n on your local machine using npm with the command `npm install n8n -g`.
   - Run n8n with the command `n8n` and create your automation workflow.
   - Save the workflow and note down the workflow ID.

3. **Creating a new Render service:**

   - Go to render.com and sign up for a new account.
   - Click on "New Service" and choose "Public Service".
   - Fill in the service details:
     - Name: Can be anything you want.
     - Repo: Use the n8n Docker repository (n8nio/n8n).
     - Branch: Use the main branch.
     - Dockerfile: Use the default Dockerfile.
     - Environment: Choose the environment where you want to run your service.
     - Add the following environment variables:
       - `N8N_BASIC_AUTH_ACTIVE=true`
       - `N8N_BASIC_AUTH_USER=<your_username>`
       - `N8N_BASIC_AUTH_PASSWORD=<your_password>`
       - `N8N_HOST=<your_render_service_url>`
       - `N8N_PORT=443`
       - `WEBHOOK_TUNNEL_URL=https://<your_render_service_url>`
       - `VUE_APP_URL_BASE_API=https://<your_render_service_url>`
       - `SUPABASE_URL=<your_supabase_url>`
       - `SUPABASE_SERVICE_ROLE_KEY=<your_supabase_service_role_key>`
       - `EXECUTIONS_PROCESS=main`
   - Click on "Create Service".

4. **Deploying your n8n workflow:**

   - Once your service is up and running, go to the n8n editor UI at `https://<your_render_service_url>`.
   - Load your saved workflow using the workflow ID.
   - Click on "Activate" to start the workflow.

5. **Testing your deployment:**

   - You can test your deployment by triggering the workflow manually or by setting up a webhook to trigger it.
   - You can check the workflow execution and results in the n8n editor UI.

Remember to replace `<your_username>`, `<your_password>`, `<your_render_service_url>`, `<your_supabase_url>`, and `<your_supabase_service_role_key>` with your actual values.