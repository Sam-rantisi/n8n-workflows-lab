Creating a logic map for a complex enterprise n8n automation pack involves mapping out the flow of data and tasks between different nodes in the network. Here is a basic example:

1. Start Node: This is the starting point of the automation process. It could be set to trigger at a specific time or event, such as receiving an email or a new entry in a database.

2. Email Node: If the trigger is an email, the email node will extract necessary information from the email, such as the sender's email address, the subject line, or any attachments.

3. Decision Node: Based on the information extracted from the email, the decision node will determine the next step in the process. For example, if the email subject line contains a certain keyword, it may route the process to a specific node.

4. Processing Nodes: These nodes carry out various tasks such as data processing, data analysis, or sending notifications. They are usually the core of the automation process.

5. Database Node: The database node can store the results from the processing nodes. It can also retrieve data for further processing.

6. Notification Node: Depending on the results, a notification node can send an email or a message to a specific person or a group of people. 

7. Error Handling Node: This node handles any errors that occur in the process. It can send error notifications, retry failed tasks, or reroute the process to a different node.

8. End Node: This signifies the end of the automation process. 

This is a basic example and the actual logic map would be more complex depending on the specifics of your enterprise's automation needs.