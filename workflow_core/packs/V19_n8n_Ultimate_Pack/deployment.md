Before you begin, you need to have an account on Render and Supabase. If you haven't already, sign up for both services. 

1. **Setting up Supabase**

    - Go to supabase.io and create a new project.
    - Once your project is ready, go to the 'settings' and then 'API' section to get the URL and public anon key. You will need these later.

2. **Setting up n8n on Render**

    - Go to render.com and create a new web service.
    - Select 'Use a Dockerfile' and input 'n8nio/n8n' as the Dockerfile.
    - Set the environment variables. You need to set the following variables:
        - N8N_BASIC_AUTH_ACTIVE=true
        - N8N_BASIC_AUTH_USER=your_username
        - N8N_BASIC_AUTH_PASSWORD=your_password
        - N8N_HOST=your_render_service_on_render.com
        - N8N_PORT=443
        - N8N_PROTOCOL=https
        - WEBHOOK_TUNNEL_URL=https://your_render_service_on_render.com/
        - NODE_ENV=production
        - N8N_ENCRYPTION_KEY=your_encryption_key
        - EXECUTIONS_PROCESS=main
        - GENERIC_TIMEZONE=your_timezone
    - Click 'Create Web Service'.

3. **Connecting n8n to Supabase**

    - Go to your n8n instance on Render and open the n8n editor.
    - Create a new workflow and add a new node.
    - Select the 'HTTP Request' node.
    - Set the 'URL' field to your Supabase URL followed by '/rest/v1/your_table_name?select=*'.
    - Set the 'Headers' field to 'apikey' and the value to your Supabase public anon key.
    - Set the 'Options' -> 'Full Response' field to true.
    - Click 'Execute Node' to test the connection to your Supabase project.

4. **Creating an automation workflow**

    - Now that you have connected n8n to Supabase, you can create an automation workflow.
    - Use the various nodes available in n8n to create your workflow. You can add triggers, actions, and more to automate your tasks.
    - Once you have created your workflow, click 'Save' to save it.

5. **Deploying your automation pack**

    - Your automation workflow is now ready to be deployed.
    - Click 'Activate' to activate your workflow. Your workflow will now run automatically according to the triggers and conditions you have set.

That's it! You have successfully deployed an n8n automation pack on Render and connected it to your Supabase project.