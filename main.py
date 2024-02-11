import streamlit as st
import warnings
from data_utils import load_and_process_csv, filter_dataframe
from visualizations import (
    plot_market_cap_distribution, sector_wise_donut_chart,
    industry_wise_donut_chart, create_global_distribution_map,
    plot_stacked_bar_chart_by_country_and_industry,
    plot_stacked_bar_chart_by_country_and_sector,
    plot_stacked_bar_chart_by_country_and_sector_matplotlib,plot_market_cap_vs_count_by_sector)

warnings.filterwarnings('ignore')
st.set_page_config(layout="wide")


def main():
  st.title("Company Data Visualisation")
  chart_type = st.sidebar.radio("Select Chart Type: ", [
      "View Data Table", "Market Cap Distribution", "Sector Wise Donut Chart",
      "Industry Wise Donut Chart", "Global Distribution of Top Companies",
      "Stacked Bar Chart by Country and Industry",
      "Stacked Bar Chart by Country and Sector",
      "Stacked Bar Chart by Country and Sector (Matplotlib)", 
    "plot_market_cap_vs_count_by_sector"
  ])

  df = load_and_process_csv("companies_data.csv")

  exclude_companies = st.text_input(
      "Enter company names to exclude (comma separated)")

  df_filtered = filter_dataframe(df, exclude_companies)

  if chart_type == "View Data Table":
    st.dataframe(df_filtered)
  elif chart_type == "Market Cap Distribution":
    top_n = st.slider("Select number of top companies:", 10, 100, 20, 10)
    fig = plot_market_cap_distribution(df_filtered, top_n)
    st.pyplot(fig)
  elif chart_type == "Sector Wise Donut Chart":
    fig = sector_wise_donut_chart(df_filtered)
    st.plotly_chart(fig)
  elif chart_type == "Industry Wise Donut Chart":
    fig = industry_wise_donut_chart(df_filtered)
    st.plotly_chart(fig)
  elif chart_type == "Global Distribution of Top Companies":
    fig = create_global_distribution_map(df_filtered)
    st.plotly_chart(fig)
  elif chart_type == "Stacked Bar Chart by Country and Industry":
    fig = plot_stacked_bar_chart_by_country_and_industry(df_filtered)
    st.plotly_chart(fig)
  elif chart_type == "Stacked Bar Chart by Country and Sector":
    fig = plot_stacked_bar_chart_by_country_and_sector(df_filtered)
    st.plotly_chart(fig)
  elif chart_type == "Stacked Bar Chart by Country and Sector (Matplotlib)":
    fig = plot_stacked_bar_chart_by_country_and_sector_matplotlib(df_filtered)
    st.pyplot(fig)
  elif chart_type == "plot_market_cap_vs_count_by_sector":
    fig = plot_market_cap_vs_count_by_sector(df_filtered)
    st.plotly_chart(fig)


if __name__ == "__main__":
  main()
