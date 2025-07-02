Creating a logic map for a complex enterprise n8n automation involves several steps, including identifying the tasks, setting their order, and determining how they will interact. Below is an outline of one possible logic map.

1. **Trigger** - This is the event that starts the automation process. For example, it could be an incoming email, a new entry in a database, or a scheduled time.

2. **Filter** - This step involves filtering the data from the trigger. For example, if the trigger is an incoming email, the filter could sort the emails based on their subject line.

3. **Retrieve Data** - This step involves retrieving necessary data from the enterprise's databases or other sources. This may be needed to process the trigger event properly.

4. **Process Data** - This step involves processing the retrieved data. This could involve calculations, data transformations, or running algorithms.

5. **Conditional Logic** - This step involves making decisions based on the processed data. If certain conditions are met, the automation process might proceed in one way. If the conditions are not met, the process might proceed differently.

6. **Action** - This is the ultimate task or tasks that the automation process is intended to perform. Depending on the data and the decisions made in the previous steps, different actions might be taken.

7. **Notification/Reporting** - After the action is completed, there may be a step to notify stakeholders or generate a report. For example, an email might be sent to a supervisor, a record might be added to a database, or a dashboard might be updated.

8. **Error Handling** - This step involves handling any errors that might occur during the automation process. This could involve sending an alert, retrying a failed operation, or skipping a step.

9. **Looping** - In some cases, the automation process might loop back to a previous step. For example, if new data has been added to a database, the process might start again from the Retrieve Data step.

Remember, this is only a rough outline. The actual logic map for a complex enterprise n8n automation will depend on the specific needs and resources of the enterprise. It may involve more steps, fewer steps, or different steps altogether.