n8n is a free and open fair-code licensed node-based workflow automation tool. Render is a unified platform to build and run all your apps and websites and Supabase adds real-time and RESTful APIs to your existing PostgreSQL database.

Here are the instructions for deploying an n8n automation pack on Render + Supabase:

Note: This guide assumes you already have an existing n8n workflow and a Supabase project.

1. **Create a repository for your n8n workflows:**

   Create a Git repository to store your n8n workflows. You can use GitHub, GitLab, or Bitbucket. For each workflow, create a .json file in the repository.

2. **Set up Render:**

   - Sign up for a Render account if you haven't already.
   - Click on "New Web Service" from your Render dashboard.
   - Connect your Git repository to Render.
   - Choose 'Docker' as the Environment and use the official n8n Docker image (`n8nio/n8n`).
   - Configure the environment variables. You would need to add `N8N_BASIC_AUTH_USER`, `N8N_BASIC_AUTH_PASSWORD`, `N8N_HOST`, `N8N_PORT`, `WEBHOOK_TUNNEL_URL` and `VUE_APP_URL_BASE_API`. You'll find the values for these variables in your n8n and Supabase dashboards.
   - Click on 'Save Web Service'.

3. **Set up Supabase:**

   - Sign up for a Supabase account if you haven't already.
   - Create a new project in Supabase.
   - Go to the 'API' section in your Supabase project settings and find the URL and public anonymous key.
   - Add these values to your Render environment variables as `SUPABASE_URL` and `SUPABASE_KEY`.

4. **Deploy your n8n workflows:**

   - From your Render dashboard, trigger a manual deploy of your web service.
   - Render will pull the latest code from your Git repository, build the Docker image, and run your n8n workflows.

5. **Testing your deployment:**

   - Once the deployment is successful, you can test your workflows by accessing the n8n editor at the URL provided by Render.
   - You should also see your workflows interacting with your Supabase database.

Remember that the environment variables and settings can vary based on the specific requirements of your n8n workflows and Supabase setup. Always refer to the official documentation for n8n, Render, and Supabase for the most accurate information.