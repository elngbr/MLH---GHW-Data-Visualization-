import matplotlib.pyplot as plt
import plotly.express as px


def plot_market_cap_distribution(df, top_n=20):
  df_sorted = df.sort_values(by="Market Cap (USD) Numerical", ascending=False)
  top_companies = df_sorted.head(top_n)
  fig, ax = plt.subplots(figsize=(20, 30))
  ax.barh(top_companies["Company"],
          top_companies["Market Cap (USD) Numerical"])
  ax.set_xlabel("Market Cap (USD)")
  ax.set_ylabel("Company")
  ax.set_title(f"Top {top_n} Companies by Market Cap (USD) in Billions")
  ax.invert_yaxis()
  return fig


def sector_wise_donut_chart(df):
  sector_counts = df["Sector"].value_counts().reset_index()
  sector_counts.columns = ["Sector", "NumberOfCompanies"]
  fig = px.pie(sector_counts,
               values="NumberOfCompanies",
               names="Sector",
               hole=0.3,
               title="Sector-wise Distribution of Companies")
  return fig


def industry_wise_donut_chart(df):
  industry_counts = df["Industry"].value_counts().reset_index()
  industry_counts.columns = ["Industry", "NumberOfCompanies"]
  fig = px.pie(industry_counts,
               values="NumberOfCompanies",
               names="Industry",
               hole=0.3,
               title="Industry-wise Distribution of Companies")
  return fig


def create_global_distribution_map(df):
  country_counts = df["Country"].value_counts().reset_index()
  country_counts.columns = ["Country", "NumberOfCompanies"]
  fig = px.choropleth(country_counts,
                      locations="Country",
                      locationmode="country names",
                      color="NumberOfCompanies",
                      hover_name="Country",
                      color_continuous_scale=px.colors.sequential.Darkmint,
                      title="Global Distribution of Top Companies")
  return fig


def plot_stacked_bar_chart_by_country_and_industry(df):
  industry_counts = df.groupby(['Country',
                                'Industry']).size().reset_index(name="Counts")
  wide_df = industry_counts.pivot(index="Country",
                                  columns="Industry",
                                  values="Counts")
  fig = px.bar(wide_df,
               x=wide_df.index,
               y=wide_df.columns,
               title="Number of Companies by Industry in Each Country")
  fig.update_layout(xaxis_title="Country",
                    yaxis_title="Number of Companies",
                    barmode="stack")
  fig.update_traces(hovertemplate="%{y} Companies in %{x}")
  return fig


def plot_stacked_bar_chart_by_country_and_sector(df):
  sector_counts = df.groupby(['Country',
                              'Sector']).size().reset_index(name="Counts")
  wide_df = sector_counts.pivot(index="Country",
                                columns="Sector",
                                values="Counts")
  fig = px.bar(wide_df,
               x=wide_df.index,
               y=wide_df.columns,
               title="Number of Companies by Sector in Each Country")
  fig.update_layout(xaxis_title="Country",
                    yaxis_title="Number of Companies",
                    barmode="stack")
  fig.update_traces(hovertemplate="%{y} Companies in %{x}")
  return fig


def plot_stacked_bar_chart_by_country_and_sector_matplotlib(df):
  sector_counts = df.groupby(['Country', 'Sector']).size().unstack()
  fig, ax = plt.subplots(figsize=(20, 15))
  sector_counts.plot(kind="bar", stacked=True, ax=ax)
  ax.set_title("Number of Companies by Sector in each Country")
  ax.set_xlabel("Country")
  ax.set_ylabel("Number of Companies")
  ax.tick_params(axis="x", rotation=90)
  ax.legend(title="Sector", loc="upper left")
  return fig


def plot_market_cap_vs_count_by_sector(df):
  sector_aggregates = df.groupby("Sector").agg(
      SumMarketCap=("Market Cap (USD) Numerical", "sum"),
      CompanyCount=("Sector", "count")).reset_index()
  fig = px.scatter(sector_aggregates,
                   x="CompanyCount",
                   y="SumMarketCap",
                   size="SumMarketCap",
                   color="Sector",
                   hover_name="Sector",
                   title="plot_market_cap_vs_count_by_sector")
  fig.update_xaxes(title_text="Count of Comapnies")
  fig.update_yaxes(title_text="Sum of Market Cap (USD)")
  return fig
