n8n is a free and open fair-code licensed node-based workflow automation tool. Render is a unified platform to build and run all your applications and websites with free SSL, a global CDN, private networks and auto deploys from Git. Supabase is an open source Firebase alternative.

Here are the steps to deploy an n8n automation pack on Render + Supabase:

1. **Create a Supabase Project:**
   - Go to supabase.io and click on "Start your project".
   - Sign in or create a new account.
   - Once logged in, click on "New Project".
   - Fill in the necessary details and click "Create new project".

2. **Create Database and Tables in Supabase:**
   - Once your project is created, go to the "Table Editor".
   - Click on "+ New Table" to create your tables and define the schema.

3. **Create a Render Account and Project:**
   - Go to render.com and click on "Sign Up" to create a new account.
   - Once logged in, click on "New+" and select "YAML".
   - Click on "New YAML" and provide a name for the service.
   - Paste your n8n YAML code and click on "Save".

4. **Configure n8n with Supabase:**
  - In your n8n project, use the Supabase node to connect to your Supabase project.
  - To do this, you'll need the Supabase URL and the anon public API key, which can be found in the settings of your Supabase project.
  - Once connected, you can start creating your workflows using the Supabase node.

5. **Deploy n8n on Render:**
   - Go back to Render and click on your YAML service.
   - Click on "Deploy" to deploy your n8n project.

6. **Test Your Workflow:**
   - Once your n8n project is deployed, you can access the n8n editor by clicking on the URL provided by Render.
   - Here you can manually trigger your workflows and check if they're running as expected.

Remember, you need to handle the security aspect such as securing your n8n editor and using secure credentials while connecting to Supabase. The exact steps might vary based on the specific requirements of your n8n automation pack.