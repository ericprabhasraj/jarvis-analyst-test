import pandas as pd
import matplotlib.pyplot as plt
from data_handler import loaded_data

def generate_chart(chart_info):
    if 'df' not in loaded_data:
        return False
    
    if not chart_info.get("chart", False):
        return False

    df = loaded_data['df']

    try:
        column = chart_info.get("column")
        kind = chart_info.get("kind", "bar")
        top_n = chart_info.get("top_n", 10)
        title = chart_info.get("title", f"{column} chart")

        if column not in df.columns:
            return False

        # Handle multi-value columns like listed_in, cast
        if column in ["listed_in", "cast"]:
            data = df[column].dropna().str.split(', ').explode().value_counts().head(top_n)
        elif column == "release_year":
            if "lowest" in title.lower() or "least" in title.lower():
                data = df[column].value_counts().sort_index().head(top_n)
            else:
                data = df[column].value_counts().sort_index().tail(top_n)
        else:
            data = df[column].dropna().value_counts().head(top_n)

        fig, ax = plt.subplots(figsize=(12, 6))

        if kind == "pie":
            data.plot(kind="pie", autopct='%1.1f%%', ax=ax)
            ax.set_ylabel('')
        else:
            data.plot(kind="bar", ax=ax, color='steelblue', edgecolor='black')
            plt.xticks(rotation=45, ha='right')

        ax.set_title(title, fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show(block=False)
        plt.pause(0.1)
        return True

    except Exception as e:
        print(f"Chart error: {e}")
        return False