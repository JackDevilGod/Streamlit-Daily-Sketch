import streamlit as st

from pathlib import Path
from random import randint

from function.folder import get_pictures

def main():
    st.header("Daily sketch tool")
    st.divider()

    new_folder = st.text_input("Path to pictures to choose from.")

    if st.button("Save path."):
        new_path = Path(new_folder)

        if not new_path.is_dir():
            st.error("Not a directory or incorrect path.")
            return

        st.session_state["picture path"] = new_path
        st.write("Path saved")

    if not ("picture path" in st.session_state):
        return

    st.write(f"current directory {st.session_state['picture path']}")

    st.session_state["picture paths"] = get_pictures(st.session_state["picture path"])

    if not ("picture paths" in st.session_state):
        return

    if not ("current picture" in st.session_state):
        st.session_state["current picture"] = st.session_state["picture paths"][randint(
            0, len(st.session_state["picture paths"]) - 1)]

    if st.button("next picture"):
        st.session_state["current picture"] = st.session_state["picture paths"][randint(
            0, len(st.session_state["picture paths"]) - 1)]

    st.image(st.session_state["current picture"])



if __name__ == '__main__':
    main()
