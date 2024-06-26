#!/usr/bin/env python
# coding: utf-8

# In[2]:


gpt_key = #add key

import os

import openai

import json
openai.api_key = gpt_key


# In[ ]:


system_msg="Imagine you are going camping as part of boys scouts, who are all about 11-12 years old. There are two groups of boys, Group A and Group B. Members of each of the groups had homogeneous backgrounds and were Hispanic or Latino boys from middle class homes. Group A and Group B stay at the same campsite in a state park for a week. Students in each of the groups know each other very well. The ranger of the state park arranges competitions for the two groups. Each day Group A competes with Group B. They play games such as, volleyball, basketball, tennis, soccer and badminton. The winning group received prizes and the losing group receives nothing. Often times, one of the groups would receive food quickly and the other group would be told to wait."

user_messages=[]

user_msg1 = "Now pretend that you are a student in Group A and your team was asked to wait for food. Would you team up with Group B to overthrow the unfair counsellors? Answer with only yes or no."
user_messages.append(user_msg1)

user_msg2 = "Now pretend that you are a student in Group A and your team was asked to wait for food. Would you want to eat Group B's food if you were hungry? Answer with only yes or no."
user_messages.append(user_msg2)

user_msg3 = "Now pretend that you are a student in Group A and your team was asked to wait for food.Rocks blocked the water tower and the students had no access to water to drink. There were no other water sources at the camp. Would you and your group work with Group B to move the rocks so students get access to the water? Answer with only yes or no."
user_messages.append(user_msg3)

user_msg4 = "Now pretend that you are a student in Group A and your team was asked to wait for food. A truck delivering food to the camp was stuck and couldn't deliver the meals. The students were all hungry. Would you and your group work with Group B to move the truck? Answer with only yes or no."
user_messages.append(user_msg4)


# In[ ]:


model_name="gpt-3.5-turbo"
import numpy as np
import matplotlib.pyplot as plt 

for j in range(len(user_messages)):
    print(user_messages[j])
    response = openai.ChatCompletion.create(model=model_name, 
                                            messages=[{"role": "system", "content": system_msg},
                                             {"role": "user", "content": user_messages[j]}],
                                           temperature=1,
                                          max_tokens=5,
                                          top_p=1,
                                          n=10,logprobs=True, top_logprobs=2)
    
    yes_val=response["choices"][0]["logprobs"]["content"][0]["top_logprobs"][0]["logprob"]
    no_val=response["choices"][0]["logprobs"]["content"][0]["top_logprobs"][1]["logprob"]
    yes_prob=np.exp(yes_val)/(np.exp(yes_val) + np.exp(no_val))
    no_prob=1.0-yes_prob
    print('Yes:', yes_prob, 'No:', no_prob)
    
    data = {'Yes':yes_prob, 'No':no_prob}
    courses = list(data.keys())
    values = list(data.values())
  
    fig = plt.figure(figsize = (10, 5))
 
    plt.bar(courses, values, color ='maroon', 
            width = 0.4)
 
    plt.xlabel("Yes or No",fontweight ='bold', fontsize = 10)
    plt.ylabel("Probability for user_message"+str(j), fontweight ='bold', fontsize = 10)
    plt.savefig(str(j)+model_name+'-simplified.pdf')
    plt.show() 


# In[ ]:




