

When we call the addition.py module inside the call\_modules\_within\_same\_package we get an

output as shown below.

This call executes the addition.py script serially by first running the print statement and then

executing the lines of codes under **if \_\_name\_\_ == '\_\_main\_\_':**

When we call the import\_addition.py module it first imports the add function and the addition\_str

string from the addition.py module. As the addition.py module is being imported, everything

inside the addition.py module is executed except for the lines of codes under **if \_\_name\_\_ ==**

**'\_\_main\_\_':.** And the output for calling the import\_addition.py is shown below.

Inside the helper\_scripts module we have several utility modules containing some helper

functions that need to be accessed and called from anywhere. To facilitate this we define the

\_\_init\_\_.py script which basically imports the required helper functions. The helper functions are

imported by specifying the absolute path of the module and is shown below.

So now the helper function has been converted to a module and can be imported from

anywhere just by writing **import helper\_scripts.** After importing like this we will have access to

the cosine\_distance, euclidean\_distance helper function. We define a script called

call\_helper.py outside the helper\_scripts directory. Inside this script we call cosine\_distance and

euclidean\_distance and output is shown below.





