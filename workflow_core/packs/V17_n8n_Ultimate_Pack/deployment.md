n8n is an open-source workflow automation tool that allows you to connect anything to everything. It supports both code and no-code solutions, making it easy to use for developers and non-developers alike.

Supabase, on the other hand, is an open-source alternative to Firebase. It offers a suite of tools for building modern, fast, and scalable applications, including a database, authentication and storage solutions, and serverless functions.

Render is a unified platform to build and run all your apps and websites with free SSL, a global CDN, private networks, and auto deploys from Git.

Here are the steps to deploy an n8n automation pack on Render + Supabase:

1. **Setup Supabase:**

   Sign up on Supabase and create a new project. After creating the project, note down the Supabase URL and the public anon key, you'll need these later.

2. **Setup n8n:**

   Install n8n on your local machine. You can do this by running `npm install n8n -g` in your terminal. Once installed, start n8n by running `n8n` in your terminal. This will start the n8n editor UI.

3. **Create your Workflow:**

   In the n8n editor UI, create a new workflow. You can do this by clicking on the "+" button on the top right corner of the UI. A workflow in n8n is a set of operations that are executed in a specific order. These operations can be anything from sending an email, making an API call, querying a database, etc.

4. **Setup Render:**

   Sign up on Render and click on the 'New' button to create a new Web Service. In the settings, set the build command to `npm run start` and the start command to `n8n`. Also, set the environment variables `N8N_HOST`, `N8N_PORT`, `N8N_PROTOCOL`, and `WEBHOOK_TUNNEL_URL` to your Render URL.

5. **Deploy:**

   Once you have everything set up, click on the 'Save & Deploy' button on Render. This will start the deployment process. Once the deployment is done, you can access your n8n workflow by visiting your Render URL.

6. **Connect n8n to Supabase:**

   In your n8n workflow, add a new node and select the 'Supabase' resource. In the settings, set the 'Operation' to 'Execute SQL Query' and the 'Query' to your SQL query. In the 'Supabase API URL' and 'Supabase Public Anon Key' fields, enter the Supabase URL and the public anon key you noted down earlier.

7. **Test:**

   Once you have everything set up, you can test your workflow by clicking on the 'Execute Workflow' button in the n8n editor UI. If everything is set up correctly, your workflow should run without any issues.

Congratulations, you have successfully deployed an n8n automation pack on Render + Supabase.