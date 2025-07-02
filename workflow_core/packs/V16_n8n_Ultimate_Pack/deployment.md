n8n is a free and open-source workflow automation tool that can be used to automate tasks, connect and manage microservices, and build custom workflows. Render is a unified platform to build and run all your apps and websites. Supabase is an open-source Firebase alternative that adds real-time and RESTful APIs to your PostgreSQL database.

Here are the steps to deploy an n8n automation pack on Render with Supabase:

1. **Create a Supabase Project**
   - Go to supabase.io and create a new project.
   - Once the project is created, take note of the 'API Url' and 'Public Anon Key' from the settings section.

2. **Setup n8n Project**
   - Clone the n8n project repository to your local machine.
   - Set up your project by installing the necessary dependencies using npm or yarn.
   - Configure your n8n project to use the Supabase API Url and Public Anon Key.

3. **Deploy to Render**
   - Go to render.com and create a new Web Service.
   - Choose your repository and branch.
   - Choose the environment as Node.
   - Set the build command as `npm run build`.
   - Set the start command as `npm start`.
   - Add the necessary environment variables. These should include the Supabase API Url and Public Anon Key.
   - Click on 'Save Web Service'. Render will now build and deploy your n8n project.

4. **Test Your Deployment**
   - Once your n8n project is deployed, you can test it by going to the public URL provided by Render.
   - Try running a workflow and check if the data is correctly stored in your Supabase database.

Remember, this is a high-level overview and the exact steps may vary based on the specifics of your n8n project and how it's set up to interact with Supabase. Always refer to the documentation provided by n8n, Render, and Supabase for the most accurate information.