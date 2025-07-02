Creating a complex enterprise automation using n8n might require several components and actions. Here's a general representation of what a logic map might look like:

1. **Trigger**: This is the event that begins the automation process. For instance, a new entry in a CRM or a new form submission. 

2. **Data Extraction**: After the trigger, the next node could be set up to extract the necessary data from the triggering event.

3. **Data Processing**: This node will involve processing the data - this could involve cleaning the data, sorting it, or even performing calculations.

4. **Decision Nodes**: These nodes are responsible for making decisions based on the data. They can branch into multiple paths depending on the conditions set. For instance, if the data meets certain criteria, it might be sent down one path; otherwise, it's sent down a different path.

5. **Action Nodes**: These nodes perform actions based on the decision nodes. These can involve sending emails, updating a database, generating reports, etc.

6. **Error Handling Nodes**: These nodes are responsible for handling any errors that might occur during the automation process.

7. **End Node**: This is the final node that marks the end of the workflow. It could be sending a final report or simply a notification that the process has been completed.

This is a very general example of what a logic map for a complex enterprise n8n automation might look like. The actual map could be much more complex and involve many more nodes depending on the specific requirements of the enterprise.