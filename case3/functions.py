import streamlit as st

def ensure_list_format(column):
    return column.apply(
        lambda x: (
            x.split(",") if isinstance(x, str) else (x if isinstance(x, list) else [])
        )
    )


def clean_list_items(column):
    return column.apply(lambda lst: [item.strip() for item in lst])


def filter_df_by_list_contains(df, filters: dict):
    filtered_df = df.copy()
    for col, search_values in filters.items():
        if not isinstance(search_values, list):
            search_values = [search_values]
        search_values = [s.lower() for s in search_values]
        filtered_df = filtered_df[
            filtered_df[col].apply(
                lambda lst: any(
                    sv in item.lower() for item in lst for sv in search_values
                )
            )
        ]
    return filtered_df



def get_filtered_actors(df, selected_genres):
    if selected_genres:
        df_filtered = filter_df_by_list_contains(df, {"Genre": selected_genres})
    else:
        df_filtered = df
    return sorted({actor for sublist in df_filtered["Actors"] for actor in sublist})


def get_filtered_genres(df, selected_actors):
    if selected_actors:
        df_filtered = filter_df_by_list_contains(df, {"Actors": selected_actors})
    else:
        df_filtered = df
    return sorted({genre for sublist in df_filtered["Genre"] for genre in sublist})


def update_selected_genres():
    st.session_state.selected_genres = st.session_state.tmp_genres


def update_selected_actors():
    st.session_state.selected_actors = st.session_state.tmp_actors