import streamlit as st # external module
import function # My own local module
import datetime #python inbuilt module

todos=function.get_todos()
st.title(" Todos App")


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://static.vecteezy.com/system/resources/thumbnails/024/041/277/small/robot-neon-high-tech-concept-sports-game-of-cyberpunk-science-fiction-a-scene-stand-pedestal-stage-illustration-and-futuristic-neon-glow-generative-ai-photo.jpg");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.write("Keep track of your tasks here!")
st.header("Tasks")
def add_todo():
    todo = st.session_state['new_todo_input']
    now = datetime.datetime.now().strftime("%d/%b/%Y %H:%M:%S")
    todos.append("\n"+todo+f"\t\t (Created At: {now})"+"\n")
    function.write_todos(todos)
    st.session_state['new_todo_input'] = ''
    st.rerun()
            
for index,todo in enumerate(todos):
    if len(todo.strip()) == 0:
        continue
    
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        del st.session_state[todo]
        function.write_todos(todos)
        
        st.rerun()   
    
st.text_input(label="Enter a todo",placeholder="Add todo",
              key='new_todo_input',on_change=add_todo)

    
    






